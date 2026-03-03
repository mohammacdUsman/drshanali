import os
import re

search_dir = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website"
html_files = []
for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

new_loader = """<!-- PAGE LOADER -->
    <div id="page-loader" class="page-loader">
        <div class="juggling-loader">
            <div class="juggling-dot"></div>
            <div class="juggling-dot"></div>
            <div class="juggling-dot"></div>
        </div>
    </div>

"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace from <!-- PAGE LOADER --> to the next tag which is <header>
    if '<!-- PAGE LOADER -->' in content:
        content = re.sub(
            r'<!-- PAGE LOADER -->.*?<header',
            new_loader + '<header',
            content,
            flags=re.DOTALL
        )
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Update juggling loader in: {os.path.basename(file)}")
