/* Ability SPA – shared page script (menu, cookie bar, scroll reveal, header shadow). */
(function () {
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('main-nav');
  if (!btn || !nav) return;
  function setOpen(open) {
    btn.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
  }
  btn.addEventListener('click', function () { setOpen(btn.getAttribute('aria-expanded') !== 'true'); });
  nav.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });

  var bar = document.getElementById('cookie-bar');
  var seen = null;
  try { seen = localStorage.getItem('cookie-ok'); } catch (e) {}
  if (!seen) bar.hidden = false;
  document.getElementById('cookie-ok').addEventListener('click', function () {
    bar.hidden = true;
    try { localStorage.setItem('cookie-ok', '1'); } catch (e) {}
  });


  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Headlines rise in word by word (masked). Only regular spaces split words, so "в&nbsp;Бургас" stays together.
  function splitWords(el) {
    var i = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = document.createDocumentFragment();
          n.textContent.split(/([ \t\n\r]+)/).forEach(function (part) {
            if (!part) return;
            if (/^[ \t\n\r]+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            var w = document.createElement('span'), s = document.createElement('span');
            w.className = 'w'; s.textContent = part; s.style.setProperty('--i', i++);
            w.appendChild(s); frag.appendChild(w);
          });
          n.parentNode.replaceChild(frag, n);
        } else if (n.nodeType === 1 && n.tagName !== 'BR') { walk(n); }
      });
    })(el);
    el.classList.add('split-ready');
  }
  if (!reduce) {
    document.querySelectorAll('.hero h1, .page-hero h1, .section-head h2, .statement-title, .cta-band h2').forEach(splitWords);
    requestAnimationFrame(function () { requestAnimationFrame(function () {
      document.querySelectorAll('.hero h1, .page-hero h1').forEach(function (h) { h.classList.add('words-in'); });
    }); });
  }

  // Scroll reveal: elements fade/rise in once as they enter the viewport.
  var revealSel = '.section-head, .statement-title, .statement-cols, .exp-grid > li, .facts-list > li, .tiles-list > li,' +
    ' .facilities .photo, .facilities .split-text, .spa-day-intro, .spa-day-prices, .first-visit-intro, .faq details,' +
    ' .location, .review, .voucher-card, .voucher-text, .two-col > *, .price-group, .contact-card, .cta-band-inner,' +
    ' .checklist > li, .price-list > div, .class-list > li';
  var items = document.querySelectorAll(revealSel);
  items.forEach(function (el) {
    var i = Array.prototype.indexOf.call(el.parentNode.children, el);
    el.style.setProperty('--d', Math.min(i, 10));   // stagger siblings
  });
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-in'); io.unobserve(e.target);
          if (e.target.classList.contains('split-ready')) e.target.classList.add('words-in');
          e.target.querySelectorAll('.split-ready').forEach(function (h) { h.classList.add('words-in'); });
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('is-in'); });
    document.querySelectorAll('.split-ready').forEach(function (h) { h.classList.add('words-in'); });
  }

  // Parallax: big photos drift a little slower than the page (inside their own frame, never over text).
  var par = [];
  if (!reduce) {
    document.querySelectorAll('.hero-bg, .page-hero-media .photo, .loc-photo').forEach(function (el) { par.push({ el: el, box: el.parentNode, k: .08 }); });
    if (window.matchMedia && matchMedia('(min-width: 1024px)').matches) {
      document.querySelectorAll('.facilities .split > .photo').forEach(function (img) {
        var f = document.createElement('div');
        f.className = 'photo-frame';
        img.parentNode.insertBefore(f, img); f.appendChild(img);
        par.push({ el: img, box: f, k: .07 });
      });
    }
    par.forEach(function (p) { p.el.classList.add('is-parallax'); });
  }
  function parallax() {
    var vh = window.innerHeight;
    par.forEach(function (p) {
      var r = p.box.getBoundingClientRect();
      if (r.bottom < -50 || r.top > vh + 50) return;
      var max = p.el.offsetHeight * .05;
      var y = Math.max(-max, Math.min(max, -(r.top + r.height / 2 - vh / 2) * p.k));
      p.el.style.translate = '0 ' + y.toFixed(1) + 'px';
    });
  }

  // Header: soft shadow once the page scrolls + thin gold reading-progress line
  var header = document.querySelector('.site-header');
  var bar = document.createElement('div');
  bar.className = 'scroll-progress'; bar.setAttribute('aria-hidden', 'true');
  header.appendChild(bar);
  var ticking = false;
  var onScroll = function () {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      ticking = false;
      var max = document.documentElement.scrollHeight - window.innerHeight;
      header.classList.toggle('is-scrolled', window.scrollY > 8);
      bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, window.scrollY / max) : 0).toFixed(4) + ')';
      parallax();
    });
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  onScroll();

  // PROTOTYPE ONLY – remove before launch: links whose target is still a [PLACEHOLDER]
  // show a short note instead of opening a broken page.
  var note;
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a');
    if (!a || !/\[|%5B/.test(a.getAttribute('href') || '')) return;
    e.preventDefault();
    if (!note) {
      note = document.createElement('div');
      note.className = 'proto-note'; note.setAttribute('role', 'status');
      document.body.appendChild(note);
    }
    note.textContent = 'Тази връзка ще бъде добавена скоро.';
    note.classList.add('is-visible');
    clearTimeout(note._t); note._t = setTimeout(function () { note.classList.remove('is-visible'); }, 2600);
  });
})();
