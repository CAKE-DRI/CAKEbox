---
title: Inclusion & Accessibility
tags: [Key Themes]
---

Equality, Diversity, Inclusion and Accessibility (EDIA) is fundamental to building a community where everyone feels welcomed, included and like they can contribute meaningfully. 

The [CAKE-CoSeC EDI Working Group](CAKE-CoSeC-EDI-WG/index.md) supports this work by developing practical guidance and identifying priority areas for action.

<!-- Enable filtering for keywords, theme is fixed -->
<div class="resources-filter">
  <label for="keyword-filter"><b>Filter by keyword:</b></label>
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
    {% if tip.theme == "inclusion" or "inclusion" in tip.keywords %}
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
    {% if resource.theme == "inclusion" or "inclusion" in resource.keywords %}
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

## Community Groups and Resource Hubs

The following groups provide curations of valuable EDIA leadership and resources:

- [CAKE-CoSeC EDI Working Group](CAKE-CoSeC-EDI-WG/index.md)
- [Women in High Performance Computing (WHPC)](https://womeninhpc.org)
- [Society of Research Software Engineering EDIA and Role Diversity Working Group](https://society-rse.org/get-involved/edia-working-group/)
- [EPSRC EDI Hub+](https://edihubplus.ac.uk/resource-centre/)
- [UKRI Equality, Diversity and Inclusion](https://www.ukri.org/what-we-do/supporting-healthy-research-and-innovation-culture/equality-diversity-and-inclusion/)
- [Move the Needle Knowledge Portal](https://alces-flight.com/move-the-needle-knowledge-base/)
- [RainbowR -  connect, support and promote LGBTQ+ people in the R community](https://rainbowr.org/)
- [Institute for Research Software News and Blogs Hub](https://www.software.ac.uk/news-and-blogs-hub)


## Interested in our other themes? 

[Explore all resources here.](../all.md)

!!! question "Have something to share?"
    Check out our [Contributing Guide](/how-to-contribute/) for our quick and easy ways to add your own resources.  


<!-- Optional keyword filter for resources and sticky notes -->
<script>
function updateKeywordFilter() {
  const keywordFilter =
    document.getElementById("keyword-filter");

  const previousKeyword = keywordFilter.value;

  // Reset the dropdown
  keywordFilter.innerHTML =
    '<option value="">All keywords</option>';

  // Collect keywords
  const keywords = new Set();

  document.querySelectorAll(
    ".resource-box, .sticky-note"
  ).forEach(item => {
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
  const excludeFilter =
    document.getElementById("exclude-keyword-filter");

  const previousKeyword = excludeFilter.value;

excludeFilter.innerHTML =
    '<option value="">All keywords</option>';

  // Collect keywords
  const keywords = new Set();

  document.querySelectorAll(
    ".resource-box, .sticky-note"
  ).forEach(item => {
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
  updateKeywordFilter();
  updateExcludeKeywordFilter();

  const selectedKeyword =
    document.getElementById("keyword-filter").value;

  const excludedKeyword =
    document.getElementById("exclude-keyword-filter").value;

  document.querySelectorAll(
    ".resource-box, .sticky-note"
  ).forEach(item => {

    const keywords = item.dataset.keywords
      ? item.dataset.keywords.split(",").map(k => k.trim())
      : [];

    const excludesKeyword =
      !excludedKeyword || !keywords.includes(excludedKeyword);

    const matchesKeyword =
      !selectedKeyword || keywords.includes(selectedKeyword);

    item.style.display =
      matchesKeyword && excludesKeyword
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