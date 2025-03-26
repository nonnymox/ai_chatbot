from django.shortcuts import render
import openai, os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("OPENAI_KEY")
print(f"API Key Loaded: {api_key[:5]}...")  # Debugging print

def chatbot(request):
    print("Chatbot view called!")  # Debugging print
    

    if not api_key:
        print("Error: API key not found!")  # Debugging print
        return render(request, 'main.html')

    if request.method == "POST":
        user_input = request.POST.get("user_input", "").strip()
        print(f"Received User Input: {user_input}")  # Debugging print

        if not user_input:
            print("No user input received.")
            return render(request, 'main.html')

        try:
            # client = openai.OpenAI(api_key=api_key)  # Pass API key to client
            client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
            )

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": user_input}],

            )
            # response = client.chat.completions.create(
            #     model="gpt-3.5-turbo",
            #     messages=[{"role": "user", "content": user_input}],
            #     max_tokens=512,
            #     temperature=0.5
            # )

            chatbot_response = response.choices[0].message.content.strip()
            print(f"Chatbot Response: {chatbot_response}")  # Debugging print

        except Exception as e:
            print(f"Error: {str(e)}")  # Debugging error print

    return render(request, 'main.html', {"response": chatbot_response})
