---
title: Community Top Tips
tags: [Central themes, Top Tips]
---

A space to share quick advice, useful experiences, and things you wish someone had told you earlier.

## Why this exists

Often the most helpful things are simple — a practical tip, something that worked, a mistake to avoid, or a small insight from experience.

**Community Top Tips is designed to make sharing those things easy.** Whether it’s about events, collaboration, communication, or inclusive practice, this is a lightweight space for sharing what you’ve learned.

Curated by the [CAKE team](https://www.cake.ac.uk/about/who-are-we).

## Explore Themes

Browse community advice by topic.

<div class="tip-theme-grid">

{% set themes = [
  {"name": "Events", "tag": "events", "icon": "🎤", "desc": "Workshops, conferences and hybrid meetings."},
  {"name": "Collaboration", "tag": "collaboration", "icon": "🤝", "desc": "Working together across teams and disciplines."},
  {"name": "Inclusion", "tag": "inclusion", "icon": "🌍", "desc": "Accessibility and inclusive community practices."},
  {"name": "Facilitation", "tag": "facilitation", "icon": "🧠", "desc": "Helping groups work better together."}
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


### Inspirations for tips: 

* “What’s one thing you wish you knew earlier?”
* “What’s a small thing that made a big difference?”
* “What advice would you give someone new to this?”
* “What mistake helped you learn something useful?”


## Contributing 
Got a tip, thought, or bit of advice to add? Click the little page icon at the top of the page to edit it. You’ll be taken to GitHub, where you can add your thoughts and send them over for review in just a few clicks. It doesn’t need to be polished or perfect, even a short tip or small insight could really help someone else.

Read our [How to contribute](../how-to-contribute/index.md) guide for more.

Please also familiarise yourself with our [Code of Conduct](../code-of-conduct.md). 

* Use welcoming and inclusive language
* Be respectful of different viewpoints and experiences
* Gracefully accept constructive criticism
* Focus on what is best for the community
* Show courtesy and respect towards others

