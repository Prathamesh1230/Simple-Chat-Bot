import random
import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey! How can I help you?"]],
    ["how are you?", ["I'm good, how about you?", "I'm doing great!"]],
    ["what is your name?", ["I am a simple chatbot.", "You can call me ChatBot!"]],
    ["(.*) your name?", ["I am a chatbot created to assist you."]],
    ["bye|goodbye", ["Goodbye!", "See you later!", "Take care!"]],
    ["(.*)", ["I am not sure about that.", "Can you rephrase?", "Tell me more!"]]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start chatting
print("Hello! I am a simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input == "bye":
        print("Chatbot: Goodbye! Have a nice day! 😊")
        break
    response = chatbot.respond(user_input)
    print("Chatbot:", response)
