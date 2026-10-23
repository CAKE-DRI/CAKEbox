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
    onchange="updateKeywordFilter(); filterResources()"
  >
    <option value="">All themes</option>
    {% for theme in themes() %}
      <option value="{{ theme }}">
        {{ theme }}
      </option>
    {% endfor %}
  </select>

  <label for="keyword-filter"><b>Filter by keyword:</b></label>
  <select
    id="keyword-filter"
    class="tip-input"
    onchange="filterResources()"
    disabled
  >
    <option value="">All keywords</option>
  </select>

  <label for="exclude-keyword-filter">
    <b>Exclude a keyword:</b>
  </label>
  <select
    id="exclude-keyword-filter"
    class="tip-input"
    onchange="filterResources()"
    disabled
  >
    <option value="">All keywords</option>
  </select>
</div>

<div class="sticky-board">
  {% for tip in tips() %}

<div class="sticky-note {{ tip.color }}"
  data-theme="{{ tip.theme }}"
  data-keywords="{{ tip.keywords | join(',') }}"
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
    Check out our [Contributing Guide](/how-to-contribute/index.md) for ways to add other types of resources  

---

### Code of Conduct

Please read our [Code of Conduct](code-of-conduct.md). 

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

<div class="keyword-picker">
  <div class="keyword-label">
    Select additional keyword(s) <span>(optional)</span>
  </div>

<div class="keyword-grid">
  {% for keyword in keywords() %}
    <label class="keyword-option">
      <input
        type="checkbox"
        name="keywords"
        value="{{ keyword }}"
      >
      <span>{{ keyword }}</span>
    </label>
  {% endfor %}

    <label class="keyword-option custom-keyword-option">
      <input
        type="checkbox"
        name="keywords"
        value="__other__"
        onchange="toggleCustomKeyword('tip', this)"
      >
      <span>Other</span>
    </label>
  </div>

  <input
    type="text"
    id="tip-custom-keyword"
    class="tip-input"
    placeholder="Enter a custom keyword"
    style="display: none;"
  >
</div>

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

<!-- Allow the input of a custom keyword -->
<script>
function toggleCustomKeyword(type, checkbox) {
  const input = document.getElementById(
    type + "-custom-keyword"
  );

  if (!input || !checkbox) return;

  input.style.display = checkbox.checked
    ? "block"
    : "none";

  if (!checkbox.checked) {
    input.value = "";
  }
}
</script>

<!-- Both themes and keywords can be selected as keywords. So, remove the selected theme from the keywords -->
<script>
function updateTipkeywords() {
  const selectedTheme =
    document.getElementById("tip-theme").value;

  document.querySelectorAll(
    ".keyword-picker .keyword-option"
  ).forEach(option => {
    const checkbox = option.querySelector("input");

    // Keep the custom keyword option visible
    if (checkbox.value === "__other__") return;

    const isPrimaryTheme =
      option.dataset.theme === selectedTheme;

    option.style.display = isPrimaryTheme ? "none" : "";

    if (isPrimaryTheme) {
      checkbox.checked = false;
    }
  });
}
</script>

