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
