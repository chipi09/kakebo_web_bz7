from flask import Flask

app = Flask(__name__) #crear una instancia de Flask

@app.route('/') #decorador
def index():
    return 'Hola, mundo!'

@app.route('/adios')
def bye():
    return 'hasta luego, cocodrilo'
