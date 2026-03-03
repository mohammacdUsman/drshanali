import re

base_file = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website\pages\education.html"
target_file = r"c:\Users\S C\.gemini\antigravity\scratch\waleed-law-website\pages\courses.html"

with open(base_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Split out the top portion (Head, Header, Mobile menu)
header_match = re.search(r'(.*?<!-- PAGE HERO -->)', html, re.DOTALL)
top_section = header_match.group(1)

# Modify title and active nav state
top_section = re.sub(r'<title>.*?</title>', '<title>Online Courses | Shan Ali — FinTech & Blockchain Legal Counsel</title>', top_section)
top_section = top_section.replace('class="nav-link active">Education</a>', 'class="nav-link">Education</a>')

# Our custom Courses HTML Body
courses_body = """
    <style>
        .courses-intro { padding: 80px 0; background-color: var(--white); text-align: center; }
        .courses-intro p { max-width: 800px; margin: 0 auto; color: var(--text-body); font-size: 1.05rem; line-height: 1.8; }
        
        .filter-section { background-color: var(--bg-light); padding: 40px 0; }
        .filter-btn-group { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 16px; align-items: center; }
        .filter-btn { padding: 12px 24px; border: 1px solid var(--border); background: var(--white); border-radius: var(--radius-sm); cursor: pointer; transition: all var(--transition); font-weight: 600; color: var(--text-body); display: flex; align-items: center; gap: 8px; }
        .filter-btn:hover { background: var(--bg-light); transform: translateY(-2px); box-shadow: var(--shadow-sm); }
        .filter-btn.active { background: var(--primary); color: #fff; border-color: var(--primary); }
        .filter-count { display: inline-block; background: rgba(0,0,0,0.06); padding: 2px 8px; border-radius: 20px; font-size: 0.8rem; font-weight: 700; color: var(--text-body); }
        .filter-btn.active .filter-count { background: rgba(255,255,255,0.2); color: #fff; }

        .courses-grid-section { padding: 80px 0; background: var(--white); }
        .courses-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 32px; }
        
        .course-card { background: var(--white); border: 1px solid var(--border); border-radius: var(--radius-md); overflow: hidden; transition: all var(--transition); display: flex; flex-direction: column; position: relative; }
        .course-card:hover { transform: translateY(-5px); box-shadow: var(--shadow-lg); border-color: var(--accent); }
        
        .course-badge { position: absolute; top: 0; right: 0; background: #2f855a; color: white; padding: 6px 16px; font-size: 0.8rem; font-weight: 700; border-bottom-left-radius: 8px; z-index: 2; letter-spacing: 1px; text-transform: uppercase; }
        
        .course-img-wrap { height: 210px; overflow: hidden; position: relative; border-bottom: 2px solid var(--accent); }
        .course-img-wrap img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s cubic-bezier(0.165, 0.84, 0.44, 1); }
        .course-card:hover .course-img-wrap img { transform: scale(1.08); }
        
        .course-content { padding: 30px 24px; flex-grow: 1; display: flex; flex-direction: column; }
        .course-provider-row { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .course-provider { font-size: 0.75rem; border: 1.5px solid var(--primary); color: var(--primary); padding: 4px 14px; border-radius: 50px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; }
        
        .course-title { font-size: 1.35rem; font-weight: 800; color: var(--primary-dark); margin-bottom: 8px; line-height: 1.35; }
        .course-auth { font-size: 0.85rem; color: var(--accent); margin-bottom: 16px; font-weight: 700; }
        .course-desc { font-size: 0.95rem; color: var(--text-body); line-height: 1.6; margin-bottom: 24px; }
        
        .course-topics { margin-bottom: 24px; flex-grow: 1; }
        .course-topics h4 { font-size: 0.95rem; color: var(--primary); margin-bottom: 12px; display: flex; align-items: center; gap: 8px; font-weight: 700; }
        .course-topics ul { list-style: none; padding: 0; }
        .course-topics li { font-size: 0.9rem; color: var(--text-body); margin-bottom: 8px; display: flex; align-items: flex-start; gap: 8px; }
        .course-topics li::before { content: "•"; color: var(--accent); font-weight: bold; font-size: 1.2rem; line-height: 1; margin-top: -2px; }
        .course-topics .extra-topics { color: var(--text-muted); font-style: italic; font-size: 0.8rem; margin-top: 8px; font-weight: 500;}
        
        .course-btn { text-align: center; display: flex; justify-content: center; align-items: center; gap: 8px; width: 100%; padding: 14px; background: var(--primary); color: #fff; font-weight: 700; border-radius: var(--radius-sm); transition: all var(--transition); text-decoration: none; border: 2px solid var(--primary); }
        .course-btn:hover { background: var(--accent); border-color: var(--accent); transform: translateY(-2px); }

        .philosophy-section { background: var(--bg-light); padding: 80px 0; }
        .philosophy-quote { font-size: 1.25rem; font-style: italic; color: var(--text-dark); text-align: center; max-width: 800px; margin: 0 auto 50px; border-left: 4px solid var(--accent); padding-left: 24px; line-height: 1.8; font-family: Georgia, serif; }
        .philosophy-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
        .phil-card { background: var(--white); padding: 40px 30px; border-radius: var(--radius-md); text-align: center; border: 1px solid var(--border); transition: all var(--transition); }
        .phil-card:hover { border-color: var(--primary); box-shadow: var(--shadow-md); transform: translateY(-4px); }
        .phil-icon { font-size: 2.5rem; margin-bottom: 20px; display: inline-block; color: var(--accent); }
        .phil-card h3 { font-size: 1.25rem; font-weight: 700; color: var(--primary); margin-bottom: 14px; }
        .phil-card p { font-size: 0.95rem; color: var(--text-body); line-height: 1.7; }

        .focus-section { padding: 80px 0; background: var(--white); }
        .focus-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
        .focus-card { background: var(--bg-light); padding: 32px 28px; border-left: 5px solid var(--primary); border-radius: var(--radius-sm); transition: all var(--transition); }
        .focus-card:hover { border-left-color: var(--accent); background: var(--white); box-shadow: var(--shadow-md); transform: translateX(4px); }
        .focus-card h3 { font-size: 1.2rem; font-weight: 800; color: var(--primary); margin-bottom: 12px; }
        .focus-card p { font-size: 0.95rem; color: var(--text-body); line-height: 1.7; }

        @media (max-width: 768px) {
            .courses-grid { grid-template-columns: 1fr; }
            .philosophy-quote { font-size: 1.1rem; padding-left: 16px; }
        }
    </style>

    <section class="page-hero">
        <div class="page-hero-content">
            <h1>Online Courses</h1>
            <p>Advancing legal expertise through continuous learning and professional development</p>
            <div class="breadcrumb">
                <a href="../index.html">Home</a><span>›</span><span>Online Courses</span>
            </div>
        </div>
    </section>

    <section class="courses-intro reveal">
        <div class="container">
            <h2 class="section-title">Continuous Learning</h2>
            <div class="divider"></div>
            <p style="margin-top:20px;">
                My commitment to professional development extends beyond formal education. I regularly pursue specialized
                online courses to stay current with emerging legal trends, technologies, and interdisciplinary approaches.
                These courses complement my formal education and inform my research and practice.
            </p>
        </div>
    </section>

    <!-- Filter Section -->
    <section class="filter-section reveal">
        <div class="container">
            <h3 style="font-size:1.1rem; color:var(--primary); font-weight:700; display:flex; gap:8px; align-items:center;">
                🔍 Filter by Category
            </h3>
            <div class="filter-btn-group" id="filterContainer">
                <button class="filter-btn active" data-filter="all">
                    All Courses <span class="filter-count">5</span>
                </button>
                <button class="filter-btn" data-filter="tech-law">
                    Technology & Law <span class="filter-count">3</span>
                </button>
                <button class="filter-btn" data-filter="business-law">
                    Business Law <span class="filter-count">1</span>
                </button>
                <button class="filter-btn" data-filter="privacy">
                    Privacy & Data Protection <span class="filter-count">1</span>
                </button>
            </div>
        </div>
    </section>

    <!-- Courses Grid -->
    <section class="courses-grid-section">
        <div class="container">
            <div class="courses-grid">
                
                <!-- AI & Law -->
                <div class="course-card reveal" data-category="tech-law">
                    <div class="course-badge">COMPLETED</div>
                    <div class="course-img-wrap">
                        <img src="../images/AI & Law.png" alt="AI & Law">
                    </div>
                    <div class="course-content">
                        <div class="course-provider-row">
                            <span class="course-provider">Coursera</span>
                            <span style="color:var(--text-muted);">↗</span>
                        </div>
                        <h3 class="course-title">AI & Law</h3>
                        <p class="course-auth">Lund University</p>
                        <p class="course-desc">Examines the relationship between artificial intelligence and legal systems, focusing on the challenges of AI regulation, liability issues, and ethical considerations in automated decision-making.</p>
                        
                        <div class="course-topics">
                            <h4>📚 Key Topics:</h4>
                            <ul>
                                <li>AI Regulatory Frameworks</li>
                                <li>Liability Issues in AI Systems</li>
                                <li>Predictive Justice and Legal Analytics</li>
                                <li>Regulation and Legal Compliance</li>
                            </ul>
                            <div class="extra-topics">+2 more topics</div>
                        </div>

                        <a href="https://coursera.org/verify/4NMQJXPUD9HS" target="_blank" class="course-btn">
                            View Certificate 🔗
                        </a>
                    </div>
                </div>

                <!-- AI and Legal Issues -->
                <div class="course-card reveal reveal-delay-1" data-category="tech-law">
                    <div class="course-badge">COMPLETED</div>
                    <div class="course-img-wrap">
                        <img src="../images/Artificial Intelligence and Legal Issues .png" alt="Artificial Intelligence and Legal Issues">
                    </div>
                    <div class="course-content">
                        <div class="course-provider-row">
                            <span class="course-provider">Coursera</span>
                            <span style="color:var(--text-muted);">↗</span>
                        </div>
                        <h3 class="course-title">Artificial Intelligence and Legal Issues</h3>
                        <p class="course-auth">Politecnico di Milano</p>
                        <p class="course-desc">This comprehensive course examines the legal challenges presented by artificial intelligence technologies, focusing on regulatory approaches, governance frameworks, and comparative legal analysis.</p>
                        
                        <div class="course-topics">
                            <h4>📚 Key Topics:</h4>
                            <ul>
                                <li>AI Governance Models</li>
                                <li>Intellectual Property in AI Content</li>
                                <li>Algorithmic Transparency</li>
                                <li>International Approaches to AI Regulation</li>
                            </ul>
                        </div>

                        <a href="https://coursera.org/verify/376VDQ6U6AYU" target="_blank" class="course-btn">
                            View Certificate 🔗
                        </a>
                    </div>
                </div>

                <!-- Privacy Law -->
                <div class="course-card reveal reveal-delay-2" data-category="privacy">
                    <div class="course-badge">COMPLETED</div>
                    <div class="course-img-wrap">
                        <img src="../images/Privacy Law and Data Protection.png" alt="Privacy Law">
                    </div>
                    <div class="course-content">
                        <div class="course-provider-row">
                            <span class="course-provider">Coursera</span>
                            <span style="color:var(--text-muted);">↗</span>
                        </div>
                        <h3 class="course-title">Privacy Law and Data Protection</h3>
                        <p class="course-auth">University of Pennsylvania</p>
                        <p class="course-desc">This advanced course delves into practical legal issues for businesses operating globally, covering compliance, competition law, cross-border regulation, and data transfer strategies.</p>
                        
                        <div class="course-topics">
                            <h4>📚 Key Topics:</h4>
                            <ul>
                                <li>General Data Protection Regulation (GDPR)</li>
                                <li>Privacy-by-Design Principles</li>
                                <li>Cross-Border Data Transfer</li>
                                <li>Data Breach Notification Requirements</li>
                            </ul>
                        </div>

                        <a href="https://coursera.org/verify/R78GMUZD8S6Z" target="_blank" class="course-btn">
                            View Certificate 🔗
                        </a>
                    </div>
                </div>

                <!-- Cloud Computing -->
                <div class="course-card reveal" data-category="tech-law">
                    <div class="course-badge">COMPLETED</div>
                    <div class="course-img-wrap">
                        <img src="../images/Cloud Computing Law .png" alt="Cloud Computing Law">
                    </div>
                    <div class="course-content">
                        <div class="course-provider-row">
                            <span class="course-provider">Coursera</span>
                            <span style="color:var(--text-muted);">↗</span>
                        </div>
                        <h3 class="course-title">Cloud Computing Law</h3>
                        <p class="course-auth">University of London</p>
                        <p class="course-desc">Covers the legal implications of cloud technologies, addressing contract management, data sovereignty, service level agreements (SLAs), and jurisdictional issues.</p>
                        
                        <div class="course-topics">
                            <h4>📚 Key Topics:</h4>
                            <ul>
                                <li>Cloud Service Agreements</li>
                                <li>Jurisdiction and Data Localization</li>
                                <li>Liability and Indemnity Clauses</li>
                                <li>Regulatory Compliance in Cloud</li>
                            </ul>
                        </div>

                        <a href="https://www.coursera.org/account/accomplishments/verify/TTEWJN22WQ6A" target="_blank" class="course-btn">
                            View Certificate 🔗
                        </a>
                    </div>
                </div>

                <!-- EU Business Law -->
                <div class="course-card reveal reveal-delay-1" data-category="business-law">
                    <div class="course-badge">COMPLETED</div>
                    <div class="course-img-wrap">
                        <img src="../images/European Business Law Understanding the Fundamentals.png" alt="EU Business Law">
                    </div>
                    <div class="course-content">
                        <div class="course-provider-row">
                            <span class="course-provider">Coursera</span>
                            <span style="color:var(--text-muted);">↗</span>
                        </div>
                        <h3 class="course-title">European Business Law: Fundamentals</h3>
                        <p class="course-auth">Lund University</p>
                        <p class="course-desc">Foundational understanding of the core principles of European business law, including internal market rules, EU institutions, and legal reasoning within the EU context.</p>
                        
                        <div class="course-topics">
                            <h4>📚 Key Topics:</h4>
                            <ul>
                                <li>EU Legal System &amp; Institutions</li>
                                <li>Free Movement of Goods &amp; Services</li>
                                <li>EU Lawmaking and Legal Reasoning</li>
                                <li>Preliminary Ruling Procedure</li>
                            </ul>
                        </div>

                        <a href="https://coursera.org/verify/MUG5AS9GJY2X" target="_blank" class="course-btn">
                            View Certificate 🔗
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Learning Philosophy -->
    <section class="philosophy-section reveal">
        <div class="container">
            <h2 class="section-title text-center">Learning Philosophy</h2>
            <div class="divider" style="margin: 0 auto 30px;"></div>
            
            <div class="philosophy-quote">
                "In the rapidly evolving intersection of law and technology, continuous learning is not optional but
                essential. My approach combines structured educational experiences with practical application to develop a
                comprehensive understanding of emerging legal challenges."
            </div>

            <div class="philosophy-grid">
                <div class="phil-card">
                    <div class="phil-icon">🧩</div>
                    <h3>Interdisciplinary Integration</h3>
                    <p>Combining legal knowledge with technical understanding to address complex challenges at the intersection of disciplines.</p>
                </div>
                <div class="phil-card">
                    <div class="phil-icon">🔧</div>
                    <h3>Practical Application</h3>
                    <p>Translating theoretical frameworks into practical legal solutions for real-world technology and business challenges.</p>
                </div>
                <div class="phil-card">
                    <div class="phil-icon">📈</div>
                    <h3>Continuous Development</h3>
                    <p>Maintaining current knowledge through ongoing education in emerging legal trends, technologies, and regulatory approaches.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Current Learning Focus -->
    <section class="focus-section reveal">
        <div class="container">
            <h2 class="section-title text-center">Current Learning Focus</h2>
            <div class="divider" style="margin: 0 auto 50px;"></div>

            <div class="focus-grid">
                <div class="focus-card">
                    <h3>Blockchain Governance Models</h3>
                    <p>Exploring decentralized governance frameworks and their legal implications for organizational structures and decision-making processes.</p>
                </div>
                <div class="focus-card">
                    <h3>Digital Asset Regulation</h3>
                    <p>Examining evolving regulatory approaches to tokenized assets, NFTs, and digital currencies across multiple jurisdictions.</p>
                </div>
                <div class="focus-card">
                    <h3>AI Ethics and Governance</h3>
                    <p>Investigating ethical frameworks and governance models for artificial intelligence systems in legal and business contexts.</p>
                </div>
            </div>
            
            <div class="text-center" style="margin-top:60px;">
                <p style="color:var(--text-body);font-size:1.05rem;margin-bottom:24px;">Interested in my professional qualifications and research? Explore my academic background and published work.</p>
                <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
                    <a href="education.html" class="btn btn-outline">Explore Education</a>
                    <a href="publications.html" class="btn btn-primary">Read Publications</a>
                </div>
            </div>
        </div>
    </section>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const btns = document.querySelectorAll('.filter-btn');
            const cards = document.querySelectorAll('.course-card');

            btns.forEach(btn => {
                btn.addEventListener('click', () => {
                    // Remove active from all
                    btns.forEach(b => b.classList.remove('active'));
                    btn.classList.add('active');

                    const filter = btn.getAttribute('data-filter');

                    cards.forEach(card => {
                        const category = card.getAttribute('data-category');
                        if (filter === 'all' || category === filter) {
                            card.style.display = 'flex';
                            setTimeout(() => { card.style.opacity = '1'; card.style.transform = 'translateY(0)'; }, 50);
                        } else {
                            card.style.opacity = '0';
                            card.style.transform = 'translateY(20px)';
                            setTimeout(() => { card.style.display = 'none'; }, 300);
                        }
                    });
                });
            });
        });
    </script>
"""

# Extract Footer
footer_match = re.search(r'(<!-- FOOTER -->.*</html>)', html, re.DOTALL)
footer_section = footer_match.group(1)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(top_section + courses_body + footer_section)

print("Created courses.html successfully")
