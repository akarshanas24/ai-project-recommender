from typing import Dict, Any

PROMPT_TEMPLATES: Dict[str, str] = {
    "greeting": "Welcome! I am your Project Recommender Assistant. How can I assist you today?",
    "skill_level": "Please tell me your skill level: 1) Beginner 2) Intermediate 3) Advanced.",
    "interest_area": "What is your area of interest? 1) Machine Learning 2) Deep Learning 3) Natural Language Processing 4) Computer Vision 5) Generative AI.",
    "language": "Which programming language do you prefer? 1) Python 2) JavaScript 3) Java 4) C++ 5) Other.",
    "time_available": "How much time do you have available? 1) 1-2 weeks 2) 2-4 weeks 3) 1-2 months 4) 2+ months.",
    "domain": "What domain are you interested in? 1) IoT 2) Blockchain 3) Data Science 4) Web Application 5) Mobile Application.",
    "project_titles": "Here are some project titles based on your preferences:\n{titles}\nWhich project interests you?",
    "problem_statements": "For the selected project, here are some problem statements:\n{statements}\nWhich problem statement do you choose?",
    "overview": "Here is an overview of the selected problem:\n1. {summary1}\n2. {summary2}\n3. {recommendation_reason}\n4. {suitability_reason}\nWould you like to explore another project? Yes / No"
}