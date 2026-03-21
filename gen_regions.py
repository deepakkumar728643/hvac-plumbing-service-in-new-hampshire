#!/usr/bin/env python3
"""Generate all NH region pages"""
import os

PHONE = "(603) 555-0192"
PHONE_LINK = "tel:+16035550192"

REGIONS = [
    {
        "file": "manchester-nh.html",
        "city": "Manchester",
        "county": "Hillsborough County",
        "slug": "manchester",
        "desc": "New Hampshire's largest city",
        "pop": "115,000+",
        "zip": "03101",
        "img": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80",
        "facts": "Manchester is the largest city in New Hampshire and a major commercial hub. With a mix of historic mill buildings, modern developments, and established residential neighborhoods, Manchester homes range from century-old triple-deckers to new construction.",
        "plumbing_note": "Older Manchester neighborhoods like Millyard, West Side, and South Manchester often have aging plumbing infrastructure including galvanized pipes and clay sewer lines that benefit from inspection and updates.",
    },
    {
        "file": "nashua-nh.html",
        "city": "Nashua",
        "county": "Hillsborough County",
        "slug": "nashua",
        "desc": "New Hampshire's second-largest city",
        "pop": "90,000+",
        "zip": "03060",
        "img": "https://images.unsplash.com/photo-1607472586893-edb57bdc0e39?w=800&q=80",
        "facts": "Nashua is NH's second-largest city and consistently ranked among the best places to live in the country. Its proximity to the Massachusetts border makes it a popular destination for commuters and families.",
        "plumbing_note": "Nashua's diverse housing stock — from older homes in the South End to newer construction in suburbs like Hollis Road — requires versatile plumbing expertise our team provides.",
    },
    {
        "file": "concord-nh.html",
        "city": "Concord",
        "county": "Merrimack County",
        "slug": "concord",
        "desc": "New Hampshire's state capital",
        "pop": "45,000+",
        "zip": "03301",
        "img": "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=800&q=80",
        "facts": "Concord is New Hampshire's state capital and home to the State House. The city's mix of government buildings, medical facilities, and established residential neighborhoods creates diverse plumbing and HVAC service needs.",
        "plumbing_note": "Many Concord homes were built in the early 1900s and still have original plumbing systems. We specialize in working on older homes while minimizing disruption to beautiful historic properties.",
    },
    {
        "file": "dover-nh.html",
        "city": "Dover",
        "county": "Strafford County",
        "slug": "dover",
        "desc": "New Hampshire's oldest city",
        "pop": "32,000+",
        "zip": "03820",
        "img": "https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=800&q=80",
        "facts": "Dover is New Hampshire's oldest city and a growing community in the Seacoast region. Its vibrant downtown, proximity to UNH, and growing residential base keep our plumbing and HVAC team busy year-round.",
        "plumbing_note": "Dover's Seacoast location and mix of historic and modern properties presents unique plumbing challenges our experienced team handles daily.",
    },
    {
        "file": "portsmouth-nh.html",
        "city": "Portsmouth",
        "county": "Rockingham County",
        "slug": "portsmouth",
        "desc": "NH Seacoast's premier city",
        "pop": "22,000+",
        "zip": "03801",
        "img": "https://images.unsplash.com/photo-1631069103703-4b5b7b3ef38f?w=800&q=80",
        "facts": "Portsmouth is one of New Hampshire's most historic and desirable cities, known for its maritime heritage, thriving dining scene, and beautiful 18th and 19th century architecture. Many Portsmouth properties are historic homes requiring specialized plumbing expertise.",
        "plumbing_note": "Portsmouth's historic homes require careful, experienced plumbing work that respects original architecture while meeting modern code requirements — exactly the kind of work our team excels at.",
    },
    {
        "file": "keene-nh.html",
        "city": "Keene",
        "county": "Cheshire County",
        "slug": "keene",
        "desc": "Southwest NH's largest city",
        "pop": "23,000+",
        "zip": "03431",
        "img": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80",
        "facts": "Keene serves as the commercial center of southwestern New Hampshire. Home to Keene State College, the city has a vibrant community of residents, businesses, and rental properties with active plumbing and HVAC needs.",
        "plumbing_note": "Keene's cold winters in the Monadnock Region mean frozen pipe prevention and heating system reliability are especially important for local homeowners and businesses.",
    },
    {
        "file": "rochester-nh.html",
        "city": "Rochester",
        "county": "Strafford County",
        "slug": "rochester",
        "desc": "Largest city in Strafford County",
        "pop": "32,000+",
        "zip": "03867",
        "img": "https://images.unsplash.com/photo-1607472586893-edb57bdc0e39?w=800&q=80",
        "facts": "Rochester is Strafford County's largest city and an important regional center in the Seacoast area. Its mix of residential neighborhoods, commercial districts, and growing industrial base creates diverse plumbing and HVAC service demand.",
        "plumbing_note": "Rochester's older residential core has many properties with aging plumbing that benefits from our inspection and upgrade services.",
    },
    {
        "file": "derry-nh.html",
        "city": "Derry",
        "county": "Rockingham County",
        "slug": "derry",
        "desc": "One of NH's fastest-growing communities",
        "pop": "34,000+",
        "zip": "03038",
        "img": "https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=800&q=80",
        "facts": "Derry is one of New Hampshire's largest and fastest-growing towns. Its excellent schools, proximity to Manchester, and strong residential base have made it a popular destination for families relocating to NH.",
        "plumbing_note": "Derry's rapid growth means both older established homes and new construction properties, and our team handles both with equal expertise.",
    },
    {
        "file": "laconia-nh.html",
        "city": "Laconia",
        "county": "Belknap County",
        "slug": "laconia",
        "desc": "Lakes Region hub city",
        "pop": "17,000+",
        "zip": "03246",
        "img": "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=800&q=80",
        "facts": "Laconia serves as the commercial center of New Hampshire's Lakes Region, bordered by Lake Winnipesaukee and Paugus Bay. The area has a significant seasonal and year-round residential base, with many lakefront properties and vacation homes.",
        "plumbing_note": "Laconia and the Lakes Region present unique plumbing challenges including seasonal home winterization, well pump services, and lakefront property plumbing that our team handles extensively.",
    },
    {
        "file": "bedford-nh.html",
        "city": "Bedford",
        "county": "Hillsborough County",
        "slug": "bedford",
        "desc": "Affluent Manchester suburb",
        "pop": "23,000+",
        "zip": "03110",
        "img": "https://images.unsplash.com/photo-1631069103703-4b5b7b3ef38f?w=800&q=80",
        "facts": "Bedford is one of New Hampshire's wealthiest communities and a highly sought-after suburb of Manchester. Known for excellent schools and upscale residential neighborhoods, Bedford homeowners expect the highest quality of service.",
        "plumbing_note": "Bedford's upscale properties often feature high-end fixtures, complex plumbing systems, and the expectation of premium service quality — standards our team consistently meets.",
    },
    {
        "file": "merrimack-nh.html",
        "city": "Merrimack",
        "county": "Hillsborough County",
        "slug": "merrimack",
        "desc": "Growing community near Nashua",
        "pop": "28,000+",
        "zip": "03054",
        "img": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80",
        "facts": "Merrimack is a rapidly growing town between Manchester and Nashua, home to Anheuser-Busch and a significant business park. Its growing population and mix of residential styles create consistent demand for professional plumbing and HVAC services.",
        "plumbing_note": "Merrimack's growth includes both established neighborhoods and new development, requiring expertise across older and modern plumbing systems.",
    },
    {
        "file": "hampton-nh.html",
        "city": "Hampton",
        "county": "Rockingham County",
        "slug": "hampton",
        "desc": "NH Seacoast beach community",
        "pop": "16,000+",
        "zip": "03842",
        "img": "https://images.unsplash.com/photo-1607472586893-edb57bdc0e39?w=800&q=80",
        "facts": "Hampton is New Hampshire's premier beach destination, home to Hampton Beach State Park and a significant year-round and seasonal residential population. Coastal properties have specific plumbing and HVAC needs.",
        "plumbing_note": "Hampton's coastal environment and seasonal properties require specialized expertise in winterization, corrosion prevention, and efficient systems for vacation homes.",
    },
    {
        "file": "exeter-nh.html",
        "city": "Exeter",
        "county": "Rockingham County",
        "slug": "exeter",
        "desc": "Historic Seacoast town",
        "pop": "15,000+",
        "zip": "03833",
        "img": "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=800&q=80",
        "facts": "Exeter is one of New Hampshire's most historic towns and home to Phillips Exeter Academy. The town's blend of historic homes, charming downtown, and growing residential areas creates steady demand for skilled plumbing and HVAC services.",
        "plumbing_note": "Exeter's many historic properties require careful, code-compliant plumbing work that preserves the character of these beautiful homes.",
    },
    {
        "file": "londonderry-nh.html",
        "city": "Londonderry",
        "county": "Rockingham County",
        "slug": "londonderry",
        "desc": "Growing Rockingham County town",
        "pop": "26,000+",
        "zip": "03053",
        "img": "https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=800&q=80",
        "facts": "Londonderry is a growing suburban community in Rockingham County, known for its apple orchards, excellent schools, and convenient location near Manchester-Boston Regional Airport.",
        "plumbing_note": "Londonderry's mix of established subdivisions and newer construction keeps our plumbing and HVAC team active year-round.",
    },
    {
        "file": "durham-nh.html",
        "city": "Durham",
        "county": "Strafford County",
        "slug": "durham",
        "desc": "Home of UNH",
        "pop": "15,000+",
        "zip": "03824",
        "img": "https://images.unsplash.com/photo-1631069103703-4b5b7b3ef38f?w=800&q=80",
        "facts": "Durham is home to the University of New Hampshire and has a vibrant college-town atmosphere. The mix of university facilities, student housing, and residential neighborhoods creates diverse plumbing and HVAC service needs.",
        "plumbing_note": "Durham's rental properties and student housing benefit from our responsive emergency plumbing services and HVAC maintenance programs.",
    },
]

