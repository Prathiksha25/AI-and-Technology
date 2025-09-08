import os
from groq import Groq
from dotenv import load_dotenv

# Load your environment variables from .env (if using it)
load_dotenv()

# Get your Groq API key from environment
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize the client
client = Groq(api_key=groq_api_key)

def ai_chatbot_response(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Updated working model
        messages=[
            {"role": "system", "content": "You are Iron Lady AI, a helpful assistant for leadership programs."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def chatbot():
    print("🤖 Iron Lady AI Chatbot (Groq): Ask me anything (type 'exit' to quit).")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break
        response = ai_chatbot_response(user_input)
        print(f"🤖 Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
