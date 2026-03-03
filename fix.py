import os
import re

search_dir = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website"
html_files = []
for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

def insert_before_contact(content, is_index):
    # Desktop
    desktop_search = r'(<li><a\s+href="pages/contact.html"\s+class="nav-link">Contact</a></li>)' if is_index else r'(<li><a\s+href="contact.html"\s+class="nav-link( active)?">Contact</a></li>)'
    desktop_rep = r'<li><a href="pages/courses.html" class="nav-link">Courses</a></li>\n            \1' if is_index else r'<li><a href="courses.html" class="nav-link">Courses</a></li>\n                        \1'
    content = re.sub(desktop_search, desktop_rep, content)

    # Mobile
    mobile_search = r'(<a\s+href="pages/contact.html"\s+class="mobile-menu-link">Contact</a>)' if is_index else r'(<a\s+href="contact.html"\s+class="mobile-menu-link( active)?">Contact</a>)'
    mobile_rep = r'<a href="pages/courses.html" class="mobile-menu-link">Courses</a>\n    \1' if is_index else r'<a href="courses.html" class="mobile-menu-link">Courses</a>\n        \1'
    content = re.sub(mobile_search, mobile_rep, content)

    # Footer
    footer_search = r'(<a\s+href="pages/contact.html"\s+class="footer-link">Contact</a>)' if is_index else r'(<a\s+href="contact.html"\s+class="footer-link( active)?">Contact</a>)'
    footer_rep = r'<a href="pages/courses.html" class="footer-link">Courses</a>\n            \1' if is_index else r'<a href="courses.html" class="footer-link">Courses</a>\n                        \1'
    content = re.sub(footer_search, footer_rep, content)

    return content

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    is_index = 'index.html' in file and 'pages' not in os.path.dirname(file)

    if is_index and 'pages/courses.html' not in content:
        content = insert_before_contact(content, True)
    elif not is_index and 'courses.html' not in content:
        content = insert_before_contact(content, False)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed: {file}")
