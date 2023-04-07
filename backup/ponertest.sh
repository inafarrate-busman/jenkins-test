#!/bin/bash
#
# Script: bk.sh
# Author: Luis Vidal, Iker Nafarrate
#
# Copyright (c) 2023 Busman View.
#
# Description: Instala los módulos necesarios a la hora de iniciar el entorno.
#


python_path=$1
odoo_path=$2
config=$3
BBDD=$4
modules=$5

if [ ! -z "$modules" ]
then
    sudo -i -u bmv $python_path/python3 $odoo_path -c $config -d $BBDD -i $modules --stop-after-init
fi

