---
title: Sprinkles of Knowledge
tags: [Central themes, Sprinkles of Knowledge]
---

Welcome to **Sprinkles of Knowledge!** This is where you can find quick tips, advice, and experiences from our community.

The most helpful ideas are often simple: a practical tip, something that worked, a mistake to avoid, or a small insight from experience.

Browse our sprinkles by the themes below or share your own. *Curated by the [CAKE team](https://www.cake.ac.uk/about/who-are-we).*

<div class="tip-theme-grid">

{% set themes = [
  {"name": "Events", "tag": "events", "icon": "🎤", "desc": "Workshops, conferences and hybrid meetings."},
  {"name": "Collaboration", "tag": "collaboration", "icon": "🤝", "desc": "Working together across teams and disciplines."},
  {"name": "Inclusion", "tag": "inclusion", "icon": "🌍", "desc": "Accessibility and inclusive community practices."},
  {"name": "Tools & Workflows", "tag": "tools", "icon": "🧠", "desc": "The right tools for the right job."}
] %}

{% for theme in themes %}

<a class="tip-theme-card" href="../community-tips/{{ theme.tag }}/">
<div class="tip-theme-icon">{{ theme.icon }}</div>
<div class="tip-theme-content">
<h3>{{ theme.name }}</h3>
<p>{{ theme.desc }}</p>
</div>

<div class="tip-theme-arrow">→</div>

</a>

{% endfor %}

</div>

## Contributing

Click on a theme and add your post-it. It doesn’t need to be polished or perfect, even a short tip or small insight could really help someone else.

!!! question "Have something else to share?"
    Submit your contribution below and the CAKE team will help to place it, or even create a new theme! 

### Inspiration 

* What’s one thing you wish you knew earlier?
* What’s a small thing that made a big difference?
* What advice would you give someone new to this?
* What mistake helped you learn something useful?

### Code of Conduct

Please read our [Code of Conduct](../code-of-conduct.md). 

We ask contributors to:
* Use welcoming and inclusive language
* Be respectful of different viewpoints and experiences
* Gracefully accept constructive criticism
* Focus on what is best for the community
* Show courtesy and respect towards others

<div class="sticky-board">

{% for tip in tips("template") %}

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

### Add your sticky note

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
    onclick="submitTip('Inclusion')">

    Submit

  </button>

</div>



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
