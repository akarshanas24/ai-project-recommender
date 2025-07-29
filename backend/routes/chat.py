from flask import Blueprint, render_template, session, redirect, request, jsonify, url_for

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat')
def chat():
    if 'user_id' not in session:
        return redirect(url_for('login_page'))
    return render_template('chat.html')

# Handle chat messages from frontend
@chat_bp.route('/chat', methods=['POST'])
def chat_api():
    if 'user_id' not in session:
        return jsonify({'reply': 'Please login to use the chatbot.'})
    data = request.get_json()
    user_message = data.get('message', '')
    # TODO: Integrate with Ollama/LLaMA 3 for real responses
    # For now, reply with a static example
    if 'aiml' in user_message.lower():
        reply = "Here are some AI/ML project ideas:\n1. Image Classification with CNNs\n2. Sentiment Analysis using NLP\n3. Fraud Detection with Machine Learning\n4. Recommendation System\n5. Chatbot using LLMs"
    else:
        reply = "Ask me for project ideas in AI/ML, Web, Mobile, IoT, Data Science, or Blockchain!"
    return jsonify({'reply': reply})
print("✅ chat.py loaded successfully!")
