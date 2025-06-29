# Fixing Remarkable 2 Stylus Coordinates
Created at 2025-06-29 10:55:42 UTC

> @ 2025-06-29 10:55:42 UTC
>
> I am using the attached python library in order to use my remarkable 2 tablet to control my mouse on a Linux machine running Wayland and Hyprland. When I hover the stylus, the following is logged from `libinput debug-events`:
> 
> ---
> 
> -event19  DEVICE_ADDED                 reMarkable pen                    seat0 default group1  cap:T  size 210x157mm left calib
>  event19  TABLET_TOOL_PROXIMITY        +4294967.295s            0.00*/0.00*     tilt: 17.90*/9.85*      distance: 0.15* pen      (0, id 0) proximity-in    axes:dpt        btn:SS2
>  event19  TABLET_TOOL_AXIS             +0.000s          0.00*/0.00      tilt: 17.90/9.85        distance: 0.15
>  event19  TABLET_TOOL_AXIS          2  +0.000s          0.00*/0.00*     tilt: 17.90/9.85        distance: 0.15
>  event19  TABLET_TOOL_AXIS          3  +0.000s          0.00*/0.00*     tilt: 17.90/9.85        distance: 0.15
>  event19  TABLET_TOOL_AXIS          4  +0.000s          0.00*/0.00*     tilt: 17.90/9.85        distance: 0.14*
>  event19  TABLET_TOOL_AXIS          5  +0.000s          0.00*/0.00*     tilt: 17.90/9.85        distance: 0.14
>  event19  TABLET_TOOL_AXIS          6  +0.000s          0.00*/0.00*     tilt: 17.90/9.62*       distance: 0.14
>  event19  TABLET_TOOL_AXIS          7  +0.000s          0.00*/0.00*     tilt: 17.90/9.40        distance: 0.14
>  event19  TABLET_TOOL_AXIS          8  +0.001s          0.00*/0.00*     tilt: 17.90/9.18        distance: 0.12*
>  event19  TABLET_TOOL_AXIS          9  +0.001s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.12
>  event19  TABLET_TOOL_AXIS         10  +0.001s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.11*
>  event19  TABLET_TOOL_AXIS         11  +0.001s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.11
>  event19  TABLET_TOOL_AXIS         12  +0.001s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.10*
>  event19  TABLET_TOOL_AXIS         13  +0.021s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.10
>  event19  TABLET_TOOL_AXIS         14  +0.021s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.10
>  event19  TABLET_TOOL_AXIS         15  +0.021s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.10
>  event19  TABLET_TOOL_AXIS         16  +0.021s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.10
>  event19  TABLET_TOOL_AXIS         17  +0.021s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.10
>  event19  TABLET_TOOL_AXIS         18  +0.021s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.10
>  event19  TABLET_TOOL_AXIS         19  +0.021s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.11*
>  event19  TABLET_TOOL_AXIS         20  +0.021s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.11
>  event19  TABLET_TOOL_AXIS         21  +0.021s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.11
>  event19  TABLET_TOOL_AXIS         22  +0.022s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.11
>  event19  TABLET_TOOL_AXIS         23  +0.022s          0.00*/0.00*     tilt: 17.90/8.95        distance: 0.11
>  event19  TABLET_TOOL_AXIS         24  +0.022s          0.00*/0.00*     tilt: 17.68*/8.95       distance: 0.11
>  event19  TABLET_TOOL_AXIS         25  +0.058s          0.00*/0.00*     tilt: 17.46/8.95        distance: 0.11
>  event19  TABLET_TOOL_AXIS         26  +0.068s          0.00*/0.00*     tilt: 17.23/8.95        distance: 0.12*
>  event19  TABLET_TOOL_AXIS         27  +0.074s          0.00*/0.00*     tilt: 17.01/8.73*       distance: 0.12
>  event19  TABLET_TOOL_AXIS         28  +0.074s          0.00*/0.00*     tilt: 17.01/8.50        distance: 0.12
>  event19  TABLET_TOOL_AXIS         29  +0.079s          0.00*/0.00*     tilt: 17.01/8.28        distance: 0.13*
>  event19  TABLET_TOOL_AXIS         30  +0.095s          0.00*/0.00*     tilt: 16.79*/8.06       distance: 0.13
>  event19  TABLET_TOOL_AXIS         31  +0.095s          0.00*/0.00*     tilt: 16.56/8.06        distance: 0.15*
>  event19  TABLET_TOOL_AXIS         32  +0.095s          0.00*/0.00*     tilt: 16.34/8.06        distance: 0.16*
>  event19  TABLET_TOOL_AXIS         33  +0.095s          0.00*/0.00*     tilt: 16.11/8.06        distance: 0.16
>  event19  TABLET_TOOL_AXIS         34  +0.095s          0.00*/0.00*     tilt: 16.11/8.06        distance: 0.18*
>  event19  TABLET_TOOL_AXIS         35  +0.095s          0.00*/0.00*     tilt: 16.11/8.06        distance: 0.18
>  event19  TABLET_TOOL_AXIS         36  +0.095s          0.00*/0.00*     tilt: 16.11/8.06        distance: 0.20*
>  event19  TABLET_TOOL_AXIS         37  +0.095s          0.00*/0.00*     tilt: 16.11/8.06        distance: 0.21*
>  event19  TABLET_TOOL_AXIS         38  +0.095s          0.00*/0.00*     tilt: 16.11/8.06        distance: 0.23*
> 
> ---
> 
> This shows that the coordinate transformation is not working as expected. How can I update the codebase to send the correct coordinates?

