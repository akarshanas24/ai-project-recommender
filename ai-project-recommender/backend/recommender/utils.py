from typing import List, Dict, Any

def normalize_choice(text: str) -> str:
    choices = {
        '1': '1', 'one': '1', 'first': '1',
        '2': '2', 'two': '2', 'second': '2',
        '3': '3', 'three': '3', 'third': '3',
        '4': '4', 'four': '4', 'fourth': '4',
        '5': '5', 'five': '5', 'fifth': '5',
    }
    return choices.get(text.strip().lower(), None)

def extract_projects(text: str) -> List[str]:
    text = (text or '').strip()
    if not text:
        return []
    return [line.strip() for line in text.splitlines() if line.strip()][:5]

def is_valid_email(email: str) -> bool:
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def generate_response(data: Dict[str, Any]) -> str:
    return f"Response generated for: {data}"

def log_user_activity(user_id: str, activity: str) -> None:
    with open('user_activity.log', 'a') as log_file:
        log_file.write(f"{user_id}: {activity}\n")