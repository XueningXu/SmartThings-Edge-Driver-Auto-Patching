import re
import configparser
import argparse
import os

config = configparser.ConfigParser()
config.read('./driver2patch.config')

def add_patched_subdriver(driver):
    subdriver = config[driver]['subdriver']     
    parent_directory = "./" + driver + "/src"
    
    src_path = "./subdrivers/" + subdriver
    dest_path = parent_directory
    os.system("cp -r {src} {dest}".format(src=src_path, dest=dest_path))


def add_device_model(mfg, model):
    subdriver = config[driver]['subdriver']     
    subdriver_path = "./" + driver + "/src/" + subdriver + "/init.lua"
    with open(subdriver_path, 'r') as f:
        code = f.read()
    patched_device_model_pattern = re.compile(r"(^local PATCHED_DEVICE_MODELS = {(?:.|\n)*?^\}$)", re.MULTILINE)
    patched_device_model_code = re.findall(patched_device_model_pattern, code)
    models = patched_device_model_code[0].split('\n')
    new_model = ' '*4 + '{{ mfr = "{mfr}", model = "{model}" }},'.format(mfr=mfg, model=model) 
    new_models = models[:1] + [new_model] + models[1:]
    new_patched_device_model_code = '\n'.join(new_models)
    result = re.sub(patched_device_model_pattern, new_patched_device_model_code, code)
    # update the driver code
    with open(subdriver_path, 'w') as f:
        f.write(result)

def construct_new_subdrivers(sub_drivers_code, new_driver):
    require_patterns = re.compile(r'require\("(.*)"\)')
    existing_drivers = re.findall(require_patterns, sub_drivers_code)
    indent = 2
    new_sub_drivers = ['sub_drivers = {']
    for exist_driver in [new_driver] + existing_drivers:
        new_sub_drivers.append(' '*2*indent + 'require("' + exist_driver + '"),')
    new_sub_drivers.append(' '*indent + '}')
    return '\n'.join(new_sub_drivers)


def update_parent_driver_template(driver):
    subdriver = config[driver]['subdriver']
    parent_driver_path = "./" + driver + "/src/init.lua"

    with open(parent_driver_path, 'r') as f:
        code = f.read()

    # try to find sub_drivers in the parent driver template within `init.lua`` file
    sub_driver_pattern = re.compile(r"(sub_drivers = \{(?:\s*|require\(.*\),?|\n)*\})", re.MULTILINE)
    sub_drivers_code = re.findall(sub_driver_pattern, code)

    # if there is a sub_drivers in the parent driver template, add one more require(...) to it
    if sub_drivers_code:
        #print('*** sub_drivers found ***\n')
        new_sub_drivers = construct_new_subdrivers(sub_drivers_code[0], subdriver)
        result = re.sub(sub_driver_pattern, new_sub_drivers, code)
    # Otherwise, create sub_drivers that include one require(...)
    else:
        #print('*** No sub_drivers found ***\n')
        # find the name of the parent driver template
        fetch_template_patterns = [re.compile(r"defaults.register_for_default_handlers\((.*),"), re.compile(r"return (.*)$")]
        matches = []
        for pat in fetch_template_patterns:
            matches.extend(re.findall(pat, code))

        # find driver template code
        driver_template_name = matches[0]
        driver_template_pattern = re.compile(r"(^local " + driver_template_name + "\s*=\s*\{(?:.|\n)*^\}$)", re.MULTILINE)
        match = re.findall(driver_template_pattern, code)
        template_code = match[0]
        template_list = template_code.split('\n')
        indent = len(template_list[1]) - len(template_list[1].strip())
        new_template_list = template_list[:1] + [' '*indent + 'sub_drivers = { require("' + subdriver + '") },'] + template_list[1:]
        new_template = '\n'.join(new_template_list)
        result = re.sub(driver_template_pattern, new_template, code)
    
    # update the driver code
    with open(parent_driver_path, 'w') as f:
        f.write(result)
    
    
if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Patch Zigbee handlers.')
    parser.add_argument('--driver', type=str, required=True, help='The folder name of the edge driver to patch')
    parser.add_argument('--model', type=str, required=True, help='The model of the device to patch')
    parser.add_argument('--mfg', type=str, help='The manufacturer of the device to patch', default=None)

    # Parse arguments
    args = parser.parse_args()
    driver = args.driver
    model = args.model
    manufacturer = args.mfg
    
    subdriver = config[driver]['subdriver']     
    parent_directory = "./" + driver + "/src"
    
    if not os.path.isdir(parent_directory + '/' + subdriver):
        add_patched_subdriver(driver)
        add_device_model(manufacturer, model)
        update_parent_driver_template(driver)
    else:
        print("[Step 3]: already patched")
