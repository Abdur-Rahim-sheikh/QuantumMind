document.getElementById('create-session').addEventListener('click', async () => {
    const session_name = 'Session ' + Math.floor(Math.random() * 1000);
    const data = await createSession(session_name);
});

const getSessions = async () => {
    const response = await fetch('/frontend-api/v1/sessions');
    const responseData = await response.json();

    return responseData.data.sessions;
}
const addSession = async (session_name, conversations=null) => {
    const sessionTabs = document.getElementById('session-tabs');
    let tab = document.createElement('li');

    tab.classList.add('sidebar-item');

    tab.innerHTML = `<a class="sidebar-link" href="#">
                        <i class="bi bi-chat-left-text"></i>
                        <span>${session_name}<span>
                    </a>`;
    sessionTabs.appendChild(tab);
}
const createSession = async (session_name) => {
    addSession(session_name);
//    add csrf
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    const response = await fetch('/frontend-api/v1/sessions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },

        body: JSON.stringify({ session_name })
    });
    const data = await response.json();
    return data;
}

const renderSessions = async () => {
    const sessions = await getSessions();
    for(let [id, session] of Object.entries(sessions)) {

        addSession(session.name, session.conversations);
    }
}

renderSessions();