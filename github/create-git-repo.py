import argparse
import sys

from utils import create_repo

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--token", help="Token de GitHub API")
parser.add_argument("-m", "--module", help="Nombre del módulo a crear")
parser.add_argument("-o", "--owner", help="Propietario del repositorio")
parser.add_argument("-v", "--version", help="Versión")
args = parser.parse_args()

token = args.token
module = args.module
owner = args.owner
version = args.version

if not token or not module or not owner or not version:
    parser.error('No se han establecido los parámetros requeridos')

create_repo(token, module, owner)