<details><summary>Thinking</summary>

Looking at the libinput debug output, I can see that the position coordinates are always showing as ```0.00*/0.00*``` which means the X and Y position values are not being sent correctly. The tilt and distance values are working fine, but the position is stuck at (0,0).

Looking at the code, particularly in ```remarkable_mouse/evdev.py```, I see that the code is intercepting and modifying coordinates for ```ABS_X``` and ```ABS_Y``` events. 

The issue appears to be that the code is only processing pen events from ```rm.pen``` stream, but it's not properly handling the coordinate remapping. Let me trace through the flow:

1. In ```evdev.py```, the ```read_tablet``` function reads from ```rm.pen```
2. It intercepts ```ABS_X``` and ```ABS_Y``` events
3. It tries to remap coordinates using ```rm.remap()```
4. Then it maps back to wacom coordinates

The problem might be that:
1. The coordinates are being improperly remapped
2. The events aren't being sent with the right values
3. The virtual device creation might be missing some capabilities

Looking more closely at the evdev.py code:

```python
# intercept EV_ABS events and modify coordinates
if types[e_type] == 'EV_ABS':
    # handle x direction
    if codes[e_type][e_code] == 'ABS_X':
        x = e_value

    # handle y direction
    if codes[e_type][e_code] == 'ABS_Y':
        y = e_value

    # map to screen coordinates so that region/monitor/orientation options are applied
    mapped_x, mapped_y = rm.remap(
        x, y,
        rm.pen_x.max, rm.pen_y.max,
        monitor.width, monitor.height,


```

I notice the coordinate mapping process involves several critical transformations. The code calculates mapped coordinates by applying offsets and scaling, ensuring the pen input aligns correctly with the screen's dimensions and orientation. The subsequent steps involve adjusting these mapped coordinates to account for monitor positioning and scaling them back to the original device's coordinate space.

The key challenge appears to be ensuring these coordinate transformations accurately translate the raw input to the desired screen position without losing precision or introducing unexpected shifts. The asterisks reveal a pattern of zero values, pointing to potential initialization or calculation problems. The coordinate tracking seems flawed, with x and y potentially remaining at their default zero state during event processing. This could stem from premature remapping before receiving valid coordinate updates or an issue in how event values are being calculated and transformed. The event modification sequence appears to have a critical flaw where coordinate transformations might occur before having complete input data.

