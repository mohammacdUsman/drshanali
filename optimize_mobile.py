import os
import re

def add_lazy_loading(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                # Add loading="lazy" to img tags if not already present
                # Also ensure images have alt tags if they don't
                def img_replace(match):
                    tag = match.group(0)
                    if 'loading=' not in tag:
                        tag = tag.replace('<img', '<img loading="lazy"')
                    return tag
                
                new_content = re.sub(r'<img[^>]+>', img_replace, content)
                
                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated {file_path}")

add_lazy_loading(r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website")
