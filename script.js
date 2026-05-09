const socket = io();

socket.on('task_update', (data) => {
    alert(data.message);
});

async function addTask(){

    const task = {
        title: document.getElementById('title').value,
        description: document.getElementById('description').value,
        priority: document.getElementById('priority').value,
        status: document.getElementById('status').value
    };

    await fetch('/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(task)
    });

    loadTasks();
}

async function loadTasks(){

    const response = await fetch('/tasks');

    const tasks = await response.json();

    let html = '';

    tasks.forEach(task => {
        html += `
            <div>
                <h3>${task.title}</h3>
                <p>${task.description}</p>
                <p>${task.priority}</p>
                <p>${task.status}</p>
            </div>
            <hr>
        `;
    });

    document.getElementById('task-list').innerHTML = html;
}

loadTasks();
