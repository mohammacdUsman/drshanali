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
        
    gall_str_d = f'\n            <li><a href="{prefix}gallery.html" class="nav-link">Gallery</a></li>'
    gall_str_m = f'\n    <a href="{prefix}gallery.html" class="mobile-menu-link">Gallery</a>'
    gall_str_f = f'\n                        <a href="{prefix}gallery.html" class="footer-link">Gallery</a>'
    
    # Desktop
    # Look for: <li><a href="pages/conferences.html" class="nav-link">Conferences</a></li>
    # (Allowing optional active class)
    if 'gallery.html' not in content:
        content = re.sub(
            rf'(<li><a href="{prefix}conferences\.html" class="nav-link(?: active)?">Conferences</a></li>)',
            r'\1' + gall_str_d,
            content
        )
        # Mobile
        content = re.sub(
            rf'(<a href="{prefix}conferences\.html" class="mobile-menu-link">Conferences</a>)',
            r'\1' + gall_str_m,
            content
        )
        # Footer
        content = re.sub(
            rf'(<a href="{prefix}conferences\.html" class="footer-link">Conferences</a>)',
            r'\1' + gall_str_f,
            content
        )
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched: {os.path.basename(file)}")
    else:
        print(f"Already patched: {os.path.basename(file)}")
