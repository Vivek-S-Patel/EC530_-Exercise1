from flask import Flask, request

app = Flask(__name__)

# Dummy database
users = []
houses = []
rooms = []
devices = []

# User Routes
@app.route('/users', methods=['POST'])
def create_user():
    username = request.json.get('username')
    house_id = request.json.get('house_id')
    return ""

@app.route('/users', methods=['GET'])
def get_users():
    return ""

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    username = request.json.get('username')
    house_id = request.json.get('house_id')
    return ""

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return ""

# House Routes
@app.route('/houses', methods=['POST'])
def create_house():
    username = request.json.get('username')
    num_rooms = request.json.get('num_rooms')
    return ""

@app.route('/houses', methods=['GET'])
def get_houses():
    return ""

@app.route('/houses/<int:house_id>', methods=['PUT'])
def update_house(house_id):
    username = request.json.get('username')
    num_rooms = request.json.get('num_rooms')
    return ""

@app.route('/houses/<int:house_id>', methods=['DELETE'])
def delete_house(house_id):
    return ""

# Room Routes
@app.route('/rooms', methods=['POST'])
def create_room():
    username = request.json.get('username')
    room_name = request.json.get('room_name')
    return ""

@app.route('/rooms', methods=['GET'])
def get_rooms():
    return ""

@app.route('/rooms/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    username = request.json.get('username')
    room_name = request.json.get('room_name')
    return ""

@app.route('/rooms/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    return ""

# Device Routes
@app.route('/devices', methods=['POST'])
def create_device():
    username = request.json.get('username')
    device_type = request.json.get('device_type')
    house_id = request.json.get('house_id')
    return ""

@app.route('/devices', methods=['GET'])
def get_devices():
    return ""

@app.route('/devices/<int:device_id>', methods=['PUT'])
def update_device(device_id):
    username = request.json.get('username')
    device_type = request.json.get('device_type')
    house_id = request.json.get('house_id')
    return ""

@app.route('/devices/<int:device_id>', methods=['DELETE'])
def delete_device(device_id):
    return ""

if __name__ == '__main__':
    app.run(debug=True)
