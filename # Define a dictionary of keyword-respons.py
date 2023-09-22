# Define a dictionary of keyword-response pairs
keyword_responses = {
    "weather": "I can provide you with the current weather information for your location.",
    "news": "I can fetch the latest news headlines for you.",
    "joke": "I can tell you a joke to brighten your day.",
    "help": "I'm here to assist you. Feel free to ask any questions you have!"
}

# Function to get a response
def get_response(message):
    message = message.lower()
    for keyword, description in keyword_responses.items():
        if keyword in message:
            return description
    return "I'm sorry, I don't have information on that topic."

# Main conversation loop
print("Hello! I'm your chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("ChatBot: Goodbye!")
        break
    response = get_response(user_input)
    print("ChatBot:", response)
