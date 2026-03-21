/* ============================================================
   PLUMBING HVAC SERVICES NH — MAIN JS
   ============================================================ */

(function () {
  'use strict';

  /* ── Mobile Navigation ───────────────────────────────────── */
  function initMobileNav() {
    const toggleBtns = document.querySelectorAll('.nav-toggle');
    const navLinks   = document.querySelector('.nav-links');
    if (!navLinks) return;

    toggleBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        navLinks.classList.toggle('open');
        btn.setAttribute('aria-expanded', navLinks.classList.contains('open'));
      });
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
      if (!e.target.closest('nav.main-nav')) {
        navLinks.classList.remove('open');
      }
    });

    // Mobile dropdown toggles
    document.querySelectorAll('.nav-links .dropdown > a').forEach(a => {
      a.addEventListener('click', function (e) {
        if (window.innerWidth <= 900) {
          e.preventDefault();
          const parent = this.parentElement;
          // Close others
          document.querySelectorAll('.nav-links .dropdown.open').forEach(d => {
            if (d !== parent) d.classList.remove('open');
          });
          parent.classList.toggle('open');
        }
      });
    });
  }

  /* ── FAQ Accordion ───────────────────────────────────────── */
  function initFAQ() {
    document.querySelectorAll('.faq-question').forEach(btn => {
      btn.addEventListener('click', function () {
        const answer = this.nextElementSibling;
        const isOpen = answer && answer.classList.contains('open');

        // Close all
        document.querySelectorAll('.faq-answer.open').forEach(a => a.classList.remove('open'));
        document.querySelectorAll('.faq-question.open').forEach(b => b.classList.remove('open'));

        // Open clicked (if it was closed)
        if (!isOpen && answer) {
          answer.classList.add('open');
          this.classList.add('open');
        }
      });
    });
  }

  /* ── Contact Form Submit ─────────────────────────────────── */
  function initContactForm() {
    const submitBtn = document.querySelector('#contactForm .form-submit, .form-submit');
    const successMsg = document.getElementById('successMsg');
    if (!submitBtn || !successMsg) return;

    submitBtn.addEventListener('click', function (e) {
      e.preventDefault();
      successMsg.style.display = 'block';
      successMsg.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });
  }

  /* ── Lead Form (Hero) ────────────────────────────────────── */
  function initLeadForm() {
    const form = document.querySelector('.lead-form');
    if (!form) return;
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      alert('Thank you! We\'ll call you within 30 minutes.\n\nFor immediate help: (603) 555-0100');
    });
  }

  /* ── Sticky Phone Visibility ─────────────────────────────── */
  function initStickyPhone() {
    const sticky = document.querySelector('.sticky-phone');
    if (!sticky) return;
    // Show after user scrolls 300px
    window.addEventListener('scroll', () => {
      sticky.style.opacity = window.scrollY > 300 ? '1' : '0';
      sticky.style.pointerEvents = window.scrollY > 300 ? 'auto' : 'none';
    }, { passive: true });
  }

  /* ── Smooth anchor scroll offset fix ────────────────────── */
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(a => {
      a.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          e.preventDefault();
          const navH = document.querySelector('nav.main-nav')?.offsetHeight || 72;
          const top = target.getBoundingClientRect().top + window.scrollY - navH - 12;
          window.scrollTo({ top, behavior: 'smooth' });
        }
      });
    });
  }

  /* ── Init ────────────────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', () => {
    initMobileNav();
    initFAQ();
    initContactForm();
    initLeadForm();
    initStickyPhone();
    initSmoothScroll();
  });

})();
