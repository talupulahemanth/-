// SavoyLife/savoylifebot/static/savoylifebot/js/chatbot.js

document.addEventListener("DOMContentLoaded", function() {
  const chatContainer = document.querySelector('.chat-container');
  const chatContent = document.querySelector('.chat-content');
  const inputField = document.querySelector('.chat-input input');
  const sendButton = document.querySelector('.chat-input button');

  sendButton.addEventListener('click', function() {
    const userMessage = inputField.value.trim();
    if (userMessage) {
      addMessage('user-message', userMessage);
      inputField.value = '';
      getBotResponse(userMessage);
    }
  });

  function addMessage(className, message) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', className);
    messageDiv.textContent = message;
    chatContent.appendChild(messageDiv);
    chatContent.scrollTop = chatContent.scrollHeight;
  }

  function getBotResponse(message) {
    // For now, let's just echo the user's message
    addMessage('bot-message', 'You said: ' + message);
  }
});
