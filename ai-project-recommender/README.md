# AI Project Recommender

This project is an AI-powered chatbot designed to recommend suitable project ideas based on user queries. It leverages natural language processing to understand user needs and provide personalized project suggestions.

## Features

- **User-Friendly Interface**: A web-based chat interface for seamless interaction with the chatbot.
- **Dynamic Recommendations**: The chatbot analyzes user input to suggest relevant project ideas.
- **Session Management**: User sessions are managed to maintain context throughout the interaction.
- **Customizable**: Easily extendable to include more features or integrate with other services.

## Project Structure

```
ai-project-recommender
├── backend
│   ├── app.py                  # Main application file
│   ├── requirements.txt         # Python dependencies
│   ├── .env.example             # Example environment variables
│   ├── recommender              # Recommender module
│   │   ├── __init__.py
│   │   ├── api.py
│   │   ├── llm.py
│   │   ├── prompt_templates.py
│   │   ├── session_manager.py
│   │   └── utils.py
│   ├── templates                # HTML templates
│   │   ├── layout.html
│   │   ├── chat.html
│   │   ├── login.html
│   │   └── signup.html
│   └── static                  # Static files
│       ├── css
│       │   └── styles.css
│       └── js
│           └── chat.js
├── docker
│   └── Dockerfile               # Docker configuration
├── tests                        # Test files
│   ├── test_api.py
│   └── test_recommender.py
├── scripts                      # Helper scripts
│   └── start.sh
├── .gitignore                   # Git ignore file
├── LICENSE                      # Licensing information
└── README.md                    # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai-project-recommender
   ```

2. Install the required dependencies:
   ```
   pip install -r backend/requirements.txt
   ```

3. Set up environment variables by copying `.env.example` to `.env` and updating the values as needed.

## Usage

1. Start the application:
   ```
   bash scripts/start.sh
   ```

2. Open your web browser and navigate to `http://localhost:5000` to interact with the chatbot.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.