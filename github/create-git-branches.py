import argparse

from utils import rename_main_branch, create_new_branch

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--token", help="Token de GitHub API")
parser.add_argument("-m", "--module", help="Nombre del módulo a crear")
parser.add_argument("-o", "--owner", help="Organización del repositorio")
parser.add_argument("-u", "--user", help="Usuario del repositorio")
parser.add_argument("-v", "--version", help="Versión")
args = parser.parse_args()

token = args.token
module = args.module
owner = args.owner
user = args.user
version = args.version

if not token or not module or (not owner and not user) or not version:
    parser.error('No se han establecido los parámetros requeridos.')

if owner and user:
    parser.error('No se puede indicar una organización y un usuario al mismo tiempo.')

is_org = True if owner else False
user = user or owner

branch_sha = rename_main_branch(token, module, user, version)

dev_branch = f"{version}_dev"
create_new_branch(token, module, user, dev_branch, branch_sha)