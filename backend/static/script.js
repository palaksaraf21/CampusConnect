function scrollToEvents() {
    document.getElementById("events").scrollIntoView({
        behavior: "smooth"
    });
}


let isLoggedIn = false;
let selectedEvent = "";


function showLogin() {

    const username = prompt("Enter username:");
    const password = prompt("Enter password:");

    if (!username || !password) {
        return;
    }

    fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {

        alert(data.message);

        if (data.success) {
            isLoggedIn = true;
        }

    });
}


function registerEvent(eventName) {

    if (!isLoggedIn) {
        alert("Please login before registering for an event.");
        return;
    }

    selectedEvent = eventName;

    document.getElementById("selectedEvent").innerText =
        "Registering for: " + eventName;

    document.getElementById("registrationModal").style.display = "flex";
}


function closeRegistration() {

    document.getElementById("registrationModal").style.display = "none";

}


function submitRegistration() {

    const name = document.getElementById("studentName").value;
    const email = document.getElementById("studentEmail").value;
    const studentId = document.getElementById("studentId").value;

    if (!name || !email || !studentId) {
        alert("Please fill in all fields.");
        return;
    }

    fetch("/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            event: selectedEvent,
            name: name,
            email: email,
            student_id: studentId
        })
    })
    .then(response => response.json())
    .then(data => {

        alert(data.message);

        if (data.success) {

            document.getElementById("studentName").value = "";
            document.getElementById("studentEmail").value = "";
            document.getElementById("studentId").value = "";

            closeRegistration();
        }

    });
}