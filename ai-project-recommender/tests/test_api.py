from flask import Flask, jsonify
import unittest

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    def test_login_page(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_signup_page(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sign Up', response.data)

    def test_chat_page(self):
        response = self.client.get('/chat')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Chat', response.data)

    def test_chatbot_response(self):
        response = self.client.post('/chatbot', json={'message': 'What projects can I work on?', 'user_id': 'test_user'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('reply', response.json)

if __name__ == '__main__':
    unittest.main()