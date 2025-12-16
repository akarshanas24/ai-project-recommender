// This file contains the JavaScript code for handling user interactions in the chat interface.

document.addEventListener('DOMContentLoaded', function() {
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatMessages = document.getElementById('chat-messages');

    chatForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const userMessage = chatInput.value.trim();
        if (userMessage) {
            appendMessage('You', userMessage);
            chatInput.value = '';
            sendMessageToChatbot(userMessage);
        }
    });

    function appendMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message');
        messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
        chatMessages.appendChild(messageElement);
        chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to the bottom
    }

    function sendMessageToChatbot(message) {
        fetch('/chatbot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            appendMessage('Bot', data.reply);
        })
        .catch(error => {
            appendMessage('Bot', "Sorry, I couldn't process your request. Please try again.");
        });
    }
});