def nav_region():
    return '''<div class="top-bar"><div class="container"><div>📍 Serving All of New Hampshire | Licensed &amp; Insured | 24/7 Emergency</div><a href="''' + PHONE_LINK + '''" class="phone-cta">📞 ''' + PHONE + '''</a></div></div>
<nav class="main-nav"><div class="container nav-inner"><a href="../index.html" class="nav-logo"><div class="logo-icon">🔧</div><div class="logo-text"><span class="line1">Plumbing HVAC Services</span><span class="line2">New Hampshire</span></div></a><button class="nav-toggle" onclick="document.querySelector('.nav-links').classList.toggle('open')">☰</button><ul class="nav-links"><li><a href="../index.html">Home</a></li><li class="dropdown"><a href="../services/index.html">Services ▾</a><ul class="dropdown-menu"><li><a href="../services/plumbing-repair.html">Plumbing Repair</a></li><li><a href="../services/drain-cleaning.html">Drain Cleaning</a></li><li><a href="../services/water-heater.html">Water Heater</a></li><li><a href="../services/hvac-installation.html">HVAC Installation</a></li><li><a href="../services/hvac-repair.html">HVAC Repair</a></li><li><a href="../services/emergency-plumbing.html">Emergency</a></li></ul></li><li class="dropdown"><a href="index.html" class="active">Service Areas ▾</a><ul class="dropdown-menu"><li><a href="manchester-nh.html">Manchester</a></li><li><a href="nashua-nh.html">Nashua</a></li><li><a href="concord-nh.html">Concord</a></li><li><a href="dover-nh.html">Dover</a></li><li><a href="portsmouth-nh.html">Portsmouth</a></li><li><a href="keene-nh.html">Keene</a></li><li><a href="index.html">All Areas →</a></li></ul></li><li><a href="../blog/index.html">Blog</a></li><li><a href="../about.html">About</a></li><li><a href="../contact.html">Contact</a></li><li><a href="''' + PHONE_LINK + '''" class="nav-cta">📞 ''' + PHONE + '''</a></li></ul></div></nav>'''

