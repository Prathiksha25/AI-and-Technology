faq_data = {
    "what programs does iron lady offer": 
        "Iron Lady offers leadership programs designed for women to build confidence, communication, and career growth skills.",
    
    "what is the program duration": 
        "The duration of Iron Lady programs typically ranges from a few weeks to several months, depending on the specific course.",
    
    "is the program online or offline": 
        "Iron Lady programs are available both online and offline for flexible learning.",
    
    "are certificates provided": 
        "Yes, certificates are provided upon successful completion of the program.",
    
    "who are the mentors" : 
        "The mentors are experienced leaders, coaches, and industry professionals dedicated to empowering women."
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for question, answer in faq_data.items():
        if question in user_input:
            return answer
    return "Sorry, I don’t know the answer to that. Please try asking about the program, duration, certificates, or mentors."

def chatbot():
    print("🤖 Iron Lady Chatbot: Ask me about our leadership programs (type 'exit' to quit).")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("🤖 Chatbot:", response)

# Run chatbot
if __name__ == "__main__":
    chatbot()
