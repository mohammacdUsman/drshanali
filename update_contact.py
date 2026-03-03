import os
import re

search_dir = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website"
html_files = []
for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Just in case there's any stray navigation book consultation
    content = re.sub(r'<a href="[^"]*" class="nav-cta"[^>]*>[^<]*<\/a>[\r\n\s]*', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<a href="[^"]*" class="mobile-menu-link"[^>]*>Book Consultation<\/a>[\r\n\s]*', '', content, flags=re.IGNORECASE)

    # Replace footer "Send a Message" with the email address
    pattern = r'<div class="footer-contact-item">\s*<span class="footer-contact-icon">✉️</span>\s*<a href="[^"]*"(?:[^>]*)>Send a Message</a>\s*</div>'
    replacement = r'''<div class="footer-contact-item">
            <span class="footer-contact-icon">✉️</span>
            <a href="mailto:drusmanka00786@gmail.com" style="color:inherit;">drusmanka00786@gmail.com</a>
          </div>'''
    content = re.sub(pattern, replacement, content)

    # For contact page specifically, add the email section
    if "contact.html" in file:
        if '<div class="contact-info-icon">✉️</div>' not in content:
            # Find the Location block and insert Email before it
            loc_pattern = r'(<div class="contact-info-item">\s*<div class="contact-info-icon">📍</div>)'
            email_block = r'''<div class="contact-info-item">
                        <div class="contact-info-icon">✉️</div>
                        <div>
                            <h4>Email</h4>
                            <a href="mailto:drusmanka00786@gmail.com" style="color:rgba(255, 255, 255, 0.8);">drusmanka00786@gmail.com</a>
                        </div>
                    </div>
                    '''
            content = re.sub(loc_pattern, email_block + r'\1', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} files.")
