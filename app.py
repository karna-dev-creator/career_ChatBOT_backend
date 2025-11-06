from flask import Flask, request, jsonify
from flask_cors import CORS
from gradio_client import Client

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "✅ Career Chatbot Backend is running!"

@app.route("/api/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        message = data.get("message", "").strip()
        if not message:
            return jsonify({"error": "Empty message"}), 400

        # Fresh session per call
        client = Client("Karna-AI/career_ChatBot")
        result = client.predict(message, api_name="/chat")

        return jsonify({"response": result})
    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
