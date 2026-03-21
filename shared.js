// shared.js — inject nav, footer, sticky phone

const PHONE = "(603) 555-0192";
const PHONE_LINK = "tel:+16035550192";
const BUSINESS = "Plumbing HVAC Services New Hampshire";
const DOMAIN = "plumbinghvacservicesnewHampshire.com";

function injectTopBar() {
  return `<div class="top-bar">
    <div class="container">
      <div>📍 Serving All of New Hampshire | Licensed & Insured | 24/7 Emergency Service</div>
      <a href="${PHONE_LINK}" class="phone-cta">📞 Call Now: ${PHONE}</a>
    </div>
  </div>`;
}

function injectNav(activePage = '') {
  return `
  <nav class="main-nav">
    <div class="container nav-inner">
      <a href="/index.html" class="nav-logo">
        <div class="logo-icon">🔧</div>
        <div class="logo-text">
          <span class="line1">Plumbing HVAC Services</span>
          <span class="line2">New Hampshire</span>
        </div>
      </a>
      <button class="nav-toggle" onclick="document.querySelector('.nav-links').classList.toggle('open')">☰</button>
      <ul class="nav-links">
        <li><a href="/index.html" class="${activePage==='home'?'active':''}">Home</a></li>
        <li class="dropdown">
          <a href="/services/index.html" class="${activePage==='services'?'active':''}">Services ▾</a>
          <ul class="dropdown-menu">
            <li><a href="/services/plumbing-repair.html">Plumbing Repair</a></li>
            <li><a href="/services/drain-cleaning.html">Drain Cleaning</a></li>
            <li><a href="/services/water-heater.html">Water Heater Services</a></li>
            <li><a href="/services/pipe-installation.html">Pipe Installation & Repair</a></li>
            <li><a href="/services/sewer-line.html">Sewer Line Services</a></li>
            <li><a href="/services/hvac-installation.html">HVAC Installation</a></li>
            <li><a href="/services/hvac-repair.html">HVAC Repair & Maintenance</a></li>
            <li><a href="/services/ac-services.html">AC Services</a></li>
            <li><a href="/services/heating-services.html">Heating Services</a></li>
            <li><a href="/services/gas-line.html">Gas Line Services</a></li>
            <li><a href="/services/emergency-plumbing.html">Emergency Plumbing</a></li>
            <li><a href="/services/bathroom-remodeling.html">Bathroom Remodeling</a></li>
          </ul>
        </li>
        <li class="dropdown">
          <a href="/regions/index.html" class="${activePage==='regions'?'active':''}">Service Areas ▾</a>
          <ul class="dropdown-menu">
            <li><a href="/regions/manchester-nh.html">Manchester</a></li>
            <li><a href="/regions/nashua-nh.html">Nashua</a></li>
            <li><a href="/regions/concord-nh.html">Concord</a></li>
            <li><a href="/regions/dover-nh.html">Dover</a></li>
            <li><a href="/regions/rochester-nh.html">Rochester</a></li>
            <li><a href="/regions/portsmouth-nh.html">Portsmouth</a></li>
            <li><a href="/regions/keene-nh.html">Keene</a></li>
            <li><a href="/regions/derry-nh.html">Derry</a></li>
            <li><a href="/regions/laconia-nh.html">Laconia</a></li>
            <li><a href="/regions/bedford-nh.html">Bedford</a></li>
            <li><a href="/regions/index.html">All Areas →</a></li>
          </ul>
        </li>
        <li><a href="/blog/index.html" class="${activePage==='blog'?'active':''}">Blog</a></li>
        <li><a href="/about.html" class="${activePage==='about'?'active':''}">About</a></li>
        <li><a href="/contact.html" class="${activePage==='contact'?'active':''}">Contact</a></li>
        <li><a href="${PHONE_LINK}" class="nav-cta">📞 ${PHONE}</a></li>
      </ul>
    </div>
  </nav>`;
}

