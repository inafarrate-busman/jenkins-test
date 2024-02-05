import argparse

from utils import create_repo, update_manifest_file

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--token", help="Token de GitHub API")
parser.add_argument("-m", "--module", help="Nombre del módulo a crear")
parser.add_argument("-o", "--owner", help="Organización del repositorio")
parser.add_argument("-v", "--version", help="Versión")
parser.add_argument("--org", help="Es una compañia", action="store_true")
args = parser.parse_args()

token = args.token
module = args.module
owner = args.owner
is_org = args.org
version = args.version

if not token or not module or not owner:
    parser.error('No se han establecido los parámetros requeridos.')

create_repo(token, module, owner, is_org)
update_manifest_file(token, module, owner, version)
