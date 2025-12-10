const chatHistory = document.getElementById('chat-history');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

async function sendMessage() {
    const query = userInput.value.trim();
    if (!query) return;

    // 1. Add User's Question to UI
    addMessage(query, 'user-message');
    userInput.value = '';
    setLoading(true);

    try {
        // 2. Call the API (Relative path works because of Nginx proxy)
        const response = await fetch('/api/v1/chat/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_question: query }) // Matches your Pydantic schema
        });

        if (!response.ok) {
            throw new Error(`Server Error: ${response.status}`);
        }

        const data = await response.json();

        // 3. Add Bot's Answer to UI
        addMessage(data.answer, 'bot-message');

    } catch (error) {
        console.error("Error:", error);
        addMessage("Sorry, I couldn't connect to the QuickLook server. Please check if the backend is running.", 'bot-message');
    } finally {
        setLoading(false);
    }
}

function addMessage(text, type) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${type}`;

    // Choose icon based on user or bot
    const icon = type === 'user-message' ? 'fa-user' : 'fa-robot';

    msgDiv.innerHTML = `
        <div class="avatar"><i class="fa-solid ${icon}"></i></div>
        <div class="bubble">${formatText(text)}</div>
    `;
    
    chatHistory.appendChild(msgDiv);
    // Auto-scroll to bottom
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

// Simple text formatting (converts newlines to <br>)
function formatText(text) {
    return text.replace(/\n/g, '<br>');
}

function setLoading(isLoading) {
    userInput.disabled = isLoading;
    sendBtn.disabled = isLoading;
    if(isLoading) {
        sendBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i>';
    } else {
        sendBtn.innerHTML = '<i class="fa-solid fa-paper-plane"></i>';
        userInput.focus();
    }
}

// Allow pressing "Enter" to send
userInput.addEventListener('keypress', (e) => {
if (e.key === 'Enter') sendMessage();
});