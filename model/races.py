from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String, Integer
from config.db import meta_data, engine

races = Table("races", meta_data, Column(
    "raceId", Integer, primary_key=True),
    Column("year", Integer),
    Column("round", Integer),
    Column("circuitId", Integer),
    Column("name", String(200)),
    Column("date", String(200)),
    Column("time", String(200)),
    Column("url", String(200)))

meta_data.create_all(engine)