function injectFooter() {
  return `
  <footer class="main-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <span class="logo-text">🔧 Plumbing HVAC Services NH</span>
          <p>New Hampshire's trusted plumbing and HVAC experts. Licensed, insured, and available 24/7 for all your residential and commercial needs.</p>
          <a href="${PHONE_LINK}" class="footer-phone">📞 ${PHONE}</a>
        </div>
        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="/services/plumbing-repair.html">Plumbing Repair</a></li>
            <li><a href="/services/drain-cleaning.html">Drain Cleaning</a></li>
            <li><a href="/services/water-heater.html">Water Heater</a></li>
            <li><a href="/services/hvac-installation.html">HVAC Installation</a></li>
            <li><a href="/services/hvac-repair.html">HVAC Repair</a></li>
            <li><a href="/services/emergency-plumbing.html">Emergency Service</a></li>
            <li><a href="/services/sewer-line.html">Sewer Line</a></li>
            <li><a href="/services/gas-line.html">Gas Line</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Service Areas</h4>
          <ul>
            <li><a href="/regions/manchester-nh.html">Manchester, NH</a></li>
            <li><a href="/regions/nashua-nh.html">Nashua, NH</a></li>
            <li><a href="/regions/concord-nh.html">Concord, NH</a></li>
            <li><a href="/regions/dover-nh.html">Dover, NH</a></li>
            <li><a href="/regions/portsmouth-nh.html">Portsmouth, NH</a></li>
            <li><a href="/regions/keene-nh.html">Keene, NH</a></li>
            <li><a href="/regions/laconia-nh.html">Laconia, NH</a></li>
            <li><a href="/regions/index.html">All Areas →</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="/about.html">About Us</a></li>
            <li><a href="/blog/index.html">Blog</a></li>
            <li><a href="/contact.html">Contact</a></li>
            <li><a href="/legal/privacy-policy.html">Privacy Policy</a></li>
            <li><a href="/legal/terms-of-service.html">Terms of Service</a></li>
            <li><a href="/legal/sitemap.html">Sitemap</a></li>
            <li><a href="/legal/disclaimer.html">Disclaimer</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container">
        <p>© 2024 ${BUSINESS}. All rights reserved. Licensed & Insured in New Hampshire.
        <a href="/legal/privacy-policy.html">Privacy Policy</a>
        <a href="/legal/terms-of-service.html">Terms</a>
        <a href="/legal/sitemap.html">Sitemap</a>
        </p>
      </div>
    </div>
  </footer>
  <a href="${PHONE_LINK}" class="sticky-phone">📞 Call Now: ${PHONE}</a>
  <script>
    // FAQ accordion
    document.querySelectorAll('.faq-question').forEach(btn => {
      btn.addEventListener('click', function() {
        const answer = this.nextElementSibling;
        const isOpen = answer.classList.contains('open');
        document.querySelectorAll('.faq-answer').forEach(a => a.classList.remove('open'));
        document.querySelectorAll('.faq-question').forEach(b => b.classList.remove('open'));
        if (!isOpen) { answer.classList.add('open'); this.classList.add('open'); }
      });
    });
    // Dropdown on mobile tap
    document.querySelectorAll('.nav-links .dropdown > a').forEach(a => {
      a.addEventListener('click', function(e) {
        if (window.innerWidth <= 900) {
          e.preventDefault();
          this.parentElement.classList.toggle('open');
        }
      });
    });
  </script>`;
}

function sidebarCTA() {
  return `
  <aside>
    <div class="sidebar-cta-card">
      <h4>🚨 Need Help Now?</h4>
      <p>Our NH plumbers are on call 24/7 — even on holidays.</p>
      <a href="${PHONE_LINK}" class="cta-phone">📞 ${PHONE}</a>
      <small style="color:rgba(255,255,255,0.7);">Free Estimates Available</small>
    </div>
    <div class="sidebar-card">
      <h4>Our Services</h4>
      <ul class="sidebar-links">
        <li><a href="/services/plumbing-repair.html">Plumbing Repair</a></li>
        <li><a href="/services/drain-cleaning.html">Drain Cleaning</a></li>
        <li><a href="/services/water-heater.html">Water Heater Services</a></li>
        <li><a href="/services/pipe-installation.html">Pipe Installation</a></li>
        <li><a href="/services/sewer-line.html">Sewer Line Services</a></li>
        <li><a href="/services/hvac-installation.html">HVAC Installation</a></li>
        <li><a href="/services/hvac-repair.html">HVAC Repair</a></li>
        <li><a href="/services/ac-services.html">AC Services</a></li>
        <li><a href="/services/heating-services.html">Heating Services</a></li>
        <li><a href="/services/gas-line.html">Gas Line Services</a></li>
        <li><a href="/services/emergency-plumbing.html">Emergency Plumbing</a></li>
      </ul>
    </div>
    <div class="sidebar-card">
      <h4>Service Areas</h4>
      <ul class="sidebar-links">
        <li><a href="/regions/manchester-nh.html">Manchester</a></li>
        <li><a href="/regions/nashua-nh.html">Nashua</a></li>
        <li><a href="/regions/concord-nh.html">Concord</a></li>
        <li><a href="/regions/dover-nh.html">Dover</a></li>
        <li><a href="/regions/portsmouth-nh.html">Portsmouth</a></li>
        <li><a href="/regions/keene-nh.html">Keene</a></li>
        <li><a href="/regions/laconia-nh.html">Laconia</a></li>
        <li><a href="/regions/bedford-nh.html">Bedford</a></li>
        <li><a href="/regions/derry-nh.html">Derry</a></li>
        <li><a href="/regions/rochester-nh.html">Rochester</a></li>
      </ul>
    </div>
  </aside>`;
}
