import os
import shutil

src_dir = r"C:\Users\S C\.gemini\antigravity\brain\ca07882a-2161-45c3-b361-20eeebac4f50"
dest_dir = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website\images"
html_file = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website\pages\courses.html"

# Grab the 5 jpg files
files = [f for f in os.listdir(src_dir) if f.startswith('media') and f.endswith('.jpg')]
files.sort()

if len(files) >= 5:
    mapping = [
        ("course_ai_law.jpg", "../images/AI & Law.png"),
        ("course_ai_legal_issues.jpg", "../images/Artificial Intelligence and Legal Issues .png"),
        ("course_cloud_computing.jpg", "../images/Cloud Computing Law .png"),
        ("course_privacy_law.jpg", "../images/Privacy Law and Data Protection.png"),
        ("course_eu_business_law.jpg", "../images/European Business Law Understanding the Fundamentals.png")
    ]
    
    # We will map them based on the analyzed logic:
    # files[0] -> AI & Law
    # files[1] -> AI & Legal Issues
    # files[2] -> Cloud Computing
    # files[3] -> Privacy Law (EU context)
    # files[4] -> EU Business Law
    
    file_mapping = {
        files[0]: mapping[0], # AI & Law
        files[1]: mapping[1], # AI & Legal Issues
        files[2]: mapping[2], # Cloud Computing
        files[3]: mapping[3], # Privacy Law
        files[4]: mapping[4], # EU Business Law
    }
    
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    for old_file, (new_name, target_html_str) in file_mapping.items():
        # Copy file
        shutil.copy(os.path.join(src_dir, old_file), os.path.join(dest_dir, new_name))
        
        # In HTML, we have alt attributes and src strings.
        # Actually it's easier to just replace the whole target string.
        html_content = html_content.replace(target_html_str, f"../images/{new_name}")

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print("Files copied and HTML updated successfully.")
else:
    print(f"Only found {len(files)} jpgs in {src_dir}")
