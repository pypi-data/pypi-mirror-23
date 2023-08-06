Tool: pg_populator_lib

Description:
************

This software is a library for pg_populator, which is  used to populate an already existing PostgreSQL service with:
- N databases. The specific amount of databases is parametrized through the -n argument.
- N tables inside each database. The specific amount of tables is parametrized through the -t argument.
- Some data rows inside every table. The specific amount of rows is parametrized through the -r argument.

This program will make sure that local postgreSQL service contains, at least, the amount of
databases and tables defined in the required command line arguments -n (--num_db) and -t (--num_tables) per database.
It will also add the amount of rows specified in the -r parameter.


Requirements:
*************

A running postgreSQL database must be previously configured.
To make this software works, the user that runs this script must have the ~/.pgpass properly configured.
To get this done, I recommend you to use the scripts stored in the next repository: https://gitlab.com/jaqm/carto_test.git


How to's:
*********

Note: The next commands are meant to be run in the same that directory in which this Readme.1st file is stored.

- Disable any previously activated virtualenv:

$ deactivate

- Enable virtualenv:

$ source venvs/1_populate_db/bin/activate

- Get the program help:

$ pg_populator_lib -v

- Run the tool (example):

Run the next command to create 10 databases with 20 tables and insert 100 rows each of them.

$ pg_populator_lib -n 10 -t 20 -r 100

python3 -m unittest tests/test_pg_populator_lib.py
