import os
import re

search_dir = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website"
html_files = []
for root, dirs, files in os.walk(search_dir):
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

index_file = os.path.join(search_dir, "index.html")
with open(index_file, "r", encoding="utf-8") as f:
    index_content = f.read()

# Capture the exact footer HTML from index.html
footer_pattern = re.compile(r'(<footer class="footer">)[\s\S]*?(</footer>)', re.MULTILINE)
m = footer_pattern.search(index_content)
if not m:
    print("Could not find footer in index.html!")
    exit(1)

master_footer = m.group(0)

for file in html_files:
    if file == index_file:
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine if the file is in a subdirectory (like pages/)
    is_subpage = ('pages' in os.path.dirname(file))
    
    if is_subpage:
        # Convert root-level links for a subpage
        # "index.html" -> "../index.html"
        local_footer = master_footer.replace('href="index.html"', 'href="../index.html"')
        # "pages/about.html" -> "about.html"
        local_footer = local_footer.replace('href="pages/', 'href="')
    else:
        # Use master exactly
        local_footer = master_footer
        
    # Replace the existing footer with the proper standardized local footer
    new_content = footer_pattern.sub(local_footer, content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Standardized full footer on: {os.path.basename(file)}")
    else:
        print(f"Footer already standard on: {os.path.basename(file)}")
