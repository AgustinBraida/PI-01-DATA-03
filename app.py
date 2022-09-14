#Importamos las librerías a utilizar
from fastapi import FastAPI

appo = FastAPI(title='Proyecto Individual 1- Data 03', 
              description='Primer proyecto individual de Henry, en el que crearemos una API utilizando FastAPI.',
              version='1.0.1')


#Pagina principal
@appo.get('/')
async def index():
    return 'Hola mundo'