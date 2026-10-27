---
title: Professional Development 
tags: [Key Themes]
---

Professional development is the ongoing process of learning, training, and building skills to advance your career. See the below tips and resources from the community on handling different scenarios.
</br>

Browse all resources under the theme of **professional development** below, or filter via keyword: 

<!-- Enable filtering for keywords, theme is fixed -->
<div class="resources-filter">
  <label for="keyword-filter"><b>Include a keyword:</b></label>
  <select
    id="keyword-filter"
    class="tip-input"
    onchange="filterResources()"
  >
    <option value="">Any keyword</option>
  </select>

  <label for="exclude-keyword-filter"><b>Exclude a keyword:</b></label>
  <select
    id="exclude-keyword-filter"
    class="tip-input"
    onchange="filterResources()"
  >
    <option value="">Don't exclude any keyword</option>
  </select>
</div>

## Resources

<!-- Show sprinkles -->
<div class="sticky-board">
  {% for tip in tips() %}
    {% if tip.theme == "professional-development" or "professional-development" in tip.keywords %}
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
{% endif %}
{% endfor %}
</div>

</br>

<!-- Show resources -->
<div class="resources-board">
  {% for resource in resources() %}
    {% if resource.theme == "professional-development" or "professional-development" in resource.keywords %}
        <div
        class="resource-box"
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

    {% endif %}
  {% endfor %}
</div>

---

## Interested in our other themes? 

[Explore all resources here.](../all.md)

!!! question "Have something to share?"
    Check out our [Contributing Guide](/how-to-contribute/index.md) for our quick and easy ways to add your own resources.  


<!-- Optional keyword filter for resources and sticky notes -->
<script>

const selectedTheme = "professional-development";

function updateKeywordFilter() {
  // const selectedTheme =
  //   document.getElementById("theme-filter").value;

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
  // const selectedTheme =
  //   document.getElementById("theme-filter").value;

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
  // const selectedTheme =
  //   document.getElementById("theme-filter").value;

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

if (typeof document$ !== "undefined") {
  document$.subscribe(function () {
    updateKeywordFilter();
    updateExcludeKeywordFilter();
    filterResources();
  });
} else {
  // Fallback for a normal page load without Material instant navigation
  updateKeywordFilter();
  updateExcludeKeywordFilter();
  filterResources();
}
</script>