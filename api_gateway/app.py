from flask import Flask, jsonify, request
import requests #gửi và nhận dữ liệu từ các dịch vụ web thông qua HTTP

app = Flask(__name__)

USER_SERVICE_URL = "http://localhost:5001"
PRODUCT_SERVICE_URL = "http://localhost:5002"

@app.route('/users', methods=['GET'])
def get_users():
    response = requests.get(f"{USER_SERVICE_URL}/users")
    return jsonify(response.json())

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    response = requests.get(f"{USER_SERVICE_URL}/users/{user_id}")
    return jsonify(response.json()), response.status_code

@app.route('/products', methods=['GET'])
def get_products():
    response = requests.get(f"{PRODUCT_SERVICE_URL}/products")
    return jsonify(response.json())

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    response = requests.get(f"{PRODUCT_SERVICE_URL}/products/{product_id}")
    return jsonify(response.json()), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)