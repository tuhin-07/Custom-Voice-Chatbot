# Flask Server

from flask import Flask, request, render_template, jsonify
import openai
import os
import requests

# openai.api_key = os.environ.get("OPENAI_API_KEY")

api = "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"

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
headers = {"Authorization": f"Bearer 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"}

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message", "")
    print('user_message: ',user_message)
    payload = {"inputs": user_message}

    response = requests.post(API_URL, headers=headers, json=payload)
    hf_response = response.json()
    reply = hf_response[0]["generated_text"] if isinstance(hf_response, list) else str(hf_response)
    print(reply,'----------------')
    return jsonify({"response": reply})
    # response = openai.ChatCompletion.create(
    #     model="gpt-4o",  # Or gpt-3.5-turbo
    #     messages=[{"role": "user", "content": user_message}]
    # )
    # reply = response.choices[0].message.content
    # return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)


