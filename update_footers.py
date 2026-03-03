import os
import re

search_dir = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website\pages"
html_files = []
for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the LinkedIn footer item and append the email item
    # In pages/*.html, the linkedin item looks like:
    # <div class="footer-contact-item"><span class="footer-contact-icon">🔗</span><a ... </a></div>
    
    # We can match up to the end of that </div> and insert our new div.
    pattern = r'(<div class="footer-contact-item"><span class="footer-contact-icon">🔗</span>.*?</a>\s*</div>)'
    
    email_block = r'''
                    <div class="footer-contact-item">
                        <span class="footer-contact-icon">✉️</span>
                        <a href="mailto:drusmanka00786@gmail.com" style="color:inherit;">drusmanka00786@gmail.com</a>
                    </div>'''
    
    if "drusmanka00786@gmail.com" not in content[content.rfind('footer-contact-item'):]: # ensure not already added in footer
        content = re.sub(pattern, r'\1' + email_block, content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated footer in {file}")

