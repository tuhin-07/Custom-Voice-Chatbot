function startListening() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-US";

  document.getElementById("bot").innerText = "";
  document.getElementById("user").innerText = "";

  recognition.start();

  recognition.onresult = function(event) {
    const text = event.results[0][0].transcript;
    document.getElementById("user").innerText = text;

    fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text })
    })
    .then(res => res.json())
    .then(data => {
      document.getElementById("bot").innerText = data.reply;
      const utter = new SpeechSynthesisUtterance(data.reply);
      speechSynthesis.speak(utter);
    });
  };
}
