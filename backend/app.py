from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login_page'))

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        # TODO: Add login logic here
        return redirect(url_for('chat'))
    return render_template('login.html')
@app.route('/chat', methods=['GET'])
def chat():
    return render_template('chat.html')

# Chatbot backend route
import requests
from flask import jsonify
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message', '')
    # Prepend a system prompt for project-related queries
    system_prompt = (
        "You are an expert AI project recommender. "
        "If the user asks for project suggestions, reply with a list of at least 5 project ideas. "
        "For each project, provide only the Title and a 1-2 sentence Description. "
        "Output each project on a separate line, not as a paragraph. Do not include skills, timeline, or tech stack unless the user asks for details about a specific project.\n"
        "Strictly format your response as follows (each project on its own line):\n"
        "1. Project Title 1: Short description.\n"
        "2. Project Title 2: Short description.\n"
        "3. Project Title 3: Short description.\n"
        "4. Project Title 4: Short description.\n"
        "5. Project Title 5: Short description.\n"
        "(Do not use paragraphs. Do not combine multiple projects in one line. Each project must be on its own line.)\n"
        "If the user asks for details about a specific project, then provide: Skills required, Estimated Timeline, and Recommended Tech Stack for that project.\n"
        "If the user says hi/hello/bye, respond briefly and politely. "
        "If the user asks something else, do your best to help.\n"
    )
    # Only prepend for project-related queries
    if any(word in user_message.lower() for word in ["project", "suggest", "idea", "recommend", "machine learning", "ai", "ml", "deep learning", "data science"]):
        prompt = system_prompt + "\nUser: " + user_message
    else:
        prompt = user_message
    try:
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                'model': 'llama3',
                'prompt': prompt,
                'stream': False
            },
            timeout=120
        )
        data = response.json()
        reply = data.get('response', 'Sorry, I could not generate a response.')
    except Exception as e:
        reply = f"Error communicating with Ollama: {e}"
    return jsonify({'reply': reply})

@app.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        # TODO: Add signup logic here
        return 'Signup POST received (add logic)'
    return render_template('signup.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Avoid favicon error

if __name__ == '__main__':
 app.run(debug=True)