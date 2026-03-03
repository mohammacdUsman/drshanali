/* =======================================
   MAIN.JS — Navigation + Reveal Animations
======================================= */

// ── Sticky Header ──────────────────────
const header = document.querySelector('.header');
if (header) {
    window.addEventListener('scroll', () => {
        header.classList.toggle('scrolled', window.scrollY > 40);
    });
}

// ── Mobile Hamburger Menu ───────────────
const hamburger = document.querySelector('.hamburger');
const mobileMenu = document.querySelector('.mobile-menu');

if (hamburger && mobileMenu) {
    const mobileLinks = mobileMenu.querySelectorAll('.mobile-menu-link');
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('open');
        mobileMenu.classList.toggle('open');
        const isOpen = mobileMenu.classList.contains('open');
        document.body.style.overflow = isOpen ? 'hidden' : '';
        document.body.classList.toggle('menu-open', isOpen);

        if (isOpen) {
            mobileLinks.forEach((link, index) => {
                link.style.animationDelay = `${index * 0.05 + 0.1}s`;
            });
        }
    });

    // Close if clicked outside
    document.addEventListener('click', (e) => {
        const isOpen = mobileMenu.classList.contains('open');
        if (isOpen && !mobileMenu.contains(e.target) && !hamburger.contains(e.target)) {
            hamburger.classList.remove('open');
            mobileMenu.classList.remove('open');
            document.body.style.overflow = '';
            document.body.classList.remove('menu-open');
        }
    });

    // Close on nav link click
    mobileMenu.querySelectorAll('.mobile-menu-link').forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('open');
            mobileMenu.classList.remove('open');
            document.body.style.overflow = '';
            document.body.classList.remove('menu-open');
        });
    });
}

// ── Active Nav Link ─────────────────────
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-link, .mobile-menu-link, .footer-link').forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    const linkPage = href.split('/').pop();
    if (linkPage === currentPage || (currentPage === '' && linkPage === 'index.html')) {
        link.classList.add('active');
    }
});

// ── Scroll Reveal Animation ─────────────
const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
            revealObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// ── Hero Slider ──────────────────────────
const heroSlides = document.querySelectorAll('.hero-slide');
const heroDots = document.querySelectorAll('.hero-dot');
let currentSlide = 0;
let slideTimer;

function goToSlide(n) {
    heroSlides.forEach(s => s.classList.remove('active'));
    heroDots.forEach(d => d.classList.remove('active'));
    currentSlide = (n + heroSlides.length) % heroSlides.length;
    if (heroSlides[currentSlide]) heroSlides[currentSlide].classList.add('active');
    if (heroDots[currentSlide]) heroDots[currentSlide].classList.add('active');
}

function startSlider() {
    if (heroSlides.length === 0) return;
    goToSlide(0);
    slideTimer = setInterval(() => goToSlide(currentSlide + 1), 5000);
}

heroDots.forEach((dot, i) => {
    dot.addEventListener('click', () => {
        clearInterval(slideTimer);
        goToSlide(i);
        slideTimer = setInterval(() => goToSlide(currentSlide + 1), 5000);
    });
});



startSlider();

// ── Interactive Map Mobile Support ───────
const mapMarkers = document.querySelectorAll('.map-marker');
mapMarkers.forEach(marker => {
    marker.addEventListener('click', (e) => {
        // Close others
        mapMarkers.forEach(m => {
            if (m !== marker) m.classList.remove('active');
        });
        marker.classList.toggle('active');
        e.stopPropagation();
    });
});
// Close tooltips when clicking outside
document.addEventListener('click', () => {
    mapMarkers.forEach(m => m.classList.remove('active'));
});

// ── Animated Stat Counters ───────────────
function animateCounter(el) {
    const target = parseInt(el.dataset.target, 10);
    const suffix = el.dataset.suffix || '';
    const duration = 2000;
    const step = duration / 60;
    const increment = target / (duration / 16);
    let current = 0;

    const timer = setInterval(() => {
        current = Math.min(current + increment, target);
        el.textContent = Math.floor(current) + suffix;
        if (current >= target) clearInterval(timer);
    }, 16);
}

