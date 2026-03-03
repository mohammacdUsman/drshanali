import os
import re

search_dir = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website"
html_files = []
for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

# Standardize the Quick Links section of the footer across all files.
for file in html_files:
    is_index = ('index.html' in os.path.basename(file) and 'pages' not in root)
    prefix = 'pages/' if is_index else ''
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define what the standard footer Quick Links section SHOULD look like exactly
    standard_footer_links = f"""                    <div class="footer-links">
                        <a href="{prefix if not is_index else ''}index.html" class="footer-link">Home</a>
                        <a href="{prefix}about.html" class="footer-link">About Me</a>
                        <a href="{prefix}practice-areas.html" class="footer-link">Practice Areas</a>
                        <a href="{prefix}education.html" class="footer-link">Education & Achievements</a>
                        <a href="{prefix}conferences.html" class="footer-link">Conferences</a>
                        <a href="{prefix}international.html" class="footer-link">International & Research</a>
                        <a href="{prefix}publications.html" class="footer-link">Publications</a>
                        <a href="{prefix}gallery.html" class="footer-link">Gallery</a>
                        <a href="{prefix}courses.html" class="footer-link">Courses</a>
                        <a href="{prefix}contact.html" class="footer-link">Contact</a>
                    </div>"""
                    
    # The tricky part is matching the existing <div class="footer-links"> under "Quick Links"
    # We look for:
    # <h4>Quick Links</h4>
    # <div class="footer-links">
    # ... any content up to </div>
    
    # We use a pattern to find the exact block under Quick Links
    pattern = re.compile(
        r'(<h4>Quick Links</h4>\s*<div class="footer-links">)[\s\S]*?(</div>)', 
        re.MULTILINE
    )
    
    # Actually wait, the `<h4>Quick Links</h4>` is the preceding sibling. 
    # The replacement is:
    replacement = f"""<h4>Quick Links</h4>\n{standard_footer_links}"""
    
    # Let's clean up index.html specific cases where `../index.html` might be generated in standard_footer_links
    if is_index:
        standard_footer_links = standard_footer_links.replace('href="index.html"', 'href="index.html"').replace('href="pages/index.html"', 'href="index.html"')
    else:
        standard_footer_links = standard_footer_links.replace('href="index.html"', 'href="../index.html"')
        
    replacement = f"""<h4>Quick Links</h4>\n{standard_footer_links}"""
    
    new_content = pattern.sub(replacement, content)
    
    
    # Also standardize mobile menu exactly to match the desktop nav items
    standard_mobile_menu = f"""<div class="mobile-menu" id="mobileMenu">
        <a href="{prefix if not is_index else ''}index.html" class="mobile-menu-link">Home</a>
        <a href="{prefix}about.html" class="mobile-menu-link">About Me</a>
        <a href="{prefix}practice-areas.html" class="mobile-menu-link">Practice Areas</a>
        <a href="{prefix}international.html" class="mobile-menu-link">Research</a>
        <a href="{prefix}publications.html" class="mobile-menu-link">Publications</a>
        <a href="{prefix}education.html" class="mobile-menu-link">Education</a>
        <a href="{prefix}conferences.html" class="mobile-menu-link">Conferences</a>
        <a href="{prefix}gallery.html" class="mobile-menu-link">Gallery</a>
        <a href="{prefix}courses.html" class="mobile-menu-link">Courses</a>
        <a href="{prefix}contact.html" class="mobile-menu-link">Contact</a>
    </div>"""

    if is_index:
        standard_mobile_menu = standard_mobile_menu.replace('href="index.html"', 'href="index.html"')
    else:
        standard_mobile_menu = standard_mobile_menu.replace('href="index.html"', 'href="../index.html"')

    mobile_pattern = re.compile(
        r'<div class="mobile-menu" id="mobileMenu">[\s\S]*?</div>',
        re.MULTILINE
    )
    new_content = mobile_pattern.sub(standard_mobile_menu, new_content)

    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Standardized footer & mobile menu on: {os.path.basename(file)}")
