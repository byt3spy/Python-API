from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
auth = HTTPBasicAuth()

# Import models and resources
from models import User, Item
from resources import item_bp

# Register Blueprints
app.register_blueprint(item_bp, url_prefix='/api/items')

# Basic authentication setup
users = {
    "admin": "password123"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

# Define the index route
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Flask API!"})

# Error handling for 404 - Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for 400 - Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

# Error handling for 500 - Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
