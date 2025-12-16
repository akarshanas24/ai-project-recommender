from flask import Blueprint, request, jsonify
from recommender.llm import generate_recommendations
from recommender.session_manager import SessionManager

api = Blueprint('api', __name__)
session_manager = SessionManager()

@api.route('/recommend', methods=['POST'])
def recommend():
    user_id = request.json.get('user_id')
    user_query = request.json.get('query')

    if not user_id or not user_query:
        return jsonify({'error': 'User ID and query are required.'}), 400

    session = session_manager.get_session(user_id)
    recommendations = generate_recommendations(user_query, session)

    return jsonify({'recommendations': recommendations})