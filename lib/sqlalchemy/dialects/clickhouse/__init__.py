from clickhouse_sqlalchemy.drivers import base
from clickhouse_sqlalchemy.drivers.http import base as http_driver

base.dialect = http_driver.dialect
