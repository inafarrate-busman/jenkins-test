#!/bin/bash
#
# Script: bk.sh
# Author: Luis Vidal, Iker Nafarrate
#
# Copyright (c) 2023 Busman View.
#
# Description: Script para backups.
#

## BEGIN CONFIG ##								          
FECHA=$(date +%d%m%Y)
path_backups_con_archivo=$1
path_backups=$2 
path_archivos=$3
has_muk=$4
path_muk=$5
## END CONFIG ##

if [ $has_muk == 1 ]
then
    tar -czvf $path_backups_con_archivo/$FECHA.archbd.tar.gz $path_backups $path_archivos $path_muk
else
    tar -czvf $path_backups_con_archivo/$FECHA.archbd.tar.gz $path_backups $path_archivos
fi