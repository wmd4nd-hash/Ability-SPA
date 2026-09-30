/* Ability Club – prototype interactions. Nothing is saved or paid; all state lives in this page. */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  // ---------- Greeting by time of day ----------
  var h = new Date().getHours();
  $('.hello span').textContent = (h < 11 ? 'Добро утро' : h < 18 ? 'Добър ден' : 'Добър вечер') + ', [ИМЕ]';

  // ---------- Sign in (any button enters – prototype) ----------
  var welcome = $('#welcome');
  $$('[data-enter]').forEach(function (b) {
    b.addEventListener('click', function () {
      welcome.classList.add('is-leaving');
      setTimeout(function () { welcome.hidden = true; drawStamps(); }, 600);
    });
  });

  // ---------- Toast ----------
  var toastEl = $('#toast'), toastT;
  function toast(msg) {
    toastEl.textContent = msg; toastEl.hidden = false;
    clearTimeout(toastT); toastT = setTimeout(function () { toastEl.hidden = true; }, 3200);
  }
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-toast]');
    if (t) toast(t.getAttribute('data-toast'));
  });

  // ---------- Tabs ----------
  function go(id) {
    $$('.screen').forEach(function (s) { s.classList.toggle('is-active', s.id === id); });
    $$('.tabbar button').forEach(function (b) {
      if (b.getAttribute('data-go') === id) b.setAttribute('aria-current', 'page'); else b.removeAttribute('aria-current');
    });
    $('.screens').scrollTop = 0;
    if (id === 's-card') drawStamps();
  }
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-go]');
    if (t) { closeDetail(); go(t.getAttribute('data-go')); }
  });

  // ---------- Stamp track (example: 6 of 10) ----------
  var STAMPS = 6, TOTAL = 10;
  function drawStamps() {
    var pct = STAMPS / TOTAL * 100;
    $('#fill').style.width = '0'; $('#knob').style.left = '0';
    setTimeout(function () { $('#fill').style.width = pct + '%'; $('#knob').style.left = pct + '%'; }, 80);
    $('#count').textContent = STAMPS; $('#bubble').textContent = STAMPS; $('#left').textContent = TOTAL - STAMPS;
  }
  if (welcome.hidden) drawStamps();

  // ---------- Push preview ----------
  $('#bell').addEventListener('click', function () {
    var p = $('#push');
    p.hidden = false;
    setTimeout(function () { p.hidden = true; }, 4200);
  });
  $('#push').addEventListener('click', function () { this.hidden = true; openDetail(1); });

  // ---------- Offers (real Burgas autumn offers, valid 28.09 – 19.10.2026) ----------
  var OFFERS = [
    ['Годишна фитнес карта', 'Фитнес зона, уреди Technogym и протеинов бар.', '260 €', '−13%', '../images/spa-burgas-fitnes-technogym-zala-1080.webp'],
    ['Годишна СПА карта', 'Фитнес, басейн и джакузи, термална зона.', '750 €', '−40%', '../images/spa-burgas-basein-simetrichen-1080.webp'],
    ['20 посещения на басейн', 'Басейн и джакузи.', '125 €', '−12%', '../images/spa-burgas-dzhakuzi-basein-1080.webp'],
    ['Пакет „Фитнес“', 'Месечна фитнес карта и 5 посещения на термалната зона.', '55 €', '−24%', '../images/finlandska-sauna-burgas-1080.webp'],
    ['Пакет „Спорт“', 'Месечна фитнес карта и 3 спортни масажа.', '130 €', '−14%', '../images/masazh-goreshti-kamani-burgas-1080.webp'],
    ['Пакет 20 СПА посещения', 'Басейн и джакузи, фитнес и термална зона.', '200 €', '−15%', '../images/spa-burgas-basein-shezlongi-1080.webp']
  ];
  var START = new Date(2026, 8, 28), END = new Date(2026, 9, 19, 23, 59);
  $('#offers').innerHTML = OFFERS.map(function (o, i) {
    return '<li><button class="offer" type="button" style="--i:' + i + '" data-offer="' + i + '">' +
      '<img src="' + o[4] + '" alt="" width="1080" height="1080">' +
      '<span><span class="offer-t">' + o[0] + '</span><span class="offer-d">' + o[1] + '</span></span>' +
      '<span class="offer-p"><b>' + o[2] + '</b><span>' + o[3] + '</span></span></button></li>';
  }).join('');
  $$('[data-city]').forEach(function (b) {
    b.addEventListener('click', function () {
      $$('[data-city]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      $('#city-burgas').hidden = b.getAttribute('data-city') !== 'burgas';
      $('#city-varna').hidden = b.getAttribute('data-city') !== 'varna';
    });
  });

  // ---------- Offer detail: price as the "time", validity as the progress bar ----------
  var detail = $('#detail'), cur = 0, opener;
  function daysLeft() {
    var now = new Date();
    if (now > END) return { pct: 100, label: 'изтекла' };
    if (now < START) return { pct: 0, label: 'от 28.09' };
    var left = Math.ceil((END - now) / 864e5);
    return { pct: (now - START) / (END - START) * 100, label: left === 1 ? '1 ден' : left + ' дни' };
  }
  function fillDetail(i) {
    var o = OFFERS[i], d = daysLeft();
    cur = i;
    $('#d-img').src = o[4];
    $('#d-t').textContent = o[0];
    $('#d-d').textContent = o[1];
    $('#d-off').textContent = o[3] + ' до 19.10';
    $('#d-p').textContent = o[2];
    $('#d-left').textContent = d.label;
    $('#d-fill').style.width = '0'; $('#d-knob').style.left = '0';
    setTimeout(function () { $('#d-fill').style.width = d.pct + '%'; $('#d-knob').style.left = d.pct + '%'; }, 80);
  }
  function openDetail(i) { fillDetail(i); detail.hidden = false; $('#d-back').focus(); }
  function closeDetail() { if (!detail.hidden) { detail.hidden = true; if (opener) opener.focus(); } }
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-offer]');
    if (t) { opener = t; openDetail(+t.getAttribute('data-offer')); }
  });
  $('#d-back').addEventListener('click', closeDetail);
  $('#d-prev').addEventListener('click', function () { fillDetail((cur + OFFERS.length - 1) % OFFERS.length); });
  $('#d-next').addEventListener('click', function () { fillDetail((cur + 1) % OFFERS.length); });

  // "Show at reception" sheet
  var sheet = $('#sheet');
  $('#d-show').addEventListener('click', function () {
    var o = OFFERS[cur];
    $('#sheet-t').textContent = o[0];
    $('#sheet-d').textContent = o[2] + ' · ' + o[3] + ' · до 19.10.2026';
    sheet.hidden = false; $('#sheet-close').focus();
  });
  function closeSheet() { sheet.hidden = true; $('#d-show').focus(); }
  $('#sheet-close').addEventListener('click', closeSheet);
  sheet.addEventListener('click', function (e) { if (e.target === sheet) closeSheet(); });
  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (!sheet.hidden) closeSheet(); else closeDetail();
  });

  // ---------- Gift voucher flow ----------
  // Prices from the Burgas spa menu (Dec 2025) and the Burgas offers page (voucher amounts)
  var CHOICES = [
    ['Сума', 'Получателят избира сам', 50],
    ['Сума', 'Получателят избира сам', 100],
    ['Пакет „Релакс“', 'Дневна СПА карта + релаксиращ масаж 60 мин', 52],
    ['Класически масаж', 'На цяло тяло, 60 мин', 45],
    ['Хамам', 'Турска баня, пилинг и пенен масаж, 45 мин', 55],
    ['СПА пакет за двама', '2 масажа, цял ден СПА, солна стая и вино', 120]
  ];
  var gift = { choice: 0, city: 'Бургас' };
  $('#gift-choices').innerHTML = CHOICES.map(function (c, i) {
    return '<button type="button" class="choice" aria-pressed="' + (i === 0) + '" data-choice="' + i + '"><span>' + c[0] +
      (c[0] === 'Сума' ? ' ' + c[2] + ' €' : '') + '<small>' + c[1] + '</small></span><b>' + c[2] + ' €</b></button>';
  }).join('');
  $$('[data-choice]').forEach(function (b) {
    b.addEventListener('click', function () {
      gift.choice = +b.getAttribute('data-choice');
      $$('[data-choice]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
    });
  });
  $$('[data-gcity]').forEach(function (b) {
    b.addEventListener('click', function () {
      gift.city = b.getAttribute('data-gcity');
      $$('[data-gcity]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
    });
  });

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function voucherHTML() {
    var c = CHOICES[gift.choice], to = $('#g-to').value.trim(), msg = $('#g-msg').value.trim();
    var until = new Date(); until.setFullYear(until.getFullYear() + 1);
    return '<img src="../images/logo-horizontal-light.png" alt="Ability SPA">' +
      '<p class="v-what">' + esc(c[0] === 'Сума' ? 'Ваучер за ' + c[2] + ' €' : c[0]) + '</p>' +
      '<p class="v-to">За: ' + esc(to || '[ИМЕ]') + '</p>' + (msg ? '<p class="v-msg">„' + esc(msg) + '“</p>' : '') +
      '<p class="v-meta"><span>' + esc(gift.city) + '</span><span>до ' + until.toLocaleDateString('bg-BG') + '</span></p>';
  }
  function step(n) {
    [1, 2, 3].forEach(function (i) {
      $('#g' + i).hidden = i !== n;
      $('#st' + i).classList.toggle('is-on', i <= n);
    });
    if (n === 3) { $('#v-preview').innerHTML = voucherHTML(); $('#pay-sum').textContent = CHOICES[gift.choice][2] + ' €'; }
    $('.screens').scrollTop = 0;
  }
  $$('[data-next]').forEach(function (b) {
    b.addEventListener('click', function () {
      var n = +b.getAttribute('data-next');
      if (n === 3 && !$('#g-to').value.trim()) { $('#g-to').focus(); toast('Добавете име на получателя.'); return; }
      step(n);
    });
  });

  var mine = [];
  $('#pay').addEventListener('click', function () {
    var c = CHOICES[gift.choice];
    mine.push([c[0] === 'Сума' ? 'Ваучер ' + c[2] + ' €' : c[0], $('#g-to').value.trim(), gift.city]);
    $('#my-vouchers').innerHTML = mine.map(function (v) {
      return '<li><span>' + esc(v[0]) + ' · за ' + esc(v[1]) + '</span><b>' + esc(v[2]) + '</b></li>';
    }).join('');
    $('#g3').hidden = true;
    var ok = document.createElement('div');
    ok.className = 'success';
    ok.innerHTML = '<div class="tick"><svg viewBox="0 0 24 24"><path d="M5 12.5 10 17l9-10"/></svg></div>' +
      '<h3>Ваучерът е готов</h3><p>В реалната версия: PDF по имейл и бутон „Добави в Wallet“ за получателя.</p>' +
      '<button class="light-btn" type="button" id="again">Още един подарък</button>' +
      '<button class="dark-btn" type="button" data-go="s-mine">Моите ваучери</button>';
    $('#gift-form').appendChild(ok);
    $('#again').addEventListener('click', function () {
      ok.remove(); $('#g-to').value = ''; $('#g-msg').value = ''; step(1);
    });
  });
})();
