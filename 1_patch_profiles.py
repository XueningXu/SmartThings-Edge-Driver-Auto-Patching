import yaml
import argparse
import os, sys
import configparser

profileName = ''
config = configparser.ConfigParser()
config.read('./custom_capability_list.config')

class IndentDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super(IndentDumper, self).increase_indent(flow, False)

def load_fingerprints(path):
    with open(path, 'r') as fp:
        fingerprints = yaml.safe_load(fp)
    return fingerprints

def save2file(new_path, fingerprints):  
    with open(new_path, "w") as f:
        yaml.dump(fingerprints, f, sort_keys=False, Dumper=IndentDumper)

def patch_fingerprints(devices, model, manufacturer=None):
    global profileName
    for device in devices:
        # if it has manufacturer, then check. Otherwise, skip this
        if manufacturer and device.get('manufacturer', None):
            if device['manufacturer'] != manufacturer:
                continue
        if device['model'] == model:
            #print(device['deviceProfileName'])
            profileName = device['deviceProfileName']
            device['deviceProfileName'] += '-patch'
            
def update_fingerprints(old_fp, new_fp, backup_fp):
    if os.path.exists(backup_fp):  # if backed up before, do not back up again
        print("[Step 1]: fingerprints backup exists")
        os.system("rm {old_fp}".format(old_fp=old_fp))
    else:
        os.system("mv {old_fp} {backup_fp}".format(old_fp=old_fp, backup_fp=backup_fp))
    os.system("mv {new_fp} {old_fp}".format(new_fp=new_fp, old_fp=old_fp))
    
    
def create_new_profile(driver, capabilities):
    global profileName
    profile_path = "./" + driver + "/profiles/" + profileName + ".yml"
    new_profile_path = "./" + driver + "/profiles/" + profileName + "-patch.yml"
    with open(profile_path, 'r') as f1:
        profiles = yaml.safe_load(f1)
    profiles["name"] += '-patch'
    custom_capabilities = []
    for cap in capabilities:
        custom_capabilities.append({'id': cap, 'version': 1})
    profiles['components'][0]['capabilities'].extend(custom_capabilities)
    with open(new_profile_path, "w") as f2:
        yaml.dump(profiles, f2, sort_keys=False, Dumper=IndentDumper)


if __name__ == "__main__":

    # Set up argument parser
    parser = argparse.ArgumentParser(description='Patch Zigbee fingerprints.')
    parser.add_argument('--driver', type=str, required=True, help='The folder name of the edge driver to patch')
    parser.add_argument('--model', type=str, required=True, help='The model of the device to patch')
    parser.add_argument('--mfg', type=str, help='The manufacturer of the device to patch', default=None)
    parser.add_argument('--attributes', type=str, help='The attributes to patch, separated by :', default=None)

    # Parse arguments
    args = parser.parse_args()
    driver = args.driver
    model = args.model
    manufacturer = args.mfg
    attributes = args.attributes
    
    # convert attributes to custom capabilities
    if attributes == 'ALL':   # include all attributes supported by the driver
        custom_capabilities = [pair[1] for pair in config.items(driver)]
    else:
        attributes = attributes.split(":")
        custom_capabilities = []
        for attr in attributes:
            try:
                custom_capabilities.append(config[driver][attr])
            except:
                print('AttributeError: {driver} does not support attribute {attr}'.format(driver=driver, attr=attr))
                sys.exit(1)
            
    fingerprints_path = "./" + driver + "/fingerprints.yml"
    patched_fingerprints_path = "./" + driver + "/fingerprints-patch.yml"
    fingerprints_backup_path = "./" + driver + "/fingerprints-old.yml"
    
    fingerprints = load_fingerprints(fingerprints_path)
    devices = fingerprints['zigbeeManufacturer']
    patch_fingerprints(devices=devices, model=model, manufacturer=manufacturer)
    save2file(patched_fingerprints_path, fingerprints)
    update_fingerprints(fingerprints_path, patched_fingerprints_path, fingerprints_backup_path)
    create_new_profile(driver, custom_capabilities)