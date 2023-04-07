#!/bin/bash
#
# Script: bk.sh
# Author: Luis Vidal, Iker Nafarrate
#
# Copyright (c) 2023 Busman View.
#
# Description: Crea una copia de seguridad de una base de datos de PostgreSQL
#

## BEGIN CONFIG ##								          
BBDD=$1
USER_POSTGRES=$2
PGPASSWORD=$3
HORA=$(date +%H%M%S) 
FECHA=$(date +%d%m%Y)
DIA=$(date +%w)
DIA1=$(date +%d)
MES=$(date +%B)
MES_NUM=$(date +%m)
MES_ANTERIOR=`expr $MES_NUM - 1`
BACKUP_DIR=$4
LOG=$5
LOG_DIARIO=$6
## END CONFIG ##

export PGPASSWORD

# TODO: eliminar sesiones abiertas

# Si no existen directorios para backups y logs los creamos en las rutas especificadas arriba

if [ ! -d $BACKUP_DIR ]; then
    mkdir -p $BACKUP_DIR
    fi

if [ ! -d $LOG ]; then
    mkdir -p $LOG
    fi

if [ ! -d $LOG_DIARIO ]; then
    mkdir -p $LOG_DIARIO
    fi


# Realizamos el backup 
echo "Creando la copia de seguridad ..."
/usr/bin/pg_dump --host localhost --port 5432 --verbose --username $USER_POSTGRES --format custom --blobs --file "$BACKUP_DIR/${BBDD}${FECHA}.backup" $BBDD > $LOG/bk_${FECHA}_dump.log 2>& 1  

# reseteando pgpassword
PGPASSWORD=""
export PGPASSWORD
