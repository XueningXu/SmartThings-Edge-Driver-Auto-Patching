# SmartThings-Edge-Driver-Auto-Patching
This is a project to automatically patch SmartThings Edge Drivers with previously unsupported Zigbee attributes.


## Download Patch Code 
Download the source code from the latest [release](https://github.com/XueningXu/SmartThings-Edge-Driver-Auto-Patching/releases/tag/sourceCode) to a local folder and copy the driver folder to be patched into the local folder. As a result, the driver folder and the shell script `auto_patch.sh` are in the same directory.
<!---
The resulting directory tree should be as follows:
```
local-folder
├── cap-patches
│   ├── button_patch.lua
│   ├── contact_patch.lua
│   ├── dimmer_patch.lua
│   ├── hue_patch.lua
│   ├── lock_patch.lua
│   ├── motion_patch.lua
│   ├── presence_patch.lua
│   ├── siren_patch.lua
│   ├── switch_patch.lua
│   └── water_patch.lua
├── subdrivers
│   ├── button-patch
|       └── init.lua
│   ├── contact-patch
|       └── init.lua
│   ├── dimmer-patch
|       └── init.lua
│   ├── hue-patch
|       └── init.lua
│   ├── lock-patch
|       └── init.lua
│   ├── motion-patch
|       └── init.lua
│   ├── presence-patch
|       └── init.lua
│   ├── siren-patch
|       └── init.lua
│   ├── switch-patch
|       └── init.lua
│   └── water-patch
|       └── init.lua
├── auto_patch.sh
├── 1_patch_profiles.py
├── 2_patch_handlers.py
├── 3_patch_subdriver.py
├── custom_capability_list.config
├── driver2patch.config
└── zigbee-lock            <-- This is the SmartThings edge driver to be patched
```
--->

## Usage Example
Before patching an edge driver, you should know exactly what device you are going to use the patched edge driver for and what attributes you want to be patched to the edge driver for this device. 
The required information includes `driverName`, `deviceModel`, `deviceManufacturerCode`, and `attributeLists`.

Below is an example of patching `zigbee-lock` edge driver for the Zigbee Yale Lock with all currently supported attributes. In the terminal, run
```
./auto_patch.sh zigbee-lock "YRD226 TSDB" Yale ALL
```

### Outputs:
1. A new folder named `zigbee-lock-backup` will be generated to back up the original edge driver in case need to restore to the original one. 
2. The folder shares the same name as the original driver folder `zigbee-lock` is the patched driver and can be directly installed in the SmartThings hub. Patched attributes will be displayed on the SmartThings app UI and can be controlled.

## Device Model and Manufacturer
Go to [https://my.smartthings.com](https://my.smartthings.com) and login. Device model and manufacturer code information can be found under *Advanced Users*. 

![1704160579456](https://github.com/XueningXu/SmartThings-Edge-Driver-Auto-Patching/assets/47044598/7806bb39-9751-47f2-9a0a-58e651aa2445)



## Currently Supported Drivers and Attributes

<table>
  <tr>
    <th> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; SmartThings Edge Drivers &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
    <th> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Attributes &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
  </tr>
  <tr>
    <td rowspan="9">zigbee-lock</td>
    <td>Language</td>
  </tr>
  <tr><td>AutoRelockTime</td></tr>
  <tr><td>SoundVolume</td></tr>
  <tr><td>OperatingMode</td></tr>
  <tr><td>EnableOneTouchLocking</td></tr>
  <tr><td>EnableInsideStatusLED</td></tr>
  <tr><td>EnablePrivacyModeButton</td></tr>
  <tr><td>WrongCodeEntryLimit</td></tr>
  <tr><td>UserCodeTemporaryDisableTime &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td></tr>
    
  <tr>
    <td>zigbee-siren</td>
    <td>MaxDuration</td>
  </tr>

  <tr>
    <td rowspan="2">hue-motion</td>
    <td>PIROccupiedToUnoccupiedDelay</td>
  </tr>
  <tr><td>MotionSensitivity</td></tr>

  <tr>
    <td rowspan="7">zigbee-switch</td>
    <td>IdentifyTime</td>
  </tr>
  <tr><td>DeviceEnabled</td></tr>
  <tr><td>OnOffTransitionTime</td></tr>
  <tr><td>OnLevel</td></tr>
  <tr><td>OnTime</td></tr>
  <tr><td>StartUpOnOff</td></tr>
  <tr><td>StartUpColorTemperatureMireds</td></tr>

  <tr>
    <td rowspan="2">zigbee-dimmer-switch</td>
    <td>CheckInInterval</td>
  </tr>
  <tr><td>FastPollTimeout</td></tr>

  <tr>
    <td rowspan="4">zigbee-contact</td>
    <td>IdentifyTime</td>
  </tr>
  <tr><td>DeviceEnabled</td></tr>
  <tr><td>CheckInInterval</td></tr>
  <tr><td>FastPollTimeout</td></tr>

  <tr>
    <td rowspan="4">zigbee-water-leak-sensor</td>
    <td>IdentifyTime</td>
  </tr>
  <tr><td>DeviceEnabled</td></tr>
  <tr><td>CheckInInterval</td></tr>
  <tr><td>FastPollTimeout</td></tr>

  <tr>
    <td rowspan="4">zigbee-button</td>
    <td>IdentifyTime</td>
  </tr>
  <tr><td>DeviceEnabled</td></tr>
  <tr><td>CheckInInterval</td></tr>
  <tr><td>FastPollTimeout</td></tr>

  <tr>
    <td rowspan="4">zigbee-motion-sensor</td>
    <td>IdentifyTime</td>
  </tr>
  <tr><td>DeviceEnabled</td></tr>
  <tr><td>CheckInInterval</td></tr>
  <tr><td>FastPollTimeout</td></tr>

  <tr>
    <td rowspan="3">zigbee-presence-sensor</td>
    <td>IdentifyTime</td>
  </tr>
  <tr><td>CheckInInterval</td></tr>
  <tr><td>FastPollTimeout</td></tr>
</table>



*More edge drivers and attributes will be supported in the near future. Stay tuned.*

