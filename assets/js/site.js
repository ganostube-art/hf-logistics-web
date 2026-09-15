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


  /* 스크롤 등장 — 모션을 끈 사용자에게는 적용하지 않습니다.
     클래스를 JS가 붙이므로, JS가 없으면 처음부터 전부 보입니다. */
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduce && 'IntersectionObserver' in window) {
    var blocks = document.querySelectorAll(
      '.sec-head, .facts .cell, .risks > *, .flow > .s, .svcs > *, ' +
      '.reasons > .rr, .hubs > .hub, .divs > .d, .split > .c, ' +
      '.contact > div, .board-scroll, .nodes, .hist, .steps'
    );

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        io.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    Array.prototype.forEach.call(blocks, function (el) {
      /* 같은 부모 안에서의 순서만큼 지연을 줘 한 줄씩 흐르게 */
      var sibs = el.parentNode ? el.parentNode.children : [el];
      var i = Array.prototype.indexOf.call(sibs, el);
      el.style.transitionDelay = Math.min(i * 55, 330) + 'ms';
      el.classList.add('hf-rv');
      io.observe(el);
    });
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
