import logging
import struct
import subprocess
from screeninfo import get_monitors
import time
from itertools import cycle
from socket import timeout as TimeoutError
import libevdev

from .codes import codes, types
from .common import get_monitor, log_event

logging.basicConfig(format='%(message)s')
log = logging.getLogger('remouse')

def create_local_device(rm):
    """Create a virtual input device that mimics the reMarkable tablet

    Args:
        rm (reMarkable): tablet settings

    Returns:
        libevdev.Device: configured virtual device
    """

    device = libevdev.Device()

    # Set device properties
    device.name = "reMarkable pen"
    device.id = {
        "bustype": 0x18,  # BUS_USB
        "vendor": 0x056a,  # Wacom
        "product": 0x0001,
        "version": 0x0100
    }

    # Enable event types
    device.enable(libevdev.EV_KEY)
    device.enable(libevdev.EV_ABS)
    device.enable(libevdev.EV_SYN)

    # Configure absolute axes with reMarkable dimensions
    # reMarkable 2 has 20967 x 15725 resolution
    absinfo_x = libevdev.InputAbsInfo(
        minimum=0,
        maximum=20967,
        resolution=100  # dots per mm
    )
    device.enable(libevdev.EV_ABS.ABS_X, absinfo_x)

    absinfo_y = libevdev.InputAbsInfo(
        minimum=0,
        maximum=15725,
        resolution=100  # dots per mm
    )
    device.enable(libevdev.EV_ABS.ABS_Y, absinfo_y)

    # Pressure
    absinfo_pressure = libevdev.InputAbsInfo(
        minimum=0,
        maximum=4095
    )
    device.enable(libevdev.EV_ABS.ABS_PRESSURE, absinfo_pressure)

    # Distance (hover)
    absinfo_distance = libevdev.InputAbsInfo(
        minimum=0,
        maximum=255
    )
    device.enable(libevdev.EV_ABS.ABS_DISTANCE, absinfo_distance)

    # Tilt
    absinfo_tilt = libevdev.InputAbsInfo(
        minimum=-9000,
        maximum=9000
    )
    device.enable(libevdev.EV_ABS.ABS_TILT_X, absinfo_tilt)
    device.enable(libevdev.EV_ABS.ABS_TILT_Y, absinfo_tilt)

    # Pen buttons
    device.enable(libevdev.EV_KEY.BTN_TOOL_PEN)
    device.enable(libevdev.EV_KEY.BTN_TOUCH)
    device.enable(libevdev.EV_KEY.BTN_STYLUS)
    device.enable(libevdev.EV_KEY.BTN_STYLUS2)

    # Create uinput device
    uinput = device.create_uinput_device()

    log.info(f"Created virtual tablet device: {uinput.devnode}")
    return uinput

def read_tablet(rm, *, orientation, monitor_num, region, threshold, mode):
    """Pipe rM evdev events to local device

    Args:
        rm (reMarkable): tablet settings and input streams
        orientation (str): tablet orientation
        monitor_num (int): monitor number to map to
        threshold (int): pressure threshold
        mode (str): mapping mode
    """

    local_device = create_local_device(rm)
    log.debug("Created virtual input device '{}'".format(local_device.devnode))

    # For Wayland, we don't need to do coordinate transformation
    # The compositor will handle mapping tablet coordinates to screen

    stream = rm.pen
    pending_events = []

    while True:
        try:
            # read evdev events from file stream
            data = stream.read(struct.calcsize(rm.e_format))
        except TimeoutError:
            continue

        # parse evdev events
        e_time, e_millis, e_type, e_code, e_value = struct.unpack(rm.e_format, data)

        if log.level == logging.DEBUG:
            log_event(e_time, e_millis, e_type, e_code, e_value)

        # Convert event type and code to libevdev format
        if e_type == libevdev.EV_SYN.value and e_code == libevdev.EV_SYN.SYN_REPORT.value:
            # Send all pending events
            if pending_events:
                local_device.send_events(pending_events)
                pending_events = []
        else:
            # Queue event
            try:
                event_type = libevdev.evbit(e_type)
                event_code = libevdev.evbit(e_type, e_code)
                event = libevdev.InputEvent(event_code, value=e_value)
                pending_events.append(event)
            except (KeyError, ValueError) as e:
                log.debug(f"Skipping unknown event: type={e_type} code={e_code}")

