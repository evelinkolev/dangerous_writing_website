from flask import Flask, render_template, request, session, jsonify
import time
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure random key

# Configuration
TIMEOUT_SECONDS = 5

# Sample text
RANDOM_TEXTS = [
    "Could you tell me about yourself and describe your background in brief?",
    "How did you hear about this position?",
    "What type of work environment do you prefer?",
    "How do you deal with pressure or stressful situations?",
    "Do you prefer working independently or on a team?"
]

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_text')
def generate_text():
    random_text = random.choice(RANDOM_TEXTS)
    session['text'] = random_text
    session['last_updated'] = time.time()
    return jsonify({'text': random_text})

@app.route('/save_text', methods=['POST'])
def save_text():
    text = request.form.get('text', '')

    # Update session with current time and text
    session['last_updated'] = time.time()
    session['text'] = text

    return jsonify({'status': 'Text saved successfully'})

@app.route('/get_text')
def get_text():
    # Return current text
    text = session.get('text', '')
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)
