#!/usr/bin/env python3
"""Generate all service pages for NH Plumbing HVAC website"""

import os

PHONE = "(603) 555-0192"
PHONE_LINK = "tel:+16035550192"

def nav(active="services"):
    return '''<div class="top-bar"><div class="container"><div>📍 Serving All of New Hampshire | Licensed &amp; Insured | 24/7 Emergency</div><a href="''' + PHONE_LINK + '''" class="phone-cta">📞 ''' + PHONE + '''</a></div></div>
<nav class="main-nav"><div class="container nav-inner"><a href="../index.html" class="nav-logo"><div class="logo-icon">🔧</div><div class="logo-text"><span class="line1">Plumbing HVAC Services</span><span class="line2">New Hampshire</span></div></a><button class="nav-toggle" onclick="document.querySelector('.nav-links').classList.toggle('open')">☰</button><ul class="nav-links"><li><a href="../index.html">Home</a></li><li class="dropdown"><a href="index.html" class="active">Services ▾</a><ul class="dropdown-menu"><li><a href="plumbing-repair.html">Plumbing Repair</a></li><li><a href="drain-cleaning.html">Drain Cleaning</a></li><li><a href="water-heater.html">Water Heater</a></li><li><a href="pipe-installation.html">Pipe Installation</a></li><li><a href="sewer-line.html">Sewer Line</a></li><li><a href="hvac-installation.html">HVAC Installation</a></li><li><a href="hvac-repair.html">HVAC Repair</a></li><li><a href="ac-services.html">AC Services</a></li><li><a href="heating-services.html">Heating Services</a></li><li><a href="gas-line.html">Gas Line</a></li><li><a href="emergency-plumbing.html">Emergency Plumbing</a></li><li><a href="bathroom-remodeling.html">Bathroom Remodeling</a></li></ul></li><li class="dropdown"><a href="../regions/index.html">Service Areas ▾</a><ul class="dropdown-menu"><li><a href="../regions/manchester-nh.html">Manchester</a></li><li><a href="../regions/nashua-nh.html">Nashua</a></li><li><a href="../regions/concord-nh.html">Concord</a></li><li><a href="../regions/dover-nh.html">Dover</a></li><li><a href="../regions/portsmouth-nh.html">Portsmouth</a></li></ul></li><li><a href="../blog/index.html">Blog</a></li><li><a href="../about.html">About</a></li><li><a href="../contact.html">Contact</a></li><li><a href="''' + PHONE_LINK + '''" class="nav-cta">📞 ''' + PHONE + '''</a></li></ul></div></nav>'''

def footer():
    return '''<footer class="main-footer"><div class="container"><div class="footer-grid"><div class="footer-brand"><span class="logo-text">🔧 Plumbing HVAC Services NH</span><p>Licensed plumbing &amp; HVAC services across New Hampshire. 24/7 emergency response statewide.</p><a href="''' + PHONE_LINK + '''" class="footer-phone">📞 ''' + PHONE + '''</a></div><div class="footer-col"><h4>Services</h4><ul><li><a href="plumbing-repair.html">Plumbing Repair</a></li><li><a href="drain-cleaning.html">Drain Cleaning</a></li><li><a href="water-heater.html">Water Heater</a></li><li><a href="hvac-installation.html">HVAC Installation</a></li><li><a href="hvac-repair.html">HVAC Repair</a></li><li><a href="emergency-plumbing.html">Emergency</a></li></ul></div><div class="footer-col"><h4>Areas</h4><ul><li><a href="../regions/manchester-nh.html">Manchester</a></li><li><a href="../regions/nashua-nh.html">Nashua</a></li><li><a href="../regions/concord-nh.html">Concord</a></li><li><a href="../regions/dover-nh.html">Dover</a></li><li><a href="../regions/portsmouth-nh.html">Portsmouth</a></li></ul></div><div class="footer-col"><h4>Company</h4><ul><li><a href="../about.html">About</a></li><li><a href="../contact.html">Contact</a></li><li><a href="../legal/privacy-policy.html">Privacy</a></li><li><a href="../legal/terms-of-service.html">Terms</a></li><li><a href="../legal/sitemap.html">Sitemap</a></li></ul></div></div></div><div class="footer-bottom"><div class="container"><p>© 2024 Plumbing HVAC Services New Hampshire. All rights reserved.</p></div></div></footer>
<a href="''' + PHONE_LINK + '''" class="sticky-phone">📞 ''' + PHONE + '''</a>
<script>document.querySelectorAll('.faq-question').forEach(b=>{b.addEventListener('click',function(){const a=this.nextElementSibling;const o=a.classList.contains('open');document.querySelectorAll('.faq-answer').forEach(x=>x.classList.remove('open'));document.querySelectorAll('.faq-question').forEach(x=>x.classList.remove('open'));if(!o){a.classList.add('open');this.classList.add('open');}});});document.querySelectorAll('.nav-links .dropdown > a').forEach(a=>{a.addEventListener('click',function(e){if(window.innerWidth<=900){e.preventDefault();this.parentElement.classList.toggle('open');}});});</script>'''

def sidebar():
    return '''<aside>
    <div class="sidebar-cta-card"><h4>🚨 Need Help Now?</h4><p>Our NH plumbers are on call 24/7.</p><a href="''' + PHONE_LINK + '''" class="cta-phone">📞 ''' + PHONE + '''</a><small style="color:rgba(255,255,255,0.7)">Free Estimates Available</small></div>
    <div class="sidebar-card"><h4>All Services</h4><ul class="sidebar-links"><li><a href="plumbing-repair.html">Plumbing Repair</a></li><li><a href="drain-cleaning.html">Drain Cleaning</a></li><li><a href="water-heater.html">Water Heater</a></li><li><a href="pipe-installation.html">Pipe Installation</a></li><li><a href="sewer-line.html">Sewer Line</a></li><li><a href="hvac-installation.html">HVAC Installation</a></li><li><a href="hvac-repair.html">HVAC Repair</a></li><li><a href="ac-services.html">AC Services</a></li><li><a href="heating-services.html">Heating Services</a></li><li><a href="gas-line.html">Gas Line</a></li><li><a href="emergency-plumbing.html">Emergency Plumbing</a></li><li><a href="bathroom-remodeling.html">Bathroom Remodeling</a></li></ul></div>
    <div class="sidebar-card"><h4>Service Areas</h4><ul class="sidebar-links"><li><a href="../regions/manchester-nh.html">Manchester</a></li><li><a href="../regions/nashua-nh.html">Nashua</a></li><li><a href="../regions/concord-nh.html">Concord</a></li><li><a href="../regions/dover-nh.html">Dover</a></li><li><a href="../regions/portsmouth-nh.html">Portsmouth</a></li><li><a href="../regions/keene-nh.html">Keene</a></li><li><a href="../regions/laconia-nh.html">Laconia</a></li><li><a href="../regions/index.html">All Areas →</a></li></ul></div>
    </aside>'''

