from fastapi import APIRouter
from config.db import engine
from schema.races_schema import RacesSchema

user = APIRouter()

# @user.get("/")
# def root(data_races : RacesSchema):
#     with engine.connect() as conn:
#         result = conn.execute(data_races.select().where(data_races.c.Anio)).first()

#         return result

# SELECT COUNT(Anio) AS Cantidad, Anio
# FROM races
# GROUP BY Anio ORDER BY Cantidad DESC;
