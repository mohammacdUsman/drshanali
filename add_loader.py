import os
import re

search_dir = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website"
html_files = []
for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

# The loader snippet
loader_html = """
    <!-- PAGE LOADER -->
    <div id="page-loader" class="page-loader">
        <div class="loader-shield">S</div>
    </div>
"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if already has loader
    if '<div id="page-loader"' not in content:
        # We need to insert it right after the <body> tag. 
        # Sometimes it's <body class="..."> or <body>. 
        # Using a regex to find opening body tag:
        # We want to insert the loader_html immediately following it.
        # So we replace <body> with <body> + loader_html
        content = re.sub(r'(<body[^>]*>)', r'\1' + loader_html, content, count=1, flags=re.IGNORECASE)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added loader to: {os.path.basename(file)}")
    else:
        print(f"Loader already in: {os.path.basename(file)}")
