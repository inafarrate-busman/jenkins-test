import argparse
import configparser

def modify_config(file_path, args):
    config = configparser.ConfigParser()
    config.read(file_path)

    for arg in args:
        option = arg.split('=')[0]
        value = arg.split('=')[1]

        section_name = 'options'  # Assuming the section name is always 'options'
        if not config.has_section(section_name):
            config.add_section(section_name)
        
        config.set(section_name, option, value)

    with open(file_path, 'w') as configfile:
        config.write(configfile)

    print("Configuration file updated successfully.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Modify values in a configuration file")
    parser.add_argument("file_path", help="Path to the configuration file")
    parser.add_argument("args", nargs='*', help="Arguments in the format key=value")

    args = parser.parse_args()

    if not args.args:
        print("No values provided to update.")
    else:
        modify_config(args.file_path, args.args)
