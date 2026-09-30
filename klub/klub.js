/* Ability Club – prototype interactions. Nothing is saved or paid; all state lives in this page. */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

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
    if (t) go(t.getAttribute('data-go'));
  });

  // ---------- Stamp card (example: 6 of 10) ----------
  var STAMPS = 6, TOTAL = 10;
  var check = '<svg viewBox="0 0 24 24"><path d="M9.5 16.2 5.3 12l-1.4 1.4 5.6 5.6L20.1 8.4 18.7 7z"/></svg>';
  var giftIcon = '<svg viewBox="0 0 24 24"><path d="M4 11h16v9H4zM3 7h18v4H3zM12 7v13M12 7c-2-4-6-3-5 0M12 7c2-4 6-3 5 0"/></svg>';
  function drawStamps() {
    var html = '';
    for (var i = 0; i < TOTAL; i++) {
      if (i < STAMPS) html += '<li class="on" style="--i:' + i + '">' + check + '</li>';
      else if (i === TOTAL - 1) html += '<li class="gift">' + giftIcon + '</li>';
      else html += '<li></li>';
    }
    $('#stamps').innerHTML = html;
    $('#left').textContent = TOTAL - STAMPS;
  }
  drawStamps();

  // ---------- Push preview ----------
  $('#bell').addEventListener('click', function () {
    var p = $('#push');
    p.hidden = false;
    setTimeout(function () { p.hidden = true; }, 4200);
  });
  $('#push').addEventListener('click', function () { this.hidden = true; go('s-promo'); });

  // ---------- Promotions (real Burgas autumn offers, valid 28.09 – 19.10.2026) ----------
  var OFFERS = [
    ['Годишна фитнес карта', 'Фитнес зона, уреди Technogym, протеинов бар', '260 €', '−13%'],
    ['Годишна СПА карта', 'Фитнес, басейн и джакузи, термална зона', '750 €', '−40%'],
    ['20 посещения на басейн', 'Басейн и джакузи', '125 €', '−12%'],
    ['Пакет „Фитнес“', 'Месечна фитнес карта + 5 посещения термална зона', '55 €', '−24%'],
    ['Пакет „Спорт“', 'Месечна фитнес карта + 3 спортни масажа', '130 €', '−14%'],
    ['Пакет 20 СПА посещения', 'Басейн и джакузи, фитнес, термална зона', '200 €', '−15%']
  ];
  $('#offers').innerHTML = OFFERS.map(function (o, i) {
    return '<li><button class="offer" type="button" style="--i:' + i + '" data-offer="' + i + '">' +
      '<span class="offer-t">' + o[0] + '</span><span class="offer-d">' + o[1] + '</span>' +
      '<span class="offer-p"><b>' + o[2] + '</b><span>' + o[3] + '</span></span></button></li>';
  }).join('');
  $$('[data-city]').forEach(function (b) {
    b.addEventListener('click', function () {
      $$('[data-city]').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      $('#city-burgas').hidden = b.getAttribute('data-city') !== 'burgas';
      $('#city-varna').hidden = b.getAttribute('data-city') !== 'varna';
    });
  });

  // Offer sheet
  var sheet = $('#sheet'), lastFocus;
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-offer]');
    if (!t) return;
    var o = OFFERS[+t.getAttribute('data-offer')];
    $('#sheet-t').textContent = o[0];
    $('#sheet-d').textContent = o[1] + ' · ' + o[2] + ' · до 19.10.2026';
    lastFocus = t; sheet.hidden = false; $('#sheet-close').focus();
  });
  function closeSheet() { sheet.hidden = true; if (lastFocus) lastFocus.focus(); }
  $('#sheet-close').addEventListener('click', closeSheet);
  sheet.addEventListener('click', function (e) { if (e.target === sheet) closeSheet(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !sheet.hidden) closeSheet(); });

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
      '<button class="btn btn-dark btn-block" type="button" id="again">Още един подарък</button>' +
      '<button class="btn btn-outline btn-block" type="button" data-go="s-mine">Моите ваучери</button>';
    $('#gift-form').appendChild(ok);
    $('#again').addEventListener('click', function () {
      ok.remove(); $('#g-to').value = ''; $('#g-msg').value = ''; step(1);
    });
  });
})();
