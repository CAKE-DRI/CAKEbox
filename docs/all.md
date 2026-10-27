---
title: 
tags: [Key Themes]
---

Discover useful resources, practical advice, and lessons learned from across the CAKE community. Explore what others have shared, or contribute something that might help someone else! *Curated by the [CAKE team](https://www.cake.ac.uk/about/who-are-we).*

- [Explore by theme](#explore-by-theme)
- [Useful Resources](#useful-resources)
- [Sprinkles of Knowledge](#sprinkles-of-knowledge)
- [Add your own](#have-something-to-share)

## Explore by theme

Looking for something specific? All of our resources are organised by a **primary theme** and may also be tagged with additional keywords to describe its content. 

Select a theme to explore its resources and sprinkles, then use the keyword filters to include or exclude specific keywords and narrow your results.

<div class="resources-filter">

  <label for="theme-filter"><b>Select a theme:</b></label>
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

  <label for="keyword-filter"><b>Include a keyword:</b></label>
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

## Useful Resources 

Explore websites, tools, guides, and other resources shared by the community. Each resource includes a short description to help you decide whether it's useful for your work.

<div class="resources-board">
  {% for resource in resources() %}

<div class="resource-box"
  data-theme="{{ resource.theme }}"
  data-keywords="{{ resource.keywords | join(',') }}"
  >

  <div class="resource-title">
    {{ resource.title }}
  </div>
  <div class="resource-url">
    <a href="{{ resource.url }}">{{ resource.url }}</a>
  </div>
  <div class="resource-text">
    {{ resource.comment }}
  </div>
  <div class="theme-badge">
    {{ resource.theme }}
  </div>

  {% if resource.keywords %}
  <div class="resource-keywords">
    {% for keyword in resource.keywords %}
    <span class="resource-keyword">{{ keyword }}</span>
    {% endfor %}
  </div>
  {% endif %}

</div>
{% endfor %}
</div>



## Sprinkles of Knowledge

Welcome to **Sprinkles of Knowledge!** This is where you can find quick tips, advice, and experiences from our community. The most helpful ideas are often simple: a practical tip, something that worked, a mistake to avoid, or a small insight from experience.

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

## Have something to share?

Found a resource that's helped you collaborate? Share it with the community! Got a tip or idea of your own? Add a little sprinkle of knowledge, too.

Whatever you'd like to share, it's quick and easy. Go for it! :)


### Share a new Sprinkle of Knowledge 

The most helpful ideas are often simple: a practical tip, something that worked, a mistake to avoid, or a small insight from experience.

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

### Link a useful resource 

Found a useful website, tool, guide, or other resource? Share the link and tell us briefly what makes it valuable.

<!-- Box for users to submit a new resource -->
<div class="resources-submit-box" id="resource-submit-box">

  <p class="resources-submit-description">
    Have a resource to share?
  </p>

  <p class="resources-submit-helper">
    We'd love to hear about websites, tools, guides, or other resources you've found useful. Post the link and tell us a little about what makes it worth sharing.
  </p>

  <p class="resources-submit-helper">
    </br>
    After clicking <strong>Submit</strong>, a GitHub issue will open
    to send it to the CAKE team for review before it goes live.
  </p>

  <input
    class="tip-input"
    id="resource-title"
    placeholder="Title"
  />

  <input
    class="tip-input"
    id="resource-url"
    placeholder="Paste the link to the resource"
  />

  <textarea
    class="tip-textarea"
    id="resource-comment"
    placeholder="What makes this resource useful? Tell us a little about it..."
  ></textarea>


<label for="resource-theme">
  Select a general theme to help us sort this resouce:
</label>

<select
  id="resource-theme"
  onchange="updateResourcekeywords()"
>
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
        onchange="toggleCustomKeyword('resource', this)"
      >
      <span>Other</span>
    </label>
  </div>

  <input
    type="text"
    id="resource-custom-keyword"
    class="tip-input"
    placeholder="Enter a custom keyword"
    style="display: none;"
  >
</div>


<button
  type="button"
  class="tip-submit-btn"
  onclick="submitResource()">
  Submit
</button>
</div>

</br>

### Something else?

Have another idea for contributing to CAKEbox? Find out how you can get involved [here](/how-to-contribute/index.md). 


### Code of Conduct

Please read our [Code of Conduct](/code-of-conduct.md). 

We ask contributors to:

* Use welcoming and inclusive language
* Be respectful of different viewpoints and experiences
* Gracefully accept constructive criticism
* Focus on what is best for the community
* Show courtesy and respect towards others


<!-- Script that takes the user input and creates the issue -->
<script>
function updateResourcekeywords() {
  const selectedTheme =
    document.getElementById("resource-theme").value;

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


// function toggleCustomKeyword(type, checkbox) {
//   const input = document.getElementById(
//     `${type}-custom-keyword`
//   );

//   if (!input || !checkbox) return;

//   input.style.display = checkbox.checked ? "block" : "none";

//   if (!checkbox.checked) {
//     input.value = "";
//   }
// }


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



function getSelectedResourceKeywords() {
  const keywords = Array.from(
    document.querySelectorAll(
      '#resource-submit-box .keyword-picker input[name="keywords"]:checked'
    )
  )
    .map(checkbox => checkbox.value)
    .filter(keyword => keyword !== "__other__");

  const customKeyword = document
    .getElementById("resource-custom-keyword")
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

function submitResource() {
  const title = document
    .getElementById("resource-title")
    .value.trim();

  let url = document
    .getElementById("resource-url")
    .value.trim();

  const comment = document
    .getElementById("resource-comment")
    .value.trim();

  // Only existing themes can be selected
  const theme = document
    .getElementById("resource-theme")
    .value;

  const keywords = getSelectedResourceKeywords();

  // Add https:// when no protocol is provided
  if (
    url &&
    !url.startsWith("http://") &&
    !url.startsWith("https://")
  ) {
    url = "https://" + url;
  }

  if (
      title.includes(":") ||
      comment.includes(":") ||
      keywords.some(keyword => keyword.includes(":"))
    ) {
    alert("Only the URL can contain a colon (:).");
    return;
  }

  if (!title || !url || !comment || !theme) {
    alert("Please fill in all required fields and select a theme.");
    return;
  }

  // Prevent the "Other" control itself being saved as a keyword
  const issueTitle = `[Resource:${theme}] ${title}`;

  const issueBody =
`type: resource
title: ${title}
url: ${url}
comment: ${comment}
theme: ${theme}
${keywords.length > 0
  ? `keywords:\n${keywords.map(keyword => `  - ${keyword}`).join("\n")}`
  : ""}`;

  const githubUrl =
    "https://github.com/CAKE-DRI/CAKEbox/issues/new"
    + "?labels=resource-submission"
    + "&title=" + encodeURIComponent(issueTitle)
    + "&body=" + encodeURIComponent(issueBody);

  window.open(githubUrl, "_blank");
}
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
document.querySelectorAll(".emoji-btn").forEach(btn => {

  btn.addEventListener("click", () => {

    document
      .querySelectorAll(".emoji-btn")
      .forEach(b => b.classList.remove("active"));

    btn.classList.add("active");
  });

});


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

// function toggleCustomKeyword(type) {
//   const checkbox = document.querySelector(
//     '.keyword-picker input[value="__other__"]'
//   );

//   const input = document.getElementById(
//     `${type}-custom-keyword`
//   );

//   if (!checkbox || !input) return;

//   input.style.display = checkbox.checked ? "block" : "none";

//   if (!checkbox.checked) {
//     input.value = "";
//   }
// }

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

function submitTip() {

  const title =
    document.getElementById("tip-title").value.trim();

  const text =
    document.getElementById("tip-text").value.trim();

  const emoji =
    document.querySelector(".emoji-btn.active").textContent;

  // Only existing themes can be selected
  const theme = document
    .getElementById("tip-theme")
    .value;

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

  if (text.length > 220) {
    alert("Please only use up to 220 charecters (~ 30 words) for a tip. Need more space? Consider writing a resource!");
    return;
  }

  if (title.length > 50) {
    alert("Please only use up to 50 charecters for a tip title");
    return;
  }

  if (!title || !text || !theme) {
    alert("Please fill in all fields.");
    return;
  }

  const issueTitle =
    `[Tip:${theme}] ${title}`;

  const issueBody =
`type: tip
theme: ${theme}
title: ${title}
emoji: ${emoji}
color: ${color}
text: ${text}
${keywords.length > 0 ? `keywords:
${keywords.map(keyword => `  - ${keyword}`).join("\n")}` : ""}`;

  const url =
    "https://github.com/CAKE-DRI/CAKEbox/issues/new"
    + "?labels=tip-submission"
    + "&title=" + encodeURIComponent(issueTitle)
    + "&body=" + encodeURIComponent(issueBody);

  window.open(url, "_blank");
}

</script>




<!-- Filter both the resources and the sticky notes -->
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
    ".resource-box, .sticky-note"
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
    ".resource-box, .sticky-note"
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

    const excludesKeyword =
      !excludedKeyword || !keywords.includes(excludedKeyword);

    const matchesTheme =
      !selectedTheme || primaryTheme === selectedTheme;

    const matchesKeyword =
      !selectedKeyword || keywords.includes(selectedKeyword);

    item.style.display =
      matchesTheme && matchesKeyword && excludesKeyword
        ? ""
        : "none";
      });
}
</script>