SERVICES = [
    {
        "file": "plumbing-repair.html",
        "title": "Plumbing Repair Services in New Hampshire",
        "meta_desc": "Expert plumbing repair services in New Hampshire. Leaky pipes, burst pipes, faucet repair, toilet repair & more. Licensed NH plumbers available 24/7. Call (603) 555-0192.",
        "h1": "Plumbing Repair Services in New Hampshire",
        "badge": "Plumbing Repair",
        "hero_desc": "Fast, reliable plumbing repair services for homes and businesses across New Hampshire. Licensed plumbers, upfront pricing, 24/7 availability.",
        "img": "https://images.unsplash.com/photo-1607472586893-edb57bdc0e39?w=800&q=80",
        "img_alt": "Licensed plumber repairing pipes in New Hampshire home",
        "intro": """<p>When a plumbing problem strikes your New Hampshire home or business, you need a licensed, experienced plumber who can respond quickly, diagnose accurately, and fix it right the first time. <strong>Plumbing HVAC Services New Hampshire</strong> provides comprehensive plumbing repair services throughout Manchester, Nashua, Concord, Dover, Portsmouth, and every community in the Granite State.</p>
        <p>Our licensed NH plumbers are equipped with modern diagnostic tools and carry a full inventory of parts so most repairs are completed in a single visit. We don't charge extra for nights, weekends, or holiday emergency calls.</p>""",
        "services_list": ["Leaky faucet repair (kitchen, bathroom, outdoor)", "Burst and frozen pipe repair", "Running toilet repair and tank rebuilds", "Pipe joint and fitting leaks", "Valve replacement and shutoff repairs", "Water pressure problems", "Garbage disposal repair and installation", "Sump pump repair and replacement", "Hose bib and outdoor spigot repair", "Under-sink plumbing repair", "Bathroom and kitchen fixture repair", "Whole-home repiping"],
        "why_h": "Why Choose Our NH Plumbers for Repairs?",
        "why_body": """<p>We understand that plumbing problems are stressful, disruptive, and often urgent. Our approach prioritizes speed, accuracy, and transparent communication every step of the way.</p>
        <ul><li><strong>Licensed & Insured:</strong> Every technician holds a valid New Hampshire plumbing license and we carry full liability insurance.</li>
        <li><strong>Upfront Pricing:</strong> We provide a written quote before any work starts. No hourly surprises, no hidden fees.</li>
        <li><strong>Warrantied Work:</strong> All repairs come with a workmanship warranty so you have peace of mind long after we leave.</li>
        <li><strong>Same-Day Availability:</strong> We offer same-day and next-day appointments across all NH service areas for non-emergency repairs.</li></ul>""",
        "faqs": [
            ("How quickly can a plumber come for an emergency repair in NH?", "For emergencies like burst pipes or major leaks, we aim to arrive within 60 minutes across most New Hampshire service areas. Call (603) 555-0192 for immediate dispatch."),
            ("Do you repair plumbing in older New Hampshire homes?", "Yes. We regularly work on older NH homes with galvanized, lead, or cast iron pipes. We assess the condition and recommend repair vs. repiping based on what's most cost-effective for you."),
            ("How much does plumbing repair cost in New Hampshire?", "Minor repairs like fixing a leaky faucet start around $75–$150. More complex repairs like pipe replacement vary widely. We always provide a free written estimate before beginning work."),
        ],
        "schema_type": "PlumbingService",
        "keyword": "plumbing repair New Hampshire",
    },
    {
        "file": "drain-cleaning.html",
        "title": "Drain Cleaning Services in New Hampshire | Professional NH Drain Cleaner",
        "meta_desc": "Professional drain cleaning services in New Hampshire. Hydro-jetting, snaking, and camera inspection for clogged drains. Same-day service. Call (603) 555-0192.",
        "h1": "Drain Cleaning Services in New Hampshire",
        "badge": "Drain Cleaning",
        "hero_desc": "Clogged drains cleared fast by licensed New Hampshire plumbers. Hydro-jetting, drain snaking, and preventive maintenance across all NH areas.",
        "img": "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=800&q=80",
        "img_alt": "Professional drain cleaning service in New Hampshire",
        "intro": """<p>A clogged drain is more than an inconvenience — it can indicate a deeper issue with your plumbing system. <strong>Plumbing HVAC Services New Hampshire</strong> offers professional drain cleaning and clearing for residential and commercial properties across all of New Hampshire.</p>
        <p>We use state-of-the-art hydro-jetting equipment and professional drain snakes to clear blockages fast, plus drain cameras to identify the root cause and prevent future clogs.</p>""",
        "services_list": ["Kitchen sink drain cleaning", "Bathroom sink & shower drain clearing", "Toilet drain clearing", "Floor drain cleaning", "Main sewer line cleaning", "Hydro-jetting for stubborn blockages", "Root intrusion removal", "Grease buildup removal (commercial)", "Drain camera inspection", "Preventive drain maintenance programs", "Slow drain diagnosis & repair", "Storm drain cleaning"],
        "why_h": "Professional Drain Cleaning vs. Store-Bought Solutions",
        "why_body": """<p>Liquid drain cleaners from the hardware store are a temporary fix at best. They can damage older pipes and rarely remove the full blockage. Our professional drain cleaning methods completely clear the line and address the underlying cause.</p>
        <ul><li><strong>Hydro-Jetting:</strong> Uses high-pressure water to scour drain walls clean — removes grease, scale, and root intrusion.</li>
        <li><strong>Professional Snaking:</strong> Our motorized drain snakes reach deep into lines that consumer tools can't access.</li>
        <li><strong>Camera Inspection:</strong> We see exactly what's causing the problem before and after cleaning to confirm complete clearance.</li>
        <li><strong>Long-Lasting Results:</strong> Professional cleaning lasts significantly longer than chemical treatments.</li></ul>""",
        "faqs": [
            ("How do I know if I need professional drain cleaning in my NH home?", "Signs include slow drainage in multiple fixtures, gurgling sounds, recurring clogs, sewage odors, or water backing up in sinks or toilets. These often indicate a deeper blockage that needs professional clearing."),
            ("Is hydro-jetting safe for older pipes?", "Hydro-jetting is safe for most pipe materials including PVC, copper, and cast iron when performed at appropriate pressure. Our technicians assess your pipe condition before recommending the right method."),
            ("How often should I have my drains professionally cleaned?", "We recommend annual drain cleaning for most NH homes, and quarterly for restaurants and commercial kitchens. Preventive cleaning is far less expensive than dealing with a full backup."),
        ],
        "schema_type": "PlumbingService",
        "keyword": "drain cleaning New Hampshire",
    },
    {
        "file": "water-heater.html",
        "title": "Water Heater Services in New Hampshire | Installation, Repair & Replacement",
        "meta_desc": "Water heater installation, repair & replacement in New Hampshire. Tank, tankless & heat pump water heaters. Same-day service available. Licensed NH plumbers. Call (603) 555-0192.",
        "h1": "Water Heater Services in New Hampshire",
        "badge": "Water Heater Services",
        "hero_desc": "Expert water heater installation, repair, and replacement across New Hampshire. Tank, tankless, and heat pump water heaters. Licensed, insured NH technicians.",
        "img": "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=800&q=80",
        "img_alt": "Water heater installation in New Hampshire home",
        "intro": """<p>Your water heater is one of the hardest-working appliances in your New Hampshire home — and when it fails, especially in winter, it's a genuine emergency. <strong>Plumbing HVAC Services New Hampshire</strong> provides same-day water heater repair and next-day installation services throughout the Granite State.</p>
        <p>We service and install all major water heater brands and types, including traditional tank, tankless (on-demand), and energy-efficient heat pump water heaters.</p>""",
        "services_list": ["Tank water heater installation & replacement", "Tankless water heater installation", "Heat pump water heater installation", "Water heater repair (all brands)", "Anode rod replacement", "Thermostat and element replacement", "Pressure relief valve replacement", "Water heater flushing & descaling", "Expansion tank installation", "Gas water heater conversion", "Electric to gas water heater conversion", "Commercial water heater services"],
        "why_h": "Choosing the Right Water Heater for Your NH Home",
        "why_body": """<p>New Hampshire's cold winters mean your water heater works overtime — efficiency and reliability matter more here than in milder climates. We help you choose the best option for your household size, budget, and energy goals.</p>
        <table><tr><th>Type</th><th>Best For</th><th>Avg. Lifespan</th><th>Energy Efficiency</th></tr>
        <tr><td>Tank (Gas/Electric)</td><td>Budget-conscious, most homes</td><td>8–12 years</td><td>Standard</td></tr>
        <tr><td>Tankless (On-Demand)</td><td>Small households, continuous hot water</td><td>15–20 years</td><td>High</td></tr>
        <tr><td>Heat Pump</td><td>Warm basements, high efficiency goals</td><td>10–15 years</td><td>Very High</td></tr></table>""",
        "faqs": [
            ("How long does water heater installation take in NH?", "Most standard tank water heater replacements take 2–3 hours. Tankless installations may take 4–6 hours depending on venting and gas line work required."),
            ("What size water heater do I need for my NH home?", "For a family of 4, a 50-gallon tank is typically sufficient. We assess your household size, peak usage times, and basement conditions to recommend the ideal size."),
            ("My water heater is leaking — is it an emergency?", "Yes, a leaking water heater should be addressed immediately to prevent water damage. Turn off the water supply to the heater and call (603) 555-0192 for emergency service."),
        ],
        "schema_type": "PlumbingService",
        "keyword": "water heater services New Hampshire",
    },
    {
        "file": "hvac-installation.html",
        "title": "HVAC Installation in New Hampshire | Furnace, AC & Heat Pump Install",
        "meta_desc": "Professional HVAC installation in New Hampshire. Furnace, central AC, heat pump, and mini-split systems. Licensed NH HVAC contractor. Free estimates. Call (603) 555-0192.",
        "h1": "HVAC Installation Services in New Hampshire",
        "badge": "HVAC Installation",
        "hero_desc": "Complete HVAC system installation across New Hampshire. Furnaces, central air conditioners, heat pumps, and mini-splits. Licensed NH HVAC contractor with manufacturer warranties.",
        "img": "https://images.unsplash.com/photo-1631069103703-4b5b7b3ef38f?w=800&q=80",
        "img_alt": "HVAC system installation in New Hampshire home",
        "intro": """<p>Investing in a new HVAC system is one of the biggest decisions you'll make for your New Hampshire home. A properly sized, expertly installed system will keep you comfortable through brutal NH winters and humid summers while minimizing energy costs for years to come.</p>
        <p><strong>Plumbing HVAC Services New Hampshire</strong> is a fully licensed HVAC contractor serving all of New Hampshire. We install systems from all major manufacturers and back every installation with manufacturer warranties plus our own labor guarantee.</p>""",
        "services_list": ["Central air conditioner installation", "Gas furnace installation & replacement", "Heat pump installation (air & ground source)", "Ductless mini-split system installation", "Boiler installation & replacement", "Dual-fuel heat pump systems", "Whole-home air handler installation", "Zoning system installation", "Smart thermostat installation", "New construction HVAC rough-in", "Commercial HVAC installation", "HVAC system design & load calculation"],
        "why_h": "Why Proper HVAC Installation Matters in New Hampshire",
        "why_body": """<p>New Hampshire's climate is demanding — temperatures range from well below zero in winter to the high 90s in summer. An improperly sized or installed HVAC system will struggle to keep up, costing you more in energy bills and repairs.</p>
        <ul><li><strong>Manual J Load Calculation:</strong> We perform a full load calculation before recommending any system size to ensure right-sizing for your NH home.</li>
        <li><strong>Licensed Installation:</strong> All HVAC installations comply with NH state codes and manufacturer specs to preserve warranties.</li>
        <li><strong>Brand-Agnostic:</strong> We install Carrier, Trane, Lennox, Bryant, Rheem, Daikin, Mitsubishi and more — we recommend what's best for your situation, not what we're incentivized to sell.</li>
        <li><strong>Post-Installation Support:</strong> We provide full training on your new system and are available for follow-up questions.</li></ul>""",
        "faqs": [
            ("How much does HVAC installation cost in New Hampshire?", "A central AC installation typically ranges from $3,500–$8,000. A new furnace runs $2,500–$6,000 installed. Heat pump systems range from $4,000–$12,000 depending on size. We provide free detailed estimates."),
            ("How long does HVAC installation take?", "A furnace or AC replacement typically takes 4–8 hours. A full new HVAC system installation may take 1–2 days. We work efficiently and leave your home clean when we're done."),
            ("Are there rebates for new HVAC systems in New Hampshire?", "Yes! NH Electric Co-op and Eversource often offer rebates for qualifying high-efficiency systems. Federal tax credits under the Inflation Reduction Act may also apply. We'll help you identify available incentives."),
        ],
        "schema_type": "HVACBusiness",
        "keyword": "HVAC installation New Hampshire",
    },
    {
        "file": "hvac-repair.html",
        "title": "HVAC Repair & Maintenance in New Hampshire | Licensed NH HVAC Technician",
        "meta_desc": "Expert HVAC repair and maintenance in New Hampshire. All brands serviced. Furnace, AC, heat pump repair. 24/7 emergency HVAC service. Call (603) 555-0192.",
        "h1": "HVAC Repair & Maintenance in New Hampshire",
        "badge": "HVAC Repair",
        "hero_desc": "Fast, reliable HVAC repair for all makes and models across New Hampshire. 24/7 emergency heating and cooling repair. Licensed NH HVAC technicians.",
        "img": "https://images.unsplash.com/photo-1585771724684-38269d6639fd?w=800&q=80",
        "img_alt": "HVAC technician repairing heating system in New Hampshire",
        "intro": """<p>When your heating or cooling system breaks down in New Hampshire — especially at the worst possible time — you need a trusted HVAC repair company that responds fast and fixes it right. <strong>Plumbing HVAC Services New Hampshire</strong> provides emergency and scheduled HVAC repair for all brands and systems throughout the state.</p>
        <p>Our certified NH HVAC technicians carry a comprehensive inventory of parts for faster first-visit repairs. We service furnaces, boilers, central AC systems, heat pumps, mini-splits, and more.</p>""",
        "services_list": ["Furnace repair (gas, oil, electric)", "Boiler repair and service", "Central air conditioner repair", "Heat pump repair", "Mini-split repair", "Thermostat repair and replacement", "Blower motor and fan repair", "Heat exchanger inspection & repair", "Refrigerant leak detection & recharge", "Compressor diagnostics", "Capacitor and contactor replacement", "Annual HVAC tune-up and maintenance"],
        "why_h": "HVAC Preventive Maintenance in New Hampshire",
        "why_body": """<p>The best way to avoid an HVAC breakdown during a NH cold snap is preventive maintenance. Our annual maintenance plans keep your system running at peak efficiency and catch small problems before they become expensive emergencies.</p>
        <ul><li><strong>Spring AC Tune-Up:</strong> Clean coils, check refrigerant, test electrical components, lubricate moving parts, verify operation.</li>
        <li><strong>Fall Heating Tune-Up:</strong> Inspect heat exchanger, clean burners, check gas pressure, verify safety controls, test ignition.</li>
        <li><strong>Priority Service:</strong> Maintenance plan members receive priority scheduling and discounts on repairs.</li>
        <li><strong>Extended Equipment Life:</strong> Well-maintained systems last 3–5 years longer than neglected ones.</li></ul>""",
        "faqs": [
            ("Why is my furnace blowing cold air in winter?", "Common causes include a dirty air filter, faulty ignitor, bad thermostat, gas supply issue, or tripped limit switch. Our NH HVAC technicians can diagnose and fix the issue same day in most cases."),
            ("My AC stopped cooling — what should I do?", "Check your filter and thermostat first. If those are fine, you may have a refrigerant leak, failed compressor, or capacitor issue. Call (603) 555-0192 and we'll dispatch a technician to your NH home."),
            ("How often should HVAC maintenance be done in New Hampshire?", "We recommend twice yearly — spring for AC and fall for heating. Given NH's extreme seasonal temperature swings, regular maintenance is especially important here."),
        ],
        "schema_type": "HVACBusiness",
        "keyword": "HVAC repair New Hampshire",
    },
    {
        "file": "emergency-plumbing.html",
        "title": "24/7 Emergency Plumber New Hampshire | Same-Hour Response",
        "meta_desc": "24/7 emergency plumbing services in New Hampshire. Burst pipes, sewage backup, flooding — we respond in 60 minutes or less. Licensed NH emergency plumber. Call (603) 555-0192 NOW.",
        "h1": "24/7 Emergency Plumbing Services in New Hampshire",
        "badge": "🚨 Emergency Plumbing",
        "hero_desc": "Plumbing emergency in New Hampshire? We respond in 60 minutes or less, 24 hours a day, 7 days a week. Licensed, insured, and ready to help right now.",
        "img": "https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=800&q=80",
        "img_alt": "Emergency plumber responding to burst pipe in New Hampshire",
        "intro": """<p><strong>If you have a plumbing emergency in New Hampshire, call us immediately: <a href="tel:+16035550192">(603) 555-0192</a>.</strong> We answer every call, 24 hours a day, 7 days a week, 365 days a year — including all holidays.</p>
        <p>Plumbing emergencies escalate quickly. A small leak becomes catastrophic water damage. A sewage backup creates a health hazard. A frozen pipe can burst and flood your home within minutes. Our emergency NH plumbers are strategically positioned across the state to reach you fast.</p>""",
        "services_list": ["Burst pipe emergency repair", "Frozen pipe thawing and repair", "Sewage backup clearing", "Flooding and water extraction", "Water main break repair", "Gas leak detection (call 911 first, then us)", "Water heater failure", "Sewer line emergency", "Toilet overflow and flooding", "Washing machine overflow", "Sump pump failure", "Water shutoff valve emergency"],
        "why_h": "What to Do During a NH Plumbing Emergency",
        "why_body": """<p>While waiting for our emergency plumber to arrive, here's what to do:</p>
        <ul><li><strong>Burst Pipe:</strong> Locate and turn off your main water shutoff valve immediately. This is typically in your basement, crawl space, or utility room. Then call (603) 555-0192.</li>
        <li><strong>Sewage Backup:</strong> Stop using all drains and toilets. Avoid contact with sewage water. Ventilate the area and call us immediately.</li>
        <li><strong>Gas Leak:</strong> Leave the building immediately, don't use electrical switches or phones inside, call 911, then call your gas company. Our licensed gas technicians can handle repairs after the area is cleared safe.</li>
        <li><strong>Flooding:</strong> Turn off electricity at the breaker if water is near outlets. Don't enter rooms with standing water and electrical hazards. Call us for emergency extraction.</li></ul>""",
        "faqs": [
            ("What qualifies as a plumbing emergency in New Hampshire?", "A plumbing emergency is any situation causing immediate water damage, health hazard, or loss of essential services. This includes burst pipes, sewage backups, major leaks, no hot water in winter, and gas leaks."),
            ("Do you charge extra for emergency plumbing calls at night or on weekends?", "We believe in transparent pricing. Our emergency service fee is clearly disclosed before we dispatch. There are no hidden overtime charges — what we quote is what you pay."),
            ("How fast can an emergency plumber arrive in New Hampshire?", "We target a 60-minute response time for emergencies across most NH service areas. In Manchester, Nashua, Concord, Dover, and Portsmouth we often arrive faster. Call (603) 555-0192 for the most current ETA."),
        ],
        "schema_type": "EmergencyService",
        "keyword": "emergency plumber New Hampshire",
    },
    {
        "file": "sewer-line.html",
        "title": "Sewer Line Services in New Hampshire | Repair, Replacement & Camera Inspection",
        "meta_desc": "Expert sewer line services in New Hampshire. Camera inspection, sewer line repair, replacement & trenchless technology. Licensed NH plumbers. Call (603) 555-0192.",
        "h1": "Sewer Line Services in New Hampshire",
        "badge": "Sewer Line Services",
        "hero_desc": "Complete sewer line services for NH homes and businesses. Camera inspection, cleaning, repair, and trenchless replacement by licensed New Hampshire plumbers.",
        "img": "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=800&q=80",
        "img_alt": "Sewer line inspection in New Hampshire",
        "intro": """<p>Sewer line problems are among the most disruptive and potentially expensive plumbing issues a New Hampshire homeowner can face. Early detection and professional repair are critical to avoiding costly excavation and property damage.</p>
        <p><strong>Plumbing HVAC Services New Hampshire</strong> offers comprehensive sewer line services including video camera inspection, hydro-jetting, spot repairs, and full trenchless sewer line replacement for properties throughout NH.</p>""",
        "services_list": ["Sewer camera inspection (video)", "Sewer line cleaning & clearing", "Root intrusion removal", "Sewer line spot repair", "Trenchless sewer line replacement (pipe lining)", "Traditional sewer line excavation & replacement", "Sewer line location & mapping", "Sewer gas leak detection", "Municipal sewer connection", "Septic to sewer conversion", "Commercial sewer services", "Emergency sewer backup clearing"],
        "why_h": "Signs You Need Sewer Line Service in NH",
        "why_body": """<p>Many sewer line problems develop gradually. Watch for these warning signs at your New Hampshire property:</p>
        <ul><li><strong>Multiple slow drains</strong> throughout the house at the same time</li>
        <li><strong>Sewage odors</strong> coming from drains or in the yard</li>
        <li><strong>Gurgling sounds</strong> from toilets when other drains run</li>
        <li><strong>Sewage backing up</strong> into the lowest drains in the home</li>
        <li><strong>Unusually green patches</strong> of grass above the sewer line</li>
        <li><strong>Sinkholes or wet spots</strong> in the yard near the sewer line path</li></ul>
        <p>If you notice any of these signs, call (603) 555-0192 to schedule a sewer camera inspection before the situation gets worse.</p>""",
        "faqs": [
            ("How much does sewer line replacement cost in New Hampshire?", "Trenchless sewer line replacement typically costs $3,000–$8,000 depending on length. Traditional excavation replacement ranges from $5,000–$15,000+. Camera inspection is typically $250–$450 and is credited toward repairs."),
            ("What causes sewer line problems in NH homes?", "Common causes include tree root intrusion, pipe corrosion (especially in older NH homes with clay or cast iron pipes), ground shifting, grease buildup, and flushing inappropriate materials."),
            ("What is trenchless sewer line repair?", "Trenchless pipe lining (CIPP) inserts a resin-coated liner into the existing pipe which hardens to form a new pipe inside the old one — no major excavation required. It's faster, less disruptive, and often less expensive than traditional replacement."),
        ],
        "schema_type": "PlumbingService",
        "keyword": "sewer line services New Hampshire",
    },
    {
        "file": "gas-line.html",
        "title": "Gas Line Services in New Hampshire | Installation, Repair & Leak Detection",
        "meta_desc": "Licensed gas line services in New Hampshire. Gas line installation, repair, leak detection & pressure testing. NH-licensed gas contractor. Call (603) 555-0192.",
        "h1": "Gas Line Services in New Hampshire",
        "badge": "Gas Line Services",
        "hero_desc": "Safe, code-compliant gas line installation and repair across New Hampshire. Licensed NH gas contractor for residential and commercial properties.",
        "img": "https://images.unsplash.com/photo-1504328345606-18bbc8c9d7d1?w=800&q=80",
        "img_alt": "Licensed gas line technician working in New Hampshire",
        "intro": """<p>Gas line work requires specialized licensing, training, and equipment — there is no room for error. <strong>Plumbing HVAC Services New Hampshire</strong> employs fully licensed gas line contractors who handle all gas piping work safely and in strict compliance with New Hampshire codes and standards.</p>
        <p>Whether you're adding a gas appliance, repairing a damaged gas line, or need emergency leak detection, our licensed NH gas professionals are available 24/7.</p>""",
        "services_list": ["New gas line installation", "Gas line extension for appliances", "Gas pipe repair", "Gas leak detection and repair", "Gas pressure testing", "Gas line shutoff valve installation", "Gas line for outdoor grills & fire pits", "Natural gas to propane conversion", "Propane to natural gas conversion", "Gas appliance connection", "Commercial gas line services", "Emergency gas line response"],
        "why_h": "Gas Safety in New Hampshire Homes",
        "why_body": """<p>Natural gas and propane are safe fuels when installed and maintained properly. However, gas leaks are a serious hazard. Here's what every NH homeowner should know:</p>
        <ul><li><strong>Know the smell:</strong> Gas has a distinctive rotten egg odor from added mercaptan. If you smell it, leave immediately and call 911.</li>
        <li><strong>Annual inspections:</strong> We recommend annual gas line inspections for older NH homes, especially those with aging iron gas pipes.</li>
        <li><strong>Never DIY gas work:</strong> Gas line work in NH requires licensed contractors. Unpermitted work creates safety hazards and insurance problems.</li>
        <li><strong>Carbon monoxide detectors:</strong> All NH homes with gas appliances should have CO detectors on every floor.</li></ul>""",
        "faqs": [
            ("Are your technicians licensed for gas line work in New Hampshire?", "Yes. All gas line work is performed by technicians who hold the required New Hampshire gas fitter license. We pull all necessary permits and our work is inspected to code."),
            ("How do I know if I have a gas leak?", "Signs include the smell of rotten eggs, hissing near gas lines or appliances, dead vegetation above underground gas lines, or a gas meter that continues running when all appliances are off. If you suspect a leak, leave immediately and call 911."),
            ("How long does gas line installation take?", "A simple appliance connection takes 1–2 hours. Running new gas lines to a new appliance location takes 3–6 hours. Whole-home gas service installation may take 1–2 days."),
        ],
        "schema_type": "PlumbingService",
        "keyword": "gas line services New Hampshire",
    },
    {
        "file": "ac-services.html",
        "title": "AC Services in New Hampshire | Air Conditioner Repair, Install & Maintenance",
        "meta_desc": "Professional AC services in New Hampshire. Air conditioner repair, installation & tune-ups for homes & businesses. Licensed NH HVAC contractor. Call (603) 555-0192.",
        "h1": "Air Conditioning Services in New Hampshire",
        "badge": "AC Services",
        "hero_desc": "Keep your New Hampshire home cool all summer. Professional AC repair, installation, and maintenance by licensed NH HVAC technicians. Same-day service available.",
        "img": "https://images.unsplash.com/photo-1631069103703-4b5b7b3ef38f?w=800&q=80",
        "img_alt": "Air conditioning service technician in New Hampshire",
        "intro": """<p>While New Hampshire winters get all the attention, summers can bring extended heat and humidity that make a reliable air conditioning system essential. <strong>Plumbing HVAC Services New Hampshire</strong> provides complete AC services — from emergency repairs to new system installations — throughout the Granite State.</p>
        <p>Our licensed NH HVAC technicians service all major AC brands and offer same-day emergency repair when your cooling system fails during a heat wave.</p>""",
        "services_list": ["Central AC repair", "Central AC installation & replacement", "Ductless mini-split installation", "Mini-split repair", "AC tune-up and maintenance", "Refrigerant recharge (EPA certified)", "AC capacitor & contactor replacement", "Compressor diagnostics", "Air handler service", "Evaporator and condenser coil cleaning", "Thermostat calibration & replacement", "Commercial AC services"],
        "why_h": "Choosing the Right AC System for Your NH Home",
        "why_body": """<p>New Hampshire homes vary widely — older homes without ductwork, modern construction, historic buildings, and everything in between. We help you choose the right cooling solution:</p>
        <ul><li><strong>Central AC:</strong> Best for homes with existing ductwork. Most cost-effective for whole-home cooling.</li>
        <li><strong>Ductless Mini-Splits:</strong> Ideal for NH homes without ductwork, room additions, garages, and basements. Very efficient.</li>
        <li><strong>Heat Pumps:</strong> Provide both heating and cooling in one system — increasingly popular in NH due to efficiency and utility rebates.</li>
        <li><strong>Window/Portable Units:</strong> We install and service these as well for targeted room cooling.</li></ul>""",
        "faqs": [
            ("Why is my AC not cooling my New Hampshire home?", "Common causes include low refrigerant, dirty coils, failed capacitor, clogged air filter, or a failing compressor. Our NH HVAC technicians will diagnose and repair your system quickly."),
            ("How much does AC installation cost in NH?", "Central AC installation ranges from $3,500–$7,500 depending on system size and home complexity. Ductless mini-splits range from $1,500–$4,000 per zone. We provide free detailed estimates."),
            ("Do you offer AC maintenance plans in New Hampshire?", "Yes! Our annual AC tune-up plans start at $89/year and include a full 18-point inspection, cleaning, and performance test. Members also receive priority service and repair discounts."),
        ],
        "schema_type": "HVACBusiness",
        "keyword": "AC services New Hampshire",
    },
    {
        "file": "heating-services.html",
        "title": "Heating Services in New Hampshire | Furnace, Boiler & Heat Pump Repair",
        "meta_desc": "Expert heating services in New Hampshire. Furnace repair, boiler service, heat pump installation & emergency heating repair. Licensed NH heating contractor. Call (603) 555-0192.",
        "h1": "Heating Services in New Hampshire",
        "badge": "Heating Services",
        "hero_desc": "Stay warm through New Hampshire winters. Licensed NH heating technicians for furnace repair, boiler service, heat pump installation, and 24/7 emergency heating repair.",
        "img": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80",
        "img_alt": "Heating system repair service in New Hampshire winter",
        "intro": """<p>In New Hampshire, a reliable heating system isn't a luxury — it's a necessity. With temperatures regularly dropping well below zero, a heating system failure can become a dangerous emergency within hours. <strong>Plumbing HVAC Services New Hampshire</strong> provides comprehensive heating services for all system types throughout the state, with 24/7 emergency response.</p>
        <p>From furnace repair to full system replacement, our licensed NH heating technicians keep your home warm when it matters most.</p>""",
        "services_list": ["Gas furnace repair & replacement", "Oil furnace service & repair", "Boiler repair and maintenance", "Boiler replacement", "Heat pump repair & installation", "Baseboard heater repair", "Radiant floor heating", "Zone control system installation", "Emergency heat repair (24/7)", "Annual furnace tune-up", "Heat exchanger inspection", "Heating system efficiency upgrades"],
        "why_h": "Preparing Your NH Heating System for Winter",
        "why_body": """<p>Fall is the ideal time to schedule a heating system tune-up before the demand of New Hampshire winter. Our fall tune-up includes:</p>
        <ul><li><strong>Heat exchanger inspection</strong> for cracks that could allow carbon monoxide into your home</li>
        <li><strong>Burner cleaning and adjustment</strong> for efficient combustion</li>
        <li><strong>Flue and venting inspection</strong> to ensure safe exhaust</li>
        <li><strong>Filter replacement</strong> and blower cleaning</li>
        <li><strong>Thermostat calibration</strong> and safety control testing</li>
        <li><strong>Full performance test</strong> under operating conditions</li></ul>""",
        "faqs": [
            ("My heat stopped working in winter — what should I do?", "Call (603) 555-0192 immediately. This is a 24/7 emergency we respond to year-round. While waiting, keep warm with space heaters if safe, and keep interior doors closed to retain heat. If you have elderly or young children at home, consider going to a warm location."),
            ("How long do furnaces last in New Hampshire?", "Most gas furnaces last 15–20 years with regular maintenance. Oil furnaces typically last 15–25 years. Heat pumps last 10–15 years. If your system is approaching end of life, replacing before it fails can save you from an emergency replacement in the middle of winter."),
            ("Are heat pumps effective in New Hampshire winters?", "Modern cold-climate heat pumps can operate effectively down to -15°F, making them viable for NH winters. Many NH homeowners use a heat pump as the primary heat source with a gas furnace as backup — maximizing efficiency while maintaining reliability."),
        ],
        "schema_type": "HVACBusiness",
        "keyword": "heating services New Hampshire",
    },
    {
        "file": "pipe-installation.html",
        "title": "Pipe Installation & Repair in New Hampshire | Copper, PVC & PEX Piping",
        "meta_desc": "Professional pipe installation and repair in New Hampshire. Copper, PVC, PEX piping. Whole-home repiping, burst pipe repair & new construction. Licensed NH plumbers. Call (603) 555-0192.",
        "h1": "Pipe Installation & Repair in New Hampshire",
        "badge": "Pipe Installation",
        "hero_desc": "Complete pipe installation and repair for NH homes and businesses. Copper, PVC, PEX repiping, burst pipe repair, and new construction plumbing by licensed New Hampshire plumbers.",
        "img": "https://images.unsplash.com/photo-1607472586893-edb57bdc0e39?w=800&q=80",
        "img_alt": "Plumber installing new pipes in New Hampshire home",
        "intro": """<p>The pipes running through your New Hampshire home or business are the circulatory system of your plumbing — and like any system, they have a lifespan. Whether you need a single pipe repaired, a section replaced, or complete repiping of an older NH property, our licensed plumbers deliver professional results.</p>
        <p>We work with all pipe materials including copper, CPVC, PVC, and modern PEX, recommending the best option for your specific application and budget.</p>""",
        "services_list": ["Copper pipe installation", "PEX pipe installation & repiping", "PVC/CPVC pipe installation", "Burst pipe repair", "Frozen pipe repair", "Whole-home repiping", "Water supply line installation", "Drain line installation", "New construction rough-in plumbing", "Pipe insulation installation", "Water pressure booster installation", "Pressure reducing valve (PRV) installation"],
        "why_h": "When Is It Time to Repipe Your NH Home?",
        "why_body": """<p>Many older New Hampshire homes were built with galvanized steel or polybutylene pipes that are well past their service life. Signs it may be time for repiping include:</p>
        <ul><li>Discolored or rusty water from the tap</li>
        <li>Persistent low water pressure throughout the home</li>
        <li>Frequent pinhole leaks or pipe failures</li>
        <li>Pipes older than 40–50 years (galvanized) or 25+ years (polybutylene)</li>
        <li>Significant pipe corrosion visible in basement or crawl space</li></ul>
        <p>Modern PEX repiping is durable, flexible, and resistant to freezing — making it an excellent choice for New Hampshire's cold climate. Contact us for a free repiping assessment.</p>""",
        "faqs": [
            ("How long does whole-home repiping take in New Hampshire?", "Most whole-home repiping projects take 2–4 days depending on home size and accessibility. We work room by room to minimize disruption and restore water service each evening."),
            ("What pipe material is best for New Hampshire homes?", "PEX is our most recommended pipe for NH homes due to its freeze resistance, flexibility, durability, and cost-effectiveness. Copper remains an excellent choice for water quality and longevity. We'll recommend the best option for your specific situation."),
            ("Will repiping increase my home's value in NH?", "Yes. Updated plumbing is a significant selling point and typically required or flagged in home inspections. Repiped homes in NH typically sell faster and command higher prices."),
        ],
        "schema_type": "PlumbingService",
        "keyword": "pipe installation New Hampshire",
    },
    {
        "file": "bathroom-remodeling.html",
        "title": "Bathroom Plumbing & Remodeling in New Hampshire | Licensed NH Plumber",
        "meta_desc": "Professional bathroom plumbing and remodeling services in New Hampshire. Tub, shower, toilet, vanity installation. Licensed NH plumbers for full bathroom renovations. Call (603) 555-0192.",
        "h1": "Bathroom Plumbing & Remodeling in New Hampshire",
        "badge": "Bathroom Remodeling",
        "hero_desc": "Transform your New Hampshire bathroom with expert plumbing services. New tubs, showers, toilets, vanities, and complete bathroom rough-in work. Licensed NH plumbers.",
        "img": "https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=800&q=80",
        "img_alt": "Bathroom remodeling plumbing services in New Hampshire",
        "intro": """<p>A bathroom remodel is one of the highest-ROI home improvements you can make in New Hampshire — and getting the plumbing right is the foundation of a successful project. <strong>Plumbing HVAC Services New Hampshire</strong> provides complete bathroom plumbing services for remodels, renovations, and new additions throughout the state.</p>
        <p>From moving drain lines to installing walk-in showers, our licensed NH plumbers work with homeowners, interior designers, and general contractors to bring bathroom visions to life.</p>""",
        "services_list": ["Toilet installation and replacement", "Walk-in shower installation", "Bathtub installation & replacement", "Freestanding tub installation", "Vanity and sink installation", "Bathroom rough-in plumbing", "Shower pan and drain installation", "Bathroom drain relocation", "Bathroom water supply rough-in", "Steam shower installation", "Bidet installation", "Bathroom fixture upgrades"],
        "why_h": "Planning Your NH Bathroom Remodel Plumbing",
        "why_body": """<p>Proper planning prevents costly surprises. Before your bathroom remodel begins, our plumbers assess:</p>
        <ul><li><strong>Existing pipe locations</strong> — moving drain lines is possible but adds cost; we help you design around existing rough-in where possible</li>
        <li><strong>Water pressure adequacy</strong> — multi-head shower systems and body sprays require adequate pressure</li>
        <li><strong>Venting requirements</strong> — all NH bathroom fixtures require proper venting per code</li>
        <li><strong>Permit requirements</strong> — significant plumbing changes in NH require permits; we handle this for you</li>
        <li><strong>Access for future repairs</strong> — we install access panels where appropriate</li></ul>""",
        "faqs": [
            ("Do I need a permit for bathroom plumbing work in New Hampshire?", "Yes, significant plumbing work including moving drain or supply lines, adding fixtures, or bathroom additions requires a permit in most NH municipalities. We handle permit applications as part of our service."),
            ("How much does bathroom plumbing cost in a NH remodel?", "Basic bathroom plumbing for a standard remodel (same layout, new fixtures) typically runs $1,500–$4,000. Moving plumbing or adding new lines can range from $3,000–$10,000+ depending on scope."),
            ("Can you work alongside our general contractor?", "Absolutely. We regularly work as the plumbing subcontractor on bathroom renovations with NH general contractors. We're familiar with coordinating rough-in schedules, inspections, and finish plumbing timelines."),
        ],
        "schema_type": "PlumbingService",
        "keyword": "bathroom plumbing remodeling New Hampshire",
    },
]

