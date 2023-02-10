#!/bin/bash
rm -rf trunkjunk2api/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations trunkjunk2api
python3 manage.py migrate trunkjunk2api
python3 manage.py loaddata users
python3 manage.py loaddata bandanacolors
python3 manage.py loaddata bandanaconditions
python3 manage.py loaddata bandanamarkings
python3 manage.py loaddata bandanapatterns
python3 manage.py loaddata bandanas
python3 manage.py loaddata bandanacollections
python3 manage.py loaddata collections
