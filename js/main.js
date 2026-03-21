// Mobile Nav
const menuToggle = document.getElementById('menuToggle');
const mobileNav = document.getElementById('mobileNav');
const mobileNavClose = document.getElementById('mobileNavClose');
if(menuToggle && mobileNav){
  menuToggle.addEventListener('click',()=>mobileNav.classList.add('open'));
  mobileNavClose.addEventListener('click',()=>mobileNav.classList.remove('open'));
}

// FAQ Accordion
document.querySelectorAll('.faq-question').forEach(q=>{
  q.addEventListener('click',()=>{
    const item=q.parentElement;
    const isOpen=item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(i=>i.classList.remove('open'));
    if(!isOpen) item.classList.add('open');
  });
});

// Scroll animations
const observer=new IntersectionObserver(entries=>{
  entries.forEach(e=>{ if(e.isIntersecting) e.target.classList.add('visible'); });
},{threshold:0.1});
document.querySelectorAll('.fade-in').forEach(el=>observer.observe(el));

// Sticky header shadow
window.addEventListener('scroll',()=>{
  const header=document.querySelector('.site-header');
  if(header) header.style.boxShadow=window.scrollY>10?'0 4px 20px rgba(0,0,0,.4)':'0 2px 12px rgba(0,0,0,.3)';
});
