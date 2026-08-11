(function () {
  'use strict';

  // Sticky header border
  var header = document.getElementById('header');
  function onScroll() {
    header.classList.toggle('is-stuck', window.scrollY > 12);
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mobile menu
  var burger = document.getElementById('burger');
  var nav = document.getElementById('nav');
  function closeMenu() {
    nav.classList.remove('is-open');
    burger.classList.remove('is-open');
    burger.setAttribute('aria-expanded', 'false');
  }
  burger.addEventListener('click', function () {
    var open = nav.classList.toggle('is-open');
    burger.classList.toggle('is-open', open);
    burger.setAttribute('aria-expanded', String(open));
  });
  nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') closeMenu();
  });
  window.addEventListener('resize', function () {
    if (window.innerWidth > 960) closeMenu();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeMenu();
  });

  // Current year
  document.getElementById('year').textContent = new Date().getFullYear();

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var reveals = document.querySelectorAll('.reveal');

  // Stagger: children of a grid animate in sequence rather than all at once
  ['.grid-cards', '.grid-3', '.pipeline', '.steps', '.benefits'].forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (group) {
      var i = 0;
      Array.prototype.forEach.call(group.children, function (child) {
        if (child.classList.contains('reveal')) {
          child.style.setProperty('--d', (i * 85) + 'ms');
          i++;
        }
      });
    });
  });

  // Reveal on scroll
  if ('IntersectionObserver' in window && !reduced) {
    // toggle rather than unobserve, so the effects replay each time an
    // element scrolls back into view instead of firing once per page load
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        entry.target.classList.toggle('is-in', entry.isIntersecting);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -50px 0px' });

    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  }

  // Highlight the nav link for whichever section is centred in the viewport
  var navLinks = {};
  document.querySelectorAll('.nav a[href^="#"]').forEach(function (a) {
    var id = a.getAttribute('href').slice(1);
    if (id && id !== 'top') navLinks[id] = a;
  });
  if ('IntersectionObserver' in window) {
    var sectionObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var link = navLinks[entry.target.id];
        if (!link || !entry.isIntersecting) return;
        for (var k in navLinks) navLinks[k].classList.remove('is-active');
        link.classList.add('is-active');
      });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });
    document.querySelectorAll('section[id]').forEach(function (s) { sectionObs.observe(s); });
  }

  // Scroll progress bar + hero parallax, all in one rAF loop so scrolling stays smooth
  var progressBar = document.getElementById('progressBar');
  var glowA = document.querySelector('.glow--a');
  var glowB = document.querySelector('.glow--b');
  var heroGrid = document.querySelector('.hero__grid');
  var heroInner = document.querySelector('.hero__inner');
  var ticking = false;

  function paint() {
    ticking = false;
    var y = window.pageYOffset;
    var max = document.documentElement.scrollHeight - window.innerHeight;

    if (progressBar) {
      progressBar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, y / max) : 0) + ')';
    }
    if (reduced) return;

    // only compute parallax while the hero is anywhere near the viewport
    var vh = window.innerHeight;
    if (y < vh * 1.5) {
      if (glowA) glowA.style.transform = 'translate3d(0,' + (y * 0.16).toFixed(1) + 'px,0)';
      if (glowB) glowB.style.transform = 'translate3d(0,' + (y * -0.10).toFixed(1) + 'px,0)';
      if (heroGrid) heroGrid.style.transform = 'translate3d(0,' + (y * 0.22).toFixed(1) + 'px,0)';
      if (heroInner) {
        heroInner.style.transform = 'translate3d(0,' + (y * 0.10).toFixed(1) + 'px,0)';
        heroInner.style.opacity = Math.max(0, 1 - y / (vh * 0.9)).toFixed(3);
      }
    }
  }
  function queuePaint() {
    if (!ticking) { ticking = true; window.requestAnimationFrame(paint); }
  }
  window.addEventListener('scroll', queuePaint, { passive: true });
  window.addEventListener('resize', queuePaint, { passive: true });
  queuePaint();
})();