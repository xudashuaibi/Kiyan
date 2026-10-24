const API_KEY = "app-tm2JeTJTFcoREHaG3wNuQXih";
const API_URL = "http://localhost:8080//v1/chat-messages";

const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

function addMessage(text, className) {
  const div = document.createElement("div");
  div.className = className;
  div.textContent = text;
  chatBox.appendChild(div);
  chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
  const text = input.value.trim();
  if (!text) return;

  addMessage("你：" + text, "user-msg");
  input.value = "";
  sendBtn.disabled = true;

  try {
    const API_KEY = "app-tm2JeTJTFcoREHaG3wNuQXih";

    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Authorization": "Bearer " + API_KEY,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        query: text,
        response_mode: "blocking",
        user: "web-user",
        inputs: {}
      })
    });

    if (!response.ok) {
      throw new Error("HTTP " + response.status);
    }

    const data = await response.json();
    addMessage("AI：" + data.answer, "ai-msg");

  } catch (error) {
    addMessage("出错了：" + error.message, "ai-msg");
  } finally {
    sendBtn.disabled = false;
    input.focus();
  }
}

sendBtn.addEventListener("click", sendMessage);

input.addEventListener("keydown", function (event) {
  if (event.key === "Enter") {
    sendMessage();
  }
});