def footer_region():
    return '''<footer class="main-footer"><div class="container"><div class="footer-grid"><div class="footer-brand"><span class="logo-text">🔧 Plumbing HVAC Services NH</span><p>Licensed plumbing &amp; HVAC services across all of New Hampshire. 24/7 emergency response.</p><a href="''' + PHONE_LINK + '''" class="footer-phone">📞 ''' + PHONE + '''</a></div><div class="footer-col"><h4>Services</h4><ul><li><a href="../services/plumbing-repair.html">Plumbing Repair</a></li><li><a href="../services/drain-cleaning.html">Drain Cleaning</a></li><li><a href="../services/water-heater.html">Water Heater</a></li><li><a href="../services/hvac-installation.html">HVAC Installation</a></li><li><a href="../services/emergency-plumbing.html">Emergency</a></li></ul></div><div class="footer-col"><h4>Service Areas</h4><ul><li><a href="manchester-nh.html">Manchester</a></li><li><a href="nashua-nh.html">Nashua</a></li><li><a href="concord-nh.html">Concord</a></li><li><a href="dover-nh.html">Dover</a></li><li><a href="portsmouth-nh.html">Portsmouth</a></li><li><a href="index.html">All Areas →</a></li></ul></div><div class="footer-col"><h4>Company</h4><ul><li><a href="../about.html">About</a></li><li><a href="../contact.html">Contact</a></li><li><a href="../legal/privacy-policy.html">Privacy</a></li><li><a href="../legal/terms-of-service.html">Terms</a></li></ul></div></div></div><div class="footer-bottom"><div class="container"><p>© 2024 Plumbing HVAC Services New Hampshire. All rights reserved.</p></div></div></footer>
<a href="''' + PHONE_LINK + '''" class="sticky-phone">📞 ''' + PHONE + '''</a>
<script>document.querySelectorAll('.faq-question').forEach(b=>{b.addEventListener('click',function(){const a=this.nextElementSibling;const o=a.classList.contains('open');document.querySelectorAll('.faq-answer').forEach(x=>x.classList.remove('open'));document.querySelectorAll('.faq-question').forEach(x=>x.classList.remove('open'));if(!o){a.classList.add('open');this.classList.add('open');}});});document.querySelectorAll('.nav-links .dropdown > a').forEach(a=>{a.addEventListener('click',function(e){if(window.innerWidth<=900){e.preventDefault();this.parentElement.classList.toggle('open');}});});</script>'''

