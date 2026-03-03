import re
import sys

# Paths
filepath = "c:\\Users\\S C\\.gemini\\antigravity\\scratch\\waleed-law-website\\pages\\education.html"

# Read file
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

# Define the new content
new_css = """
  <style>
    /* Layout */
    .edu-max-w-4xl { max-width: 56rem; margin: 0 auto; padding: 0 1rem; }
    .edu-max-w-6xl { max-width: 72rem; margin: 0 auto; padding: 0 1rem; }

    /* Hero Banner */
    .ed-hero {
      position: relative;
      height: 60vh;
      background: linear-gradient(135deg, var(--primary-dark), var(--primary));
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }

    .ed-hero-overlay {
      position: absolute;
      inset: 0;
      background-color: rgba(0, 0, 0, 0.4);
      z-index: 10;
    }

    .ed-hero-image {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .ed-hero-content {
      position: relative;
      z-index: 20;
      text-align: center;
      color: var(--white);
      transform: translateY(0);
      opacity: 1;
      transition: transform 1s, opacity 1s;
    }

    .ed-hero-content.ed-hidden {
      transform: translateY(2.5rem);
      opacity: 0;
    }

    .ed-hero-title {
      font-size: clamp(2.5rem, 5vw, 4.5rem);
      font-weight: 800;
      letter-spacing: 0.1em;
      margin-bottom: 1rem;
    }

    .ed-hero-subtitle {
      font-size: clamp(1.1rem, 2vw, 1.5rem);
      font-weight: 300;
      letter-spacing: 0.05em;
    }

    .ed-bounce {
      animation: ed-bounce 2s infinite;
      margin-top: 2rem;
    }

    @keyframes ed-bounce {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-10px); }
    }

    /* Introduction */
    .ed-intro {
      padding: 5rem 1rem;
      background-color: var(--bg-section);
    }

    .ed-intro-content {
      max-width: 56rem;
      margin: 0 auto;
      text-align: center;
    }

    .ed-section-title {
      font-size: 2.25rem;
      font-weight: 700;
      margin-bottom: 2rem;
      color: var(--primary);
    }

    .ed-intro-text {
      font-size: 1.15rem;
      color: var(--text-body);
      line-height: 1.8;
    }

    /* Filter Controls */
    .ed-filter-controls {
      max-width: 72rem;
      margin: 0 auto 2rem;
      padding: 1rem;
      background-color: var(--white);
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border);
    }

    .ed-filter-title {
      font-size: 1.25rem;
      font-weight: 600;
      margin-bottom: 1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--text-dark);
    }

    .ed-filter-options {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
    }

    .ed-filter-btn {
      background-color: var(--white);
      border: 1px solid var(--border);
      border-radius: 50px;
      padding: 0.5rem 1.25rem;
      font-size: 0.875rem;
      font-weight: 600;
      cursor: pointer;
      transition: all var(--transition);
      color: var(--text-body);
    }

    .ed-filter-btn:hover {
      border-color: var(--accent);
      background-color: var(--cream);
      color: var(--primary);
    }

    .ed-filter-btn.active {
      background-color: var(--primary);
      color: var(--white);
      border-color: var(--primary);
    }

    /* Timeline - Horizontal Cards */
    .ed-timeline-section {
      padding: 3rem 1rem 5rem;
      background-color: var(--white);
    }

    .ed-timeline {
      max-width: 72rem;
      margin: 0 auto;
    }

    .ed-timeline-item {
      margin-bottom: 3rem;
      transform: translateY(0);
      opacity: 1;
      transition: all 0.7s;
      perspective: 1000px;
    }

    .ed-timeline-item.ed-hidden {
      display: none;
    }

    /* Enhanced Card Animations */
    @keyframes ed-cardEntrance {
      from { opacity: 0; transform: translateY(25px) rotateX(5deg); }
      to { opacity: 1; transform: translateY(0) rotateX(0); }
    }

    .ed-card-animate {
      animation: ed-cardEntrance 0.8s cubic-bezier(0.215, 0.61, 0.355, 1) forwards;
      opacity: 0;
    }

    /* Horizontal Education Cards */
    .ed-education-card {
      display: flex;
      align-items: stretch;
      background-color: var(--white);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border);
      overflow: hidden;
      gap: 2rem;
      transition: all 0.5s cubic-bezier(0.215, 0.61, 0.355, 1);
    }

    .ed-education-card:hover {
      transform: translateY(-5px);
      box-shadow: var(--shadow-lg);
      border-color: transparent;
    }

    .ed-card-image-container {
      flex-shrink: 0;
      width: 320px;
      position: relative;
      overflow: hidden;
    }

    .ed-card-image {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: all 0.5s;
    }

    .ed-education-card:hover .ed-card-image {
      transform: scale(1.05);
    }

    .ed-card-image-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(to right, transparent, rgba(0,0,0,0.1));
      transition: all 0.5s;
    }

    .ed-card-period {
      position: absolute;
      top: 1rem;
      left: 1rem;
      background-color: var(--primary);
      color: var(--white);
      padding: 0.5rem 1rem;
      border-radius: 50px;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.8rem;
      font-weight: 700;
      z-index: 10;
      box-shadow: var(--shadow-sm);
    }

    .ed-card-content {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 1.2rem;
      padding: 2.5rem 2.5rem 2.5rem 0;
    }

    .ed-card-header {
      border-bottom: 2px solid var(--bg-light);
      padding-bottom: 1rem;
      transition: all 0.3s;
    }

    .ed-education-card:hover .ed-card-header {
      border-bottom-color: var(--accent);
    }

    .ed-card-title {
      font-size: 1.6rem;
      font-weight: 700;
      margin-bottom: 0.4rem;
      color: var(--primary);
    }

    .ed-card-subtitle {
      font-size: 1.15rem;
      color: var(--text-dark);
      margin-bottom: 0.5rem;
      font-weight: 500;
    }

    .ed-card-location {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--text-muted);
      font-size: 0.85rem;
    }

    .ed-card-details {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1.5rem;
    }

    .ed-card-detail-section h5 {
      font-weight: 700;
      margin-bottom: 0.8rem;
      color: var(--text-dark);
      font-size: 0.95rem;
    }

    .ed-card-detail {
      font-size: 0.9rem;
      color: var(--text-body);
      margin-bottom: 0.5rem;
      line-height: 1.6;
    }

    .ed-card-detail strong {
      color: var(--primary);
    }

    .ed-card-highlight {
      background-color: var(--cream);
      padding: 1.2rem;
      border-radius: var(--radius-sm);
      border-left: 4px solid var(--accent);
      margin-top: auto;
    }

    .ed-card-highlight p {
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--primary);
      margin: 0;
    }

    .ed-achievements-title {
      font-weight: 700;
      margin-bottom: 0.8rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--text-dark);
      font-size: 0.95rem;
    }

    .ed-achievements-list {
      font-size: 0.9rem;
      color: var(--text-body);
      list-style: none;
      padding-left: 0;
    }

    .ed-achievements-list li {
      display: flex;
      align-items: flex-start;
      gap: 0.8rem;
      margin-bottom: 0.5rem;
      line-height: 1.5;
    }

    .ed-bullet {
      width: 6px;
      height: 6px;
      background-color: var(--accent);
      border-radius: 50%;
      margin-top: 0.4rem;
      flex-shrink: 0;
    }

    /* Additional Activities - Horizontal Cards */
    .ed-activities-section {
      padding: 5rem 1rem;
      background-color: var(--bg-section);
    }

    .ed-activities-container {
      display: flex;
      flex-direction: column;
      gap: 2rem;
      margin-top: 3rem;
    }

    .ed-activity-card {
      display: flex;
      align-items: flex-start;
      background-color: var(--white);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border);
      padding: 2.5rem;
      gap: 2.5rem;
      transform: translateY(0);
      opacity: 1;
      transition: all 0.5s cubic-bezier(0.215, 0.61, 0.355, 1);
    }

    .ed-activity-card:hover {
      transform: translateY(-5px);
      box-shadow: var(--shadow-lg);
      border-color: transparent;
    }

    .ed-activity-icon-section {
      flex-shrink: 0;
      width: 180px;
      text-align: center;
    }

    .ed-activity-icon-container {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--primary-dark), var(--primary));
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 1.2rem;
      box-shadow: var(--shadow-sm);
      transition: all 0.3s;
    }

    .ed-activity-card:hover .ed-activity-icon-container {
      transform: scale(1.1) rotate(5deg);
      background: linear-gradient(135deg, var(--primary), var(--accent));
    }

    .ed-activity-title {
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--primary);
    }

    .ed-activity-content {
      flex: 1;
    }

    .ed-activity-items {
      display: grid;
      grid-template-columns: 1fr;
      gap: 2rem;
    }

    @media (min-width: 768px) {
      .ed-activity-items {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    .ed-activity-item {
      border-left: 3px solid var(--bg-light);
      padding-left: 1.2rem;
      transition: all 0.3s;
    }

    .ed-activity-card:hover .ed-activity-item {
      border-left-color: var(--accent);
    }

    .ed-activity-item-title {
      font-weight: 700;
      margin-bottom: 0.6rem;
      color: var(--text-dark);
      font-size: 1rem;
      line-height: 1.4;
    }

    .ed-activity-item-detail {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 0.4rem;
    }
    
    .ed-activity-item-detail strong {
      color: var(--text-body);
    }

    .ed-activity-item-description {
      font-size: 0.9rem;
      color: var(--text-body);
      line-height: 1.6;
      margin-top: 0.8rem;
    }

    /* Icons */
    .ed-icon {
      display: inline-block;
      width: 1.5rem;
      height: 1.5rem;
      stroke: currentColor;
      stroke-width: 2;
      fill: none;
      stroke-linecap: round;
      stroke-linejoin: round;
    }

    .ed-icon-sm { width: 1.1rem; height: 1.1rem; }
    .ed-icon-lg { width: 2rem; height: 2rem; }
    .ed-icon-xl { width: 2.5rem; height: 2.5rem; stroke: #fff;}

    /* Utilities */
    .ed-text-center { text-align: center; }
    .ed-mb-16 { margin-bottom: 4rem; }
    .ed-flex { display: flex; }
    .ed-items-center { align-items: center; }
    .ed-justify-between { justify-content: space-between; }

    /* Responsive */
    @media (max-width: 992px) {
      .ed-education-card {
        flex-direction: column;
        gap: 0;
      }
      .ed-card-image-container {
        width: 100%;
        height: 250px;
      }
      .ed-card-content {
        padding: 2rem;
      }
    }

    @media (max-width: 768px) {
      .ed-card-details {
        grid-template-columns: 1fr;
        gap: 2rem;
      }
      .ed-activity-card {
        flex-direction: column;
        text-align: center;
        padding: 2rem;
      }
      .ed-activity-icon-section {
        width: 100%;
      }
      .ed-activity-items {
        grid-template-columns: 1fr;
      }
      .ed-activity-item {
        border-left: none;
        border-top: 3px solid var(--bg-light);
        padding-left: 0;
        padding-top: 1.2rem;
      }
      .ed-filter-options {
        justify-content: center;
      }
      .ed-filter-title {
        justify-content: center;
      }
    }
  </style>
"""

