// ============================================
// SHARED COMPONENTS - header & footer
// ============================================

const PHONE = '(603) 555-0100';
const PHONE_HREF = 'tel:6035550100';
const BUSINESS = 'Plumbing HVAC Services New Hampshire';
const TAGLINE = 'NH\'s #1 Plumbing & HVAC Experts';

function renderHeader(activePage = '') {
  return `
  <div class="top-bar">
    <div class="container">
      <span>📍 Serving All of New Hampshire — Licensed & Insured</span>
      <span>🕐 24/7 Emergency Service Available &nbsp;|&nbsp; <a href="${PHONE_HREF}">${PHONE}</a></span>
    </div>
  </div>
  <header>
    <div class="container">
      <div class="header-inner">
        <a href="/index.html" class="logo">
          <div class="logo-icon">🔧</div>
          <div class="logo-text">
            <strong>Plumbing HVAC NH</strong>
            <span>New Hampshire's Trusted Experts</span>
          </div>
        </a>
        <nav>
          <a href="/index.html" ${activePage==='home'?'class="active"':''}>Home</a>
          <div class="dropdown">
            <a href="/pages/services/">Services</a>
            <div class="dropdown-menu wide">
              <a href="/pages/services/plumbing-repair.html">🔧 Plumbing Repair</a>
              <a href="/pages/services/drain-cleaning.html">🚿 Drain Cleaning</a>
              <a href="/pages/services/water-heater.html">🌡️ Water Heater</a>
              <a href="/pages/services/leak-detection.html">💧 Leak Detection</a>
              <a href="/pages/services/sewer-line.html">🏗️ Sewer Line</a>
              <a href="/pages/services/toilet-repair.html">🚽 Toilet Repair</a>
              <a href="/pages/services/pipe-repair.html">🔩 Pipe Repair</a>
              <a href="/pages/services/hvac-installation.html">❄️ HVAC Installation</a>
              <a href="/pages/services/ac-repair.html">🌬️ AC Repair</a>
              <a href="/pages/services/furnace-repair.html">🔥 Furnace Repair</a>
              <a href="/pages/services/emergency-plumbing.html">🚨 Emergency Plumbing</a>
              <a href="/pages/services/gas-line.html">⚠️ Gas Line Services</a>
            </div>
          </div>
          <div class="dropdown">
            <a href="/pages/regions/">Service Areas</a>
            <div class="dropdown-menu wide">
              <a href="/pages/regions/manchester.html">Manchester</a>
              <a href="/pages/regions/nashua.html">Nashua</a>
              <a href="/pages/regions/concord.html">Concord</a>
              <a href="/pages/regions/derry.html">Derry</a>
              <a href="/pages/regions/dover.html">Dover</a>
              <a href="/pages/regions/rochester.html">Rochester</a>
              <a href="/pages/regions/salem.html">Salem</a>
              <a href="/pages/regions/merrimack.html">Merrimack</a>
              <a href="/pages/regions/hudson.html">Hudson</a>
              <a href="/pages/regions/londonderry.html">Londonderry</a>
              <a href="/pages/regions/portsmouth.html">Portsmouth</a>
              <a href="/pages/regions/laconia.html">Laconia</a>
            </div>
          </div>
          <a href="/pages/blog/">Blog</a>
          <a href="/pages/about.html">About</a>
          <a href="/pages/contact.html">Contact</a>
        </nav>
        <a href="${PHONE_HREF}" class="btn-call-header">📞 ${PHONE}</a>
        <div class="hamburger" aria-label="Menu">
          <span></span><span></span><span></span>
        </div>
      </div>
    </div>
  </header>`;
}

function renderFooter() {
  return `
  <footer>
    <div class="footer-top">
      <div class="container">
        <div class="footer-grid">
          <div class="footer-brand">
            <div class="logo">
              <div class="logo-icon">🔧</div>
              <div class="logo-text">
                <strong>Plumbing HVAC NH</strong>
                <span>New Hampshire's Trusted Experts</span>
              </div>
            </div>
            <p>Licensed, bonded & insured plumbing and HVAC company serving all of New Hampshire. Available 24/7 for emergencies. Over 15 years of trusted service across NH communities.</p>
            <div class="footer-contact-item">📞 <a href="${PHONE_HREF}">${PHONE}</a></div>
            <div class="footer-contact-item">📧 <a href="mailto:info@plumbinghvacnh.com">info@plumbinghvacnh.com</a></div>
            <div class="footer-contact-item">📍 Serving All of New Hampshire</div>
            <div class="license-badges" style="margin-top:14px;">
              <span class="badge">✓ Licensed</span>
              <span class="badge">✓ Insured</span>
              <span class="badge">✓ BBB A+</span>
            </div>
          </div>
          <div class="footer-col">
            <h4>Our Services</h4>
            <ul>
              <li><a href="/pages/services/plumbing-repair.html">Plumbing Repair</a></li>
              <li><a href="/pages/services/drain-cleaning.html">Drain Cleaning</a></li>
              <li><a href="/pages/services/water-heater.html">Water Heater</a></li>
              <li><a href="/pages/services/leak-detection.html">Leak Detection</a></li>
              <li><a href="/pages/services/sewer-line.html">Sewer Line</a></li>
              <li><a href="/pages/services/hvac-installation.html">HVAC Installation</a></li>
              <li><a href="/pages/services/ac-repair.html">AC Repair</a></li>
              <li><a href="/pages/services/furnace-repair.html">Furnace Repair</a></li>
              <li><a href="/pages/services/emergency-plumbing.html">Emergency Service</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Service Areas</h4>
            <ul>
              <li><a href="/pages/regions/manchester.html">Manchester</a></li>
              <li><a href="/pages/regions/nashua.html">Nashua</a></li>
              <li><a href="/pages/regions/concord.html">Concord</a></li>
              <li><a href="/pages/regions/derry.html">Derry</a></li>
              <li><a href="/pages/regions/dover.html">Dover</a></li>
              <li><a href="/pages/regions/portsmouth.html">Portsmouth</a></li>
              <li><a href="/pages/regions/rochester.html">Rochester</a></li>
              <li><a href="/pages/regions/salem.html">Salem</a></li>
              <li><a href="/pages/regions/">All Areas →</a></li>
            </ul>
          </div>
          <div class="footer-col">
            <h4>Company</h4>
            <ul>
              <li><a href="/pages/about.html">About Us</a></li>
              <li><a href="/pages/blog/">Blog</a></li>
              <li><a href="/pages/contact.html">Contact</a></li>
              <li><a href="/pages/legal/privacy-policy.html">Privacy Policy</a></li>
              <li><a href="/pages/legal/terms-of-service.html">Terms of Service</a></li>
              <li><a href="/pages/legal/disclaimer.html">Disclaimer</a></li>
              <li><a href="/pages/sitemap.html">Sitemap</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="footer-bottom">
        <span>© 2024 Plumbing HVAC Services New Hampshire. All rights reserved.</span>
        <span>NH Plumbing License #XXXX | HVAC Lic. #XXXX</span>
      </div>
    </div>
  </footer>
  <div class="sticky-call">
    <a href="${PHONE_HREF}">📞 Call Now for FREE Estimate: ${PHONE}</a>
  </div>`;
}

if (typeof module !== 'undefined') module.exports = { renderHeader, renderFooter };
