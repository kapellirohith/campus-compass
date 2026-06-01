document.addEventListener('DOMContentLoaded', () => {
  // 1. Intersection Observer for Fade-Up Animations
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.fade-up').forEach(el => {
    observer.observe(el);
  });

  // 2. Stabilized Ticker Logic
  const tickers = document.querySelectorAll('.ticker-item');
  if (tickers.length > 0) {
    let currentTicker = 0;
    // Initial fade in
    setTimeout(() => {
      tickers[currentTicker].classList.add('active');
    }, 100);
    
    setInterval(() => {
      tickers[currentTicker].classList.remove('active');
      currentTicker = (currentTicker + 1) % tickers.length;
      tickers[currentTicker].classList.add('active');
    }, 4500);
  }

  // 3. Premium Quiz Logic with Editorial Results
  const quizForm = document.getElementById('club-quiz-form');
  if (quizForm) {
    quizForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const q1 = document.querySelector('input[name="q1"]:checked')?.value;
      const q2 = document.querySelector('input[name="q2"]:checked')?.value;
      const q3 = document.querySelector('input[name="q3"]:checked')?.value;
      
      if (!q1 || !q2 || !q3) {
        alert("Please answer all 3 questions to get your personalized recommendation.");
        return;
      }
      
      const answers = [q1, q2, q3];
      const counts = { A:0, B:0, C:0, D:0, E:0 };
      
      answers.forEach(ans => counts[ans]++);
      
      let highestCount = 0;
      let winningLetter = 'A';
      
      for (const [letter, count] of Object.entries(counts)) {
        if (count > highestCount) {
          highestCount = count;
          winningLetter = letter;
        }
      }
      
      const resultsMap = {
        'A': {
          name: 'Chakravyuha Technical Club',
          why: 'You enjoy building projects and learning through execution rather than theory.',
          action: 'Find their booth during club induction week and sign up.',
          advice: 'Do not wait until second year to start building. The students who grow fastest join early.'
        },
        'B': {
          name: 'Team bi0s',
          why: 'You have a natural curiosity for breaking systems to understand how they work securely.',
          action: 'Join their beginner CTF training sessions.',
          advice: 'Cybersecurity has a steep learning curve. The community will pull you through the hardest parts.'
        },
        'C': {
          name: 'IEEE',
          why: 'You value deep technical research and want to connect with the global engineering ecosystem.',
          action: 'Attend their first technical paper presentation seminar.',
          advice: 'Use IEEE to find mentors who are publishing research, not just doing assignments.'
        },
        'D': {
          name: 'AYUDH',
          why: 'You realize that not everything important happens in a classroom, and you value social impact.',
          action: 'Volunteer for their first weekend campus initiative.',
          advice: 'Balance is everything in engineering. This community will keep you grounded.'
        },
        'E': {
          name: 'E-Cell',
          why: 'You look at problems and think about scalable solutions and execution.',
          action: 'Go to their first startup pitching session, even just to listen.',
          advice: 'Ideas are cheap. Surround yourself with people who actually execute them.'
        }
      };
      
      const result = resultsMap[winningLetter];
      const resultContainer = document.getElementById('quiz-result-container');
      
      // Inject Editorial Content
      document.getElementById('res-name').innerText = result.name;
      document.getElementById('res-why').innerText = result.why;
      document.getElementById('res-action').innerText = result.action;
      document.getElementById('res-advice').innerText = result.advice;
      
      resultContainer.style.display = 'block';
      
      // Smooth scroll to result
      setTimeout(() => {
        resultContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }, 100);
    });
  }
});