The hovering behavior introduces another layer of complexity. The tablet's event transmission during stylus hovering might differ significantly from direct contact, potentially explaining the zero-value output. Investigating the actual event stream from the reMarkable device could provide crucial insights into this unexpected behavior.

The coordinate transformation process reveals potential mathematical inconsistencies. The current remapping strategy involves multiple coordinate space translations that might not align with libinput's expectations. Specifically, the final scaling step using tablet max values divided by total screen size seems problematic for Wayland input handling.

Examining libinput's device configuration requirements suggests a fundamental misalignment. The documentation emphasizes reporting native device coordinate ranges, which implies the current transformation approach may fundamentally misunderstand how tablet input should be mapped.

The core issue appears to be unnecessary coordinate manipulation. Instead of manually transforming coordinates, the virtual device should simply transmit the tablet's original coordinate space, allowing the Wayland compositor to manage precise screen coordinate translation.

</details>

Looking at the libinput output, the position coordinates are stuck at ```0.00*/0.00*```, which indicates the coordinate transformation isn't working correctly. The issue is likely in how the ```evdev.py``` module handles coordinate remapping for Wayland.

The problem appears to be that the code is trying to do manual coordinate transformation when it should let the Wayland compositor (Hyprland) handle the mapping. In Wayland, tablet devices report their native coordinates, and the compositor handles mapping them to screen coordinates.

Here's how to fix the ```evdev.py``` file:

```python
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

        # For Wayland, pass events through without coordinate transformation
        # The Wayland compositor handles the mapping
        
        try:
            # pass events directly to libevdev
            e_bit = libevdev.evbit(e_type, e_code)
            e = libevdev.InputEvent(e_bit, value=e_value)
            local_device.send_events([e])
        except KeyError as e:
            log.debug(f"Invalid evdev event: type:{e_type} code:{e_code}")
```

The key insight is that Wayland compositors expect tablet devices to report their native coordinates. The compositor then handles:
- Mapping tablet coordinates to screen coordinates
- Applying monitor selection and orientation
- Handling multi-monitor setups

If you need more control over the mapping (for the region/monitor/orientation options), you'll need to configure this through Hyprland's input configuration instead of doing it in the driver. 【1】

To debug further, you can run the tool with ```--debug``` flag to see what raw events are being received from the tablet:

```bash
sudo remouse --debug --evdev
```

This will show if the tablet is actually sending coordinate events when hovering.


_References_:
- [repomix-packaged]()

