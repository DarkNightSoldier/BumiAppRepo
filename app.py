import src
from flask import Flask, jsonify, request, make_response
from flask.helpers import send_from_directory
from flask_cors import CORS
from src.objetos.usuario import Cliente, Funcionario

# Ini app.
app = Flask(__name__)

# Cors.
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
  return send_from_directory('./static', path)

# Main page.
@app.route('/')
def root():
    """
    Return the frontend of the application.
    """
    return send_from_directory("./static", 'index.html')

@app.route("/api/status", methods = ["GET"])
def status():
    """
    App Status
    """
    Cliente()
    return jsonify({'status' : 200})

if __name__ == '__main__':
    app.run(debug=False)

@app.route('/usuario/crear_usuario', methods = ["POST"])
def crear_usuario():
    datos = request.data
    cliente = Cliente(*datos)
    
    return jsonify({'status' : 200})