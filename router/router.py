from fastapi import APIRouter
from config.db import conn, engine
from model.races import races
from schema.races_schema import RacesSchema
from sqlalchemy import func,Table, Column, desc
from sqlalchemy.orm import sessionmaker


user = APIRouter()
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()
@user.get("/")
def root():
    # return conn.execute(races.select().where(races.c.year == 2019)).fetchall()
    # return conn.execute(Session(func.count(races.year), races.year).group_by(races.year)).all()
    return session.query(races, func.count(races.c.year)).group_by(races.c.year).order_by(desc(races.c.year)).first()


    # with engine.connect() as conn:
    #     result = conn.execute(races.select()).fetchall()

    #     return result

# SELECT COUNT(Anio) AS Cantidad, Anio
# FROM races
# GROUP BY Anio ORDER BY Cantidad DESC;