> @ 2025-06-29 10:58:12 UTC
>
> After making those changes I get the following from the debug stream:
> 
> --
> 
> sudo python -m remarkable_mouse.remarkable_mouse --evdev --password FDcOwIc9vu --debug --monitor 1
> Debugging enabled...
> Connecting to input '10.11.99.1'
> Detected reMarkable2
> Pen:/dev/input/event1
> Touch:/dev/input/event2
> Button:/dev/input/event0
> Connected to 10.11.99.1
> Created virtual input device '/dev/input/event19'
> 1751194657.486322 - EV_KEY    BTN_TOOL_PEN         1
> 1751194657.486322 - EV_ABS    ABS_X             2838
> 1751194657.486322 - EV_ABS    ABS_Y            13585
> 1751194657.486322 - EV_ABS    ABS_DISTANCE        66
> 1751194657.486322 - EV_ABS    ABS_TILT_X         600
> 1751194657.486322 - EV_ABS    ABS_TILT_Y       -1000
> 1751194657.486322 - EV_SYN    SYN_REPORT           0
> 1751194657.488126 - EV_ABS    ABS_X             2839
> 1751194657.488126 - EV_ABS    ABS_Y            13586
> 1751194657.488126 - EV_SYN    SYN_REPORT           0
> 1751194657.489987 - EV_ABS    ABS_X             2841
> 1751194657.489987 - EV_ABS    ABS_DISTANCE        67
> 1751194657.489987 - EV_SYN    SYN_REPORT           0
> 1751194657.491823 - EV_ABS    ABS_X             2844
> 1751194657.491823 - EV_ABS    ABS_Y            13587
> 1751194657.491823 - EV_ABS    ABS_DISTANCE        68
> 1751194657.491823 - EV_ABS    ABS_TILT_X         700
> 1751194657.491823 - EV_SYN    SYN_REPORT           0
> 1751194657.493666 - EV_ABS    ABS_X             2867
> 1751194657.493666 - EV_ABS    ABS_Y            13588
> 1751194657.493666 - EV_ABS    ABS_DISTANCE        69
> 1751194657.493666 - EV_SYN    SYN_REPORT           0
> 1751194657.495522 - EV_ABS    ABS_X             2899
> 1751194657.495522 - EV_ABS    ABS_Y            13589
> 1751194657.495522 - EV_ABS    ABS_DISTANCE        71
> 1751194657.495522 - EV_SYN    SYN_REPORT           0
> 1751194657.497366 - EV_ABS    ABS_X             2937
> 1751194657.497366 - EV_ABS    ABS_DISTANCE        72
> 1751194657.497366 - EV_SYN    SYN_REPORT           0
> 1751194657.499238 - EV_ABS    ABS_X             2982
> 1751194657.499238 - EV_ABS    ABS_Y            13590
> 1751194657.499238 - EV_ABS    ABS_DISTANCE        74
> 1751194657.499238 - EV_SYN    SYN_REPORT           0
> 1751194657.501074 - EV_ABS    ABS_X             3035
> 1751194657.501074 - EV_ABS    ABS_Y            13591
> 1751194657.501074 - EV_ABS    ABS_DISTANCE        76
> 1751194657.501074 - EV_ABS    ABS_TILT_X         600
> 1751194657.501074 - EV_SYN    SYN_REPORT           0
> 1751194657.502923 - EV_ABS    ABS_X             3084
> 1751194657.502923 - EV_ABS    ABS_DISTANCE        77
> 1751194657.502923 - EV_SYN    SYN_REPORT           0
> 1751194657.504756 - EV_ABS    ABS_X             3136
> 1751194657.504756 - EV_ABS    ABS_DISTANCE        79
> 1751194657.504756 - EV_SYN    SYN_REPORT           0
> 1751194657.506603 - EV_ABS    ABS_X             3189
> 1751194657.506603 - EV_ABS    ABS_Y            13590
> 1751194657.506603 - EV_ABS    ABS_DISTANCE        80
> 1751194657.506603 - EV_SYN    SYN_REPORT           0
> 1751194657.508453 - EV_ABS    ABS_X             3245
> 1751194657.508453 - EV_ABS    ABS_Y            13589
> 1751194657.508453 - EV_ABS    ABS_DISTANCE        82
> 1751194657.508453 - EV_SYN    SYN_REPORT           0
> 1751194657.510318 - EV_ABS    ABS_X             3306
> 1751194657.510318 - EV_ABS    ABS_Y            13587
> 1751194657.510318 - EV_ABS    ABS_DISTANCE        83
> 1751194657.510318 - EV_SYN    SYN_REPORT           0
> 1751194657.512157 - EV_ABS    ABS_X             3369
> 1751194657.512157 - EV_ABS    ABS_Y            13584
> 1751194657.512157 - EV_ABS    ABS_DISTANCE        85
> 1751194657.512157 - EV_SYN    SYN_REPORT           0
> 1751194657.513998 - EV_ABS    ABS_X             3435
> 1751194657.513998 - EV_ABS    ABS_Y            13581
> 1751194657.513998 - EV_ABS    ABS_DISTANCE        87
> 1751194657.513998 - EV_SYN    SYN_REPORT           0
> 1751194657.515850 - EV_ABS    ABS_X             3496
> 1751194657.515850 - EV_ABS    ABS_Y            13567
> 1751194657.515850 - EV_ABS    ABS_DISTANCE        90
> 1751194657.515850 - EV_SYN    SYN_REPORT           0
> 1751194657.517703 - EV_ABS    ABS_X             3560
> 1751194657.517703 - EV_ABS    ABS_Y            13555
> 1751194657.517703 - EV_ABS    ABS_DISTANCE        92
> 1751194657.517703 - EV_SYN    SYN_REPORT           0
> 1751194657.519547 - EV_ABS    ABS_X             3627
> 1751194657.519547 - EV_ABS    ABS_Y            13542
> 1751194657.519547 - EV_ABS    ABS_DISTANCE        95
> 1751194657.519547 - EV_ABS    ABS_TILT_Y        -900
> 1751194657.519547 - EV_SYN    SYN_REPORT           0
> 1751194657.521101 - EV_ABS    ABS_X             3687
> 1751194657.521101 - EV_ABS    ABS_Y            13531
> 1751194657.521101 - EV_SYN    SYN_REPORT           0
> 1751194657.522954 - EV_ABS    ABS_X             3737
> 1751194657.522954 - EV_ABS    ABS_Y            13520
> 1751194657.522954 - EV_SYN    SYN_REPORT           0
> 1751194657.524799 - EV_KEY    BTN_TOOL_PEN         0
> 1751194657.524799 - EV_SYN    SYN_REPORT           0
> 

