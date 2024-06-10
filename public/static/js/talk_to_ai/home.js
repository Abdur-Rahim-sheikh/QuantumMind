let selected_session_id = null;
document.getElementById('query-submit').addEventListener('click', async () => {
    const query = document.getElementById('query').value;
    const session_id = selected_session_id;
    conversationContainer.appendChild(getMessageBox(query), userData=true);
    const responseData = await askQuestion(session_id, query);
    const conversationContainer = document.getElementById(session_id);
    conversationContainer.appendChild(getMessageBox(responseData.data.response));

});
document.getElementById('create-session').addEventListener('click', async () => {
    const session_name = 'Session ' + Math.floor(Math.random() * 1000);
    const data = await createSession(session_name);
});


const askQuestion = async (session_id, query) => {
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const response = await fetch('/talk-to-ai', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            "session_id": session_id,
            "query": query
        })
    });
    const responseData = await response.json();
    return responseData;
}
const getSessions = async () => {
    const response = await fetch('/frontend-api/v1/sessions');
    const responseData = await response.json();

    return responseData.data.sessions;
}
const getMessageBox = (text, userData=false) => {
    let messageContainer = document.createElement('div');
    messageContainer.classList.add('message-container');
    messageContainer.innerHTML = `<div class="message">${text}</div>`;
    if (userData){
        messageContainer.style.textAlign = 'right';
    }
    return messageContainer;
}
const buildConversation = (session_id, conversations) => {
    let conversationContainer = document.createElement('div');
    conversationContainer.classList.add('conversation-container','w-100', 'h-100', 'd-flex', 'flex-column','d-none');
    conversationContainer.id = session_id;
    conversations.forEach(message => {
        conversationContainer.appendChild(getMessageBox(message));
    })
    return conversationContainer;
}
const selectSession = (session_id) => {
    if (selected_session_id != null){
        let oldSession = document.getElementById(`tab-${selected_session_id}`);
        oldSession.style.fontWeight = 'normal';
        let oldConversation = document.getElementById(selected_session_id);
        oldConversation.classList.add('d-none');
    }
    let currentSession = document.getElementById(`tab-${session_id}`);
    currentSession.style.fontWeight = 'bold';
    let currentConversation = document.getElementById(session_id);
    currentSession.classList.remove('d-none');

    selected_session_id = session_id;
//    make it's text bold
}
const addSession = async (session_id, session_name, conversations=[]) => {
    const sessionContainer = document.getElementById('conversation-container');
    let session = await buildConversation(session_id, conversations);
    sessionContainer.appendChild(session);
    const sessionTabs = document.getElementById('session-tabs');
    let tab = document.createElement('li');
    tab.id = `tab-${session_id}`;

    tab.classList.add('sidebar-item');

    tab.innerHTML = `<a class="sidebar-link" href="#">
                        <i class="bi bi-chat-left-text"></i>
                        <span>${session_name}<span>
                    </a>`;
    tab.addEventListener('click', () => {
        selectSession(session_id);
    });
    sessionTabs.appendChild(tab);
    selectSession(session_id);
}
const createSession = async (session_name) => {
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    const response = await fetch('/frontend-api/v1/sessions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },

        body: JSON.stringify({ session_name })
    });

    const responseData = await response.json();

    addSession(responseData.data.session_id, session_name);
    return;
}

const renderSessions = async () => {
    const sessions = await getSessions();
    for(let [id, session] of Object.entries(sessions)) {

        addSession(id,session.name, session.conversations);
    }
}

renderSessions();