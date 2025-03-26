from django.shortcuts import render
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")  # Ensure using the correct key

def chatbot(request):
    print("Chatbot view called!")  

    if not api_key:
        print("Error: API key not found!")  
        return render(request, 'main.html')

    chatbot_response = None  # Initialize to avoid UnboundLocalError

    if request.method == "POST":
        user_input = request.POST.get("user_input", "").strip()
        print(f"Received User Input: {user_input}")  

        if not user_input:
            print("No user input received.")
            return render(request, 'main.html')

        try:
            client = Groq(api_key=api_key)

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a multilingual translator. Translate the user's text to Nigerian Pidgin accurately while preserving its meaning."},
                    {"role": "user", "content": user_input}
                ]
            )

            chatbot_response = response.choices[0].message.content.strip()
            print(f"Chatbot Response: {chatbot_response}")  

        except Exception as e:
            print(f"Error: {str(e)}")  

    return render(request, 'main.html', {"response": chatbot_response})
