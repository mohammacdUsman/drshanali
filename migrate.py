import os
import re

base_dir = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website"
pages_dir = os.path.join(base_dir, "pages")
edu_path = os.path.join(pages_dir, "education.html")
conf_path = os.path.join(pages_dir, "conferences.html")

with open(edu_path, 'r', encoding='utf-8') as f:
    edu_content = f.read()

conf_pattern = re.compile(
    r'(<!-- CONFERENCES & WINTER SCHOOLS -->.*?)</section>\s*(<script>.*?</script>)?\s*(<section\s+style="background:linear-gradient)',
    re.DOTALL
)

match = conf_pattern.search(edu_content)
if not match:
    print("Could not find conferences section.")
    exit(1)

conf_section = match.group(1) + "</section>\n\n    " + (match.group(2) if match.group(2) else "") + "\n\n    "
cta_section_start = match.group(3)

# Build new education.html content
new_edu_content = edu_content[:match.start()] + cta_section_start + edu_content[match.end(3):]

# Read edu again to construct conferences.html
conf_page_content = edu_content[:match.start()] + conf_section + cta_section_start + edu_content[match.end(3):]

# Update Title and active links in conf_page_content
conf_page_content = conf_page_content.replace(
    "<title>Education | Shan Ali — FinTech & Blockchain Legal Counsel</title>",
    "<title>Conferences & Winter Schools | Shan Ali — FinTech & Blockchain Legal Counsel</title>"
)

hero_old = """    <section class="page-hero">
        <div class="page-hero-content">
            <h1>Education &amp; Achievements</h1>
            <p>Academic Excellence | Honours &amp; Awards | Certifications &amp; Skills</p>
            <div class="breadcrumb">
                <a href="../index.html">Home</a>
                <span>›</span>
                <span>Education &amp; Achievements</span>
            </div>
        </div>
    </section>"""

hero_new = """    <section class="page-hero">
        <div class="page-hero-content">
            <h1>Conferences &amp; Winter Schools</h1>
            <p>International Programmes | Keynote Speeches | Workshops</p>
            <div class="breadcrumb">
                <a href="../index.html">Home</a>
                <span>›</span>
                <span>Conferences &amp; Winter Schools</span>
            </div>
        </div>
    </section>"""

conf_page_content = conf_page_content.replace(hero_old, hero_new)

edu_awards_pattern = re.compile(r'(</section>\s*)<!-- EDUCATION & AWARDS -->.*?(<!-- CONFERENCES & WINTER SCHOOLS -->)', re.DOTALL)
conf_page_content = edu_awards_pattern.sub(r'\1\2', conf_page_content)


def update_nav(html_content, active_page=None):
    if active_page == 'conferences':
        html_content = html_content.replace('href="education.html" class="nav-link active"', 'href="education.html" class="nav-link"')
        html_content = html_content.replace(
            '<li><a href="education.html" class="nav-link">Education</a></li>',
            '<li><a href="education.html" class="nav-link">Education</a></li>\n                        <li><a href="conferences.html" class="nav-link active">Conferences</a></li>'
        )
    else:
        html_content = html_content.replace(
            '<li><a href="education.html" class="nav-link active">Education</a></li>',
            '<li><a href="education.html" class="nav-link active">Education</a></li>\n                        <li><a href="conferences.html" class="nav-link">Conferences</a></li>'
        )
        html_content = html_content.replace(
            '<li><a href="education.html" class="nav-link">Education</a></li>',
            '<li><a href="education.html" class="nav-link">Education</a></li>\n                        <li><a href="conferences.html" class="nav-link">Conferences</a></li>'
        )
        html_content = html_content.replace(
            '<li><a href="pages/education.html" class="nav-link">Education</a></li>',
            '<li><a href="pages/education.html" class="nav-link">Education</a></li>\n                        <li><a href="pages/conferences.html" class="nav-link">Conferences</a></li>'
        )

    # mobile menu
    html_content = html_content.replace(
        '<a href="education.html" class="mobile-menu-link">Education</a>',
        '<a href="education.html" class="mobile-menu-link">Education</a>\n        <a href="conferences.html" class="mobile-menu-link">Conferences</a>'
    )
    html_content = html_content.replace(
        '<a href="pages/education.html" class="mobile-menu-link">Education</a>',
        '<a href="pages/education.html" class="mobile-menu-link">Education</a>\n        <a href="pages/conferences.html" class="mobile-menu-link">Conferences</a>'
    )
    
    # fix footer links
    html_content = html_content.replace(
        '<a href="education.html" class="footer-link">Education &amp; Achievements</a>',
        '<a href="education.html" class="footer-link">Education &amp; Achievements</a>\n                        <a href="conferences.html" class="footer-link">Conferences</a>'
    )
    html_content = html_content.replace(
        '<a href="pages/education.html" class="footer-link">Education &amp; Achievements</a>',
        '<a href="pages/education.html" class="footer-link">Education &amp; Achievements</a>\n                        <a href="pages/conferences.html" class="footer-link">Conferences</a>'
    )

    return html_content

conf_page_content = update_nav(conf_page_content, 'conferences')
new_edu_content = update_nav(new_edu_content, 'education')

with open(edu_path, 'w', encoding='utf-8') as f:
    f.write(new_edu_content)

print(f"Written new education.html, lengths: old={len(edu_content)}, new={len(new_edu_content)}")

with open(conf_path, 'w', encoding='utf-8') as f:
    f.write(conf_page_content)

print(f"Written conferences.html, length: {len(conf_page_content)}")

count = 0
for filename in os.listdir(pages_dir):
    if filename.endswith(".html") and filename not in ["education.html", "conferences.html"]:
        p = os.path.join(pages_dir, filename)
        with open(p, 'r', encoding='utf-8') as f:
            c = f.read()
        c = update_nav(c)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)
        count += 1

index_path = os.path.join(base_dir, "index.html")
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        idx_c = f.read()
    idx_c = update_nav(idx_c)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(idx_c)
    count += 1

print(f"Updated {count} other HTML files via update_nav")
