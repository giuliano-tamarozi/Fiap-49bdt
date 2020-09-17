from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Hola FIAP!</h1>\nMBA! versão 2 o/"

if __name__ == '__main__':
    application.run()
