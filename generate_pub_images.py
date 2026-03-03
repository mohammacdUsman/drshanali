import os
import re
import urllib.request
import urllib.parse
import time

base_dir = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website"
pub_html_path = os.path.join(base_dir, "pages", "publications.html")
images_dir = os.path.join(base_dir, "images", "publications")

if not os.path.exists(images_dir):
    os.makedirs(images_dir)

pubs = [
    {
        "pattern": r'(<img src="data:image/svg\+xml.*?alt="DAOs in Italy".*?>)',
        "prompt": "Abstract minimalistic rendering of a blockchain network and glowing nodes, dark blue and gold aesthetic, professional publication cover",
        "filename": "pub_dao.jpg"
    },
    {
        "pattern": r'(<img src="data:image/svg\+xml.*?alt="Blockchain and Cognitive Liberty".*?>)',
        "prompt": "Abstract glowing human brain connected to digital blockchain nodes, cyan and purple, professional publication cover",
        "filename": "pub_cognitive.jpg"
    },
    {
        "pattern": r'(<img src="data:image/svg\+xml.*?alt="AI in the Metaverse".*?>)',
        "prompt": "Abstract professional representation of AI code in a virtual reality metaverse, elegant tech aesthetic",
        "filename": "pub_metaverse.jpg"
    },
    {
        "pattern": r'(<img src="data:image/svg\+xml.*?alt="Minority Shareholders Pakistan".*?>)',
        "prompt": "Abstract modern skyscraper corporate building looking up, professional stylized corporate law publication cover",
        "filename": "pub_derivative_1.jpg"
    },
    {
        "pattern": r'(<img src="data:image/svg\+xml.*?alt="Derivative Action Minority Shareholders".*?>)',
        "prompt": "Elegant wooden judge gavel resting on a glowing digital contract, professional corporate law aesthetic",
        "filename": "pub_derivative_2.jpg"
    },
    {
        "pattern": r'(<img src="data:image/svg\+xml.*?alt="Cyber Terrorism".*?>)',
        "prompt": "Abstract digital padlock over a background of falling green matrix code data, cybersecurity concept",
        "filename": "pub_cyber_terror.jpg"
    },
    {
        "pattern": r'(<img src="data:image/svg\+xml.*?alt="Cyber Warfare".*?>)',
        "prompt": "Abstract professional representation of global cyber warfare, digital earth with glowing red attack vectors",
        "filename": "pub_cyber_war.jpg"
    },
    {
        "pattern": r'(<img src="data:image/svg\+xml.*?alt="Web Based Trading".*?>)',
        "prompt": "Abstract high tech financial trading charts and glowing candlesticks, deep blue and gold aesthetic",
        "filename": "pub_web_trading.jpg"
    },
    {
        "pattern": r'(<img src="data:image/svg\+xml.*?alt="Foreign Arbitral Award".*?>)',
        "prompt": "Elegant map of the world superimposed with a silver balance scale of justice, international law concept",
        "filename": "pub_foreign_arbitral.jpg"
    },
    {
        "pattern": r'(<img src="data:image/svg\+xml.*?alt="Arbitral Award Pakistan".*?>)',
        "prompt": "Abstract representation of legal documents and a judge gavel, professional international law concept",
        "filename": "pub_pk_arbitral.jpg"
    },
    {
        "pattern": r'(<img src="data:image/svg\+xml.*?alt="Robotic Weapons".*?>)',
        "prompt": "Abstract dark menacing robotic arm or AI eye, tech law concept, moody professional aesthetic",
        "filename": "pub_robotic_weapons.jpg"
    },
    {
        "pattern": r'(<img src="data:image/svg\+xml.*?alt="Commercial Frauds".*?>)',
        "prompt": "Abstract representation of massive cargo shipping containers with a digital glowing secure lock, professional lighting",
        "filename": "pub_commercial_frauds.jpg"
    },
    {
        "pattern": r'(<img src="data:image/svg\+xml.*?alt="Minority Shareholders UK USA".*?>)',
        "prompt": "Abstract representation of a small glowing golden chess pawn standing among silver pawns, corporate power dynamic concept",
        "filename": "pub_minority_uk_usa.jpg"
    }
]

with open(pub_html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

for p in pubs:
    img_path = os.path.join(images_dir, p['filename'])
    if not os.path.exists(img_path):
        encoded_prompt = urllib.parse.quote(p['prompt'])
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=600&height=400&nologo=true"
        print(f"Downloading {p['filename']}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response, open(img_path, 'wb') as out_file:
                out_file.write(response.read())
            time.sleep(1) # Be nice to the API
        except Exception as e:
            print(f"Error downloading {p['filename']}: {e}")
            continue
            
    # Replace in HTML
    replacement = f'<img src="../images/publications/{p["filename"]}" alt="Publication Cover" class="blog-card-img" />'
    html_content = re.sub(p['pattern'], replacement, html_content)

with open(pub_html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("All publication images generated and HTML updated!")
