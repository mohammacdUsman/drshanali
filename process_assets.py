import os
import re

# Directory containing the website
root_dir = r"e:\ShanAli-law-website"

# Regex for emojis
emoji_pattern = re.compile(
    "["
    "\U0001f300-\U0001f6ff"  # Miscellaneous Symbols and Pictographs to Emoticons
    "\U0001f900-\U0001f9ff"  # Supplemental Symbols and Pictographs
    "\u2600-\u26ff"          # Miscellaneous Symbols
    "\u2700-\u27bf"          # Dingbats
    "\U0001f1e0-\U0001f1ff"  # Flags (iOS/etc)
    "]+", 
    flags=re.UNICODE
)

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove emojis
    content = emoji_pattern.sub('', content)

    # 2. Update favicon
    # Rel path calculation for links
    rel_depth = file_path.replace(root_dir, "").count(os.sep) - 1
    img_prefix = "../" * rel_depth if rel_depth > 0 else ""
    favicon_path = f"{img_prefix}images/favicon.png"

    # Replace existing favicon link
    # Pattern: <link rel="icon" href="...">
    content = re.sub(
        r'<link rel="icon"\s+href="[^"]+"[^>]*>',
        f'<link rel="icon" href="{favicon_path}" type="image/png">',
        content
    )

    # 3. Replace "S" in logo-shield and footer-shield
    # <div class="logo-shield">S</div>
    # <div class="footer-shield">S</div>
    content = re.sub(
        r'(<div class="logo-shield">)S(</div>)',
        rf'\1<img src="{favicon_path}" alt="Logo" style="width:100%; height:100%; object-fit:contain; padding:4px;">\2',
        content
    )
    content = re.sub(
        r'(<div class="footer-shield">)S(</div>)',
        rf'\1<img src="{favicon_path}" alt="Logo" style="width:100%; height:100%; object-fit:contain; padding:4px;">\2',
        content
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# Process all HTML files
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".html"):
            process_file(os.path.join(root, file))

print("Processing complete.")
