import os
import argparse

def get_subdirectories(path):
    subdirectories = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            subdirectories.append(item_path)
    return subdirectories

def main():
    parser = argparse.ArgumentParser(description="List subdirectories within a directory")
    parser.add_argument("--path", help="Path of the directory")
    parser.add_argument("--oca", help="Path of the OCA addons directory")
    parser.add_argument("--dev", help="Path of the development addons directory")
    parser.add_argument("--odoo", help="Path of the Odoo server directory")
    parser.add_argument("--third-party", help="Path of the third-party addons directory")
    args = parser.parse_args()

    if args.oca or args.dev or args.odoo or args.third_party:
        input_path = args.path if args.path else os.getcwd()
        oca_path = args.oca if args.oca else f"{input_path}/addons/oca"
        dev_path = args.dev if args.dev else f"{input_path}/addons/addons_development"
        odoo_path = args.odoo if args.odoo else f"{input_path}/server"
        third_party_path = args.third_party if args.third_party else f"{input_path}/addons/third_party_addons"

        if not os.path.exists(oca_path):
            return

        oca_addons_paths = get_subdirectories(oca_path)
        addons_path = [
            f"{odoo_path}/odoo/addons",
            f"{odoo_path}/addons",
            *oca_addons_paths,
            third_party_path,
            dev_path,
        ]

        print(",".join(addons_path))
        return 0
    else:
        raise Exception("At least one of the additional arguments (--oca, --dev, --odoo, --third-party) must be provided.")
        return 1
    

if __name__ == "__main__":
    main()
