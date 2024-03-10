from flask import Flask, render_template, request, jsonify
import json
import re
import numpy as np

app = Flask(__name__)

# Load intents from JSON file
def load_intents(file_path):
    with open(file_path, 'r') as file:
        intents = json.load(file)
        return intents

# Load intents from JSON
intents_file_path = 'intents.json'  # Specify the path to your intents JSON file
intents = load_intents(intents_file_path)

# Chatbot function
def chatbot_response(user_input):
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
    
    return response

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for chat
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    bot_response = chatbot_response(user_input)
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
