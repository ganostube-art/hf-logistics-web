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
