/* HF LOGISTICS — 공통 스크립트 */
(function () {
  'use strict';

  /* 모바일 내비게이션 */
  var toggle = document.querySelector('.navtoggle');
  var nav = document.getElementById('nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.textContent = open ? 'CLOSE' : 'MENU';
    });
  }

  /* 현재 페이지 표시 */
  var here = location.pathname.split('/').pop() || 'index.html';
  Array.prototype.forEach.call(document.querySelectorAll('.nav a[href]'), function (a) {
    if (a.getAttribute('href') === here) a.setAttribute('aria-current', 'page');
  });

  /* 푸터 연도 */
  Array.prototype.forEach.call(document.querySelectorAll('[data-year]'), function (el) {
    el.textContent = new Date().getFullYear();
  });


  /* 스크롤 등장 · 숫자 카운트 · 스케줄 행 캐스케이드
     모션을 끈 사용자에게는 적용하지 않습니다.
     클래스를 JS가 붙이므로, JS가 없으면 처음부터 전부 보입니다. */
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!reduce && 'IntersectionObserver' in window) {

    var ease = function (t) { return 1 - Math.pow(1 - t, 3); };

    /* 사실 스트립 숫자를 0에서 올림 */
    var countUp = function (el) {
      var node = el.firstChild;
      if (!node || node.nodeType !== 3) return;
      var raw = node.nodeValue.trim();
      var target = parseFloat(raw.replace(/,/g, ''));
      if (!isFinite(target)) return;
      var grouped = raw.indexOf(',') > -1;
      var t0 = null, dur = 1100;
      var step = function (ts) {
        if (t0 === null) t0 = ts;
        var k = Math.min((ts - t0) / dur, 1);
        var v = Math.round(target * ease(k));
        node.nodeValue = grouped ? v.toLocaleString('en-US') : String(v);
        if (k < 1) requestAnimationFrame(step);
      };
      node.nodeValue = '0';
      requestAnimationFrame(step);
    };

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        var num = e.target.querySelector && e.target.querySelector('.v');
        if (num) countUp(num);
        io.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    var stagger = function (list, cls, per, cap) {
      Array.prototype.forEach.call(list, function (el) {
        var sibs = el.parentNode ? el.parentNode.children : [el];
        var i = Array.prototype.indexOf.call(sibs, el);
        el.style.transitionDelay = Math.min(i * per, cap) + 'ms';
        el.classList.add(cls);
        io.observe(el);
      });
    };

    stagger(document.querySelectorAll(
      '.sec-head, .facts .cell, .risks > *, .flow > .s, .svcs > *, ' +
      '.reasons > .rr, .hubs > .hub, .divs > .d, .split > .c, ' +
      '.contact > div, .nodes, .hist, .steps, .checks'
    ), 'hf-rv', 70, 420);

    stagger(document.querySelectorAll('table.data tbody tr'), 'hf-row', 60, 480);
  }

  /* 스크롤 시 헤더 분리 */
  var head = document.querySelector('.masthead');
  if (head) {
    var onScroll = function () {
      head.classList.toggle('scrolled', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* 견적 요청 폼 — 백엔드 연결 전까지 메일 클라이언트로 전달 */
  var form = document.getElementById('quote-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var get = function (k) { return (d.get(k) || '').toString().trim(); };
      var body = [
        '회사명: ' + get('company'),
        '담당자: ' + get('name'),
        '연락처: ' + get('phone'),
        '이메일: ' + get('email'),
        '문의 유형: ' + get('type'),
        '출발지 / 품목: ' + get('cargo'),
        '',
        '내용',
        get('message')
      ].join('\n');
      location.href = 'mailto:info@hflogistics.co.kr'
        + '?subject=' + encodeURIComponent('[견적·문의] ' + (get('company') || '홈페이지 접수'))
        + '&body=' + encodeURIComponent(body);
      var msg = document.getElementById('quote-status');
      if (msg) msg.textContent = '메일 작성 창을 열었습니다. 전송이 되지 않으면 032-888-0824로 연락 주십시오.';
    });
  }
})();
