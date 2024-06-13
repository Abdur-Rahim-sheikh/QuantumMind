const md = window.markdownit();
let selected_session_id = null;

const sessionTabs = document.getElementById('session-tabs');
const sessionContainer = document.getElementById('session-container');
const queryElement = document.getElementById('query');
const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;


document.getElementById('query').addEventListener('keypress', async (e) => {
    if (e.key === 'Enter') {
        handleQuery();
    }
});

document.getElementById('query-submit-button').addEventListener('click', async () => {
    handleQuery();
});
document.getElementById('create-session').addEventListener('click', async () => {
    const session_name = 'Session ' + Math.floor(Math.random() * 1000);
    const data = await createSession(session_name);
});


const askQuestion = async (session_id, query) => {
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

const selectSession = (session_id) => {
    if (selected_session_id != null){
        let oldSession = sessionTabs.querySelector(`#tab-${selected_session_id}`);
        oldSession.style.fontWeight = 'normal';
        let oldConversation = sessionContainer.querySelector(`[id='${selected_session_id}'`);
        oldConversation.classList.add('d-none');
    }
    let currentSession = sessionTabs.querySelector(`#tab-${session_id}`);
    currentSession.style.fontWeight = 'bold';
    let currentConversation = sessionContainer.querySelector(`[id='${session_id}'`);
    currentConversation.classList.remove('d-none');

    selected_session_id = session_id;
    //    make it's text bold
}
const deleteSession = async (session_id) => {

    const response = await fetch(`/frontend-api/v1/sessions`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ "session_id": session_id })
    });

    if (response.ok === false) {
        alert('Failed to delete session');
        return;
    }

    let sessionTab = sessionTabs.querySelector(`#tab-${session_id}`);
    sessionTab.remove();
    let sessionContainer = sessionContainer.querySelector(`#session_id`);
    sessionContainer.remove();

    let tabs = sessionTabs.querySelectorAll('.sidebarItem');
    if (tabs.length > 0) {
        selectSession(tabs[0].id.split('-')[1]);
    }
    else {
        selected_session_id = null;
    }
}

const addSession = async (session_id, session_name, conversations=[]) => {

    let session = await buildConversation(session_id, conversations);
    sessionContainer.appendChild(session);

    let tab = document.createElement('li');
    tab.id = `tab-${session_id}`;
    tab.classList.add('sidebar-item');
    tab.tabIndex = 0;


    let link = document.createElement('a');
    link.classList.add('sidebar-link');
    let icon = document.createElement('i');
    icon.classList.add('bi', 'bi-chat-left-text');
    link.appendChild(icon);
    let span = document.createElement('span');
    span.textContent = session_name;

    link.appendChild(span);
    tab.appendChild(link);
    tab.addEventListener('click', () => {
        selectSession(session_id);
    });
    tab.addEventListener('keydown', (e) => {

        if (e.key === 'Delete') {
            deleteSession(session_id);
        }
    });
    sessionTabs.appendChild(tab);
    selectSession(session_id);
}
const createSession = async (session_name) => {
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
const getMessageBox = (text, userData = false) => {
    let messageContainer = document.createElement('div');
    messageContainer.classList.add('d-flex', userData ? 'justify-content-end' : 'justify-content-start', 'mb-3');

    let logo = userData ? '/static/img/human.jpg' : '/static/img/bot.png';
    let userClass = userData ? 'text-bg-light text-dark' : 'text-bg-secondary text-white';

    messageContainer.innerHTML = `
        <div class="d-flex align-items-start ${userData ? 'flex-row-reverse' : ''}">
            <img src="${logo}" alt="logo" class="rounded-circle me-2" style="width: 40px; height: 40px;">
            <div class="p-3 rounded ${userClass}" style="max-width: 100%;">
                ${md.render(text)}
            </div>
        </div>
    `;
    return messageContainer;
}

const buildConversation = (session_id, conversations) => {
    let conversationContainer = document.createElement('div');
    conversationContainer.classList.add('conversation-container','d-none');
    conversationContainer.id = session_id;
    conversations.forEach((message, idx) => {
        let user = ! (idx & 1);
        conversationContainer.appendChild(getMessageBox(message, user));
    })
    return conversationContainer;
}
const handleQuery = async () => {

    const query = queryElement.value;
    queryElement.value = '';
    const session_id = selected_session_id;
    const conversationContainer = sessionContainer.querySelector(`[id='${session_id}']`);
    conversationContainer.appendChild(getMessageBox(query, true));
    const responseData = await askQuestion(session_id, query);

    conversationContainer.appendChild(getMessageBox(responseData.data.response));

}
const renderSessions = async () => {
    const sessions = await getSessions();
    for(let [id, session] of Object.entries(sessions)) {

        addSession(id,session.name, session.conversations);
    }
}

renderSessions();