# SmartThings-Edge-Driver-Auto-Patching
This is a project to automatically patch SmartThings Edge Drivers with previously unsupported Zigbee attributes.


## Download Patch Code 
Download the entire project to a local folder and copy the driver folder to be patched into the local folder. As a result, the driver folder and `auto_patch.sh` are in the same directory.
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
The required information includes `driverName`, `deviceModel`, `deviceManufacturer`, and `attributeLists`.

Below is an example of patching `zigbee-lock` edge driver for the Zigbee Yale Lock with all currently supported attributes. In the terminal, run
```
./auto_patch.sh zigbee-lock "YRD226 TSDB" Yale ALL
```

### Outputs:
1. A new folder named `zigbee-lock-backup` will be generated to back up the original edge driver in case need to restore to the original one. 
2. The folder shares the same name as the original driver folder `zigbee-lock` is the patched driver and can be directly installed in the SmartThings hub. Patched attributes will be displayed on the SmartThings app UI and can be controlled.


## Currently Supported Drivers and Attributes

| SmartThings Edge Drivers | Attributes |
| --- | --- |
| zigbee-lock | Language |
|             | AutoRelockTime |
|             | SoundVolume |
|             | OperatingMode |
|             | EnableOneTouchLocking |
|             | EnableInsideStatusLED |
|             | EnablePrivacyModeButton |
|             | WrongCodeEntryLimit |
|             | UserCodeTemporaryDisableTime |
| zigbee-siren | MaxDuration |
| hue-motion | PIROccupiedToUnoccupiedDelay |
|            | MotionSensitivity |
| zigbee-switch | IdentifyTime |
|               | DeviceEnabled |
|               | OnOffTransitionTime |
|               | OnLevel |
|               | OnTime |
|               | StartUpOnOff |
|               | StartUpColorTemperatureMireds |
| zigbee-dimmer-switch | checkInInterval |
|                      | FastPollTimeout |
| zigbee-contact | IdentifyTime |
|                | DeviceEnabled |
|                | checkInInterval |
|                | FastPollTimeout |
| zigbee-water-leak-sensor | IdentifyTime |
|                          | DeviceEnabled |
|                          | checkInInterval |
|                          | FastPollTimeout |
| zigbee-button | IdentifyTime |
|               | DeviceEnabled |
|               | checkInInterval |
|               | FastPollTimeout |
| zigbee-motion-sensor | IdentifyTime |
|                      | DeviceEnabled |
|                      | checkInInterval |
|                      | FastPollTimeout |
| zigbee-presence-sensor | IdentifyTime |
|                        | checkInInterval |
|                        | FastPollTimeout |


