import os
import re
import json

base_dir = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website"
img_dir = os.path.join(base_dir, "images")
gallery_file = os.path.join(base_dir, "pages", "gallery.html")

# Find all image files
valid_exts = {'.png', '.jpg', '.jpeg'}
img_files = []
for f in os.listdir(img_dir):
    ext = os.path.splitext(f)[1].lower()
    if ext in valid_exts:
        # Avoid including SVGs like the logo if there are any, just stick to png/jpg
        img_files.append(f'../images/{f}')

# Format as JavaScript array string
js_array_str = json.dumps(img_files, indent=12)

# Open gallery.html and replace masterImageList
with open(gallery_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace using regex looking for the masterImageList block
pattern = re.compile(r'(const masterImageList\s*=\s*\[)[\s\S]*?(\];)', re.MULTILINE)
new_content = pattern.sub(rf'\1\n            {js_array_str[1:-1]}        \2', content)

# Also update displayCount to 24 instead of 12 to show more images at once:
new_content = re.sub(r'const displayCount\s*=\s*12;', 'const displayCount = 24;', new_content)

with open(gallery_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Added {len(img_files)} images to gallery!")
