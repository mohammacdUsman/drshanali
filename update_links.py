import os
import re

base_path = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website"
html_files = []

for root, dirs, files in os.walk(base_path):
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

# regex to find the button, usually `<a href="contact.html" class="nav-cta">Book Consultation</a>`
# or `<a href="pages/contact.html" class="nav-cta">Book Consultation</a>`
# or `<a href="contact.html" class="mobile-menu-link" style="color:var(--accent)">Book Consultation</a>`
# or similar.
btn_pattern1 = re.compile(r'<a href="[^"]*contact\.html" class="nav-cta">Book Consultation<\/a>[\r\n]*', re.IGNORECASE)
btn_pattern2 = re.compile(r'<a href="[^"]*contact\.html" class="mobile-menu-link"[^>]*>Book Consultation<\/a>[\r\n]*', re.IGNORECASE)

form_pattern = re.compile(r'<form id="contactForm" novalidate>', re.IGNORECASE)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = btn_pattern1.sub('', content)
    new_content = btn_pattern2.sub('', new_content)

    if file.endswith('contact.html'):
        new_content = form_pattern.sub('<form id="contactForm" action="https://formsubmit.co/drusmanka00786@gmail.com" method="POST" novalidate>', new_content)

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
