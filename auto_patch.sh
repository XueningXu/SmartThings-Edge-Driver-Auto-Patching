#!/bin/bash

# Define the Python script filename
PYTHON_SCRIPT_1="1_patch_profiles.py"
PYTHON_SCRIPT_2="2_patch_handlers.py"
PYTHON_SCRIPT_3="3_patch_subdriver.py"


if [ "$#" -ne 4 ]; then
    echo $'ArgumentError: Illegal number of arguments. Four arguments required as follows: \n\tDriverName Model Manufacturer Attributes'
    exit 1
fi

# Define the arguments
#DRIVER_ARG="zigbee-lock"
#MODEL_ARG="YRD226 TSDB"
#MANUFACTURER_ARG="Yale"   # default: None
#ATTRIBUTES_ARG="ALL"
DRIVER_ARG=$1
MODEL_ARG=$2
MANUFACTURER_ARG=$3   # default: None
ATTRIBUTES_ARG=$4

# backup the original driver
cp -r "$DRIVER_ARG" "$DRIVER_ARG-backup"

# Step1: Patch fingerprints
python $PYTHON_SCRIPT_1 --driver "$DRIVER_ARG" --model "$MODEL_ARG" --mfg "$MANUFACTURER_ARG" --attributes "$ATTRIBUTES_ARG"
# Step2: Patch handler functions
python $PYTHON_SCRIPT_2 --driver "$DRIVER_ARG"
# Step3: Patch subdriver
python $PYTHON_SCRIPT_3 --driver "$DRIVER_ARG" --model "$MODEL_ARG" --mfg "$MANUFACTURER_ARG"