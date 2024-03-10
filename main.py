import json
import re
import numpy as np

# Load intents from JSON file
def load_intents(file_path):
    with open(file_path, 'r') as file:
        intents = json.load(file)
        return intents

# Load intents from JSON
intents_file_path = 'intents.json'  # Specify the path to your intents JSON file
intents = load_intents(intents_file_path)

# Main loop
print("Chatbot: Hello! How can I help you today?")
while True:
    user_input = input("You: ")

    # Check for specific patterns in user input
    matched_intent = None
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            # Modify pattern to include character classes and make it case insensitive
            pattern_regex = re.sub(r'\b(\w+)\b', r'(\1|u)', pattern)  # Replace "you" with "(you|u)"
            if re.search(pattern_regex, user_input, re.IGNORECASE):
                matched_intent = intent
                break
        if matched_intent:
            break

    # Select response based on matched intent
    if matched_intent:
        response = np.random.choice(matched_intent['responses'])
    else:
        response = "I'm sorry, I don't understand."

    print("Chatbot:", response)
