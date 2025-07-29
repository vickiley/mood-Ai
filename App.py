from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def home():
    return "🎧 AI Playlist Generator is running!"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    mood = data.get("mood", "chill")
    prompt = f"Suggest a trending English playlist for Gen Z based on the mood: {mood}. Include song name and artist."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.8,
        )

        reply = response['choices'][0]['message']['content']
        return jsonify({"playlist": reply})
    except Exception as e:
        return jsonify({"error": str(e)})
