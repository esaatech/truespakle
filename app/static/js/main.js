// Add your JavaScript code here
document.addEventListener('DOMContentLoaded', () => {
    console.log('Application loaded');

    // Google Analytics Section Tracking
    function trackSectionView(sectionId) {
        gtag('event', 'page_view', {
            page_title: 'TrueSparkles - ' + sectionId,
            page_path: '/#' + sectionId
        });
    }

    // Add tracking to navigation links
    const navLinks = document.querySelector('.nav-links');
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            const sectionId = link.getAttribute('href').substring(1);
            trackSectionView(sectionId);
            navLinks.classList.remove('active');
        });
    });

    // Track form submissions
    const contactForm = document.querySelector('form');
    if (contactForm) {
        contactForm.addEventListener('submit', function() {
            gtag('event', 'form_submission', {
                'form_name': 'contact_form',
                'form_type': 'contact'
            });
        });
    }

    // FAQ Accordion
    const faqItems = document.querySelectorAll('.faq-item');
    
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        
        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            
            // Close all FAQ items
            faqItems.forEach(faq => faq.classList.remove('active'));
            
            // Open clicked item if it wasn't active
            if (!isActive) {
                item.classList.add('active');
            }
        });
    });

    // Flash Messages Auto-dismiss
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 500);
        }, 5000);
    });

    // Navigation scroll effect
    const nav = document.querySelector('.main-nav');
    const navToggle = document.getElementById('navToggle');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    });

    // Mobile navigation toggle
    navToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });

    // Close mobile menu when clicking a link
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('active');
        });
    });
}); 