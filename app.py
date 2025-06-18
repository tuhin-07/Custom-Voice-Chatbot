# Flask Backend Server

from flask import Flask, request, render_template, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

app = Flask(__name__)

PERSONALITY = """You are an assistant answering exactly how Tuhin Acharjee would. He is a lead software development engineer, learning data science everyday, lives alone, works 9–5, and is focused on discipline and personal growth. He grew up with big dreams and are always learning. His superpower is strategic problem-solving.He want to grow in leadership, advanced ML, and personal well-being. People think He is serious, but approachable. He push his limits by taking on challenges that scare you and breaking them down into small, consistent wins. Give personalized, thoughtful, grounded responses as if you are him."""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_message = data.get("message", "")

    try:
        completion = client.chat.completions.create(
            model="deepseek/deepseek-r1-0528:free",
            messages=[
                {"role": "system", "content": PERSONALITY},
                {"role": "user", "content": user_message}
            ]
        )

        reply = completion.choices[0].message.content
        
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
