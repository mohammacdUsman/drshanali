import os
import re

search_dir = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website"
html_files = []
for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

for file in html_files:
    is_index = ('index.html' in os.path.basename(file) and 'pages' not in root)
    prefix = 'pages/' if is_index else ''
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # 1. Clean up "Courses" links injected near CTA buttons "btn btn-accent" or similar
    # These typically look like: <a href="courses.html" class="mobile-menu-link">Courses</a>\n        <a href="contact.html" class="btn btn-accent">📅 Book A Consultation</a>
    # Or in index.html <a href="pages/courses.html" class="mobile-menu-link">Courses</a>\n        <a href="pages/contact.html" class="btn btn-accent">
    
    content = re.sub(
        r'<a href=".*?courses\.html"\s*class="mobile-menu-link">Courses</a>\s*(<a href="[^"]*contact\.html"[^>]*class="(?:btn[^"]*)"[^>]*>)',
        r'\1',
        content
    )
    
    # Clean up index.html CTA
    content = re.sub(
        r'<a href="pages/courses\.html"\s*class="mobile-menu-link">Courses</a>\s*(<a href="pages/contact\.html"\s*class="btn btn-accent">)',
        r'\1',
        content
    )

    # 2. Fix improperly styled footer links
    # <a href="courses.html" class="mobile-menu-link">Courses</a>\n        <a href="contact.html" class="footer-link">Contact</a>
    # We want it to be <a href="courses.html" class="footer-link">Courses</a> completely aligned.
    
    bad_footer = rf'<a href="{prefix}courses.html" class="mobile-menu-link">Courses</a>\s*<a href="{prefix}contact.html" class="footer-link">Contact</a>'
    good_footer = rf'<a href="{prefix}courses.html" class="footer-link">Courses</a>\n                        <a href="{prefix}contact.html" class="footer-link">Contact</a>'
    
    content = re.sub(bad_footer, good_footer, content)
    
    # Just in case, fix pure class mismatches inside the footer section
    # If <a href="courses.html" class="mobile-menu-link">Courses</a> exists within footer links div, change it
    
    if content != original_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned unwanted Courses links: {os.path.basename(file)}")
    else:
        print(f"Already clean: {os.path.basename(file)}")