<!-- You can select multiple keywords, this function retrieves everything that was selected -->
<script>
function getSelectedTipKeywords() {
  const keywords = Array.from(
    document.querySelectorAll(
      '#tip-submit-box .keyword-picker input[name="keywords"]:checked'
    )  
  )
    .map(checkbox => checkbox.value)
    .filter(keyword => keyword !== "__other__");

  const customKeyword = document
    .getElementById("tip-custom-keyword")
    .value.trim();

  if (customKeyword) {
    keywords.push(customKeyword);
  }

  // Remove duplicates, ignoring case
  return [...new Map(
    keywords.map(keyword => [
      keyword.toLowerCase(),
      keyword
    ])
  ).values()];
}
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

  const keywords = getSelectedTipKeywords();

  const color =
    document
    .querySelector(".colour-btn.active")
    .dataset.colour;

  if (
      title.includes(":") ||
      text.includes(":") ||
      keywords.some(keyword => keyword.includes(":"))
    ) {
    alert("Only the URL can contain a colon (:).");
    return;
  }

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
theme: ${theme}
${keywords.length > 0 ? `keywords:
${keywords.map(keyword => `  - ${keyword}`).join("\n")}` : ""}`;

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
function updateKeywordFilter() {
  const selectedTheme =
    document.getElementById("theme-filter").value;

  const keywordFilter =
    document.getElementById("keyword-filter");

  // Remember the current keyword, if possible
  const previousKeyword = keywordFilter.value;

  // Reset the dropdown
  keywordFilter.innerHTML =
    '<option value="">All keywords</option>';

  // Require a theme before selecting a keyword
  keywordFilter.disabled = !selectedTheme;

  if (!selectedTheme) {
    return;
  }

  // Collect keywords belonging to the selected theme
  const keywords = new Set();

  document.querySelectorAll(
    ".sticky-note"
  ).forEach(item => {
    if (item.dataset.theme !== selectedTheme) {
      return;
    }

    const itemKeywords = item.dataset.keywords
      ? item.dataset.keywords.split(",")
      : [];

    itemKeywords.forEach(keyword => {
      const cleanedKeyword = keyword.trim();

      if (cleanedKeyword) {
        keywords.add(cleanedKeyword);
      }
    });
  });

  // Populate the dropdown alphabetically
  [...keywords].sort().forEach(keyword => {
    const option = document.createElement("option");
    option.value = keyword;
    option.textContent = keyword;
    keywordFilter.appendChild(option);
  });

  // Preserve the selection if it's still available
  if (keywords.has(previousKeyword)) {
    keywordFilter.value = previousKeyword;
  }
}

function updateExcludeKeywordFilter() {
  const selectedTheme =
    document.getElementById("theme-filter").value;

  const excludeFilter =
    document.getElementById("exclude-keyword-filter");

  const previousKeyword = excludeFilter.value;

  // Reset the dropdown
  excludeFilter.innerHTML =
    '<option value="">All keywords</option>';

  // Require a theme before selecting a keyword
  excludeFilter.disabled = !selectedTheme;

  if (!selectedTheme) {
    return;
  }

  // Collect keywords belonging to the selected theme
  const keywords = new Set();

  document.querySelectorAll(
    ".sticky-note"
  ).forEach(item => {
    if (item.dataset.theme !== selectedTheme) {
      return;
    }

    const itemKeywords = item.dataset.keywords
      ? item.dataset.keywords.split(",")
      : [];

    itemKeywords.forEach(keyword => {
      const cleanedKeyword = keyword.trim();

      if (cleanedKeyword) {
        keywords.add(cleanedKeyword);
      }
    });
  });

  // Populate the dropdown alphabetically
  [...keywords].sort().forEach(keyword => {
    const option = document.createElement("option");
    option.value = keyword;
    option.textContent = keyword;
    excludeFilter.appendChild(option);
  });

  // Preserve the selection if it's still available
  if (keywords.has(previousKeyword)) {
    excludeFilter.value = previousKeyword;
  }
}

function filterResources() {
  const selectedTheme =
    document.getElementById("theme-filter").value;

  // Refresh available keywords when the theme changes
  updateKeywordFilter();
  updateExcludeKeywordFilter();

  const selectedKeyword =
    document.getElementById("keyword-filter").value;

  const excludedKeyword =
    document.getElementById("exclude-keyword-filter").value;

  document.querySelectorAll(
    ".resource-box, .sticky-note"
  ).forEach(item => {
    const primaryTheme = item.dataset.theme;

    const keywords = item.dataset.keywords
      ? item.dataset.keywords.split(",").map(k => k.trim())
      : [];

    const matchesTheme =
      !selectedTheme || primaryTheme === selectedTheme;

    const matchesKeyword =
      !selectedKeyword || keywords.includes(selectedKeyword);

    const excludesKeyword =
      !excludedKeyword || !keywords.includes(excludedKeyword);

    item.style.display =
      matchesTheme && matchesKeyword && excludesKeyword ? "" : "none";
  });
}
</script>