const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.querySelectorAll('[data-target]').forEach(animateCounter);
            counterObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.4 });

document.querySelectorAll('.stats, .stats-strip').forEach(el => counterObserver.observe(el));

// ── Team Carousel ───────────────────────
const teamSlides = document.querySelectorAll('.team-slide');
const teamCounter = document.querySelector('.team-counter');
const teamPrev = document.getElementById('teamPrev');
const teamNext = document.getElementById('teamNext');
let teamCurrent = 0;

function showTeamSlide(n) {
    teamSlides.forEach(s => s.classList.remove('active'));
    teamCurrent = (n + teamSlides.length) % teamSlides.length;
    if (teamSlides[teamCurrent]) teamSlides[teamCurrent].classList.add('active');
    if (teamCounter) {
        teamCounter.innerHTML = `<span>${teamCurrent + 1}</span> / ${teamSlides.length}`;
    }
}

if (teamSlides.length > 0) {
    showTeamSlide(0);
    teamPrev && teamPrev.addEventListener('click', () => showTeamSlide(teamCurrent - 1));
    teamNext && teamNext.addEventListener('click', () => showTeamSlide(teamCurrent + 1));
}

// ── Smooth Scroll for anchor links ──────
document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
        const target = document.querySelector(a.getAttribute('href'));
        if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// ── Contact Booking Tabs & Calendar UI ──
const bookingTabs = document.querySelectorAll('.booking-tab');
const bookingPanels = document.querySelectorAll('.booking-panel');

if (bookingTabs.length > 0) {
    bookingTabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active class
            bookingTabs.forEach(t => t.classList.remove('active'));
            bookingPanels.forEach(p => p.classList.remove('active'));
            // Add active class
            tab.classList.add('active');
            const target = document.getElementById(tab.dataset.target);
            if (target) target.classList.add('active');
        });
    });

    // Calendar Date Selection
    const calendarDates = document.querySelectorAll('.calendar-date:not(.empty):not(.disabled)');
    calendarDates.forEach(date => {
        date.addEventListener('click', () => {
            calendarDates.forEach(d => d.classList.remove('selected'));
            date.classList.add('selected');
        });
    });

    // Time Slot Selection
    const timeSlots = document.querySelectorAll('.time-slot:not(.disabled)');
    timeSlots.forEach(slot => {
        slot.addEventListener('click', () => {
            timeSlots.forEach(s => s.classList.remove('selected'));
            slot.classList.add('selected');
        });
    });

    // Confirm Booking
    const btnConfirmBooking = document.getElementById('btnConfirmBooking');
    if (btnConfirmBooking) {
        btnConfirmBooking.addEventListener('click', () => {
            const selectedDate = document.querySelector('.calendar-date.selected');
            const selectedTime = document.querySelector('.time-slot.selected');
            if (selectedDate && selectedTime) {
                btnConfirmBooking.textContent = 'Booking Confirmed ✓';
                btnConfirmBooking.style.background = '#28a745';
                btnConfirmBooking.style.color = '#fff';
            } else {
                alert('Please select a date and time slot first.');
            }
        });
    }
}

// ── Interactive Compliance Quiz ──────────
const quizSteps = document.querySelectorAll('.quiz-step');
const progressBar = document.getElementById('quizProgress');

