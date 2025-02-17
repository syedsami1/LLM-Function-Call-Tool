import sys
import os
# Adding the 'app' directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))

from flask import Flask, request, jsonify
from model_loader import llm  # Now import llm from model_loader

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the LLM Chatbot API!"

    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = llm(user_input)
    return jsonify({"response": response})
if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000, debug=True)