new_html = """
  <!-- Hero Banner -->
  <section class="ed-hero" id="education">
    <div class="ed-hero-overlay"></div>
    <img src="https://images.unsplash.com/photo-1541339907198-e08756dedf3f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1200&h=600&q=80" alt="Education Background" class="ed-hero-image">
    <div class="ed-hero-content ed-hidden">
      <h1 class="ed-hero-title">EDUCATION</h1>
      <p class="ed-hero-subtitle">Academic Excellence & Continuous Learning</p>
      <div class="ed-bounce">
        <svg class="ed-icon ed-icon-lg" viewBox="0 0 24 24">
          <polyline points="6 9 12 15 18 9"></polyline>
        </svg>
      </div>
    </div>
  </section>

  <!-- Introduction -->
  <section class="ed-intro">
    <div class="ed-intro-content">
      <h2 class="ed-section-title">Academic Background</h2>
      <p class="ed-intro-text">
        My educational journey reflects a dedication to legal scholarship and a commitment to understanding the
        evolving intersection of law and technology. Through rigorous academic pursuit and continuous learning, I
        have developed expertise in blockchain law, digital governance, and emerging technologies.
      </p>
    </div>
  </section>

  <!-- Filter Controls -->
  <div class="ed-filter-controls">
    <div class="ed-flex ed-items-center ed-justify-between" style="flex-wrap: wrap; gap: 1rem; justify-content: center;">
      <h3 class="ed-filter-title">
        <svg class="ed-icon" viewBox="0 0 24 24">
          <polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"></polygon>
        </svg>
        Filter Education
      </h3>
      <div class="ed-filter-options">
        <button class="ed-filter-btn active" data-filter="all">All</button>
        <button class="ed-filter-btn" data-filter="degree">Degrees</button>
        <button class="ed-filter-btn" data-filter="summer-school">Summer Schools</button>
        <button class="ed-filter-btn" data-filter="conference">Conferences</button>
        <button class="ed-filter-btn" data-filter="workshop">Workshops</button>
      </div>
    </div>
  </div>

  <!-- Education Timeline -->
  <section class="ed-timeline-section">
    <div class="ed-timeline">
      <!-- PhD -->
      <div class="ed-timeline-item" data-category="degree">
        <div class="ed-education-card">
          <div class="ed-card-image-container">
            <img src="https://images.unsplash.com/photo-1592280771190-3e2e4d571952?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&h=600&q=80" alt="University of Padova" class="ed-card-image">
            <div class="ed-card-image-overlay"></div>
            <div class="ed-card-period">
              <svg class="ed-icon ed-icon-sm" viewBox="0 0 24 24">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="16" y1="2" x2="16" y2="6"></line>
                <line x1="8" y1="2" x2="8" y2="6"></line>
                <line x1="3" y1="10" x2="21" y2="10"></line>
              </svg>
              2023 – Present
            </div>
          </div>

          <div class="ed-card-content">
            <div class="ed-card-header">
              <h3 class="ed-card-title">Ph.D. Law Scholar</h3>
              <h4 class="ed-card-subtitle">University of Padova</h4>
              <div class="ed-card-location">
                <svg class="ed-icon ed-icon-sm" viewBox="0 0 24 24">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>
                <span>Via VIII Febbraio, 2, 35122 Padova PD Italy</span>
              </div>
            </div>

            <div class="ed-card-details">
              <div class="ed-card-detail-section">
                <h5>Academic Details</h5>
                <p class="ed-card-detail"><strong>Status:</strong> In Progress</p>
                <p class="ed-card-detail"><strong>Thesis:</strong> Digital rhetoric and legal, economic, and social applications of the blockchain network on the Web 3.0</p>
                <p class="ed-card-detail">Examining the legal implications of blockchain technology, decentralized autonomous organizations, and digital assets within European legal frameworks.</p>
              </div>

              <div class="ed-card-detail-section">
                <h5 class="ed-achievements-title">
                  <svg class="ed-icon ed-icon-sm" viewBox="0 0 24 24">
                    <circle cx="12" cy="8" r="7"></circle>
                    <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline>
                  </svg>
                  Key Achievements
                </h5>
                <ul class="ed-achievements-list">
                  <li><span class="ed-bullet"></span>Published 3 research papers on blockchain law</li>
                  <li><span class="ed-bullet"></span>Presented at 5 international conferences</li>
                  <li><span class="ed-bullet"></span>Recipient of research excellence grant</li>
                </ul>
              </div>
            </div>

            <div class="ed-card-highlight">
              <p>Visiting Research Student at Nottingham Law School, Nottingham Trent University, UK (July 2024 - Present)</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Master's -->
      <div class="ed-timeline-item" data-category="degree">
        <div class="ed-education-card">
          <div class="ed-card-image-container">
            <img src="https://images.unsplash.com/photo-1541339907198-e08756dedf3f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&h=600&q=80" alt="Bahria University Islamabad" class="ed-card-image">
            <div class="ed-card-image-overlay"></div>
            <div class="ed-card-period">
              <svg class="ed-icon ed-icon-sm" viewBox="0 0 24 24">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="16" y1="2" x2="16" y2="6"></line>
                <line x1="8" y1="2" x2="8" y2="6"></line>
                <line x1="3" y1="10" x2="21" y2="10"></line>
              </svg>
              2019 – 2021
            </div>
          </div>

          <div class="ed-card-content">
            <div class="ed-card-header">
              <h3 class="ed-card-title">Master of Law (LLM)</h3>
              <h4 class="ed-card-subtitle">Bahria University Islamabad</h4>
              <div class="ed-card-location">
                <svg class="ed-icon ed-icon-sm" viewBox="0 0 24 24">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>
                <span>Shangrilla Rd, E 8/1, Islamabad, Pakistan</span>
              </div>
            </div>

            <div class="ed-card-details">
              <div class="ed-card-detail-section">
                <h5>Academic Details</h5>
                <p class="ed-card-detail"><strong>Grade:</strong> CGPA = 3.93/4.00 Grade = A (With Distinction)</p>
                <p class="ed-card-detail"><strong>Thesis:</strong> Corporate Governance in Digital Age</p>
                <p class="ed-card-detail">Advanced research in corporate governance, technology law, and international legal frameworks.</p>
              </div>

              <div class="ed-card-detail-section">
                <h5 class="ed-achievements-title">
                  <svg class="ed-icon ed-icon-sm" viewBox="0 0 24 24">
                    <circle cx="12" cy="8" r="7"></circle>
                    <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline>
                  </svg>
                  Key Achievements
                </h5>
                <ul class="ed-achievements-list">
                  <li><span class="ed-bullet"></span>Dean's List for 4 consecutive semesters</li>
                  <li><span class="ed-bullet"></span>Best thesis award in Technology Law</li>
                  <li><span class="ed-bullet"></span>Student representative in academic council</li>
                </ul>
              </div>
            </div>

            <div class="ed-card-highlight">
              <p>LL.M. Gold Medal Qualifier | Graduated with highest distinction.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Bachelor's -->
      <div class="ed-timeline-item" data-category="degree">
        <div class="ed-education-card">
          <div class="ed-card-image-container">
            <img src="https://images.unsplash.com/photo-1523050854058-8df90110c9f1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=800&h=600&q=80" alt="Government College University Faisalabad" class="ed-card-image">
            <div class="ed-card-image-overlay"></div>
            <div class="ed-card-period">
              <svg class="ed-icon ed-icon-sm" viewBox="0 0 24 24">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="16" y1="2" x2="16" y2="6"></line>
                <line x1="8" y1="2" x2="8" y2="6"></line>
                <line x1="3" y1="10" x2="21" y2="10"></line>
              </svg>
              2013 – 2018
            </div>
          </div>

          <div class="ed-card-content">
            <div class="ed-card-header">
              <h3 class="ed-card-title">Bachelor of Law (LLB)</h3>
              <h4 class="ed-card-subtitle">Government College University Faisalabad</h4>
              <div class="ed-card-location">
                <svg class="ed-icon ed-icon-sm" viewBox="0 0 24 24">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>
                <span>Kotwali Rd, Gurunanakpura, Faisalabad, Pakistan</span>
              </div>
            </div>

            <div class="ed-card-details">
              <div class="ed-card-detail-section">
                <h5>Academic Details</h5>
                <p class="ed-card-detail"><strong>Grade:</strong> CGPA = 3.46/4.00 Grade = A</p>
                <p class="ed-card-detail"><strong>Thesis:</strong> Constitutional Law and Human Rights</p>
                <p class="ed-card-detail">Foundational legal studies with focus on constitutional law, contract law, and corporate law.</p>
              </div>

              <div class="ed-card-detail-section">
                <h5 class="ed-achievements-title">
                  <svg class="ed-icon ed-icon-sm" viewBox="0 0 24 24">
                    <circle cx="12" cy="8" r="7"></circle>
                    <polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline>
                  </svg>
                  Key Achievements
                </h5>
                <ul class="ed-achievements-list">
                  <li><span class="ed-bullet"></span>Moot court competition winner</li>
                  <li><span class="ed-bullet"></span>Legal aid society volunteer</li>
                  <li><span class="ed-bullet"></span>Academic excellence scholarship recipient</li>
                </ul>
              </div>
            </div>

            <div class="ed-card-highlight">
              <p>Consistently maintained top academic performance throughout the program.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Additional Activities -->
  <section class="ed-activities-section">
    <div class="ed-max-w-6xl">
      <h2 class="ed-section-title ed-text-center ed-mb-16">Additional Academic Activities</h2>

      <div class="ed-activities-container">
        <!-- Summer Schools -->
        <div class="ed-timeline-item" data-category="summer-school">
          <div class="ed-activity-card">
            <div class="ed-activity-icon-section">
              <div class="ed-activity-icon-container">
                <svg class="ed-icon ed-icon-xl" viewBox="0 0 24 24">
                  <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
                  <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>
                </svg>
              </div>
              <h3 class="ed-activity-title">Summer Schools</h3>
            </div>

            <div class="ed-activity-content">
              <div class="ed-activity-items">
                <div class="ed-activity-item">
                  <h4 class="ed-activity-item-title">ITLL Summer School on NFTs, Metaverse, and the Law</h4>
                  <p class="ed-activity-item-detail"><strong>Duration:</strong> Five days</p>
                  <p class="ed-activity-item-detail"><strong>Organized by:</strong> University of Padua</p>
                  <p class="ed-activity-item-description">Legal challenges and regulatory frameworks for non-fungible tokens and metaverse environments.</p>
                </div>

                <div class="ed-activity-item">
                  <h4 class="ed-activity-item-title">European Digital Law Summer Institute</h4>
                  <p class="ed-activity-item-detail"><strong>Duration:</strong> Two weeks</p>
                  <p class="ed-activity-item-detail"><strong>Organized by:</strong> University of Amsterdam</p>
                  <p class="ed-activity-item-description">Comprehensive study of EU digital regulations and privacy law.</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Conferences -->
        <div class="ed-timeline-item" data-category="conference">
          <div class="ed-activity-card">
            <div class="ed-activity-icon-section">
              <div class="ed-activity-icon-container">
                <svg class="ed-icon ed-icon-xl" viewBox="0 0 24 24">
                  <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                  <circle cx="9" cy="7" r="4"></circle>
                  <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                  <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                </svg>
              </div>
              <h3 class="ed-activity-title">Conferences</h3>
            </div>

            <div class="ed-activity-content">
              <div class="ed-activity-items">
                <div class="ed-activity-item">
                  <h4 class="ed-activity-item-title">AI Governance and Digital Security Conference</h4>
                  <p class="ed-activity-item-detail"><strong>Organized by:</strong> University of Manchester and Indiana University</p>
                  <p class="ed-activity-item-description">Regulatory approaches to artificial intelligence, ethics in AI development, and digital security frameworks.</p>
                </div>

                <div class="ed-activity-item">
                  <h4 class="ed-activity-item-title">International Blockchain Law Symposium</h4>
                  <p class="ed-activity-item-detail"><strong>Organized by:</strong> Oxford University</p>
                  <p class="ed-activity-item-description">Global perspectives on cryptocurrency regulation and smart contract law.</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Workshops -->
        <div class="ed-timeline-item" data-category="workshop">
          <div class="ed-activity-card">
            <div class="ed-activity-icon-section">
              <div class="ed-activity-icon-container">
                <svg class="ed-icon ed-icon-xl" viewBox="0 0 24 24">
                  <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path>
                </svg>
              </div>
              <h3 class="ed-activity-title">Workshops</h3>
            </div>

            <div class="ed-activity-content">
              <div class="ed-activity-items">
                <div class="ed-activity-item">
                  <h4 class="ed-activity-item-title">Mapping Grey Areas in International Legal Approaches to The Failure of Crypto Firms</h4>
                  <p class="ed-activity-item-detail"><strong>Date:</strong> August 12-13, 2024</p>
                  <p class="ed-activity-item-detail"><strong>Location:</strong> Nottingham Trent University, UK</p>
                  <p class="ed-activity-item-description">International regulatory responses to cryptocurrency market failures and legal remedies.</p>
                </div>

                <div class="ed-activity-item">
                  <h4 class="ed-activity-item-title">Research Methodology Workshop</h4>
                  <p class="ed-activity-item-detail"><strong>Date:</strong> September 18, 2024</p>
                  <p class="ed-activity-item-detail"><strong>Location:</strong> Nottingham Trent University, UK</p>
                  <p class="ed-activity-item-description">Inductive and deductive approaches in research question development and building theory to enhance originality.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Licenses, Skills, Languages (Retained from original layout, restyled slightly) -->
  <section style="padding:4rem 1rem;background-color:var(--white);">
      <div class="container ed-max-w-6xl">
        <h2 class="ed-section-title ed-text-center" style="margin-bottom:3rem;">Licenses &amp; Core Competencies</h2>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px, 1fr));gap:30px;">
            <div style="background:var(--bg-section);padding:2rem;border-radius:var(--radius-md);border:1px solid var(--border);">
                <h3 style="color:var(--primary);margin-bottom:1.5rem;font-size:1.3rem;display:flex;align-items:center;gap:10px;">📋 Licenses &amp; Certifications</h3>
                <div style="margin-bottom:1.5rem;">
                    <strong>Islamabad High Court Bar Associate</strong>
                    <p style="color:var(--text-muted);font-size:0.95rem;margin-top:0.3rem;">Licensed Attorney — Islamabad High Court &amp; Bar Council</p>
                </div>
                <div>
                    <strong>Online Courses (MOOCs)</strong>
                    <ul style="font-size:0.9rem;color:var(--text-body);padding-left:1.2rem;margin-top:0.6rem;line-height:1.6;">
                        <li>AI &amp; Law — Lund University (Coursera)</li>
                        <li>Artificial Intelligence and Legal Issues — Politecnico di Milano</li>
                        <li>Privacy Law and Data Protection — University of Pennsylvania</li>
                        <li>Cloud Computing Law: Data Protection &amp; Cybersecurity — QM</li>
                        <li>European Business Law Series — Lund University</li>
                    </ul>
                </div>
            </div>

            <div style="background:var(--bg-section);padding:2rem;border-radius:var(--radius-md);border:1px solid var(--border);">
                <h3 style="color:var(--primary);margin-bottom:1.5rem;font-size:1.3rem;display:flex;align-items:center;gap:10px;">🛠️ Technical Skills</h3>
                <div class="team-specialties" style="flex-wrap:wrap;gap:10px;justify-content:flex-start;">
                    <span class="team-tag">Legal Research</span>
                    <span class="team-tag">Legal Writing</span>
                    <span class="team-tag">Corporate Law</span>
                    <span class="team-tag">FinTech</span>
                    <span class="team-tag">Blockchain Law</span>
                    <span class="team-tag">Contract Negotiation</span>
                    <span class="team-tag">AML / KYC</span>
                    <span class="team-tag">Civil Litigation</span>
                    <span class="team-tag">Criminal Law</span>
                    <span class="team-tag">Mendeley</span>
                    <span class="team-tag">Zotero</span>
                </div>

                <h3 style="color:var(--primary);margin:2.5rem 0 1rem;font-size:1.3rem;display:flex;align-items:center;gap:10px;">🌐 Languages</h3>
                <p style="font-size:1rem;color:var(--text-body);"><strong>Urdu</strong> — Native <br><br> <strong>English</strong> — Fluent (C1 Reading, B2 Listening/Writing/Speaking)</p>
            </div>
        </div>
      </div>
  </section>

  <!-- Script for Interactivity -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      setTimeout(() => {
        const heroContent = document.querySelector('.ed-hero-content');
        if(heroContent) heroContent.classList.remove('ed-hidden');
      }, 300);

      function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return (
          rect.top <= (window.innerHeight || document.documentElement.clientHeight) * 0.8 &&
          rect.bottom >= 0
        );
      }

      function handleScrollAnimations() {
        document.querySelectorAll('.ed-timeline-item').forEach((item, index) => {
          if (isInViewport(item)) {
            const card = item.querySelector('.ed-education-card, .ed-activity-card');
            if (card && !card.classList.contains('ed-card-animate')) {
              card.classList.add('ed-card-animate');
            }
          }
        });
      }

      handleScrollAnimations();
      window.addEventListener('scroll', handleScrollAnimations);

      const filterButtons = document.querySelectorAll('.ed-filter-btn');
      const timelineItems = document.querySelectorAll('.ed-timeline-item');

      filterButtons.forEach(button => {
        button.addEventListener('click', () => {
          filterButtons.forEach(btn => btn.classList.remove('active'));
          button.classList.add('active');

          const filterValue = button.getAttribute('data-filter');

          timelineItems.forEach(item => {
            item.classList.add('ed-hidden');
            const card = item.querySelector('.ed-education-card, .ed-activity-card');
            if (card) {
                card.classList.remove('ed-card-animate');
            }
            
            if (filterValue === 'all' || item.getAttribute('data-category') === filterValue) {
               item.classList.remove('ed-hidden');
               if (card) {
                 setTimeout(() => card.classList.add('ed-card-animate'), 50);
               }
            }
          });
        });
      });
    });
  </script>
"""

# Insert the CSS into head
new_content = re.sub(
    r'(</head>)', 
    lambda m: new_css + m.group(1), 
    content, 
    flags=re.IGNORECASE|re.DOTALL
)

# Remove the old page hero and old Academic Background section
# The old content starts with <!-- PAGE HERO --> and ends right before <!-- HIGHLIGHT: LLM GOLD MEDAL -->
pattern = r'<!-- PAGE HERO -->.*?<!-- HIGHLIGHT: LLM GOLD MEDAL -->'
new_content = re.sub(
    pattern, 
    new_html + "\n\n    <!-- HIGHLIGHT: LLM GOLD MEDAL -->", 
    new_content, 
    flags=re.IGNORECASE|re.DOTALL
)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Updated {filepath}")
