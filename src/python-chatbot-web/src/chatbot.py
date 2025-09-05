from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

client = Groq(
    api_key=os.getenv("API_KEY")  # change your API key here
)

def get_chatbot_response(user_message):
    completion = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",  # change your AI model here
        messages=[
            {
                "role": "system",
                "content": "You are a customer support of online japanese snack shop."
            },
            {
                "role": "user",
                "content": user_message
            }
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

    remove_until = "</think>"  # For some models
    index = response.find(remove_until)
    if index != -1:
        response = response[index + len(remove_until):]

    return response.strip()  # Send this string from response.strip() to your api