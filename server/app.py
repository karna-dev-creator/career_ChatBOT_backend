from flask import Flask, request, jsonify
from gradio_client import Client
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend access

# Connect to your Hugging Face Space
client = Client("Karna-AI/career_ChatBot")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    try:
        result = client.predict(message, api_name="/chat")
        return jsonify({"response": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
