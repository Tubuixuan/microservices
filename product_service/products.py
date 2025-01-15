products = [
    {"id": 1, "name": "Laptop", "price": 1500},
    {"id": 2, "name": "Phone", "price": 800}
]

def get_all_products():
    return products

def get_product_by_id(product_id):
    return next((product for product in products if product['id'] == product_id), None)