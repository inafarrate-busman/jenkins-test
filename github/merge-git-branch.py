import argparse

from utils import check_brach_name, get_dev_branch, merge_dev_branch

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--token", help="Token de GitHub API")
parser.add_argument("-m", "--module", help="Nombre del módulo a crear")
parser.add_argument("-o", "--owner", help="Organización del repositorio")
parser.add_argument("-v", "--version", help="Versión")
args = parser.parse_args()

token = args.token
module = args.module
owner = args.owner
version = args.version

if not token or not module or not owner or not version:
    parser.error('No se han establecido los parámetros requeridos.')

check_brach_name(version)
dev_branch = get_dev_branch(version)

merge_dev_branch(token, module, owner, dev_branch, version)

