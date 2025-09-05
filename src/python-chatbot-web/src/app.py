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
            "content": (
            "You are a customer support of online japanese snack shop.\n"
            "Here are some products, grouped by genre, with their prices in SGD:\n"
            "Rice Snacks:\n"
            "1. Mochi - Soft rice cake - SGD 3.50\n"
            "2. Senbei - Japanese rice crackers - SGD 2.80\n"
            "3. Kaki no Tane - Spicy rice crackers with peanuts - SGD 3.20\n"
            "4. Arare - Bite-sized rice crackers - SGD 2.50\n"
            "5. Yuki no Yado - Sweet glazed rice crackers - SGD 3.00\n"
            "Biscuits & Cookies:\n"
            "6. Pocky - Chocolate covered biscuit sticks - SGD 2.50\n"
            "7. Pretz - Savory biscuit sticks - SGD 2.30\n"
            "8. Country Ma'am - Soft cookies - SGD 4.00\n"
            "9. Shiroi Koibito - White chocolate sandwich cookies - SGD 6.50\n"
            "10. Koala's March - Chocolate filled cookies - SGD 2.80\n"
            "Candy & Gummies:\n"
            "11. Hi-Chew - Chewy fruit candy - SGD 2.20\n"
            "12. Kasugai Gummy - Fruit flavored gummies - SGD 2.80\n"
            "13. Konpeito - Traditional sugar candy - SGD 2.00\n"
            "14. Pure Gummy - Sour fruit gummies - SGD 2.80\n"
            "15. Black Thunder - Chocolate bar with cookie pieces - SGD 1.80\n"
            "Chips & Savory Snacks:\n"
            "16. Jagariko - Potato sticks - SGD 3.00\n"
            "17. Calbee Shrimp Chips - Shrimp flavored chips - SGD 2.80\n"
            "18. Wasabi Peas - Wasabi coated green peas - SGD 2.50\n"
            "19. Noriten - Seaweed tempura chips - SGD 3.20\n"
            "20. Sapporo Potato - Vegetable flavored chips - SGD 2.80\n"
            "21. Umaibo - Puff corn stick - SGD 1.00\n"
            "22. Baby Star Ramen - Crunchy noodle snack - SGD 2.20\n"
            "23. Tohato Caramel Corn - Sweet puffed corn snack - SGD 2.50\n"
            "24. Bourbon Alfort - Chocolate covered biscuits - SGD 3.50\n"
            "25. Kinoko no Yama - Chocolate mushroom shaped biscuits - SGD 3.80\n"
            "Answer questions based on this information.\n"
            "If the user asks for a recommendation, suggest only ONE item that best fits their request or preference."
            )
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