def region_sidebar(city):
    return f'''<aside>
    <div class="sidebar-cta-card"><h4>🚨 Need a Plumber in {city}?</h4><p>Licensed NH technicians on call 24/7. Fast response in {city}.</p><a href="{PHONE_LINK}" class="cta-phone">📞 {PHONE}</a><small style="color:rgba(255,255,255,0.7)">Free Estimates Available</small></div>
    <div class="sidebar-card"><h4>Services in {city}</h4><ul class="sidebar-links"><li><a href="../services/plumbing-repair.html">Plumbing Repair</a></li><li><a href="../services/drain-cleaning.html">Drain Cleaning</a></li><li><a href="../services/water-heater.html">Water Heater</a></li><li><a href="../services/pipe-installation.html">Pipe Installation</a></li><li><a href="../services/sewer-line.html">Sewer Line</a></li><li><a href="../services/hvac-installation.html">HVAC Installation</a></li><li><a href="../services/hvac-repair.html">HVAC Repair</a></li><li><a href="../services/ac-services.html">AC Services</a></li><li><a href="../services/heating-services.html">Heating Services</a></li><li><a href="../services/emergency-plumbing.html">Emergency Plumbing</a></li></ul></div>
    <div class="sidebar-card"><h4>Nearby Areas</h4><ul class="sidebar-links"><li><a href="manchester-nh.html">Manchester</a></li><li><a href="nashua-nh.html">Nashua</a></li><li><a href="concord-nh.html">Concord</a></li><li><a href="dover-nh.html">Dover</a></li><li><a href="portsmouth-nh.html">Portsmouth</a></li><li><a href="index.html">All NH Areas →</a></li></ul></div>
    </aside>'''

