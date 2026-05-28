---
title: Tools & Workflows
tags: [Sprinkles of Knowledge, Tools & Workflows]
---

# 🧠 Tools & Workflows 
This theme is about **finding the right tools for the right job.** What tools have helped you? What workflows save time or make collaboration easier?

Add your sprinkles of knowledge below: a quick tip, small insight, or lesson learned.

<div class="sticky-board">

{% for tip in tips("tools") %}

<div class="sticky-note {{ tip.color }}">
  <div class="note-title">
    {{ tip.emoji }} {{ tip.title }}
  </div>

  <div class="note-text">
    {{ tip.text }}
  </div>
</div>

{% endfor %}

</div>

---

## Add your sticky note

<div class="submit-box">

  <p class="submit-description">
    Share a tip, lesson learned, or useful advice with the community.
  </p>
  
  <p class="submit-helper">
  </br>
  After clicking <strong>Submit</strong>, a GitHub issue will open
  with your tip pre-filled. Simply click <strong>Create issue</strong>
  to send it to the CAKE team for review before it goes live.
</p>

  <input
    class="tip-input"
    id="tip-title"
    placeholder="Title"
  />

  <textarea
    class="tip-textarea"
    id="tip-text"
    placeholder="Your text..."
  ></textarea>

  <div class="tip-controls">


<div class="emoji-picker">
  <p class="emoji-label">
    Select an emoji:
  </p>

  <div class="emoji-grid" id="tip-emoji">

    <button type="button" class="emoji-btn active">🤝</button>
    <button type="button" class="emoji-btn">💡</button>
    <button type="button" class="emoji-btn">📝</button>
    <button type="button" class="emoji-btn">🚀</button>
    <button type="button" class="emoji-btn">🎯</button>
    <button type="button" class="emoji-btn">🌟</button>
    <button type="button" class="emoji-btn">📚</button>
    <button type="button" class="emoji-btn">🧠</button>
    <button type="button" class="emoji-btn">✨</button>
    <button type="button" class="emoji-btn">🎨</button>
    <button type="button" class="emoji-btn">💬</button>
    <button type="button" class="emoji-btn">🔍</button>
    <button type="button" class="emoji-btn">📌</button>
    <button type="button" class="emoji-btn">🛠️</button>
    <button type="button" class="emoji-btn">🔥</button>
    <button type="button" class="emoji-btn">📖</button>
    <button type="button" class="emoji-btn">📱</button>
    <button type="button" class="emoji-btn">🙌</button>
  </div>
</div>

<div class="colour-picker">

  <p class="emoji-label">
    Select your colour:
  </p>

  <div class="colour-grid" id="tip-colour">

    <button
      type="button"
      class="colour-btn yellow active"
      data-colour="yellow">
    </button>

    <button
      type="button"
      class="colour-btn blue"
      data-colour="blue">
    </button>

    <button
      type="button"
      class="colour-btn green"
      data-colour="green">
    </button>

    <button
      type="button"
      class="colour-btn pink"
      data-colour="pink">
    </button>

  </div>

</div>

</div>

<div class="submit-button-row">

  <button
    class="tip-submit-btn"
    onclick="submitTip('tools')">

    Submit

  </button>

</div>

---

## Explore our other themes

<!-- material/tags {include: [Sprinkles of Knowledge]} -->


</div>

<script>

document.querySelectorAll(".emoji-btn").forEach(btn => {

  btn.addEventListener("click", () => {

    document
      .querySelectorAll(".emoji-btn")
      .forEach(b => b.classList.remove("active"));

    btn.classList.add("active");
  });

});

</script>

<script>

document.querySelectorAll(".colour-btn").forEach(btn => {

  btn.addEventListener("click", () => {

    document
      .querySelectorAll(".colour-btn")
      .forEach(b => b.classList.remove("active"));

    btn.classList.add("active");
  });

});

</script>

<script>
function submitTip(theme) {

  const title =
    document.getElementById("tip-title").value.trim();

  const text =
    document.getElementById("tip-text").value.trim();

  const emoji =
    document.querySelector(".emoji-btn.active").textContent;

  const color =
    document
    .querySelector(".colour-btn.active")
    .dataset.colour;

  if (!title || !text) {
    alert("Please fill in both title and text.");
    return;
  }

  const issueTitle =
    `[Tip:${theme}] ${title}`;

  const issueBody =
`theme: ${theme}
title: ${title}
emoji: ${emoji}
color: ${color}
text: ${text}`;

  const url =
    "https://github.com/CAKE-DRI/CAKEbox/issues/new"
    + "?labels=tip-submission," + theme
    + "&title=" + encodeURIComponent(issueTitle)
    + "&body=" + encodeURIComponent(issueBody);

  window.open(url, "_blank");
}
</script>
