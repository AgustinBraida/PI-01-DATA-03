from fastapi import APIRouter
from config.db import conn, engine
from model.tablas import races, drivers, results, constructor
from schema.races_schema import RacesSchema
from sqlalchemy import func,Table, Column, desc
from sqlalchemy.orm import sessionmaker


user = APIRouter()
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session()

@user.get("/")
def root():
    # return conn.execute(races.select()).fetchall()
    primer_puesto = session.query(results, func.count(results.c.position)).where(results.c.position == 1).group_by(results.c.driverId).order_by(desc(results.c.position)).first()
    circuito = session.query(races, func.count(races.c.name)).group_by(races.c.name).order_by(desc(races.c.name)).first()
    year = session.query(races, func.count(races.c.year)).group_by(races.c.year).order_by(desc(races.c.year)).first()
    return f"El Año con más carrera fue el: {year['year']}   ||   El circuito más corrido: {circuito['name']}   ||   El Piloto con mayor cantidad de primeros puestos es: Lewis Hamilton con el ID: {primer_puesto['driverId']}"
