import os
import re

# Directory containing the website
root_dir = r"e:\ShanAli-law-website"

# Broad emoji regex
# Includes common ones like 📅, 🏛️, etc.
emoji_pattern = re.compile(
    r"["
    r"\U0001f300-\U0001f6ff"  # Miscellaneous Symbols and Pictographs to Emoticons
    r"\U0001f900-\U0001f9ff"  # Supplemental Symbols and Pictographs
    r"\u2600-\u26ff"          # Miscellaneous Symbols
    r"\u2700-\u27bf"          # Dingbats
    r"\U0001f1e0-\U0001f1ff"  # Flags
    r"\u2300-\u23ff"          # Miscellaneous Technical
    r"\u2500-\u2b5f"          # Various symbols
    r"]+", 
    flags=re.UNICODE
)

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove emojis
    content = emoji_pattern.sub('', content)
    
    # 2. Update favicon
    rel_depth = file_path.replace(root_dir, "").count(os.sep) - 1
    img_prefix = "../" * rel_depth if rel_depth > 0 else ""
    favicon_path = f"{img_prefix}images/favicon.png"

    # Ensure favicon link is correct
    # If link rel="icon" exists, replace it. If not, maybe add it? (Already exists in my build)
    content = re.sub(
        r'<link rel="icon"\s+href="[^"]+"[^>]*>',
        f'<link rel="icon" href="{favicon_path}" type="image/png">',
        content
    )

    # 3. Restore "S" in shields (Undo previous mistake)
    # Replaces the img-based logo shield back to text "S"
    content = re.sub(
        r'<div class="(logo|footer)-shield">.*?<img.*?>.*?</div>',
        r'<div class="\1-shield">S</div>',
        content,
        flags=re.DOTALL
    )
    
    # Just in case some were not caught by DOTALL or variation
    content = re.sub(
        r'<div class="(logo|footer)-shield">S</div>',
        r'<div class="\1-shield">S</div>',
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
