from flask import Flask, jsonify, request
import uuid
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# In-memory storage
users = []

@app.route('/')
def home():
    return "User Service is running! Use /users to POST or GET users."

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json

    # Basic validation
    if not data or 'name' not in data or 'email' not in data:
        return jsonify({"error": "Name and email are required"}), 400

    if not isinstance(data['name'], str) or not isinstance(data['email'], str):
        return jsonify({"error": "Name and email must be strings"}), 400

    user = {
        "id": str(uuid.uuid4()),
        "name": data['name'].strip(),
        "email": data['email'].strip()
    }
    users.append(user)
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Start the app
if __name__ == '__main__':
    port = int(os.getenv("PORT", 5050))
    app.run(host='0.0.0.0', port=port, debug=False)

