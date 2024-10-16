# Simple rule-based chatbot

def chatbot_response(user_input):
    # Convert user input to lowercase for easier matching
    user_input = user_input.lower()
    # Responses based on simple if-else logic
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "your name" in user_input:
        return "I'm your friendly chatbot. You can call me ChatBot!"
    elif "what can you do" in user_input:
        return "I can help answer your questions and chat with you!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Running the chatbot
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    if "bye" in user_input.lower():
        break #Fixed indentation here as well
