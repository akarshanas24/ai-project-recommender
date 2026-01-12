# AI Project Recommender Chatbot

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.1-lightgrey.svg)](https://flask.palletsprojects.com/)

An intelligent AI-powered chatbot that recommends personalized project ideas based on user queries. Built with Flask, MongoDB, and integrated with Ollama for natural language processing, this application helps users discover suitable AI and software project ideas tailored to their skills, interests, and constraints.

## 🚀 Features

- **Intelligent Recommendations**: Leverages advanced NLP to understand user intent and provide relevant project suggestions
- **Web-Based Chat Interface**: Clean, responsive UI for seamless user interaction
- **User Authentication**: Secure login/signup system with session management
- **Conversation History**: Persistent chat history stored in MongoDB
- **Extensible Architecture**: Modular design for easy feature additions
- **Comprehensive Testing**: Unit tests for core functionality

## 🏗️ Architecture

The application follows a microservices-inspired architecture with clear separation of concerns:

- **Frontend**: HTML/CSS/JavaScript templates served by Flask
- **Backend**: Flask application handling API requests and business logic
- **Database**: MongoDB for user data and chat history
- **AI Engine**: Ollama integration for language model capabilities
- **Session Management**: In-memory session handling with database persistence

## 📁 Project Structure

```
ai-project-recommender/
├── README.md                           # Main project README
├── ai-project-recommender/             # Core project folder
│   ├── LICENSE                         # MIT License
│   ├── README.md                       # Project documentation
│   ├── backend/                        # Backend application
│   │   ├── app.py                      # Main Flask application
│   │   ├── requirements.txt            # Python dependencies
│   │   ├── static/                     # Static assets
│   │   │   ├── css/
│   │   │   │   └── styles.css          # Stylesheet
│   │   │   └── js/
│   │   │       └── chat.js             # Chat interface JavaScript
│   │   └── templates/                  # HTML templates
│   │       ├── chat.html               # Chat page
│   │       ├── layout.html             # Base layout
│   │       ├── login.html              # Login page
│   │       └── signup.html             # Signup page
│   └── docker/
│       └── Dockerfile                  # Docker configuration
└── db/                                 # Database related files
```

## 🛠️ Prerequisites

Before running this application, ensure you have the following installed:

- **Python 3.9+**: [Download here](https://www.python.org/downloads/)
- **MongoDB**: Local installation or cloud instance (MongoDB Atlas)
- **Ollama**: For AI model serving [Installation guide](https://ollama.ai/)
- **Git**: For cloning the repository

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ai-project-recommender.git
   cd ai-project-recommender
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r backend/requirements.txt
   # Or for the alternative backend: pip install -r ai-project-recommender/backend/requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   # Create .env file in backend/ directory
   cp backend/.env.example backend/.env
   # Edit .env with your configuration
   ```

5. **Start MongoDB** (if running locally):
   ```bash
   mongod  # Or use your preferred MongoDB startup method
   ```

6. **Start Ollama** and pull a model:
   ```bash
   ollama serve
   ollama pull llama3  # Or your preferred model
   ```

## ⚙️ Configuration

Create a `.env` file in the `backend/` directory with the following variables:

```env
FLASK_SECRET=your-secret-key-here
MONGO_URI=mongodb://localhost:27017/
OLLAMA_URL=http://localhost:11434/api/generate
OLLAMA_MODEL=llama3
```

## 🎯 Usage

### Local Development

1. **Start the application**:
   ```bash
   python backend/app.py
   # Or use the script: bash ai-project-recommender/scripts/start.sh
   ```

2. **Open your browser** and navigate to `http://localhost:5000`

3. **Register/Login** and start chatting with the AI recommender!

## 📡 API Endpoints

The application provides RESTful API endpoints:

- `GET /` - Home page
- `GET/POST /login` - User authentication
- `GET/POST /signup` - User registration
- `GET/POST /chat` - Chat interface and message handling
- `POST /api/recommend` - Direct API for recommendations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](ai-project-recommender/LICENSE) file for details.

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [MongoDB](https://www.mongodb.com/) - NoSQL database
- [Ollama](https://ollama.ai/) - Local LLM serving
- [Bootstrap](https://getbootstrap.com/) - UI framework (if used)

## 📞 Support

If you have any questions or issues:

- Open an issue on GitHub
- Check the [Wiki](https://github.com/yourusername/ai-project-recommender/wiki) for documentation
- Join our [Discord](https://discord.gg/yourserver) community

---
