from flask import Flask, jsonify, request
from users import get_all_users, get_user_by_id

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(get_all_users())

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)