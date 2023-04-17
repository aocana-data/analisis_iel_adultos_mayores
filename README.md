# MONSTRY DATA ANALISIS COMPLETITUD Y EXACTITUD

Este proyecto tiene como fin de poder obtener el analisis de completitud y exactitud utilizando un archivo _config.json_ el cual nos permite obtener los distintos tipos de

# BUILDER

Se encarga de cargar todos los datos de la configuración para ser usados dentro del DataClean

# DATA CLEAN

-   sociolaboral.data_columnas():  
    Nos permite obtener la información de la data utilizando samples de la misma data ingestada, se puede usar como elemento previo

# VALIDADORES

-   Funciones donde se manejan por medio de REGEXP:

    LISTA DE VALIDADORES DISPONIBLES EN EL ARCHIVO DE DEFAULT

# MYSQL SAMPLE

-   Verifica la conexion con una db creada en mysql-docker steps para crearla, directamente con la base creada en el volumen
    -   Pasos para levantar la base de prueba:
    -   sudo docker compose up -d --build
    -   sudo docker exec mysql mysql -u root -p1234 -h mysql -e "create database users;"
    -   sudo docker exec -it mysql bash
        -   mysql -u root -p1234 -h localhost --port=3306 users < /var/lib/db_mysql/dump_db.sql
