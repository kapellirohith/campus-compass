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

  // 2. Ticker Logic
  const tickers = document.querySelectorAll('.ticker-item');
  if (tickers.length > 0) {
    let currentTicker = 0;
    tickers[currentTicker].classList.add('active');
    
    setInterval(() => {
      tickers[currentTicker].classList.remove('active');
      currentTicker = (currentTicker + 1) % tickers.length;
      tickers[currentTicker].classList.add('active');
    }, 4000); // Rotate every 4 seconds
  }

  // 3. Quiz Logic
  const quizForm = document.getElementById('club-quiz-form');
  if (quizForm) {
    quizForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const q1 = document.querySelector('input[name="q1"]:checked')?.value;
      const q2 = document.querySelector('input[name="q2"]:checked')?.value;
      const q3 = document.querySelector('input[name="q3"]:checked')?.value;
      
      if (!q1 || !q2 || !q3) {
        alert("Please answer all 3 questions to get your result.");
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
        'A': 'Chakravyuha Technical Club',
        'B': 'Team bi0s',
        'C': 'IEEE',
        'D': 'AYUDH',
        'E': 'E-Cell'
      };
      
      const resultContainer = document.getElementById('quiz-result-container');
      const resultText = document.getElementById('quiz-result-text');
      
      resultText.innerText = "You belong in: " + resultsMap[winningLetter];
      resultContainer.style.display = 'block';
    });
  }
});