<details><summary>Thinking</summary>

The user is showing debug output that confirms the reMarkable tablet is sending coordinate events (ABS_X and ABS_Y), but when viewed through libinput debug-events, the coordinates show as 0.00*/0.00*. This means the events are being received but not properly passed through to the virtual device or the virtual device is not configured correctly.

Looking at the debug output:
- The tablet is sending ABS_X values like 2838, 2839, etc.
- The tablet is sending ABS_Y values like 13585, 13586, etc.
- These are raw tablet coordinates

The issue is that the virtual device created by libevdev needs to be configured with the proper axis ranges and resolution information so that libinput can properly interpret the coordinates.

I need to look at the code to see how the virtual device is being created and configured.

</details>

Great! The debug output shows that the reMarkable is sending coordinate events (ABS_X and ABS_Y), but they're showing as 0.00*/0.00* in libinput. This indicates the virtual device isn't properly configured with the correct axis ranges.

Let me search for how the virtual device is created:

<anycopy>
<document_content path="repomix-packaged.md">
<search>
def create_local_device
</search>
</document_content>
</anycopy>

Let me look for the device creation function in the evdev module:

<anycopy>
<document_content path="repomix-packaged.md">
<search>
create_local_device(rm)
</search>
</document_content>
</anycopy>

<anycopy>
<document_content path="repomix-packaged.md">
<search>
libevdev.Device
</search>
</document_content>
</anycopy>

Let me search for the virtual device setup:

<anycopy>
<document_content path="repomix-packaged.md">
<search>
virtual_input = VirtualInput
</search>
</document_content>
</anycopy>

<anycopy>
<document_content path="repomix-packaged.md">
<search>
class VirtualInput
</search>
</document_content>
</anycopy>

Based on the code structure, the issue is that the virtual device needs to be configured with the proper axis information for the reMarkable tablet. Here's how to fix the ```evdev.py``` file to properly configure the virtual device:

```python
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
```

And update the ```read_tablet``` function to use this properly configured device:

```python
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
```

The key changes are:
1. Properly configuring the virtual device with the correct axis ranges and resolution
2. Setting the device to identify as a tablet (with proper vendor/product IDs)
3. Batching events and sending them together when SYN_REPORT is received

This should make the tablet coordinates visible to libinput and allow Hyprland to properly map them to your screen.


---

_Generated by [The Assistant](https://kagi.com/assistant)_