def generate_region(r):
    city = r["city"]
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Plumbing &amp; HVAC Services in {city}, NH | Licensed {city} Plumber</title>
  <meta name="description" content="Professional plumbing and HVAC services in {city}, NH. Licensed {city} plumbers for drain cleaning, water heater, pipe repair, HVAC installation & emergency service. Call (603) 555-0192." />
  <link rel="canonical" href="https://plumbinghvacservicesnewHampshire.com/regions/{r['file']}" />
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"Plumber","name":"Plumbing HVAC Services New Hampshire — {city}","telephone":"+16035550192","description":"Licensed plumbing and HVAC services in {city}, NH.","areaServed":{{"@type":"City","name":"{city}","containedIn":{{"@type":"State","name":"New Hampshire"}}}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"348"}}}}</script>
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>
{nav_region()}
<div class="page-hero">
  <div class="container">
    <span class="badge">📍 {city}, NH</span>
    <h1>Plumbing &amp; HVAC Services in {city}, New Hampshire</h1>
    <p>Licensed, insured plumbers and HVAC technicians serving {city} and {r["county"]}. Same-day service, 24/7 emergency response, and free estimates on all major work.</p>
    <div style="margin-top:24px;display:flex;gap:14px;flex-wrap:wrap;">
      <a href="tel:+16035550192" class="btn-primary">📞 Call {PHONE} Now</a>
      <a href="../contact.html" class="btn-secondary">Get Free Estimate</a>
    </div>
    <div class="hero-trust" style="margin-top:28px;padding-top:24px;border-top:1px solid rgba(255,255,255,0.15);">
      <div class="trust-item"><span class="num">24/7</span><span class="label">Emergency Service</span></div>
      <div class="trust-item"><span class="num">4.9★</span><span class="label">Google Rating</span></div>
      <div class="trust-item"><span class="num">60min</span><span class="label">Emergency ETA</span></div>
      <div class="trust-item"><span class="num">Free</span><span class="label">Estimates</span></div>
    </div>
  </div>
</div>
<div class="breadcrumb"><div class="container"><a href="../index.html">Home</a> <span>›</span> <a href="index.html">Service Areas</a> <span>›</span> {city}, NH</div></div>

