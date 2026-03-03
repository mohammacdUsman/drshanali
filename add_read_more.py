import re

filepath = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website\pages\education.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add CSS
css_to_add = """
    .ed-card-expandable {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.5s cubic-bezier(0, 1, 0, 1);
      display: flex;
      flex-direction: column;
      gap: 1.2rem;
    }
    .ed-card-expandable.expanded {
      max-height: 1500px;
      transition: max-height 0.8s ease-in-out;
    }
    .ed-read-more-btn {
      background: none;
      border: none;
      color: var(--primary);
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 0;
      margin-top: -10px;
      transition: color var(--transition);
      align-self: flex-start;
      margin-top: auto;
    }
    .ed-read-more-btn:hover {
      color: var(--accent);
    }
    .ed-read-more-btn svg {
      width: 18px;
      height: 18px;
      transition: transform var(--transition);
    }
    .ed-read-more-btn.expanded svg {
      transform: rotate(180deg);
    }
"""

if ".ed-card-expandable" not in content:
    content = content.replace("/* Utilities */", css_to_add + "\n    /* Utilities */")

# 2. Add JS
js_to_add = """
            window.toggleReadMoreEdu = function(btn) {
                const expandable = btn.previousElementSibling;
                expandable.classList.toggle('expanded');
                btn.classList.toggle('expanded');
                if (expandable.classList.contains('expanded')) {
                    btn.innerHTML = 'Read Less <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>';
                } else {
                    btn.innerHTML = 'Read More <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>';
                }
            };
"""
if "toggleReadMoreEdu" not in content:
    content = content.replace("function handleScrollAnimations() {", js_to_add + "\n            function handleScrollAnimations() {")

# 3. Modify HTML
# Find all occurrences of ed-card-details to the end of ed-card-highlight
parts = content.split('<div class="ed-card-details">')
new_content = parts[0]

for i in range(1, len(parts)):
    part = parts[i]
    # In this part, we need to find the end of `ed-card-highlight`
    # It looks like: ... <div class="ed-card-highlight"> ... </div> \s* </div>
    # We will split by `<div class="ed-card-highlight">`
    sub_parts = part.split('<div class="ed-card-highlight">')
    if len(sub_parts) == 2:
        details_content = sub_parts[0]
        # Next is the highlight content
        highlight_split = sub_parts[1].split('</div>', 1) # First </div> closes the highlight paragraph or whatever
        
        # Actually it's safer to just regex matching the closing of ed-card-highlight
        # ed-card-highlight always has a nested <p>, so it's <p>...</p>\n</div>
        import re
        m = re.search(r'(.*?</div>\s*)(</div>\s*</div>)', sub_parts[1], flags=re.DOTALL)
        if m:
            pass # this regex assumes it's followed by </div> </div> for ed-card-content and ed-education-card
        
new_content_2 = re.sub(
    r'(<div class="ed-card-details">.*?</p>\s*</div>)(\s*</div>\s*</div>)',
    r'<div class="ed-card-expandable">\n\1\n</div>\n<button class="ed-read-more-btn" onclick="toggleReadMoreEdu(this)">Read More <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></button>\2',
    content,
    flags=re.DOTALL
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content_2)
print("Updated successfully")
