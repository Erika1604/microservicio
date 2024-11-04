from flask import Flask, jsonify
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

pedidos = [{"id": 1, "usuario_id": 1, "producto": "Laptop"}]

@app.route('/api/pedidos', methods=['GET'])
def obtener_pedidos():
    return jsonify({"data": pedidos, "status": "success"})

if __name__ == '__main__':
    port = int(os.getenv('ORDERS_SERVICE_PORT', 5001))
    app.run(port=port, debug=True)