<section class="section">
  <div class="container">
    <div class="content-layout">
      <article class="content-body">
        <h2>Your Local Plumber &amp; HVAC Contractor in {city}, NH</h2>
        <p>{r["facts"]} Whether you need an emergency plumber at 2 AM or a planned HVAC installation, <strong>Plumbing HVAC Services New Hampshire</strong> is your trusted local partner in {city}.</p>
        <p>{r["plumbing_note"]} Our licensed technicians are familiar with local building codes, permit requirements, and the specific challenges {city} homeowners face.</p>
        <img src="{r["img"]}" alt="Plumbing and HVAC services in {city}, New Hampshire" loading="lazy" />
        
        <h2>Plumbing Services We Offer in {city}, NH</h2>
        <p>Our {city} plumbers handle every type of residential and commercial plumbing service:</p>
        <ul>
          <li><a href="../services/plumbing-repair.html">Plumbing repair</a> — leaks, burst pipes, faucets, toilets</li>
          <li><a href="../services/drain-cleaning.html">Drain cleaning</a> — clogged drains, hydro-jetting, main line clearing</li>
          <li><a href="../services/water-heater.html">Water heater installation &amp; repair</a> — tank, tankless, heat pump</li>
          <li><a href="../services/pipe-installation.html">Pipe installation &amp; repiping</a> — copper, PEX, PVC</li>
          <li><a href="../services/sewer-line.html">Sewer line services</a> — camera inspection, repair, replacement</li>
          <li><a href="../services/gas-line.html">Gas line installation &amp; repair</a> — licensed NH gas fitter</li>
          <li><a href="../services/bathroom-remodeling.html">Bathroom plumbing</a> — remodels, new fixtures, rough-in</li>
          <li><a href="../services/emergency-plumbing.html">24/7 emergency plumbing</a> in {city}</li>
        </ul>

        <h2>HVAC Services in {city}, New Hampshire</h2>
        <p>From sweltering NH summers to frigid winters, we keep {city} homes and businesses comfortable year-round:</p>
        <ul>
          <li><a href="../services/hvac-installation.html">HVAC system installation</a> — furnace, AC, heat pump, mini-splits</li>
          <li><a href="../services/hvac-repair.html">HVAC repair &amp; maintenance</a> — all makes and models</li>
          <li><a href="../services/ac-services.html">Air conditioning services</a> — repair, tune-up, installation</li>
          <li><a href="../services/heating-services.html">Heating services</a> — furnace, boiler, heat pump repair</li>
          <li>24/7 emergency HVAC repair in {city}</li>
        </ul>
        
        <div style="background:linear-gradient(135deg,var(--accent),#c4320a);border-radius:12px;padding:32px;text-align:center;margin:32px 0;">
          <h3 style="color:#fff;margin-bottom:8px;">Need a Plumber or HVAC Tech in {city} Today?</h3>
          <p style="color:rgba(255,255,255,0.88)">Same-day and emergency service available in {city}, NH.</p>
          <a href="tel:+16035550192" style="display:inline-flex;align-items:center;gap:8px;background:#fff;color:var(--accent);font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:1.4rem;padding:14px 32px;border-radius:8px;margin-top:12px;">📞 {PHONE}</a>
        </div>
        
        <h2>Why {city} Homeowners Choose Plumbing HVAC Services NH</h2>
        <ul>
          <li><strong>Licensed &amp; Insured:</strong> Fully licensed plumbers and HVAC contractors in the state of New Hampshire</li>
          <li><strong>Local Knowledge:</strong> We know {city}'s building codes, local permit requirements, and common plumbing challenges</li>
          <li><strong>Fast Response:</strong> Average 60-minute emergency response to {city} addresses</li>
          <li><strong>Transparent Pricing:</strong> Written estimates before work begins — no surprises on your {city} service call</li>
          <li><strong>Satisfaction Guarantee:</strong> 100% satisfaction on all work performed in {city}</li>
        </ul>
        
        <h2>Frequently Asked Questions — Plumbing &amp; HVAC in {city}, NH</h2>
        <div>
          <div class="faq-item"><button class="faq-question">Do you offer 24/7 emergency plumbing in {city}, NH? <span class="icon">+</span></button><div class="faq-answer"><p>Yes. We provide around-the-clock emergency plumbing in {city}. Call (603) 555-0192 any time, day or night, and we'll dispatch a licensed NH plumber to your {city} address. We target a 60-minute arrival time.</p></div></div>
          <div class="faq-item"><button class="faq-question">Are your {city} plumbers licensed in New Hampshire? <span class="icon">+</span></button><div class="faq-answer"><p>Absolutely. All technicians serving {city} are licensed by the state of New Hampshire, fully insured, and background-checked. We carry all required permits for work in {r["county"]}.</p></div></div>
          <div class="faq-item"><button class="faq-question">How quickly can a plumber get to my {city} home? <span class="icon">+</span></button><div class="faq-answer"><p>For emergencies, our average response time in {city} is under 60 minutes. For scheduled appointments, we offer same-day or next-day service in most cases. We provide a narrow arrival window and always call ahead.</p></div></div>
          <div class="faq-item"><button class="faq-question">Do you offer free estimates in {city}? <span class="icon">+</span></button><div class="faq-answer"><p>Yes. We offer free estimates on all major plumbing and HVAC projects in {city}. Call (603) 555-0192 or use our contact form to schedule your free assessment.</p></div></div>
        </div>
        
        <h2>Other NH Areas We Serve Near {city}</h2>
        <p>In addition to {city}, we serve all surrounding communities in {r["county"]} and throughout New Hampshire. <a href="index.html">View our full service area list →</a></p>
      </article>
      {region_sidebar(city)}
    </div>
  </div>
</section>
{footer_region()}
</body></html>'''

os.makedirs("/home/claude/plumbing-hvac-nh/regions", exist_ok=True)
for r in REGIONS:
    path = f"/home/claude/plumbing-hvac-nh/regions/{r['file']}"
    with open(path, "w") as f:
        f.write(generate_region(r))
    print(f"Created: {r['file']}")

print(f"\nGenerated {len(REGIONS)} region pages!")
