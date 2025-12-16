from flask import jsonify
import requests

class LLMInterface:
    def __init__(self, model_url):
        self.model_url = model_url

    def generate_response(self, prompt):
        try:
            response = requests.post(self.model_url, json={'prompt': prompt})
            response.raise_for_status()
            return response.json().get('response', '')
        except requests.exceptions.RequestException as e:
            return f"Error communicating with the language model: {str(e)}"