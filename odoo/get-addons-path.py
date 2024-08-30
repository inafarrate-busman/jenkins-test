from os import path, listdir, getcwd
import argparse

def get_subdirectories(directory):
    subdirectories = []
    for item in listdir(directory):
        item_path = path.join(directory, item)
        if path.isdir(item_path) and '@' not in item:
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

    if args.path or args.oca or args.dev or args.odoo or args.third_party:
        input_path = args.path if args.path else getcwd()
        oca_path = args.oca if args.oca else f"{input_path}/addons/oca"
        dev_path = args.dev if args.dev else f"{input_path}/addons/addons_development"
        odoo_path = args.odoo if args.odoo else f"{input_path}/server"
        third_party_path = args.third_party if args.third_party else f"{input_path}/addons/third_party_addons"
        prs_path = path.normpath(path.join(args.dev, "../prs")) if args.dev else f"{input_path}/addons/prs"
        override_path = path.normpath(path.join(args.dev, "../override")) if args.dev else f"{input_path}/addons/override"

        if not path.exists(oca_path):
            return

        prs_path = [prs_path] if path.exists(prs_path) else []
        override_path = [override_path] if path.exists(override_path) else []
        oca_addons_paths = get_subdirectories(oca_path)
        addons_path = [
            *override_path,
            f"{odoo_path}/odoo/addons",
            f"{odoo_path}/addons",
            *prs_path,
            *oca_addons_paths,
            third_party_path,
            dev_path,
        ]

        print(",".join(addons_path))
        return 0
    else:
        raise Exception("At least one of the additional arguments (--oca, --dev, --odoo, --third-party, --path) must be provided.")
        return 1
    

if __name__ == "__main__":
    main()
