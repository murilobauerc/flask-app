''' importamos a classe base do Flask, ou seja, o Werkzeug que é uma biblioteca WSGI para enfim ter a abstração de métodos simples
    e termos o workflow que desejamos.
'''
from flask import Flask

# criamos uma instancia da classe base do Flask que chamaremos de app
app = Flask('flask-app')

@app.route("/")
def hello_world():
    return "Olá mundo! Essa é a minha primeira aplicação web utilizando Flask!", 200

app.run()