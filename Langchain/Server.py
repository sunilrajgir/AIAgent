from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route("/")
def home():
    return "Flask server is running on localhost!"


if __name__ == "__main__":
    # Run on localhost (127.0.0.1) on port 5000 with debug mode enabled
    app.run(host="127.0.0.1", port=5000, debug=True)



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