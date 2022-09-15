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

drivers = Table("drivers", meta_data, Column(
    "driverId", Integer, primary_key=True),
    Column("nombre", String(200)))

results = Table("results", meta_data, Column(
    "resultsId", Integer, primary_key=True),
    Column("driverId", Integer),
    Column("position", Integer),
    Column("points", Integer),
    Column("constructorId", Integer))
    
constructor = Table("constructor", meta_data, Column(
    "constructorId", Integer, primary_key=True),
    Column("nationality", String(200)))

meta_data.create_all(engine)