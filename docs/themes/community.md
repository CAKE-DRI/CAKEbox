---
title: Community
tags: [Top Tips, Events]
---

# 🎤 Community

Tips for community.

---
# 🟨 Community Tips Wall

A live collection of tips shared by the community.

<div id="tips-wall" class="sticky-board">
  Loading tips...
</div>

<script>
const repo = "CAKE-DRI/CAKEbox";

async function loadTips() {
  const response = await fetch(
    `https://api.github.com/repos/${repo}/issues?labels=top-tip&state=open`
  );

  const issues = await response.json();

  const container = document.getElementById("tips-wall");

  container.innerHTML = "";

  issues.forEach((issue, index) => {
    const colors = ["yellow", "blue", "pink", "green"];
    const color = colors[index % colors.length];

    const note = document.createElement("div");
    note.className = `sticky-note ${color}`;

    note.innerHTML = `
      <div class="note-title">${issue.title}</div>
      <div class="note-text">${issue.body}</div>
    `;

    container.appendChild(note);
  });
}
loadTips();
</script>
