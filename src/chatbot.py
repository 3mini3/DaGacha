from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

client = Groq(
    # DO NOT PUT API KEY ON GITHUB, USE .env FILE IF YOU ARE
    api_key = os.getenv("API_KEY")  # change your API key here
)
completion = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",  # change your AI model here
    messages=[
        {
        "role": "system",
        "content": "You are a customer support of online japanese snack shop."
      },
      {
        "role": "user",
        "content": ""
      },
      {"role" : "user",
       "content" :""
       }
    ],
    # when you change model, remember to change down here too!
    # For hallucination, experiment with this number. From 0 to 2.
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
    
print(response.strip())  # Send this string from response.strip() to your api