def generate_service_page(svc):
    faq_html = ""
    for q, a in svc["faqs"]:
        faq_html += f'''<div class="faq-item"><button class="faq-question">{q} <span class="icon">+</span></button><div class="faq-answer"><p>{a}</p></div></div>\n'''

    services_html = "\n".join(f"<li>{s}</li>" for s in svc["services_list"])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{svc["title"]}</title>
  <meta name="description" content="{svc["meta_desc"]}" />
  <link rel="canonical" href="https://plumbinghvacservicesnewHampshire.com/services/{svc["file"]}" />
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"{svc["schema_type"]}","name":"Plumbing HVAC Services New Hampshire","telephone":"+16035550192","description":"{svc["meta_desc"]}","areaServed":{{"@type":"State","name":"New Hampshire"}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.9","reviewCount":"348"}}}}</script>
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>
{nav()}
<div class="page-hero">
  <div class="container">
    <span class="badge">{svc["badge"]}</span>
    <h1>{svc["h1"]}</h1>
    <p>{svc["hero_desc"]}</p>
    <div style="margin-top:24px;display:flex;gap:14px;flex-wrap:wrap;">
      <a href="tel:+16035550192" class="btn-primary">📞 Call {PHONE} Now</a>
      <a href="../contact.html" class="btn-secondary">Get Free Estimate</a>
    </div>
  </div>
</div>
<div class="breadcrumb"><div class="container"><a href="../index.html">Home</a> <span>›</span> <a href="index.html">Services</a> <span>›</span> {svc["badge"]}</div></div>

<section class="section">
  <div class="container">
    <div class="content-layout">
      <article class="content-body">
        {svc["intro"]}
        <img src="{svc["img"]}" alt="{svc["img_alt"]}" loading="lazy" />
        <h2>Our {svc["badge"]} in New Hampshire</h2>
        <ul>{services_html}</ul>
        <h2>{svc["why_h"]}</h2>
        {svc["why_body"]}
        <div style="background:linear-gradient(135deg,var(--accent),#c4320a);border-radius:12px;padding:32px;text-align:center;margin:32px 0;">
          <h3 style="color:#fff;margin-bottom:8px;">Ready to Schedule Service in New Hampshire?</h3>
          <p style="color:rgba(255,255,255,0.88)">Our licensed NH technicians are standing by. Call now for same-day service and free estimates.</p>
          <a href="tel:+16035550192" style="display:inline-flex;align-items:center;gap:8px;background:#fff;color:var(--accent);font-family:\'Barlow Condensed\',sans-serif;font-weight:800;font-size:1.4rem;padding:14px 32px;border-radius:8px;margin-top:12px;">📞 {PHONE}</a>
        </div>
        <h2>Frequently Asked Questions</h2>
        <div>{faq_html}</div>
        <h2>Serving All of New Hampshire</h2>
        <p>We provide {svc["badge"].lower()} throughout New Hampshire including <a href="../regions/manchester-nh.html">Manchester</a>, <a href="../regions/nashua-nh.html">Nashua</a>, <a href="../regions/concord-nh.html">Concord</a>, <a href="../regions/dover-nh.html">Dover</a>, <a href="../regions/portsmouth-nh.html">Portsmouth</a>, <a href="../regions/keene-nh.html">Keene</a>, <a href="../regions/laconia-nh.html">Laconia</a>, <a href="../regions/derry-nh.html">Derry</a>, <a href="../regions/rochester-nh.html">Rochester</a>, <a href="../regions/bedford-nh.html">Bedford</a>, and all surrounding communities. <a href="../regions/index.html">See all service areas →</a></p>
      </article>
      {sidebar()}
    </div>
  </div>
</section>
{footer()}
</body></html>'''

os.makedirs("/home/claude/plumbing-hvac-nh/services", exist_ok=True)
for svc in SERVICES:
    path = f"/home/claude/plumbing-hvac-nh/services/{svc['file']}"
    with open(path, "w") as f:
        f.write(generate_service_page(svc))
    print(f"Created: {path}")

print(f"\nGenerated {len(SERVICES)} service pages!")
