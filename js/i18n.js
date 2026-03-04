/* =======================================
   I18N.JS — Multi-language Support
   ======================================= */

const translations = {
    en: {
        // Navigation
        "nav-home": "Home",
        "nav-about": "About Me",
        "nav-practice": "Practice Areas",
        "nav-research": "Research",
        "nav-publications": "Publications",
        "nav-education": "Education",
        "nav-conferences": "Conferences",
        "nav-gallery": "Gallery",
        "nav-courses": "Courses",
        "nav-contact": "Contact",

        "mega-digital": "Digital Law",
        "mega-general": "General Practice",

        // Hero
        "hero-badge": "Islamabad High Court Bar Associate",
        "hero-title-1": "Navigating the<br /><span>Future of Law</span> — FinTech & Blockchain",
        "hero-desc-1": "PhD Fellow in Blockchain Law. Expert legal counsel in DeFi, digital assets, Web3 compliance, and cross-border regulatory frameworks.",
        "hero-title-2": "Corporate & Commercial<br /><span>Legal Expertise</span> in Pakistan",
        "hero-desc-2": "Licensed attorney before the Islamabad High Court. Advising businesses, startups, and institutions on corporate law, AML compliance, and FinTech regulation.",
        "hero-title-3": "Scholarly Research &<br /><span>International</span> Perspective",
        "hero-desc-3": "13+ peer-reviewed publications. Research Fellowships at University of Zurich & visiting researcher at institutions across Europe — bringing global insight to every case.",
        "book-consultation": "Book A Consultation",
        "learn-more": "Learn More →",

        // Trust Badges
        "badge-lawyer": "Islamabad High Court Bar Associate",
        "badge-phd": "PhD Fellow — Blockchain Law",
        "badge-uzh": "UZH Research Fellow — Blockchain DLT & Law",
        "badge-honors": "Summa Cum Laude — LL.M.",
        "badge-pubs": "13+ Peer-Reviewed Publications",

        // About Section (Home)
        "about-label": "About",
        "about-title": "Meet <span>Shan Ali</span>,<br />Blockchain & FinTech Legal Counsel",
        "about-text-1": "Shan Ali is a distinguished legal professional specialising in FinTech, Web3, and Blockchain Law. He is a PhD Fellow in Blockchain Law, licensed attorney before the Islamabad High Court, and a prolific scholar with over 13 peer-reviewed publications in leading international journals.",
        "about-quote": "\"The intersection of technology and law is not a challenge — it is an opportunity to build a more equitable digital future.\"",
        "about-text-2": "With experience spanning Anti-Money Laundering (AML), DeFi compliance, cross-border corporate law, and international research fellowships at institutions across Europe, Shan Ali brings a truly global perspective to every legal matter.",
        "about-li-1": "Islamabad High Court Bar Associate",
        "about-li-2": "Islamabad Bar Council Member",
        "about-li-3": "PhD Fellow in Blockchain Law (Ongoing)",
        "about-li-4": "LL.M. — Summa Cum Laude",
        "about-li-5": "Research Fellow — University of Zurich (UZH)",
        "about-btn": "Full Profile →",

        // Practice Areas (Home)
        "practice-label": "What I Do",
        "practice-title": "Practice Areas",
        "practice-subtitle": "Comprehensive legal expertise spanning digital assets, FinTech regulation, corporate law, and international compliance.",
        "practice-read-more": "Read More",
        "practice-view-all": "View All Practice Areas →",

        "pa-1-title": "FinTech & Blockchain Law",
        "pa-1-desc": "Expert legal advice on blockchain technology, smart contracts, DeFi protocols, digital asset regulation, and cryptocurrency compliance frameworks.",
        "pa-2-title": "Corporate & Commercial Law",
        "pa-2-desc": "Full-spectrum corporate legal services: company formation, shareholder disputes, M&A advisory, regulatory compliance, and commercial contracts.",
        "pa-3-title": "AML / KYC & Compliance",
        "pa-3-desc": "Anti-money laundering officer (MLRO) services, KYC framework design, compliance audits, and regulatory reporting under FinTech and AML legislation.",
        "pa-4-title": "Civil Litigation",
        "pa-4-desc": "Expert representation in civil disputes including contract matters, property conflicts, tort claims, and declaratory suits before Pakistan's courts.",
        "pa-5-title": "International & Cross-Border Law",
        "pa-5-desc": "Cross-border legal expertise in international arbitration, foreign arbitral awards, bilateral investment treaties, and multi-jurisdictional corporate compliance.",
        "pa-6-title": "Cybersecurity & Digital Rights",
        "pa-6-desc": "Legal advisory on cyber warfare, digital self-defense law, cybercrime under PECA, data privacy, and AI-related legal challenges.",

        // Why Choose Me
        "why-label": "Why Choose Me",
        "why-title": "Excellence You Can Trust",
        "why-1-title": "PhD-Level Expertise",
        "why-1-desc": "Currently pursuing a PhD in Blockchain Law with a focus on DAOs, digital governance, and regulatory reform in Italy and Pakistan.",
        "why-2-title": "International Research Background",
        "why-2-desc": "Research fellowships at University of Zurich and visiting researcher at institutions in the UK, Italy, and Germany — bringing global legal insights.",
        "why-3-title": "Prolific Scholar",
        "why-3-desc": "13+ peer-reviewed publications in international journals covering blockchain, AI law, cyber warfare, corporate governance, and arbitration.",
        "why-4-title": "Tech-Forward Legal Thinking",
        "why-4-desc": "Specialization in emerging legal areas — DeFi, NFTs, metaverse law, AI legislation — ensuring you get cutting-edge legal advice.",
        "why-5-title": "Client-First Approach",
        "why-5-desc": "From individual disputes to corporate mandates, every client receives personalized, strategic legal counsel tailored to their specific needs.",
        "why-6-title": "Strict Confidentiality",
        "why-6-desc": "Your information is protected by the highest standards of attorney-client privilege and professional confidentiality.",

        // CTA Banner
        "cta-title": "Ready to Discuss Your Legal Matter?",
        "cta-desc": "Get a free initial consultation in FinTech Law, Blockchain Compliance, Corporate Law, or any legal matter. I'm here to help.",
        "cta-btn-book": "Book Free Consultation",
        "cta-btn-linkedin": "LinkedIn Profile",

        // About Page (Specific Content)
        "about-pg-hero-title": "About Shan Ali",
        "about-pg-hero-desc": "FinTech, Web3 & Corporate Legal Counsel | PhD Fellow in Blockchain Law | Licensed Attorney",
        "about-pg-label": "Profile",
        "about-pg-role": "FinTech, Web3 & Corporate Legal Counsel",
        "about-pg-bio-1": "Shan Ali is a distinguished legal professional specialising in FinTech, Web3, and Blockchain Law. He is currently a PhD Fellow in Blockchain Law with a focus on Decentralised Autonomous Organisations (DAOs), AI legal frameworks, and DeFi regulatory reform. He is a licensed attorney before the Islamabad High Court and a member of the Islamabad Bar Council.",
        "about-pg-bio-2": "With over 13 peer-reviewed publications in leading international journals and research fellowships at the University of Zurich (UZH) and institutions across the UK and Europe, Shan Ali brings an unparalleled combination of legal scholarship and practical expertise to every matter.",

        // Footer
        "footer-desc": "FinTech, Web3 & Corporate Legal Counsel — PhD Fellow in Blockchain Law — providing expert legal services in Pakistan and internationally.",
        "footer-quick-links": "Quick Links",
        "footer-courts": "Courts & Affiliations",
        "footer-contact": "Contact",
        "footer-rights": "© 2025 Shan Ali. FinTech & Blockchain Legal Counsel. All rights reserved."
    },
    it: {
        // Navigation
        "nav-home": "Home",
        "nav-about": "Chi Sono",
        "nav-practice": "Aree di Competenza",
        "nav-research": "Ricerca",
        "nav-publications": "Pubblicazioni",
        "nav-education": "Istruzione",
        "nav-conferences": "Conferenze",
        "nav-gallery": "Galleria",
        "nav-courses": "Corsi",
        "nav-contact": "Contatti",

        "mega-digital": "Diritto Digitale",
        "mega-general": "Pratica Generale",

        // Hero
        "hero-badge": "Associato del Foro dell'Alta Corte di Islamabad",
        "hero-title-1": "Navigando il<br /><span>Futuro del Diritto</span> — FinTech & Blockchain",
        "hero-desc-1": "Dottorando in Diritto della Blockchain. Esperto consulente legale in DeFi, asset digitali, conformità Web3 e quadri normativi transfrontalieri.",
        "hero-title-2": "Esperienza Legale<br /><span>Societaria e Commerciale</span> in Pakistan",
        "hero-desc-2": "Avvocato abilitato presso l'Alta Corte di Islamabad. Consulenza ad aziende, startup e istituzioni su diritto societario, conformità AML e regolamentazione FinTech.",
        "hero-title-3": "Ricerca Accademica &<br /><span>Prospettiva Internazionale</span>",
        "hero-desc-3": "Oltre 13 pubblicazioni sottoposte a revisione paritaria. Borse di ricerca presso l'Università di Zurigo e ricercatore ospite in istituzioni in tutta Europa.",
        "book-consultation": "Prenota una Consulenza",
        "learn-more": "Scopri di Più →",

        // Trust Badges
        "badge-lawyer": "Associato del Foro dell'Alta Corte di Islamabad",
        "badge-phd": "Dottorando — Diritto della Blockchain",
        "badge-uzh": "Ricercatore UZH — Blockchain DLT e Diritto",
        "badge-honors": "Summa Cum Laude — LL.M.",
        "badge-pubs": "Oltre 13 Pubblicazioni Scientifiche",

        // About Section (Home)
        "about-label": "Profilo",
        "about-title": "Incontra <span>Shan Ali</span>,<br />Consulente Legale Blockchain & FinTech",
        "about-text-1": "Shan Ali è un illustre professionista legale specializzato in FinTech, Web3 e Diritto della Blockchain. È un dottorando in Diritto della Blockchain, avvocato abilitato presso l'Alta Corte di Islamabad e un prolifico studioso con oltre 13 pubblicazioni sottoposte a revisione paritaria.",
        "about-quote": "\"L'intersezione tra tecnologia e diritto non è una sfida, ma un'opportunità per costruire un futuro digitale più equo.\"",
        "about-text-2": "Con un'esperienza che spazia dall'Anti-Riciclaggio (AML), alla conformità DeFi, al diritto societario transfrontaliero e alle borse di ricerca internazionali in tutta Europa, Shan Ali porta una prospettiva veramente globale in ogni questione legale.",
        "about-li-1": "Associato del Foro dell'Alta Corte di Islamabad",
        "about-li-2": "Membro del Consiglio dell'Ordine di Islamabad",
        "about-li-3": "Dottorando in Diritto della Blockchain (In corso)",
        "about-li-4": "LL.M. — Summa Cum Laude",
        "about-li-5": "Ricercatore — Università di Zurigo (UZH)",
        "about-btn": "Profilo Completo →",

        // Practice Areas (Home)
        "practice-label": "Cosa Faccio",
        "practice-title": "Aree di Competenza",
        "practice-subtitle": "Competenza legale completa che spazia dagli asset digitali alla regolamentazione FinTech, dal diritto societario alla conformità internazionale.",
        "practice-read-more": "Scopri di più",
        "practice-view-all": "Tutte le Aree di Competenza →",

        "pa-1-title": "Diritto FinTech & Blockchain",
        "pa-1-desc": "Consulenza legale esperta su tecnologia blockchain, smart contracts, protocolli DeFi, regolamentazione degli asset digitali e conformità cripto.",
        "pa-2-title": "Diritto Societario & Commerciale",
        "pa-2-desc": "Servizi legali societari completi: costituzione societaria, controversie tra soci, consulenza M&A, conformità normativa e contratti commerciali.",
        "pa-3-title": "AML / KYC & Conformità",
        "pa-3-desc": "Servizi di responsabile anti-riciclaggio (MLRO), progettazione di framework KYC, audit di conformità e reporting normativo FinTech e AML.",
        "pa-4-title": "Contenzioso Civile",
        "pa-4-desc": "Rappresentanza esperta in controversie civili inclusi contratti, conflitti di proprietà, reclami per illeciti civili e cause dichiarative in Pakistan.",
        "pa-5-title": "Diritto Internazionale & Transfrontaliero",
        "pa-5-desc": "Esperienza legale transfrontaliera in arbitrato internazionale, lodi arbitrali stranieri, trattati bilaterali di investimento e conformità societaria multi-giurisdizionale.",
        "pa-6-title": "Cybersicurezza & Diritti Digitali",
        "pa-6-desc": "Consulenza legale su guerra informatica, diritto di autodifesa digitale, criminalità informatica (PECA), privacy dei dati e sfide legali dell'AI.",

        // Why Choose Me
        "why-label": "Perché Scegliermi",
        "why-title": "Eccellenza di Cui Ti Puoi Fidare",
        "why-1-title": "Competenza a Livello di Dottorato",
        "why-1-desc": "Attualmente sta conseguendo un dottorato in Diritto della Blockchain con focus su DAO, governance digitale e riforme normative in Italia e Pakistan.",
        "why-2-title": "Background di Ricerca Internazionale",
        "why-2-desc": "Borse di ricerca presso l'Università di Zurigo e ricercatore ospite nel Regno Unito, in Italia e in Germania — portando intuizioni legali globali.",
        "why-3-title": "Studioso Prolifico",
        "why-3-desc": "Oltre 13 pubblicazioni in riviste internazionali che coprono blockchain, diritto AI, guerra informatica, governance societaria e arbitrato.",
        "why-4-title": "Pensiero Legale Orientato al Futuro",
        "why-4-desc": "Specializzazione in aree legali emergenti — DeFi, NFT, diritto del metaverso, legislazione AI — garantendo una consulenza legale all'avanguardia.",
        "why-5-title": "Approccio Centrato sul Cliente",
        "why-5-desc": "Dalle controversie individuali ai mandati societari, ogni cliente riceve una consulenza legale strategica e personalizzata.",
        "why-6-title": "Rigorosa Riservatezza",
        "why-6-desc": "Le tue informazioni sono protette dai più alti standard di segreto professionale avvocato-cliente e riservatezza.",

        // CTA Banner
        "cta-title": "Pronto a Discutere la Tua Questione Legale?",
        "cta-desc": "Ottieni una prima consulenza gratuita in diritto FinTech, conformità blockchain, diritto societario o qualsiasi questione legale.",
        "cta-btn-book": "Prenota Consulenza Gratuita",
        "cta-btn-linkedin": "Profilo LinkedIn",

        // About Page (Specific Content)
        "about-pg-hero-title": "Chi è Shan Ali",
        "about-pg-hero-desc": "Consulente FinTech, Web3 e Societario | Dottorando in Blockchain | Avvocato Abilitato",
        "about-pg-label": "Profilo",
        "about-pg-role": "Consulente Legale FinTech, Web3 e Societario",
        "about-pg-bio-1": "Shan Ali è un illustre professionista legale specializzato in FinTech, Web3 e Diritto della Blockchain. Attualmente è dottorando in Diritto della Blockchain con focus su Organizzazioni Autonome Decentralizzate (DAO), quadri legali AI e riforma normativa DeFi.",
        "about-pg-bio-2": "Con oltre 13 pubblicazioni e borse di ricerca presso l'Università di Zurigo (UZH), Shan Ali combina borsa di studio legale e competenza pratica in ogni questione.",

        // Footer
        "footer-desc": "Consulente legale FinTech, Web3 e societario — Dottorando in Diritto della Blockchain — fornisce servizi legali esperti in Pakistan e a livello internazionale.",
        "footer-quick-links": "Link Rapidi",
        "footer-courts": "Corti e Affiliazioni",
        "footer-contact": "Contatto",
        "footer-rights": "© 2025 Shan Ali. Consulente legale FinTech e Blockchain. Tutti i diritti riservati."
    },
    de: {
        // Navigation
        "nav-home": "Startseite",
        "nav-about": "Über Mich",
        "nav-practice": "Rechtsgebiete",
        "nav-research": "Forschung",
        "nav-publications": "Publikationen",
        "nav-education": "Bildung",
        "nav-conferences": "Konferenzen",
        "nav-gallery": "Galerie",
        "nav-courses": "Kurse",
        "nav-contact": "Kontakt",

        "mega-digital": "Digitales Recht",
        "mega-general": "Allgemeine Praxis",

        // Hero
        "hero-badge": "Mitglied der Anwaltskammern am High Court Islamabad",
        "hero-title-1": "Die Zukunft des Rechts<br /><span>navigieren</span> — FinTech & Blockchain",
        "hero-desc-1": "Doktorand im Blockchain-Recht. Experte für Rechtsberatung in den Bereichen DeFi, digitale Assets, Web3-Compliance und grenzüberschreitende Regulierung.",
        "hero-title-2": "Gesellschafts- & Wirtschaftsrecht<br /><span>Expertise</span> in Pakistan",
        "hero-desc-2": "Zugelassener Rechtsanwalt am High Court Islamabad. Beratung von Unternehmen, Startups und Institutionen in den Bereichen Gesellschaftsrecht, AML-Compliance und FinTech-Regulierung.",
        "hero-title-3": "Scholarly Research &<br /><span>Internationale</span> Perspektive",
        "hero-desc-3": "Über 13 begutachtete Publikationen. Forschungsstipendien an der Universität Zürich & Gastforscher an Institutionen in ganz Europa.",
        "book-consultation": "Beratung buchen",
        "learn-more": "Mehr erfahren →",

        // Trust Badges
        "badge-lawyer": "Zugelassener Anwalt am High Court Islamabad",
        "badge-phd": "Doktorand — Blockchain-Recht",
        "badge-uzh": "UZH Forschungsstipendiat — Blockchain DLT & Recht",
        "badge-honors": "Summa Cum Laude — LL.M.",
        "badge-pubs": "13+ Begutachtete Publikationen",

        // About Section (Home)
        "about-label": "Über Mich",
        "about-title": "Lernen Sie <span>Shan Ali</span> kennen,<br />Rechtsberater für Blockchain & FinTech",
        "about-text-1": "Shan Ali ist ein profilierter Rechtsexperte, spezialisiert auf FinTech, Web3 und Blockchain-Recht. Er ist Doktorand für Blockchain-Recht, zugelassener Anwalt am High Court Islamabad und ein produktiver Wissenschaftler mit über 13 Publikationen in führenden internationalen Fachzeitschriften.",
        "about-quote": "\"Die Schnittstelle von Technologie und Recht ist keine Herausforderung — sie ist eine Chance, eine gerechtere digitale Zukunft aufzubauen.\"",
        "about-text-2": "Mit Erfahrung in den Bereichen Geldwäscheprävention (AML), DeFi-Compliance, grenzüberschreitendes Gesellschaftsrecht und internationalen Forschungsstipendien in ganz Europa bringt Shan Ali eine globale Perspektive ein.",
        "about-li-1": "Zugelassener Anwalt am High Court Islamabad",
        "about-li-2": "Mitglied des Bar Council Islamabad",
        "about-li-3": "Doktorand im Blockchain-Recht (Laufend)",
        "about-li-4": "LL.M. — Summa Cum Laude",
        "about-li-5": "Forschungsstipendiat — Universität Zürich (UZH)",
        "about-btn": "Vollständiges Profil →",

        // Practice Areas (Home)
        "practice-label": "Leistungen",
        "practice-title": "Rechtsgebiete",
        "practice-subtitle": "Umfassende Rechtsexpertise in den Bereichen digitale Assets, FinTech-Regulierung, Gesellschaftsrecht und internationale Compliance.",
        "practice-read-more": "Mehr lesen",
        "practice-view-all": "Alle Rechtsgebiete anzeigen →",

        "pa-1-title": "FinTech & Blockchain-Recht",
        "pa-1-desc": "Kompetente Rechtsberatung zu Blockchain-Technologie, Smart Contracts, DeFi-Protokollen, Regulierung digitaler Assets und Krypto-Compliance.",
        "pa-2-title": "Gesellschafts- & Wirtschaftsrecht",
        "pa-2-desc": "Umfassende gesellschaftsrechtliche Leistungen: Unternehmensgründung, Gesellschafterstreitigkeiten, M&A-Beratung und Wirtschaftsverträge.",
        "pa-3-title": "AML / KYC & Compliance",
        "pa-3-desc": "Geldwäschebeauftragter (MLRO), Design von KYC-Systemen, Compliance-Audits und regulatorisches Berichtswesen unter FinTech- und AML-Gesetzen.",
        "pa-4-title": "Zivilprozessrecht",
        "pa-4-desc": "Kompetente Vertretung in Zivilstreitigkeiten, einschließlich Vertragsangelegenheiten, Immobilienkonflikten und Feststellungsklagen vor pakistanischen Gerichten.",
        "pa-5-title": "Internationales & Grenzüberschreitendes Recht",
        "pa-5-desc": "Grenzüberschreitende Expertise in internationaler Schiedsgerichtsbarkeit, ausländischen Schiedssprüchen und multi-jurisdiktionaler Compliance.",
        "pa-6-title": "Cybersecurity & Digitale Rechte",
        "pa-6-desc": "Rechtsberatung zu Cyber-Kriegsführung, digitalem Selbstverteidigungsrecht, Cyberkriminalität (PECA), Datenschutz und KI-Herausforderungen.",

        // Why Choose Me
        "why-label": "Warum Ich",
        "why-title": "Exzellenz, der Sie vertrauen können",
        "why-1-title": "Expertise auf Promotionsebene",
        "why-1-desc": "Promoviert derzeit im Blockchain-Recht mit Schwerpunkt auf DAOs, Digital Governance und Regulierungsreformen in Italien und Pakistan.",
        "why-2-title": "Internationaler Forschungs-Background",
        "why-2-desc": "Forschungsstipendien an der Universität Zürich und Gastforscher im Vereinigten Königreich, Italien und Deutschland.",
        "why-3-title": "Produktiver Wissenschaftler",
        "why-3-desc": "Über 13 Publikationen in internationalen Fachzeitschriften zu Blockchain, KI-Recht, Cyber-Kriegsführung und Corporate Governance.",
        "why-4-title": "Zukunftsorientiertes Rechtsdenken",
        "why-4-desc": "Spezialisierung auf aufstrebende Rechtsgebiete — DeFi, NFTs, Metaverse-Recht, KI-Gesetzgebung — für modernste Rechtsberatung.",
        "why-5-title": "Mandanten-zentrierter Ansatz",
        "why-5-desc": "Vom individuellen Streitfall bis zum Firmenmandat erhält jeder Mandant eine persönliche, strategische Rechtsberatung.",
        "why-6-title": "Strenge Vertraulichkeit",
        "why-6-desc": "Ihre Informationen sind durch die höchsten Standards des Anwaltsgeheimnisses und der beruflichen Verschwiegenheit geschützt.",

        // CTA Banner
        "cta-title": "Bereit, Ihr rechtliches Anliegen zu besprechen?",
        "cta-desc": "Erhalten Sie eine kostenlose Erstberatung im FinTech-Recht, Blockchain-Compliance, Gesellschaftsrecht oder anderen Rechtsgebieten.",
        "cta-btn-book": "Kostenlose Beratung buchen",
        "cta-btn-linkedin": "LinkedIn Profil",

        // About Page (Specific Content)
        "about-pg-hero-title": "Über Shan Ali",
        "about-pg-hero-desc": "FinTech, Web3 & Gesellschaftsrecht | Doktorand Blockchain | Anwalt",
        "about-pg-label": "Profil",
        "about-pg-role": "Rechtsberater für FinTech, Web3 & Gesellschaftsrecht",
        "about-pg-bio-1": "Shan Ali ist ein profilierter Rechtsexperte für FinTech, Web3 und Blockchain-Recht. Aktuell promoviert er im Blockchain-Recht mit Fokus auf DAOs und DeFi.",
        "about-pg-bio-2": "Mit über 13 Publikationen und Stationen an der UZH verbindet Shan Ali wissenschaftliche Tiefe mit praktischer Erfahrung.",

        // Footer
        "footer-desc": "Rechtsberater für FinTech, Web3 & Gesellschaftsrecht — Doktorand im Blockchain-Recht — bietet kompetente Rechtsdienstleistungen in Pakistan und international.",
        "footer-quick-links": "Quick Links",
        "footer-courts": "Gerichte & Zugehörigkeiten",
        "footer-contact": "Kontakt",
        "footer-rights": "© 2025 Shan Ali. Rechtsberater für FinTech & Blockchain. Alle Rechte vorbehalten."
    }
};

