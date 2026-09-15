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



  /* 히어로 슬라이더 — 해상 · 항공 · 중장비
     JS가 .js-on 을 붙이기 전에는 첫 슬라이드가 그대로 보이므로,
     스크립트가 막혀도 히어로가 비지 않습니다. */
  (function () {
    var box = document.getElementById('slides');
    if (!box) return;
    var slides = box.querySelectorAll('.slide');
    var tabs = document.querySelectorAll('.hdot');
    if (slides.length < 2) return;

    var HOLD = 6500;
    var slow = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var cur = 0, timer = null, paused = false;

    box.classList.add('js-on');

    var show = function (i) {
      cur = (i + slides.length) % slides.length;
      Array.prototype.forEach.call(slides, function (el, k) {
        el.classList.toggle('is-active', k === cur);
        el.setAttribute('aria-hidden', k === cur ? 'false' : 'true');
      });
      Array.prototype.forEach.call(tabs, function (t, k) {
        var on = k === cur;
        t.setAttribute('aria-selected', on ? 'true' : 'false');
        t.setAttribute('tabindex', on ? '0' : '-1');
        var bar = t.querySelector('.bar');
        if (!bar) return;
        /* 진행 막대를 0에서 다시 채웁니다 */
        bar.style.transition = 'none';
        bar.style.width = '0';
        if (on && !slow && !paused) {
          void bar.offsetWidth;
          bar.style.transition = 'width ' + HOLD + 'ms linear';
          bar.style.width = '100%';
        }
      });
    };

    var stop = function () {
      if (timer) { clearInterval(timer); timer = null; }
    };
    var play = function () {
      stop();
      if (slow) return;
      timer = setInterval(function () { show(cur + 1); }, HOLD);
    };

    var go = function (i) { show(i); play(); };

    Array.prototype.forEach.call(tabs, function (t, k) {
      t.addEventListener('click', function () { go(k); });
      t.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight') { e.preventDefault(); go(cur + 1); tabs[(cur) % tabs.length].focus(); }
        if (e.key === 'ArrowLeft') { e.preventDefault(); go(cur - 1); tabs[(cur) % tabs.length].focus(); }
      });
    });

    /* 읽는 동안에는 넘어가지 않게 */
    var hold = function () { paused = true; stop(); };
    var release = function () { paused = false; show(cur); play(); };
    box.addEventListener('mouseenter', hold);
    box.addEventListener('mouseleave', release);
    box.addEventListener('focusin', hold);
    box.addEventListener('focusout', release);
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) stop(); else if (!paused) { show(cur); play(); }
    });

    show(0);
    play();
  })();

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
        if (e.target.querySelectorAll) {
          Array.prototype.forEach.call(e.target.querySelectorAll('.v'), countUp);
        }
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
      '.sec-head, .facts .grid, .risks, .flow, .svcs, .reasons, ' +
      '.hubs, .divs, .split, .contact, .nodes, .hist, .steps, .checks'
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

  /* 견적 요청 폼 — 백엔드 연결 전까지 메일 클라이언트로 전달.
     문구는 <html lang> 을 보고 고릅니다. */
  var form = document.getElementById('quote-form');
  if (form) {
    var L = (document.documentElement.lang || 'ko').slice(0, 2);
    var T = {
      ko: {co:'회사명', nm:'담당자', ph:'연락처', em:'이메일', ty:'문의 유형', cg:'출발지 / 품목',
           ms:'내용', sub:'[견적·문의]', anon:'홈페이지 접수',
           ok:'메일 작성 창을 열었습니다. 전송이 되지 않으면 032-888-0824로 연락 주십시오.'},
      en: {co:'Company', nm:'Contact', ph:'Phone', em:'Email', ty:'Enquiry type', cg:'Origin / Cargo',
           ms:'Message', sub:'[Quote enquiry]', anon:'Website enquiry',
           ok:'Your email client should now be open. If the message does not send, please call +82-32-888-0824.'},
      zh: {co:'公司名称', nm:'联系人', ph:'联系电话', em:'邮箱', ty:'咨询类型', cg:'起运地 / 品名',
           ms:'咨询内容', sub:'[报价咨询]', anon:'网站咨询',
           ok:'已打开邮件撰写窗口。若无法发送，请致电 +82-32-888-0824。'}
    }[L] || null;
    if (T) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var d = new FormData(form);
        var g = function (k) { return (d.get(k) || '').toString().trim(); };
        var body = [
          T.co + ': ' + g('company'), T.nm + ': ' + g('name'),
          T.ph + ': ' + g('phone'), T.em + ': ' + g('email'),
          T.ty + ': ' + g('type'), T.cg + ': ' + g('cargo'),
          '', T.ms, g('message')
        ].join('\n');
        location.href = 'mailto:dydw0625@nate.com'
          + '?subject=' + encodeURIComponent(T.sub + ' ' + (g('company') || T.anon))
          + '&body=' + encodeURIComponent(body);
        var msg = document.getElementById('quote-status');
        if (msg) msg.textContent = T.ok;
      });
    }
  }
})();
