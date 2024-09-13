from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

products = [
    {'id': 1, 'name': 'Laptop', 'price': 1000},
    {'id': 2, 'name': 'Smartphone', 'price': 500}
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = {
        'id': len(products) + 1,
        'name': data['name'],
        'price': data['price']
    }
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/api/sync', methods=['POST'])
def sync_data():
    sync_status = {'status': 'Data Sync Completed Successfully'}
    return jsonify(sync_status), 200

if __name__ == '__main__':
    app.run(debug=True)
