import os

search_dir = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website"
html_files = []
for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

# The link we want to insert.
nav_str_desktop = '<li><a href="{prefix}gallery.html" class="nav-link">Gallery</a></li>'
nav_str_mobile = '<a href="{prefix}gallery.html" class="mobile-menu-link">Gallery</a>'
footer_str = '<a href="{prefix}gallery.html" class="footer-link">Gallery</a>'

for file in html_files:
    # Set prefix correctly based on whether it's index.html or in pages/
    is_index = ('index.html' in os.path.basename(file) and 'pages' not in root)
    prefix = 'pages/' if is_index else ''
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We want to add Gallery after Conferences.
    
    # 1. Desktop Nav
    desktop_target = f'<li><a href="{prefix}conferences.html" class="nav-link'
    if desktop_target in content:
        # Find where the conferences </li> ends to insert after it
        parts = content.split(desktop_target)
        if len(parts) > 1:
            rest = parts[1]
            end_li_idx = rest.find('</li>')
            if end_li_idx != -1:
                end_li_idx += 5 # Length of </li>
                # Splice in the gallery link
                if f'{prefix}gallery.html' not in content:
                    content = parts[0] + desktop_target + rest[:end_li_idx] + '\n                        ' + nav_str_desktop.format(prefix=prefix) + rest[end_li_idx:]

    # 2. Mobile Nav
    mobile_target = f'<a href="{prefix}conferences.html" class="mobile-menu-link'
    if mobile_target in content:
        # Find where the </a> ends
        parts = content.split(mobile_target)
        if len(parts) > 1:
            rest = parts[1]
            end_a_idx = rest.find('</a>')
            if end_a_idx != -1:
                end_a_idx += 4
                if f'{prefix}gallery.html" class="mobile-menu-link"' not in content:
                    content = parts[0] + mobile_target + rest[:end_a_idx] + '\n        ' + nav_str_mobile.format(prefix=prefix) + rest[end_a_idx:]

    # 3. Footer Nav
    footer_target = f'<a href="{prefix}conferences.html" class="footer-link'
    if footer_target in content:
        # Find where the </a> ends
        parts = content.split(footer_target)
        if len(parts) > 1:
            rest = parts[1]
            end_a_idx = rest.find('</a>')
            if end_a_idx != -1:
                end_a_idx += 4
                if f'{prefix}gallery.html" class="footer-link"' not in content:
                    content = parts[0] + footer_target + rest[:end_a_idx] + '\n                        ' + footer_str.format(prefix=prefix) + rest[end_a_idx:]

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated navs in: {os.path.basename(file)}")
