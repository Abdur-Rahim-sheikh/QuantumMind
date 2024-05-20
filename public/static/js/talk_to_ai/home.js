

const getSessions = async () => {
    const response = await fetch('/api/sessions');
    const data = await response.json();
    return data;
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
    const response = await fetch('/api/sessions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ session_name })
    });
    const data = await response.json();
    return data;
}