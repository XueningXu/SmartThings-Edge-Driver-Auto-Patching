import configparser
import argparse
import os

def patch_handlers(driver):
    config = configparser.ConfigParser()
    config.read('./driver2patch.config')
    filename = config[driver]['filename']
    patch_src = './cap-patches/' + filename + '.lua'
    patch_dest = './' + driver + '/src/' + filename + '.lua'
    if not os.path.exists(patch_dest):
        os.system("cp {patch_src} {patch_dest}".format(patch_src=patch_src, patch_dest=patch_dest))
    else:
        print("[Step 2]: patch handlers exist.")


if __name__ == "__main__":
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Patch Zigbee handlers.')
    parser.add_argument('--driver', type=str, required=True, help='The folder name of the edge driver to patch')

    # Parse arguments
    args = parser.parse_args()
    driver = args.driver
    patch_handlers(driver)