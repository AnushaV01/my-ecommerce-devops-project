from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)
users = []

@app.route('/')
def home():
    return "User Service is running! Use /users to POST or GET users."

@app.route('/users', methods=['POST'])
def create_users():
    data=request.json
    user={
        "name":data['name'],
        "email":data['email'],
        "id":str(uuid.uuid4())
    }
    users.append(user)
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5050)
