#!/bin/bash

# Nombre de la aplicación
NAME="naaraWeb"

# Directorio del proyecto Django
DJANGODIR=/root/Proyecto-naara/naaraWeb

# Archivo de socket UNIX para comunicarse con Nginx
SOCKFILE=/root/Proyecto-naara/run/gunicorn.sock 

# Usuario y grupo bajo el cual se ejecutará Gunicorn
USER=root
GROUP=root

# Número de trabajadores para Gunicorn
NUM_WORKERS=3

# Módulo de configuración de Django que se utilizará
DJANGO_SETTINGS_MODULE=naaraWeb.settings

# Módulo WSGI de Django que se utilizará para la aplicación
DJANGO_WSGI_MODULE=naaraWeb.wsgi

echo "Corriendo Proyecto $NAME "

cd $DJANGODIR


# Activar el entorno virtual
source venv/bin/activate

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Crear el directorio de ejecución si no existe
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Iniciar Gunicorn
exec venv/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
 --name $NAME \
 --workers $NUM_WORKERS \
 --user=$USER --group=$GROUP \
 --bind=unix:$SOCKFILE \
 --log-level=info \
 --log-file=-