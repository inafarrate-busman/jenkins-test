#!/bin/bash
#
# Script: bk.sh
# Author: Luis Vidal, Iker Nafarrate
#
# Copyright (c) 2023 Busman View.
#
# Description: Script para Restaura BD en copia.
#

## BEGIN CONFIG #
BBDD=$1
BBDD2=$2
USER_POSTGRES=$3
PGPASSWORD=$4
FECHA=$(date +%d%m%Y)
BACKUP_DIR=$5
## END CONFIG ##

export PGPASSWORD

# Borramos la base de datos copia
/usr/bin/dropdb -U $USER_POSTGRES ${BBDD2}

# Creamos de nuevo la base de datos vacía copia
echo "Creando la base de datos vacía ${BBDD2}..."
/usr/bin/createdb -U $USER_POSTGRES -T template1 ${BBDD2}

# Restauramos el backup a la base de datos vacía copia
echo "Procediendo a hacer la restauración del backup..."
/usr/bin/pg_restore --host localhost --port 5432 --username $USER_POSTGRES --dbname "${BBDD2}" "$BACKUP_DIR/${BBDD}${FECHA}.backup" 

# reseteando pgpassword
PGPASSWORD=""
export PGPASSWORD
