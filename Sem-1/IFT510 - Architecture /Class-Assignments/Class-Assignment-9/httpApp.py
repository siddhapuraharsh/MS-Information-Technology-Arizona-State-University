# Name: Harsh Siddhapura
# Enrollment No.: 1230169813
# Date: 10/20/2023

from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data as a dictionary (you can replace this with a database)
data = {
    '1': {'name': 'Harsh', 'age': 22},
    '2': {'name': 'Ramaswami', 'age': 19},
    '3': {'name': 'John', 'age': 30},
    '4': {'name': 'Alice', 'age': 25}
}

@app.route('/', methods=['GET'])
def home():
    return jsonify("Hello IFT 510 Class 3:30 PM")

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(data)

@app.route('/api/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = data.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@app.route('/api/users', methods=['POST'])
def create_user():
    new_user = request.json
    if 'name' in new_user and 'age' in new_user:
        user_id = str(len(data) + 1)
        data[user_id] = new_user
        return jsonify({'message': 'User created', 'user_id': user_id}), 201
    return jsonify({'error': 'Invalid request data'}), 400

@app.route('/api/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    user = data.get(user_id)
    if user:
        updated_user = request.json
        user.update(updated_user)
        return jsonify({'message': 'User updated', 'user': user})
    return jsonify({'error': 'User not found'}), 404

@app.route('/api/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = data.get(user_id)
    if user:
        del data[user_id]
        return jsonify({'message': 'User deleted'})
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)