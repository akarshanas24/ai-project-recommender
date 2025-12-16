from flask import session

class SessionManager:
    def __init__(self):
        self.user_sessions = {}

    def get_session(self, user_id):
        return self.user_sessions.setdefault(user_id, {
            'stage': 'greeting',
            'skill_level': None,
            'interest_area': None,
            'language': None,
            'time_available': None,
            'domain': None,
            'recommended_projects': '',
            'selected_project': None,
            'problem_statements': '',
            'selected_problem': None
        })

    def clear_session(self, user_id):
        if user_id in self.user_sessions:
            del self.user_sessions[user_id]

    def update_session(self, user_id, key, value):
        session = self.get_session(user_id)
        session[key] = value

    def reset_session(self, user_id):
        if user_id in self.user_sessions:
            self.user_sessions[user_id] = {
                'stage': 'greeting',
                'skill_level': None,
                'interest_area': None,
                'language': None,
                'time_available': None,
                'domain': None,
                'recommended_projects': '',
                'selected_project': None,
                'problem_statements': '',
                'selected_problem': None
            }