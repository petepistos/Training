const TopicShell = (() => {
  let currentSection = null;

  function qs(selector, root = document) {
    return root.querySelector(selector);
  }

  function qsa(selector, root = document) {
    return Array.from(root.querySelectorAll(selector));
  }

  function stopVoice() {
    if ('speechSynthesis' in window) window.speechSynthesis.cancel();
  }

  function speak(text) {
    stopVoice();
    if (!('speechSynthesis' in window)) return;
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 0.92;
    utterance.pitch = 0.95;
    window.speechSynthesis.speak(utterance);
  }

  function openSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (!section) return;
    currentSection = sectionId;
    qsa('.narrative-section').forEach(s => s.classList.remove('active'));
    qsa('.panel-card').forEach(p => p.classList.toggle('active', p.dataset.section === sectionId));
    section.classList.add('active');
    section.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  function speakCurrentSection() {
    const section = currentSection ? document.getElementById(currentSection) : qs('.narrative-section.active');
    if (!section) return;
    const text = section.dataset.narration || section.innerText;
    speak(text);
  }

  function gradeQuiz() {
    stopVoice();
    let score = 0;
    const cards = qsa('.quiz-card');

    cards.forEach((card) => {
      const correct = Number(card.dataset.answer);
      const selected = qs('input[type="radio"]:checked', card);
      qsa('.answer', card).forEach(label => {
        label.classList.remove('correct', 'wrong');
        const input = qs('input', label);
        const value = Number(input.value);
        if (value === correct) label.classList.add('correct');
        if (selected && input.checked && value !== correct) label.classList.add('wrong');
      });

      if (selected && Number(selected.value) === correct) score++;
      const explanation = qs('.explanation', card);
      if (explanation) {
        explanation.textContent = card.dataset.explanation || '';
        explanation.style.display = 'block';
      }
    });

    const result = qs('#quiz-result');
    if (result) {
      const pct = Math.round((score / cards.length) * 100);
      const feedback = score >= 5
        ? 'Strong result. The key concepts are understood.'
        : score >= 4
          ? 'Good result. Review the explanations for the missed items.'
          : 'Needs review. Revisit the narrative sections and try again.';
      result.innerHTML = `<strong>${score} / ${cards.length} correct (${pct}%)</strong><br><br>${feedback}`;
      result.style.display = 'block';
      result.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }

  function init() {
    qsa('[data-section]').forEach(el => {
      el.addEventListener('click', () => openSection(el.dataset.section));
    });
    const first = qs('.narrative-section');
    if (first) openSection(first.id);
  }

  return { init, openSection, speakCurrentSection, stopVoice, gradeQuiz };
})();

document.addEventListener('DOMContentLoaded', TopicShell.init);
