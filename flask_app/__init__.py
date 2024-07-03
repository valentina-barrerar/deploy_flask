#Importar Flask
from flask import Flask

#Inicializar la app
app = Flask(__name__)

#Indicar clave secreta, necesaria para la sesión
app.secret_key = "Llave secreta"