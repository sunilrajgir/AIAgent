from flask import Flask, jsonify, request, render_template
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = BASE_DIR / "templates"
EXPECTED_FILE = TEMPLATE_DIR / "index.html"

print("\n" + "="*50)
print(f"1. Flask is looking in: {TEMPLATE_DIR}")
print(f"2. Does templates folder exist? {TEMPLATE_DIR.exists()}")
print(f"3. Does index.html exist inside it? {EXPECTED_FILE.exists()}")
if TEMPLATE_DIR.exists():
    print(f"4. Actual contents of templates folder: {os.listdir(TEMPLATE_DIR)}")
print("="*50 + "\n")

# Explicitly point Flask to the correct folder
app = Flask(__name__, template_folder=str(TEMPLATE_DIR))


# Initialize the Flask application
port = 5000
# app = Flask(__name__, template_folder=template_dir)
host = "127.0.0.1"

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')
    # return "Flask server is running on localhost!"

#http://localhost:5000/

if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)




@app.route("/api/user", methods=["GET"])
def get_user_profile():
    # This data is sent back as JSON (like an Express res.json)
    user_info = {
        "username": "coder123",
        "role": "developer",
        "status": "active"
    }
    return jsonify(user_info)


@app.route("/api/login", methods=["POST"])
def login_user():
    # Grab the JSON data sent in the request body
    incoming_data = request.get_json()
    
    # Read specific fields from the sent data
    username = incoming_data.get("username")
    password = incoming_data.get("password")
    
    # Process the data (Simple check for demonstration)
    if username == "coder123" and password == "secret123":
        return jsonify({"message": "Login successful!", "authenticated": True}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401