#! /bin/bash

/opt/mssql-tools18/bin/sqlcmd -S ${DATABASE_HOST} -U sa -P ${DATABASE_PASSWORD} -C -i /app/initdb.sql
python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:8000