class LanguageManager {
    constructor() {
        this.currentLang = localStorage.getItem('selectedLanguage') || 'en';
        this.init();
    }

    init() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.start());
        } else {
            this.start();
        }
    }

    start() {
        this.updateUI();
        this.createSwitcher();
    }

    setLanguage(lang) {
        if (!translations[lang]) return;
        this.currentLang = lang;
        localStorage.setItem('selectedLanguage', lang);
        this.updateUI();

        // Update switcher active state
        document.querySelectorAll('.lang-option').forEach(opt => {
            opt.classList.toggle('active', opt.dataset.lang === lang);
        });

        const event = new CustomEvent('languageChanged', { detail: { lang } });
        document.dispatchEvent(event);
    }

    updateUI() {
        document.documentElement.lang = this.currentLang;
        const currentTranslations = translations[this.currentLang];

        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.dataset.i18n;
            if (currentTranslations[key]) {
                if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                    el.placeholder = currentTranslations[key];
                } else {
                    el.innerHTML = currentTranslations[key];
                }
            }
        });
    }

    createSwitcher() {
        if (document.querySelector('.lang-switcher')) return;

        const headerInner = document.querySelector('.header-inner');
        const mobileMenu = document.querySelector('.mobile-menu');

        if (headerInner) {
            const desktopSwitcher = this.buildSwitcher('desktop-lang-switcher');
            const hamburger = document.querySelector('.hamburger');
            if (hamburger) {
                headerInner.insertBefore(desktopSwitcher, hamburger);
            } else {
                headerInner.appendChild(desktopSwitcher);
            }
        }

        if (mobileMenu) {
            const mobileSwitcher = this.buildSwitcher('mobile-lang-switcher');
            mobileMenu.prepend(mobileSwitcher);
        }
    }

    buildSwitcher(extraClass) {
        const switcherContainer = document.createElement('div');
        switcherContainer.className = `lang-switcher ${extraClass}`;

        const currentLangDisplay = document.createElement('button');
        currentLangDisplay.className = 'lang-current';
        currentLangDisplay.innerHTML = `<span>${this.currentLang.toUpperCase()}</span>`;

        const langDropdown = document.createElement('div');
        langDropdown.className = 'lang-dropdown';

        ['en', 'it', 'de'].forEach(lang => {
            const option = document.createElement('div');
            option.className = `lang-option ${this.currentLang === lang ? 'active' : ''}`;
            option.dataset.lang = lang;
            option.textContent = lang.toUpperCase();
            option.addEventListener('click', () => {
                this.setLanguage(lang);
                // Update all switcher displays
                document.querySelectorAll('.lang-current span').forEach(s => {
                    s.textContent = lang.toUpperCase();
                });
                // Update active states in all dropdowns
                document.querySelectorAll('.lang-option').forEach(opt => {
                    opt.classList.toggle('active', opt.dataset.lang === lang);
                });
            });
            langDropdown.appendChild(option);
        });

        switcherContainer.appendChild(currentLangDisplay);
        switcherContainer.appendChild(langDropdown);
        return switcherContainer;
    }
}

const langManager = new LanguageManager();
window.langManager = langManager;
