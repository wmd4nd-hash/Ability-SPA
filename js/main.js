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


  // PROTOTYPE ONLY – colour palettes to compare. Shown once a page is opened with ?palette=a…g (kept while browsing).
  if (document.documentElement.hasAttribute('data-palette-ui')) {
    var pals = [['a', 'Сегашна', '#FFFFFF', '#201A18'], ['b', 'Топъл пясък', '#DDD3C0', '#201A18'], ['c', 'Злато', '#C39F76', '#201A18'],
      ['d', 'Мока', '#F1E9DC', '#3A2C26'], ['e', 'Вечер', '#201A18', '#C39F76'], ['f', 'Басейн', '#F1ECE3', '#16302F'],
      ['g', 'Светла', '#F7F2EA', '#201A18']];
    var pick = document.createElement('div');
    pick.className = 'palette-picker'; pick.setAttribute('role', 'group'); pick.setAttribute('aria-label', 'Цветова комбинация (прототип)');
    pick.innerHTML = '<button type="button" class="pp-toggle" aria-expanded="false" aria-label="Цветове"><i></i></button><span>Цветове</span>' + pals.map(function (x) {
      return '<button type="button" data-p="' + x[0] + '" aria-label="' + x[0].toUpperCase() + ' · ' + x[1] + '" title="' + x[0].toUpperCase() + ' · ' + x[1] + '"><i style="--a:' + x[2] + ';--b:' + x[3] + '"></i></button>';
    }).join('');
    var mark = function () {
      var cur = document.documentElement.getAttribute('data-palette') || 'a';
      pick.querySelectorAll('[data-p]').forEach(function (b) {
        var on = b.getAttribute('data-p') === cur;
        b.setAttribute('aria-pressed', String(on));
        if (on) pick.querySelector('.pp-toggle i').setAttribute('style', b.querySelector('i').getAttribute('style'));
      });
    };
    pick.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      if (b.classList.contains('pp-toggle')) { var o = pick.classList.toggle('is-open'); b.setAttribute('aria-expanded', String(o)); return; }
      var v = b.getAttribute('data-p');
      document.documentElement.setAttribute('data-palette', v);
      try { sessionStorage.setItem('palette', v); history.replaceState(null, '', location.pathname + '?palette=' + v + location.hash); } catch (err) {}
      mark(); pick.classList.remove('is-open'); pick.querySelector('.pp-toggle').setAttribute('aria-expanded', 'false');
    });
    mark(); document.body.appendChild(pick);
  }

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
    document.querySelectorAll('.hero h1, .hero2 h1, .page-hero h1, .section-head h2, .statement-title, .cta-band h2').forEach(splitWords);
    requestAnimationFrame(function () { requestAnimationFrame(function () {
      document.querySelectorAll('.hero h1, .hero2 h1, .page-hero h1').forEach(function (h) { h.classList.add('words-in'); });
    }); });
  }

  // Scroll reveal: elements fade/rise in once as they enter the viewport.
  var revealSel = '.section-head, .statement-title, .statement-cols, .exp-grid > li, .facts-list > li, .tiles-list > li,' +
    ' .facilities .photo, .facilities .split-text, .spa-day-intro, .spa-day-prices, .first-visit-intro, .faq details,' +
    ' .location, .review, .voucher-card, .voucher-text, .two-col > *, .price-group, .contact-card, .cta-band-inner,' +
    ' .checklist > li, .price-list > div, .class-list > li, .about-text > p, .about-facts > li, .spots-bar, .spots';
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

  // Бургас / Варна switch (homepage): changes every 5 s. The timer is an invisible CSS animation on the active tab
  // animation; when it ends, the next city shows – so pausing it (button, hover, focus, off-screen) pauses the switch.
  // Picking a city stops the automatic change for good; reduced motion never starts it.
  document.querySelectorAll('.city-switch').forEach(function (sw) {
    var tabs = Array.prototype.slice.call(sw.querySelectorAll('[role="tab"]'));
    var pause = sw.querySelector('.cs-pause');
    function select(tab, focus) {
      tabs.forEach(function (t) {
        var on = t === tab;
        t.setAttribute('aria-selected', String(on)); t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute('aria-controls')).classList.toggle('is-active', on);
      });
      if (focus) tab.focus();
    }
    function stop() { sw.classList.remove('is-auto'); }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { stop(); select(t); });
      t.addEventListener('keydown', function (e) {
        var n = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (!n) return;
        e.preventDefault(); stop(); select(tabs[(i + n + tabs.length) % tabs.length], true);
      });
      t.querySelector('.cs-bar').addEventListener('animationend', function () {
        if (sw.classList.contains('is-auto')) select(tabs[(i + 1) % tabs.length]);
      });
    });
    if (reduce || tabs.length < 2) return;
    sw.classList.add('is-auto');
    pause.addEventListener('click', function () {
      var paused = sw.classList.toggle('is-paused');
      pause.setAttribute('aria-pressed', String(paused));
      pause.setAttribute('aria-label', pause.getAttribute(paused ? 'data-play' : 'data-pause'));
    });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) { sw.classList.toggle('is-offscreen', !en[0].isIntersecting); }).observe(sw);
    }
  });

  // Locations carousel (homepage): arrows page through it, the Бургас / Варна chips jump to each city's intro card
  // and show which city is in view. Without JS it is a plain sideways-scrolling row and the chips are anchor links.
  document.querySelectorAll('.spots-wrap').forEach(function (w) {
    var track = w.querySelector('.spots');
    var btns = w.querySelectorAll('.spots-btn');
    var chips = Array.prototype.slice.call(w.querySelectorAll('.chip'));
    var how = reduce ? 'auto' : 'smooth';
    function leftOf(el) {
      return track.scrollLeft + el.getBoundingClientRect().left - track.getBoundingClientRect().left - parseFloat(getComputedStyle(track).paddingLeft);
    }
    function update() {
      var x = track.scrollLeft, max = track.scrollWidth - track.clientWidth;
      btns[0].disabled = x <= 2; btns[1].disabled = x >= max - 2;
      var mid = track.getBoundingClientRect().left + track.clientWidth / 2, cur = chips[0];
      chips.forEach(function (c) {
        var t = document.getElementById(c.getAttribute('href').slice(1));
        if (t && t.getBoundingClientRect().left <= mid) cur = c;
      });
      if (x >= max - 2) cur = chips[chips.length - 1];
      chips.forEach(function (c) { if (c === cur) c.setAttribute('aria-current', 'true'); else c.removeAttribute('aria-current'); });
      // focusable for keyboard scrolling only while it actually scrolls sideways
      if (max > 1) track.setAttribute('tabindex', '0'); else track.removeAttribute('tabindex');
    }
    btns.forEach(function (b) {
      b.addEventListener('click', function () { track.scrollBy({ left: +b.getAttribute('data-dir') * track.clientWidth * .8, behavior: how }); });
    });
    chips.forEach(function (c) {
      c.addEventListener('click', function (e) {
        var t = document.getElementById(c.getAttribute('href').slice(1));
        if (!t) return;
        e.preventDefault();
        track.scrollTo({ left: leftOf(t), behavior: how });
      });
    });
    var queued = false;
    track.addEventListener('scroll', function () {
      if (queued) return; queued = true;
      requestAnimationFrame(function () { queued = false; update(); });
    }, { passive: true });
    window.addEventListener('resize', update);
    update();
  });

  // Parallax: big photos drift a little slower than the page (inside their own frame, never over text).
  var par = [];
  if (!reduce) {
    document.querySelectorAll('.hero-bg, .page-hero-media .photo, .loc-photo, .city-img').forEach(function (el) { par.push({ el: el, box: el.parentNode, k: .08 }); });
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

  // Language offer: visitors whose browser is not in the page's language (e.g. hotel guests from abroad)
  // get one line at the very top with a link to the other language. Dismissed once = gone.
  (function () {
    var lang = document.documentElement.lang === 'en' ? 'en' : 'bg';
    var other = lang === 'bg' ? 'en' : 'bg';
    var langs = (navigator.languages && navigator.languages.length ? navigator.languages : [navigator.language || '']).map(function (l) { return String(l).toLowerCase(); });
    var wantsBg = langs.some(function (l) { return l.indexOf('bg') === 0; });
    if ((lang === 'bg') === wantsBg) return;
    try { if (localStorage.getItem('lang-hint-off')) return; } catch (e) {}
    var link = document.querySelector('.lang a[lang="' + other + '"]');
    if (!link) return;
    var hint = document.createElement('div');
    hint.className = 'lang-hint'; hint.setAttribute('role', 'region'); hint.setAttribute('aria-label', other === 'en' ? 'Language' : 'Език');
    hint.innerHTML = other === 'en'
      ? '<p lang="en">This website is also in English.</p><a lang="en" hreflang="en">English</a><button type="button" aria-label="Close">×</button>'
      : '<p lang="bg">Сайтът е и на български.</p><a lang="bg" hreflang="bg">Български</a><button type="button" aria-label="Затвори">×</button>';
    hint.querySelector('a').href = link.href;
    hint.querySelector('button').addEventListener('click', function () {
      hint.remove();
      try { localStorage.setItem('lang-hint-off', '1'); } catch (e) {}
    });
    var skip = document.querySelector('.skip-link');
    document.body.insertBefore(hint, skip ? skip.nextSibling : document.body.firstChild);
  })();

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
