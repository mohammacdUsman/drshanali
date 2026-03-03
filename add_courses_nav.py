import os
import re

search_dir = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website"
html_files = []
for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

# Navigation item to add
nav_desktop = r'                        <li><a href="courses.html" class="nav-link">Courses</a></li>\n                        <li><a href="contact.html"'
nav_mobile = r'        <a href="courses.html" class="mobile-menu-link">Courses</a>\n        <a href="contact.html"'
footer_link = r'                        <a href="courses.html" class="footer-link">Courses</a>\n                        <a href="contact.html"'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already added
    if 'href="courses.html"' not in content:
        # We need to adjust paths if it's index.html vs pages/*.html
        if 'pages' not in file and 'index.html' in file:
            # in index.html, it's pages/courses.html
            nav_desktop_idx = nav_desktop.replace('courses.html', 'pages/courses.html').replace('contact.html', 'pages/contact.html')
            nav_mobile_idx = nav_mobile.replace('courses.html', 'pages/courses.html').replace('contact.html', 'pages/contact.html')
            footer_link_idx = footer_link.replace('courses.html', 'pages/courses.html').replace('contact.html', 'pages/contact.html')
            
            content = re.sub(r'                        <li><a href="pages/contact.html"', nav_desktop_idx, content)
            content = re.sub(r'        <a href="pages/contact.html"', nav_mobile_idx, content)
            content = re.sub(r'                        <a href="pages/contact.html"', footer_link_idx, content)

        else:
            # in pages/
            content = re.sub(r'                        <li><a href="contact.html"', nav_desktop, content)
            content = re.sub(r'        <a href="contact.html"', nav_mobile, content)
            content = re.sub(r'                        <a href="contact.html"', footer_link, content)
            
            if 'courses.html' in file:
                # Active state for courses.html
                content = content.replace('class="nav-link">Courses</a>', 'class="nav-link active">Courses</a>')

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated navigation in {file}")
