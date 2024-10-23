<script>
// Establish WebSocket connection for real-time updates
let socket = new WebSocket("ws://localhost:8000/ws/tasks/");

// Listen for messages from the WebSocket
socket.onmessage = function(event) {
    let data = JSON.parse(event.data);
    let updatesDiv = document.getElementById('updates');

    // Display new notification in the UI
    let notification = document.createElement('div');
    notification.textContent = "Task: " + data.title + " | Status: " + data.status + " | Deadline: " + data.deadline;
    updatesDiv.appendChild(notification);
};

// Handle WebSocket connection open event
socket.onopen = function(event) {
    console.log("WebSocket connection established");
};

// Handle WebSocket errors
socket.onerror = function(error) {
    console.error("WebSocket Error: ", error);
};
</script>