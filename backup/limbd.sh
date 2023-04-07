#!/bin/bash
#
# Script: bk.sh
# Author: Luis Vidal, Iker Nafarrate
#
# Copyright (c) 2023 Busman View.
#
# Description: Busca todos los archivos de mas de 4 dias (en el dir y subdirectorios) con extension .backup y los elimina.
#
backup_path=$1

find $backup_path/ -name "*.backup" -mtime +4 -exec rm {} \;