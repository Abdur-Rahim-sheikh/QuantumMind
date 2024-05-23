

const getSessions = async () => {
    const response = await fetch('/frontend-api/v1/sessions');
    const responseData = await response.json();
    console.log(responseData.data.sessions);
    return responseData.data.sessions;
}
const addSessionToTab = async (session_name) => {
    const sessionTabs = document.getElementById('session-tabs');
    let tab = document.createElement('li');

    tab.classList.add('nav-item');
    tab.innerHTML = `<a class="nav-link" href="#">${session_name}</a>`;
    sessionTabs.appendChild(sessionTab);
}
const createSession = async (session_name) => {
    addSessionToTab(session_name);

    const response = await fetch('/frontend-api/v1/sessions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ session_name })
    });
    const data = await response.json();
    return data;
}

const renderSessions = async () => {
    const sessions = await getSessions();
    console.log(sessions);
    sessions.ForEach(session => {
        addSessionToTab(session.name);
    });
}

renderSessions();