# SmartThings-Edge-Driver-Auto-Patching
This is a project to automatically patch SmartThings Edge Drivers with previously unsupported Zigbee attributes.
```
localFolder
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
└── driver2patch.config
```
