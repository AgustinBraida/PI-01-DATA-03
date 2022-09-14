#Importamos las librerías a utilizar
from fastapi import FastAPI
from router.router import user

app = FastAPI(title='Proyecto Individual 1- Data 03', 
              description='Primer proyecto individual de Henry, en el que crearemos una API utilizando FastAPI.',
              version='1.0.1')


#Pagina principal
app.include_router(user)