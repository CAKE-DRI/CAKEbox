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

## Explore by theme

Looking for something specific? Choose a theme and/or keyword to filter the resources and community tips below.

<div class="resources-filter">

  <label for="theme-filter"><b>Filter by theme:</b></label>

  <select
    id="theme-filter"
    class="tip-input"
    onchange="filterResources()"
  >
    <option value="">All themes</option>

    {% for theme in themes() %}
      <option value="{{ theme }}">
        {{ theme }}
      </option>
    {% endfor %}
  </select>

</div>

<div class="sticky-board">
  {% for tip in tips() %}

<div class="sticky-note {{ tip.color }}"
  data-theme="{{ tip.theme }}"
  >

  <div class="note-title">
    {{ tip.emoji }} {{ tip.title }}
  </div>

  <div class="note-text">
    {{ tip.text }}
  </div>
</div>

{% endfor %}

</div>

<br>

## Contribute your own Sprinkles

The most helpful ideas are often simple: a practical tip, something that worked, a mistake to avoid, or a small insight from experience.

Use the submission below to add your post-it. It doesn’t need to be polished or perfect, even a short tip or small insight could really help someone else.

---

### Inspiration 

* What’s one thing you wish you knew earlier?
* What’s a small thing that made a big difference?
* What advice would you give someone new to this?
* What mistake helped you learn something useful?

!!! question "Have something else to share?"
    Check out our [Contributing Guide](/CAKEbox/docs/how-to-contribute/index.md) for ways to add other types of resources  

---

### Code of Conduct

Please read our [Code of Conduct](../code-of-conduct.md). 

We ask contributors to:

* Use welcoming and inclusive language
* Be respectful of different viewpoints and experiences
* Gracefully accept constructive criticism
* Focus on what is best for the community
* Show courtesy and respect towards others

--- 

<!-- Move the add-your-sticky-note input to here -->

<div class="submit-box" id="tip-submit-box">

  <p class="submit-description">
    Share a quick tip, lesson learned, or useful advice with the community.
  </p>

  <p class="submit-helper">
  </br>
    After clicking <strong>Submit</strong>, a GitHub issue will open
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

<label for="tip-theme">Select a general theme to help us sort this tip:</label>

  <select id="tip-theme">

  <option value="">Select a theme</option>

    {% for theme in themes() %}
      <option value="{{ theme }}">
        {{ theme | replace("-", " ") | title }}
      </option>
    {% endfor %}
  </select>

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

<button
  type="button"
  class="tip-submit-btn"
  onclick="submitTip()">
  Submit
</button>

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
function submitTip() {

  const title =
    document.getElementById("tip-title").value.trim();

  const text =
    document.getElementById("tip-text").value.trim();

  const emoji =
    document.querySelector(".emoji-btn.active").textContent;

  const theme = 
    document.getElementById("tip-theme").value;

  const color =
    document
    .querySelector(".colour-btn.active")
    .dataset.colour;

  if (!title || !text || !theme) {
    alert("Please fill in all fields.");
    return;
  }

  const issueTitle =
    `[Tip:${theme}] ${title}`;

  const issueBody =
`title: ${title}
emoji: ${emoji}
color: ${color}
text: ${text}
theme: ${theme}`; 

  const url =
    "https://github.com/eleanor-broadway/CAKEbox/issues/new"
    + "?labels=tip-submission,"
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



<!-- Add functionality to filter the stickys via theme -->
<script>


function filterResources() {
  const selectedTheme =
    document.getElementById("theme-filter").value;

  document.querySelectorAll(".sticky-note").forEach(item => {
      const primaryTheme = item.dataset.theme;

      const matchesTheme =
        !selectedTheme || primaryTheme === selectedTheme;

        item.style.display = matchesTheme ? "" : "none";
    });
}
</script>