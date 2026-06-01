/* ========================================
   CAMPUS COMPASS — V3 Institutional Interactions
   "Clean, Predictable, Trustworthy."
   ======================================== */

document.addEventListener('DOMContentLoaded', () => {

  // 1. Intersection Observer for Subtle Fade-Ups
  const fadeElements = document.querySelectorAll('.fade-up');
  
  if ('IntersectionObserver' in window) {
    const fadeObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in-view');
          // Optional: Unobserve after fade-in for static behavior, 
          // or keep observing to replay animation if desired. We will unobserve for a clean feel.
          fadeObserver.unobserve(entry.target);
        }
      });
    }, { 
      threshold: 0.1, 
      rootMargin: '0px 0px -50px 0px' 
    });

    fadeElements.forEach(el => fadeObserver.observe(el));
  } else {
    // Fallback for older browsers
    fadeElements.forEach(el => el.classList.add('in-view'));
  }

  // 2. Smooth Anchor Scrolling for Navigation
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        // Offset for the fixed navbar (approx 80px)
        const offset = 80;
        const bodyRect = document.body.getBoundingClientRect().top;
        const elementRect = target.getBoundingClientRect().top;
        const elementPosition = elementRect - bodyRect;
        const offsetPosition = elementPosition - offset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });

  // Note: All parallax and scroll-hijacking from V2 has been removed 
  // to prioritize usability, scannability, and institutional trust.

});
