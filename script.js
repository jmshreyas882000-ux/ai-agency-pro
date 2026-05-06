function scrollToContact() {
  document.getElementById("contact").scrollIntoView();
}

function sendData() {
  const data = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    message: document.getElementById("message").value
  };

  fetch("http://127.0.0.1:5000/contact", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(data => alert("Submitted Successfully"));
}
function login() {
  fetch("http://127.0.0.1:5000/login", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      username: "admin",
      password: "admin"
    })
  })
  .then(res => res.json())
  .then(data => {
    localStorage.setItem("token", data.token);
    alert("Login Success");
  });
}

function chatAI() {
  const msg = prompt("Ask AI:");

  fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message: msg})
  })
  .then(res => res.json())
  .then(data => alert(data.reply));
}
