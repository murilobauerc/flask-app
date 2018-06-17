from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Olá mundo! Essa é a minha primeira aplicação web utilizando Flask!", 200

app.run()