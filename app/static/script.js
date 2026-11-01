document.addEventListener("DOMContentLoaded", () => {
  const screeningForm = document.getElementById("screening-form");
  const screeningResult = document.getElementById("screening-result");
  const chatInput = document.getElementById("chat-input");
  const chatBtn = document.getElementById("chat-btn");
  const chatBox = document.getElementById("chat-box");

  screeningForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const payload = {
      job_title: document.getElementById("job_title").value,
      candidate_name: document.getElementById("candidate_name").value,
      job_description: document.getElementById("job_description").value,
      resume_text: document.getElementById("resume_text").value,
      skills: ["sql", "python", "powerbi", "dashboard"]
    };

    const response = await fetch("/api/screen-candidate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    const result = await response.json();
    screeningResult.innerHTML = `
      <h4>Result</h4>
      <p><strong>Nama:</strong> ${result.candidate_name}</p>
      <p><strong>Posisi:</strong> ${result.job_title}</p>
      <p><strong>Skor:</strong> ${result.match_score}%</p>
      <p><strong>Rekomendasi:</strong> ${result.recommendation}</p>
      <p><strong>Ringkasan:</strong> ${result.summary}</p>
      <p><strong>Strengths:</strong> ${result.strengths.join(", ")}</p>
      <p><strong>Gaps:</strong> ${result.gaps.length ? result.gaps.join(", ") : "Tidak ada"}</p>
    `;
  });

  chatBtn.addEventListener("click", async () => {
    const question = chatInput.value.trim();
    if (!question) return;

    addChatMessage("user", question);
    chatInput.value = "";

    const response = await fetch("/api/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ question })
    });

    const data = await response.json();
    addChatMessage("bot", data.answer);
  });

  function addChatMessage(type, text) {
    const message = document.createElement("div");
    message.className = `chat-message ${type}`;
    message.textContent = text;
    chatBox.appendChild(message);
  }
});
