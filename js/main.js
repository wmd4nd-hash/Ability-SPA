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

  // Scroll reveal: elements fade/rise in once as they enter the viewport.
  var revealSel = '.section-head, .statement-title, .statement-cols, .exp-grid > li, .facts-list > li, .tiles-list > li,' +
    ' .facilities .photo, .facilities .split-text, .spa-day-intro, .spa-day-prices, .first-visit-intro, .faq details,' +
    ' .location, .review, .voucher-card, .voucher-text, .two-col > *, .price-group, .contact-card, .cta-band-inner';
  var items = document.querySelectorAll(revealSel);
  items.forEach(function (el) {
    var i = Array.prototype.indexOf.call(el.parentNode.children, el);
    el.style.setProperty('--d', Math.min(i, 5));   // stagger siblings
  });
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('is-in'); });
  }

  // Header gets a soft shadow once the page scrolls
  var header = document.querySelector('.site-header');
  var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 8); };
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();

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
