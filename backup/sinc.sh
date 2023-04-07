#!/bin/bash
#
# Script: bk.sh
# Author: Luis Vidal, Iker Nafarrate
#
# Copyright (c) 2023 Busman View.
#
# Description: Script para deshabilitar crones.
#

## BEGIN CONFIG ##
BBDD=$1
USER_POSTGRES=$2
PGPASSWORD=$3
FECHA=$(date +%d%m%Y)
LOG=$4
HOST=$5
path_to_sql_file=$6
## END CONFIG ##

export PGPASSWORD

# ejecutamos script contra pruebas
echo "Procediendo ejecutar sentencia sql..."
psql -h $HOST -U $USER_POSTGRES -d ${BBDD} -p 5432 -f $path_to_sql_file

# reseteando pgpassword
PGPASSWORD=""
export PGPASSWORD


