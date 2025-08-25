from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json(force=True, silent=True) or {}
        msg = data.get("message", "")
        return jsonify({"reply": f"Otrzymano: {msg}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/health", methods=["GET"])
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
