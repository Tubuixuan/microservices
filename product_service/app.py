from flask import Flask, jsonify, request
from products import get_all_products, get_product_by_id

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(get_all_products())

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)