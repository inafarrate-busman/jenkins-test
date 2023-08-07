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
    parser.add_argument("path", help="Path of the directory")
    args = parser.parse_args()

    input_path = args.path
    if not os.path.exists(input_path):
        print("The path does not exist.")
        return
    

    oca_path = get_subdirectories(input_path)
    addons_path = [
        f"{input_path}/server/odoo/addons",
        f"{input_path}/server/addons",
        *oca_path,
        f"{input_path}/addons/third_party_addons",
        f"{input_path}/addons/addons_development",
    ]

    print(", ".join(addons_path))
    return 0
    

if __name__ == "__main__":
    main()
