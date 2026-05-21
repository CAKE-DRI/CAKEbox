---
title: Collaboration
---

# 🤝 Collaboration

Tips, lessons learned, and community advice about working together effectively.

<div class="sticky-board">

{% for tip in tips.collaboration %}

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

## ✨ Share your experience

Got a useful collaboration tip, lesson learned, or idea?

<div class="submit-box">

  <input
    id="tip-title"
    class="md-input"
    type="text"
    placeholder="Tip title" />

  <textarea
    id="tip-text"
    class="md-input"
    rows="5"
    placeholder="Share your experience or advice..."></textarea>

  <label for="tip-emoji"><strong>Emoji</strong></label>

  <select id="tip-emoji" class="md-input">
    <option>🤝</option>
    <option>💡</option>
    <option>📝</option>
    <option>🚀</option>
    <option>🎯</option>
    <option>✨</option>
  </select>

  <label for="tip-colour"><strong>Sticky note colour</strong></label>

  <select id="tip-colour" class="md-input">
    <option value="yellow">Yellow</option>
    <option value="blue">Blue</option>
    <option value="green">Green</option>
    <option value="pink">Pink</option>
  </select>

  <button
    class="md-button md-button--primary"
    onclick="submitTip()">
    ✨ Add tip
  </button>

</div>

<script>

function submitTip() {

  const title = document.getElementById("tip-title").value;
  const text = document.getElementById("tip-text").value;
  const emoji = document.getElementById("tip-emoji").value;
  const colour = document.getElementById("tip-colour").value;

  const issueTitle =
    `[Collaboration Tip] ${title}`;

  const issueBody =
`title: ${title}

emoji: ${emoji}

color: ${colour}

text:
${text}`;

  const url =
  "https://github.com/mzhc13/CAKEbox/issues/new"
    + "?labels=top-tip,collaboration"
    + "&title=" + encodeURIComponent(issueTitle)
    + "&body=" + encodeURIComponent(issueBody);

  window.open(url, "_blank");
}

</script>
