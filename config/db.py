from sqlalchemy import create_engine, MetaData

#Creamos la conección a la base de datos
engine = create_engine("mysql://root:8080/bin/1234567@localhost:3306/PI01_DATA03")

meta_data = MetaData()



