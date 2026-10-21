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


## Contributing

Click on a theme and add your post-it. It doesn’t need to be polished or perfect, even a short tip or small insight could really help someone else.

!!! question "Have something else to share?"
    Struggling to place your contribution? Get in touch and we can help or create a new theme. Contact the CAKE team on [Slack](https://join.slack.com/t/cake-dri/shared_invite/zt-3w3ymqha8-SnreNHd4W3V8pBEwsfZrxA) or via email at [cake@jiscmail.ac.uk](cake@jiscmail.ac.uk). 

---

### Inspiration 

* What’s one thing you wish you knew earlier?
* What’s a small thing that made a big difference?
* What advice would you give someone new to this?
* What mistake helped you learn something useful?

---

### Code of Conduct

Please read our [Code of Conduct](../code-of-conduct.md). 

We ask contributors to:

* Use welcoming and inclusive language
* Be respectful of different viewpoints and experiences
* Gracefully accept constructive criticism
* Focus on what is best for the community
* Show courtesy and respect towards others


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