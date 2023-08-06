=============
pycsvdb
=============
Read csv and insert into DB
Requirements
-----------------

- Python 3.x
- hashlib
- pandas
- sqlalchemy
- shelve
- numpy

Installation
-----------------
::

    $ pip install pycsvdb


Example
-----------------

::

   from pycsvdb import CsvManage

   CsvManage(db_config_file="config.ini", file_name="filename.csv", primary_key="id", table_name="table_name")

Confi.ini format
-----------------

::

    [DB]


    sqlalchemy.url = postgresql://postgres:password@localhost:5432/postgres

    stage_schema = stage_table

    prod_schema = prod_table
