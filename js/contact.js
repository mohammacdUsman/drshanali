/* =======================================
   CONTACT.JS — Form Validation & Submission
======================================= */

const form = document.getElementById('contactForm');
const successMsg = document.getElementById('formSuccess');

function validateField(group, input) {
    const isEmpty = !input.value.trim();
    const isEmail = input.type === 'email';
    const emailOk = isEmail ? /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value) : true;

    const hasError = isEmpty || !emailOk;
    group.classList.toggle('error', hasError);

    const errEl = group.querySelector('.form-error');
    if (errEl) {
        if (isEmpty) errEl.textContent = 'This field is required.';
        else if (!emailOk) errEl.textContent = 'Please enter a valid email address.';
    }

    return !hasError;
}

if (form) {
    // Live validation on blur
    form.querySelectorAll('input, textarea').forEach(input => {
        input.addEventListener('blur', () => {
            validateField(input.closest('.form-group'), input);
        });
        input.addEventListener('input', () => {
            if (input.closest('.form-group').classList.contains('error')) {
                validateField(input.closest('.form-group'), input);
            }
        });
    });

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        // Honeypot check
        const honeypot = form.querySelector('input[name="hp_email"]');
        if (honeypot && honeypot.value) {
            console.log("Spam detected.");
            return;
        }

        let allValid = true;
        // Validate all required fields
        form.querySelectorAll('input[required], textarea[required]').forEach(input => {
            const group = input.closest('.form-group');
            if (group) {
                const isValid = validateField(group, input);
                if (!isValid) allValid = false;
            }
        });

        if (allValid) {
            const btn = form.querySelector('button[type="submit"]');
            btn.disabled = true;
            btn.textContent = 'Sending...';

            let actionUrl = form.action;
            // Force AJAX endpoint for FormSubmit to avoid CORS issues
            if (actionUrl.includes('formsubmit.co') && !actionUrl.includes('/ajax/')) {
                actionUrl = actionUrl.replace('formsubmit.co/', 'formsubmit.co/ajax/');
            }

            fetch(actionUrl, {
                method: 'POST',
                body: new FormData(form),
                headers: {
                    'Accept': 'application/json'
                }
            })
                .then(response => response.json())
                .then(data => {
                    // FormSubmit sometimes returns boolean, sometimes string "true" / "false"
                    if (data.success === true || data.success === "true") {
                        if (successMsg) successMsg.classList.add('show');
                        form.reset();
                    } else {
                        // This happens if FormSubmit rejects the AJAX request (e.g. localhost testing restrictions)
                        // We fall back to standard HTML submission when API fails
                        form.submit();
                    }
                })
                .catch(error => {
                    // Network error or CORS failure, fallback to native submission
                    form.submit();
                })
                .finally(() => {
                    btn.disabled = false;
                    btn.textContent = 'Send Message →';

                    if (successMsg) {
                        setTimeout(() => {
                            successMsg.classList.remove('show');
                        }, 5000);
                    }
                });
        }
    });
}
