(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Intro logo animation (once per browser session) ---------- */
  const intro = $('.intro-loader');
  if (intro && document.documentElement.classList.contains('intro')) {
    const finish = () => {
      document.documentElement.classList.remove('intro');
      intro.remove();
      try { sessionStorage.setItem('introSeen', '1'); } catch (e) {}
    };
    intro.addEventListener('animationend', (e) => { if (e.target === intro) finish(); });
    setTimeout(() => { if (intro.isConnected) finish(); }, 4000); // safety net
  } else if (intro) {
    intro.remove();
  }

  /* ---------- Theme toggle ---------- */
  $('#theme-toggle').addEventListener('click', () => {
    const next = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.dataset.theme = next;
    try { localStorage.setItem('theme', next); } catch (e) {}
  });

  /* ---------- Typing tagline ---------- */
  const typed = $('#typed');
  const lines = JSON.parse(typed.dataset.lines || '[]');
  if (reduceMotion) { typed.textContent = lines[0] || ''; }
  else if (lines.length) {
    let li = 0, ci = 0, deleting = false;
    (function tick() {
      const line = lines[li];
      ci += deleting ? -1 : 1;
      typed.textContent = line.slice(0, ci);
      let delay = deleting ? 35 : 70;
      if (!deleting && ci === line.length) { deleting = true; delay = 1800; }
      else if (deleting && ci === 0) { deleting = false; li = (li + 1) % lines.length; delay = 400; }
      setTimeout(tick, delay);
    })();
  }

  /* ---------- Reveal on scroll + count-up stats ---------- */
  const countUp = (el) => {
    const target = +el.dataset.count;
    if (reduceMotion) { el.textContent = target; return; }
    const start = performance.now(), dur = 1400;
    const step = (now) => {
      const p = Math.min((now - start) / dur, 1);
      el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      e.target.classList.add('visible');
      $$('[data-count]', e.target).forEach(countUp);
      io.unobserve(e.target);
    });
  }, { threshold: 0.12 });
  $$('.reveal').forEach((el) => io.observe(el));

  /* ---------- Active nav link ---------- */
  const navLinks = $$('.nav-links a');
  const sectionIO = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) navLinks.forEach((a) => a.classList.toggle('active', a.hash === '#' + e.target.id));
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  $$('section[id]').forEach((s) => sectionIO.observe(s));

  /* ---------- Experience accordion ---------- */
  $$('.job-head').forEach((btn) => btn.addEventListener('click', () => {
    const open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', String(!open));
    btn.nextElementSibling.hidden = open;
  }));

  /* ---------- Project category tabs ---------- */
  const tabs = $$('.tab');
  tabs.forEach((tab) => tab.addEventListener('click', () => {
    tabs.forEach((t) => t.classList.toggle('active', t === tab));
    const cat = tab.dataset.cat;
    $$('.project').forEach((p) => p.classList.toggle('hidden-cat', cat !== 'All' && p.dataset.cat !== cat));
  }));

  /* ---------- Skill filter: highlight jobs & projects using a skill ---------- */
  const chips = $$('.chip');
  const items = $$('.job, .project');
  const result = $('#skill-result');
  const clearBtn = $('#clear-skill');
  const norm = (s) => s.toLowerCase().replace(/\.js$/, '');

  function applySkill(skill) {
    chips.forEach((c) => c.classList.toggle('active', c.dataset.skill === skill));
    clearBtn.hidden = !skill;
    if (!skill) {
      items.forEach((it) => it.classList.remove('dim'));
      $$('.tag.hit').forEach((t) => t.classList.remove('hit'));
      result.hidden = true;
      return;
    }
    let jobs = 0, projects = 0;
    items.forEach((it) => {
      const has = it.dataset.skills.split('|').some((s) => norm(s) === norm(skill));
      it.classList.toggle('dim', !has);
      $$('.tag', it).forEach((t) => t.classList.toggle('hit', norm(t.textContent) === norm(skill)));
      if (has) it.classList.contains('job') ? jobs++ : projects++;
      if (has && it.classList.contains('job')) {
        const head = $('.job-head', it);
        head.setAttribute('aria-expanded', 'true');
        head.nextElementSibling.hidden = false;
      }
    });
    // A filter shouldn't hide matches behind a category tab.
    $('.tab[data-cat="All"]').click();
    result.hidden = false;
    result.innerHTML = (jobs || projects)
      ? `<strong>${skill}</strong>: used in ${jobs} role${jobs === 1 ? '' : 's'} and ${projects} project${projects === 1 ? '' : 's'}, highlighted below. ` +
        `<a href="#experience">Jump to experience ↓</a>`
      : `<strong>${skill}</strong> is part of Neelima's toolkit. <button class="link-btn" data-ask="What experience does Neelima have with ${skill}?">Ask the assistant about it →</button>`;
  }
  chips.forEach((c) => c.addEventListener('click', () =>
    applySkill(c.classList.contains('active') ? null : c.dataset.skill)));
  clearBtn.addEventListener('click', () => applySkill(null));
  result.addEventListener('click', (e) => { if (e.target.dataset.ask) askQuestion(e.target.dataset.ask); });

  /* ---------- Copy email ---------- */
  $('#copy-email').addEventListener('click', async (e) => {
    const email = e.currentTarget.dataset.email;
    try { await navigator.clipboard.writeText(email); $('#copied').hidden = false; setTimeout(() => ($('#copied').hidden = true), 2500); }
    catch { window.location.href = 'mailto:' + email; }
  });

  /* =================================================================
     Chat assistant
     ================================================================= */
  const chat = $('#chat'), log = $('#chat-log'), form = $('#chat-form'), input = $('#chat-input');
  const sendBtn = $('.send', form), fab = $('.chat-fab');
  const history = []; // {role, content}
  let busy = false;

  const openChat = () => {
    chat.hidden = false; fab.classList.add('seen');
    try { sessionStorage.setItem('chatSeen', '1'); } catch (e) {}
    setTimeout(() => input.focus(), 50);
  };
  try { if (sessionStorage.getItem('chatSeen')) fab.classList.add('seen'); } catch (e) {}
  $$('[data-open-chat]').forEach((b) => b.addEventListener('click', () => (chat.hidden ? openChat() : (chat.hidden = true))));
  $('#chat-close').addEventListener('click', () => (chat.hidden = true));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') chat.hidden = true; });
  $$('.suggest').forEach((b) => b.addEventListener('click', () => askQuestion(b.textContent)));
  $$('.ask-about').forEach((b) => b.addEventListener('click', () => askQuestion(b.dataset.question)));

  // Minimal, safe markdown: escape HTML first, then **bold**, bullet lists, paragraphs.
  const esc = (s) => s.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  function renderMd(text) {
    const out = []; let list = null;
    for (const raw of esc(text).split('\n')) {
      const line = raw.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
      const m = line.match(/^\s*[-*•]\s+(.*)/);
      if (m) { (list ||= []).push(`<li>${m[1]}</li>`); continue; }
      if (list) { out.push(`<ul>${list.join('')}</ul>`); list = null; }
      if (line.trim()) out.push(`<p>${line}</p>`);
    }
    if (list) out.push(`<ul>${list.join('')}</ul>`);
    return out.join('');
  }

  function addMsg(cls, html) {
    const div = document.createElement('div');
    div.className = 'msg ' + cls;
    div.innerHTML = html;
    log.appendChild(div);
    log.scrollTop = log.scrollHeight;
    return div;
  }

  function askQuestion(q) {
    if (chat.hidden) openChat();
    input.value = q;
    form.requestSubmit();
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const q = input.value.trim();
    if (!q || busy) return;
    busy = true; sendBtn.disabled = true; input.value = '';
    $('#suggestions')?.remove();

    addMsg('user', esc(q));
    history.push({ role: 'user', content: q });
    const bubble = addMsg('bot', '<span class="typing"><span></span><span></span><span></span></span>');
    let answer = '', errored = false;

    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ messages: history }),
      });
      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        throw new Error(body.error || 'Something went wrong. Please try again.');
      }
      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let buf = '';
      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        buf += decoder.decode(value, { stream: true });
        let nl;
        while ((nl = buf.indexOf('\n')) >= 0) {
          const line = buf.slice(0, nl); buf = buf.slice(nl + 1);
          if (!line.trim()) continue;
          const evt = JSON.parse(line);
          if (evt.error) throw new Error(evt.error);
          answer += evt.t;
          bubble.innerHTML = renderMd(answer);
          log.scrollTop = log.scrollHeight;
        }
      }
      if (!answer) throw new Error('No response received. Please try again.');
      history.push({ role: 'assistant', content: answer });
    } catch (err) {
      errored = true;
      history.pop(); // drop the unanswered question so the conversation stays valid
      bubble.className = 'msg error';
      bubble.textContent = err.message;
    } finally {
      busy = false; sendBtn.disabled = false;
      if (!errored) input.focus();
    }
  });
})();
