import os

schema_json = """  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "LegalService",
        "name": "Shan Ali — FinTech & Blockchain Legal Counsel",
        "description": "Specialized legal services in FinTech Law, Blockchain Regulation, DeFi Compliance, and Corporate Law.",
        "url": "https://waleedcojuris.com/",
        "address": {
          "@type": "PostalAddress",
          "addressLocality": "Islamabad",
          "addressCountry": "PK"
        },
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": 33.6844,
          "longitude": 73.0479
        },
        "openingHoursSpecification": {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday"
          ],
          "opens": "09:00",
          "closes": "18:00"
        },
        "sameAs": [
          "https://www.linkedin.com/in/shan-ali-blockchain/"
        ]
      },
      {
        "@type": "Person",
        "name": "Shan Ali",
        "jobTitle": "FinTech & Blockchain Legal Counsel",
        "knowsAbout": ["Blockchain Law", "FinTech Regulation", "DeFi Compliance", "Corporate Law", "International Law"],
        "description": "PhD Fellow in Blockchain Law and licensed attorney at Islamabad High Court.",
        "sameAs": [
          "https://www.linkedin.com/in/shan-ali-blockchain/"
        ]
      }
    ]
  }
  </script>
"""

def add_schema(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if 'application/ld+json' not in content:
                    new_content = content.replace('</head>', schema_json + '</head>')
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Added schema to {file}")

if __name__ == "__main__":
    add_schema(".")
