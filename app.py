from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory list of valid keys (resets if app restarts)
valid_keys = [
    "RIALR-KHSHA-4P5PU-YHR4Z"
]

@app.route("/")
def home():
    return "Key-based Login API is running!"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    key = data.get("key")

    if key in valid_keys:
        return jsonify({"status": "success", "token": "fake_jwt_token"})
    else:
        return jsonify({"status": "error", "message": "Invalid key"}), 401

@app.route("/add_key", methods=["POST"])
def add_key():
    data = request.get_json()
    new_key = data.get("key")

    if new_key and new_key not in valid_keys:
        valid_keys.append(new_key)
        return jsonify({"status": "success", "message": f"Key {new_key} added"})
    else:
        return jsonify({"status": "error", "message": "Key already exists or invalid"}), 400

@app.route("/remove_key", methods=["POST"])
def remove_key():
    data = request.get_json()
    key_to_remove = data.get("key")

    if key_to_remove in valid_keys:
        valid_keys.remove(key_to_remove)
        return jsonify({"status": "success", "message": f"Key {key_to_remove} removed"})
    else:
        return jsonify({"status": "error", "message": "Key not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
