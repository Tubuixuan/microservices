users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

def get_all_users():
    return users

def get_user_by_id(user_id):
    return next((user for user in users if user['id'] == user_id), None)