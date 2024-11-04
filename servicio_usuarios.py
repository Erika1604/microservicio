from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

usuarios = [{"id": 1, "nombre": "Ana"}, {"id": 2, "nombre": "Berto"}]

@app.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify({"data": usuarios, "status": "success"})

if __name__ == '__main__':
    port = int(os.getenv('USERS_SERVICE_PORT', 5000))
    app.run(port=port, debug=True)
