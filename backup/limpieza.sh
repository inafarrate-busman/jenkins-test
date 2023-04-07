#!/bin/bash
#
# Script: bk.sh
# Author: Luis Vidal, Iker Nafarrate
#
# Copyright (c) 2023 Busman View.
#
# Description: busca todos los archivos de mas de 6 dias (en el dir y subdirectorios) con extension .backup y los elimina.
#

path_backups_con_archivos=$1

find $path_backups_con_archivos/ -name "*tar.gz" -mtime +6 -exec rm {} \;
