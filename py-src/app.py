from flask import Flask, render_template, request, jsonify
from chatbot import client  # Import the chatbot client from chatbot.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if user_message:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
            {
            "role": "system",
            "content":" you are a staff of "
            },
            {"role": "user", "content": user_message}
            ],
            temperature=1,
            max_completion_tokens=4096,
            top_p=0.95,
            stream=True,
            stop=None
        )

        response = ""
        for chunk in completion:
            response += chunk.choices[0].delta.content or ""

        remove_until = "</think>"
        index = response.find(remove_until)
        if index != -1:
            response = response[index + len(remove_until):]

        return jsonify({'response': response.strip()})
    return jsonify({'response': 'No message received.'})

if __name__ == '__main__':
    app.run(debug=True)