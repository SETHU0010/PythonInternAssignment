from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import socket
import json

app = Flask(__name__)

# Task 2: Database Management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apps.db'
db = SQLAlchemy(app)

# Database Model
class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(80), nullable=False)
    version = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(200), nullable=False)

def initialize_db():
    with app.app_context():
        db.create_all()
        # Add sample data
        sample_app = App(app_name="Sample App", version="1.0", description="A sample app.")
        db.session.add(sample_app)
        db.session.commit()

# Task 1: Backend Development
@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.get_json()
    new_app = App(app_name=data['app_name'], version=data['version'], description=data['description'])
    db.session.add(new_app)
    db.session.commit()
    return jsonify({"message": "App added successfully", "id": new_app.id}), 201

@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    app_entry = App.query.get(id)
    if app_entry:
        return jsonify({"id": app_entry.id, "app_name": app_entry.app_name, "version": app_entry.version, "description": app_entry.description})
    return jsonify({"error": "App not found"}), 404

@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    app_entry = App.query.get(id)
    if app_entry:
        db.session.delete(app_entry)
        db.session.commit()
        return jsonify({"message": "App deleted successfully"})
    return jsonify({"error": "App not found"}), 404

@app.route('/')
def index():
    return render_template('index.html')

# Task 3: Virtual Android System Simulation
class VirtualAndroidSystem:
    def __init__(self):
        self.device_model = "VirtualDeviceX"
        self.os_version = "Android 12.0"
        self.memory = "4GB"

    def display_system_info(self):
        system_info = {
            "Device Model": self.device_model,
            "OS Version": self.os_version,
            "Available Memory": self.memory
        }
        print("System Info:", system_info)
        return system_info

    def install_app(self, apk_name):
        print(f"Installing {apk_name}...")
        return f"{apk_name} installed successfully!"

virtual_android = VirtualAndroidSystem()

# Task 4: Basic Networking
@app.route('/send-data', methods=['POST'])
def send_data():
    server_host = "127.0.0.1"
    server_port = 65432

    # Mock data from the virtual Android system
    data_to_send = {
        "device_id": "12345",
        "system_info": virtual_android.display_system_info()
    }

    # Send data to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_host, server_port))
        s.sendall(json.dumps(data_to_send).encode('utf-8'))
        response = s.recv(1024).decode('utf-8')
        print("Received from server:", response)
    return jsonify({"response": response})

# Run Flask API
if __name__ == '__main__':
    with app.app_context():
        initialize_db()
    app.run(debug=True)
