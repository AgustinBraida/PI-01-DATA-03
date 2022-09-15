from sqlalchemy import create_engine, MetaData



#Creamos la conección a la base de datos
engine = create_engine("mysql+pymysql://root:1234567@localhost:3306/PI_01_DATA_03")




meta_data = MetaData()

conn = engine.connect()