if (quizSteps.length > 0) {
    let currentStep = 0;

    // Handle Option Selection
    document.querySelectorAll('.quiz-option').forEach(option => {
        option.addEventListener('click', (e) => {
            // Prevent default if clicking the label directly to avoid double firing
            // but let the radio button check itself.
            const parent = option.closest('.quiz-options');
            parent.querySelectorAll('.quiz-option').forEach(opt => opt.classList.remove('selected'));
            option.classList.add('selected');
            const radio = option.querySelector('input[type="radio"]');
            if (radio) radio.checked = true;
        });
    });

    const updateProgress = () => {
        if (progressBar) {
            const progress = ((currentStep + 1) / (quizSteps.length)) * 100;
            progressBar.style.width = `${progress}%`;
        }
    };

    const showStep = (stepIndex) => {
        quizSteps.forEach(s => s.classList.remove('active'));
        quizSteps[stepIndex].classList.add('active');
        currentStep = stepIndex;
        updateProgress();
    };

    // Next Buttons
    document.querySelectorAll('.btn-next').forEach((btn, idx) => {
        btn.addEventListener('click', () => {
            // Optional: validate if an option is selected
            const currentOptions = quizSteps[currentStep].querySelectorAll('input[type="radio"]');
            let answered = false;
            currentOptions.forEach(r => { if (r.checked) answered = true; });

            if (currentOptions.length > 0 && !answered) {
                alert('Please select an option to continue.');
                return;
            }
            if (currentStep < quizSteps.length - 1) showStep(currentStep + 1);
        });
    });

    // Prev Buttons
    document.querySelectorAll('.btn-prev').forEach((btn) => {
        btn.addEventListener('click', () => {
            if (currentStep > 0) showStep(currentStep - 1);
        });
    });

    // Finish Quiz
    const btnFinish = document.querySelector('.btn-finish');
    if (btnFinish) {
        btnFinish.addEventListener('click', () => {
            const currentOptions = quizSteps[currentStep].querySelectorAll('input[type="radio"]');
            let answered = false;
            currentOptions.forEach(r => { if (r.checked) answered = true; });
            if (!answered) {
                alert('Please select an option to continue.');
                return;
            }

            // Calculate score
            let score = 0;
            const q1 = document.querySelector('input[name="q1"]:checked')?.value || 'no';
            const q2 = document.querySelector('input[name="q2"]:checked')?.value || 'no';
            const q3 = document.querySelector('input[name="q3"]:checked')?.value || 'no';

            if (q1 === 'yes') score += 33;
            else if (q1 === 'partial') score += 15;

            if (q2 === 'yes') score += 33;
            else if (q2 === 'partial') score += 15;

            if (q3 === 'yes') score += 34;

            const scoreCircle = document.getElementById('quizScore');
            const quizTitle = document.getElementById('quizTitle');
            const quizDesc = document.getElementById('quizDesc');

            scoreCircle.textContent = `${score}%`;

            if (score >= 80) {
                scoreCircle.style.color = '#28a745';
                scoreCircle.style.borderColor = '#28a745';
                quizTitle.textContent = 'High Compliance';
                quizDesc.textContent = 'Your business demonstrates strong adherence to regulations. Protect your operations further with our advanced corporate retainer.';
            } else if (score >= 40) {
                scoreCircle.style.color = '#c9923a';
                scoreCircle.style.borderColor = '#c9923a';
                quizTitle.textContent = 'Moderate Risk Detected';
                quizDesc.textContent = 'Your business has some compliance gaps that could lead to financial penalties or legal disputes.';
            } else {
                scoreCircle.style.color = '#dc3545';
                scoreCircle.style.borderColor = '#dc3545';
                quizTitle.textContent = 'High Risk Detected';
                quizDesc.textContent = 'Urgent action is recommended. Your current regulatory posture exposes the business to significant legal liabilities.';
            }

            showStep(quizSteps.length - 1);
        });
    }
}

// ── Live Regulatory Policy Tracker ───────
const trackerContent = document.getElementById('policyTrackerContent');
if (trackerContent) {
    // Simulate a brief flash update every 15 seconds to simulate live data arrival
    setInterval(() => {
        const originalBg = trackerContent.style.backgroundColor;
        trackerContent.style.transition = 'background-color 0.3s ease';
        trackerContent.style.backgroundColor = 'rgba(201, 146, 58, 0.15)';

        setTimeout(() => {
            trackerContent.style.backgroundColor = originalBg || 'transparent';
        }, 600);
    }, 15000);
}

// ── Page Loader ──────────────────────────
window.addEventListener('load', () => {
    const loader = document.getElementById('page-loader');
    if (loader) {
        setTimeout(() => {
            loader.classList.add('fade-out');
        }, 300); // Small 300ms delay to ensure smooth transition
    }
});
