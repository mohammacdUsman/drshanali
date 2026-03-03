import os
import re

pub_html_path = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website\pages\publications.html"

pubs = [
    {
        "pattern": r'(<img\s*src="data:image/svg\+xml[\s\S]*?alt="DAOs in Italy"[\s\S]*?>)',
        "url": "https://images.unsplash.com/photo-1639762681485-074b7f4ec651?auto=format&fit=crop&w=600&q=80"
    },
    {
        "pattern": r'(<img\s*src="data:image/svg\+xml[\s\S]*?alt="Blockchain and Cognitive Liberty"[\s\S]*?>)',
        "url": "https://images.unsplash.com/photo-1559757175-5700dde675bc?auto=format&fit=crop&w=600&q=80"
    },
    {
        "pattern": r'(<img\s*src="data:image/svg\+xml[\s\S]*?alt="AI in the Metaverse"[\s\S]*?>)',
        "url": "https://images.unsplash.com/photo-1622979135225-d2ba269cf1ac?auto=format&fit=crop&w=600&q=80"
    },
    {
        "pattern": r'(<img\s*src="data:image/svg\+xml[\s\S]*?alt="Minority Shareholders Pakistan"[\s\S]*?>)',
        "url": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=600&q=80"
    },
    {
        "pattern": r'(<img\s*src="data:image/svg\+xml[\s\S]*?alt="Derivative Action Minority Shareholders"[\s\S]*?>)',
        "url": "https://images.unsplash.com/photo-1589829085413-56de8ae18c73?auto=format&fit=crop&w=600&q=80"
    },
    {
        "pattern": r'(<img\s*src="data:image/svg\+xml[\s\S]*?alt="Cyber Terrorism"[\s\S]*?>)',
        "url": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=600&q=80"
    },
    {
        "pattern": r'(<img\s*src="data:image/svg\+xml[\s\S]*?alt="Cyber Warfare"[\s\S]*?>)',
        "url": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=600&q=80"
    },
    {
        "pattern": r'(<img\s*src="data:image/svg\+xml[\s\S]*?alt="Web Based Trading"[\s\S]*?>)',
        "url": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=600&q=80"
    },
    {
        "pattern": r'(<img\s*src="data:image/svg\+xml[\s\S]*?alt="Foreign Arbitral Award"[\s\S]*?>)',
        "url": "https://images.unsplash.com/photo-1521295121783-8a321d551ad2?auto=format&fit=crop&w=600&q=80"
    },
    {
        "pattern": r'(<img\s*src="data:image/svg\+xml[\s\S]*?alt="Arbitral Award Pakistan"[\s\S]*?>)',
        "url": "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=600&q=80"
    },
    {
        "pattern": r'(<img\s*src="data:image/svg\+xml[\s\S]*?alt="Robotic Weapons"[\s\S]*?>)',
        "url": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=600&q=80"
    },
    {
        "pattern": r'(<img\s*src="data:image/svg\+xml[\s\S]*?alt="Commercial Frauds"[\s\S]*?>)',
        "url": "https://images.unsplash.com/photo-1494412519320-aa6da3e05a9d?auto=format&fit=crop&w=600&q=80"
    },
    {
        "pattern": r'(<img\s*src="data:image/svg\+xml[\s\S]*?alt="Minority Shareholders UK USA"[\s\S]*?>)',
        "url": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=600&q=80"
    }
]

with open(pub_html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

count = 0
for p in pubs:
    # Use re.IGNORECASE just in case
    alt_match = re.search(r'alt="(.*?)"', p['pattern'])
    alt_text = alt_match.group(1) if alt_match else "Publication Image"
    
    replacement = f'<img src="{p["url"]}" alt="{alt_text}" class="blog-card-img" />'
    new_content, num_subs = re.subn(p['pattern'], replacement, html_content)
    if num_subs > 0:
        html_content = new_content
        count += 1

with open(pub_html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Images assigned successfully! Fixed {count} tags.")
