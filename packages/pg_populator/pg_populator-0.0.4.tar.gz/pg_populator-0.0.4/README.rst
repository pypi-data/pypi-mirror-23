Tool: pg_populator

Description:
************

This program populates an already existing PostgreSQL service with:
- N databases. The specific amount of databases is parametrized through the -n argument.
- N tables inside each database. The specific amount of tables is parametrized through the -t argument.
- Some data rows inside every table. The specific amount of rows is parametrized through the -r argument.

This program will make sure that local postgreSQL service contains, at least, the amount of
databases and tables defined in the required command line arguments -n (--num_db) and -t (--num_tables) per database.
It will also add the amount of rows specified in the -r parameter.
This program will NOT delete any database, table or row.


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

$ ./run -v

- Run the tool (example):

Run the next command to create 10 databases with 20 tables and insert 100 rows each of them.

$ ./run -n 10 -t 20 -r 100

