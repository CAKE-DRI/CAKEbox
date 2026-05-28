---
title: Sprinkles of Knowledge
tags: [Central themes, Sprinkles of Knowledge]
---


<style>
.md-content h1:first-of-type::before {
  content: "🧁";
}


</style>



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


<script>
(function () {

  const KEY = "cameFromHome";

  // Only trigger if user came from home
  if (!sessionStorage.getItem(KEY)) return;

  
  sessionStorage.removeItem(KEY);


  const colours = [
    "#ff4d6d",
    "#ffd166",
    "#06d6a0",
    "#118ab2",
    "#8338ec",
    "#ff9f1c"
  ];

  function createSprinkle() {
    const sprinkle = document.createElement("div");

    sprinkle.className = "cake-sprinkle";

    sprinkle.style.left =
      Math.random() * window.innerWidth + "px";

    sprinkle.style.backgroundColor =
      colours[Math.floor(Math.random() * colours.length)];

    sprinkle.style.animationDuration =
      0.8 + Math.random() * 1.2 + "s";

    sprinkle.style.transform =
      `rotate(${Math.random() * 360}deg)`;

    document.body.appendChild(sprinkle);

    setTimeout(() => {
      sprinkle.remove();
    }, 2200);
  }

  const interval = setInterval(() => {
    createSprinkle();
  }, 20);

  setTimeout(() => {
    clearInterval(interval);

    // Allow future visits to trigger again
    window.sprinklesRunning = false;

  }, 1600);

})();
</script>