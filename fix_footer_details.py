import os
import re

index_file = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website\index.html"
with open(index_file, "r", encoding="utf-8") as f:
    content = f.read()

# Fix the wrapping linkedin text
content = content.replace(">linkedin.com/in/shan-ali-blockchain</a>", ">LinkedIn</a>")

# Fix the envelope emoji to standard HTML entity to prevent box rendering issues
content = content.replace("✉️", "&#9993;")
content = content.replace("📍", "&#128205;")
content = content.replace("🔗", "&#128279;")

with open(index_file, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html footer details fixed.")
