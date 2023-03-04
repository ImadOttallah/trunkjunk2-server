#!/bin/bash
rm -rf trunkjunk2api/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations trunkjunk2api
python3 manage.py migrate trunkjunk2api
python3 manage.py loaddata users
python3 manage.py loaddata bandana_colors
python3 manage.py loaddata bandana_conditions
python3 manage.py loaddata bandana_markings
python3 manage.py loaddata bandana_patterns
python3 manage.py loaddata bandanas
python3 manage.py loaddata collections
python3 manage.py loaddata bandana_collections
