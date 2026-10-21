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
/* ---------- theme + audience ---------- */
(function () {
  'use strict';
  var root = document.documentElement;

  /* theme: light is the default, dark is opt in, choice is remembered */
  function applyTheme(t) {
    if (t === 'dark') root.setAttribute('data-theme', 'dark');
    else root.removeAttribute('data-theme');
  }
  var btn = document.getElementById('themebtn');
  if (btn) {
    btn.addEventListener('click', function () {
      var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      try { localStorage.setItem('at-theme', next); } catch (e) {}
    });
  }

  /* audience: which half of the business the visitor is here for */
  var EMPLOYER = ['/start', '/talent-acquisition', '/software', '/how-we-work', '/services', '/industries',
                  '/recruitment-agency-pune', '/talent-acquisition-firm-pune'];
  var CANDIDATE = ['/candidates', '/jobs'];

  function audFromPath(p) {
    for (var i = 0; i < CANDIDATE.length; i++) if (p.indexOf(CANDIDATE[i]) === 0) return 'candidate';
    for (var j = 0; j < EMPLOYER.length; j++) if (p.indexOf(EMPLOYER[j]) === 0) return 'employer';
    return null;
  }

  function applyAud(a) {
    root.setAttribute('data-aud', a);
    var nav = document.getElementById('nav');
    if (nav) {
      nav.querySelectorAll('[data-aud]').forEach(function (el) {
        el.style.display = el.getAttribute('data-aud') === a ? '' : 'none';
      });
    }
    document.querySelectorAll('[data-set-aud]').forEach(function (el) {
      el.classList.toggle('is-on', el.getAttribute('data-set-aud') === a);
    });
  }

  var fromPath = audFromPath(location.pathname);
  var stored = null;
  try { stored = localStorage.getItem('at-aud'); } catch (e) {}
  applyAud(fromPath || stored || 'employer');

  /* clicking the toggle records the choice, then the link navigates normally */
  document.querySelectorAll('[data-set-aud]').forEach(function (el) {
    el.addEventListener('click', function () {
      try { localStorage.setItem('at-aud', el.getAttribute('data-set-aud')); } catch (e) {}
    });
  });

  /* landing on a page that belongs to one side settles the preference */
  if (fromPath) { try { localStorage.setItem('at-aud', fromPath); } catch (e) {} }
})();

/* ---------- AI ring system ----------
   Built in script rather than written into every template, so the markup
   stays out of the page source and every hero on the site picks it up.
   Purely decorative: aria-hidden, pointer-events none, never focusable. */
(function () {
  var heroes = document.querySelectorAll('.hero');
  if (!heroes.length) return;

  var reduce = window.matchMedia &&
               window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function dial() {
    var ticks = '';
    for (var i = 0; i < 60; i++) {
      var major = i % 5 === 0;
      ticks += '<line x1="320" y1="104" x2="320" y2="' + (major ? 118 : 111) +
               '" transform="rotate(' + (i * 6) + ' 320 320)" ' +
               'stroke="var(--dial)" stroke-opacity=".5" stroke-width="' + (major ? 2 : 1.2) + '"/>';
    }
    /* three gold comets chasing each other round the sweep ring, each with a
       tail of shrinking, fading dots trailing behind the direction of travel.
       The group turns clockwise, so "behind" is a negative rotation. */
    var comets = '';
    for (var c = 0; c < 3; c++) {
      var lead = -c * 11;
      for (var k = 7; k >= 1; k--) {
        comets += '<circle cx="320" cy="56" r="' + (4.2 - k * 0.42).toFixed(2) +
                  '" fill="var(--dial-2)" opacity="' + (0.72 - k * 0.088).toFixed(2) +
                  '" transform="rotate(' + (lead - k * 2.4) + ' 320 320)"/>';
      }
      comets += '<circle cx="320" cy="56" r="4.6" fill="var(--dial-2)" ' +
                'transform="rotate(' + lead + ' 320 320)"/>';
    }

    /* sonar style waves pushing outward from the centre, staggered */
    var waves = '';
    for (var w = 0; w < 3; w++) {
      waves += '<g class="r-wave" style="animation-delay:' + (w * 2.2) + 's">' +
               '<circle cx="320" cy="320" r="230" stroke="var(--dial)" ' +
               'stroke-width="1.7" opacity=".75"/></g>';
    }

    return '<svg viewBox="0 0 640 640" fill="none" aria-hidden="true" focusable="false">' +
      '<defs>' +
        '<linearGradient id="agSweep" x1="0" y1="0" x2="1" y2="0">' +
          '<stop offset="0" stop-color="var(--dial)" stop-opacity="0"/>' +
          '<stop offset="1" stop-color="var(--dial)" stop-opacity="1"/>' +
        '</linearGradient>' +
        '<radialGradient id="agCore">' +
          '<stop offset="0" stop-color="var(--dial)" stop-opacity=".16"/>' +
          '<stop offset="1" stop-color="var(--dial)" stop-opacity="0"/>' +
        '</radialGradient>' +
        /* bloom around the sweep and the comets, so they read as lit rather
           than drawn. filterUnits has to be generous or the blur gets clipped */
        '<filter id="agGlow" x="-30%" y="-30%" width="160%" height="160%">' +
          '<feGaussianBlur stdDeviation="5" result="b"/>' +
          '<feMerge><feMergeNode in="b"/><feMergeNode in="b"/>' +
          '<feMergeNode in="SourceGraphic"/></feMerge>' +
        '</filter>' +
        '<filter id="agGlowGold" x="-40%" y="-40%" width="180%" height="180%">' +
          '<feGaussianBlur stdDeviation="3.4" result="b"/>' +
          '<feMerge><feMergeNode in="b"/><feMergeNode in="b"/>' +
          '<feMergeNode in="SourceGraphic"/></feMerge>' +
        '</filter>' +
      '</defs>' +
      '<circle cx="320" cy="320" r="158" fill="url(#agCore)"/>' +
      waves +
      '<g class="r-spin"><circle cx="320" cy="320" r="300" stroke="var(--dial)" stroke-opacity=".4" stroke-width="1.3" stroke-dasharray="2 12"/></g>' +
      '<g class="r-spin-rev"><circle cx="320" cy="320" r="264" stroke="var(--dial)" stroke-width="2" stroke-opacity=".75" stroke-dasharray="150 92 42 92"/></g>' +
      '<g class="r-sweep" filter="url(#agGlow)"><circle cx="320" cy="320" r="264" stroke="url(#agSweep)" stroke-width="3.2" stroke-dasharray="130 1530" stroke-linecap="round"/></g>' +
      '<g class="r-tick">' + ticks + '</g>' +
      '<g class="r-spin"><circle cx="320" cy="320" r="86" stroke="var(--dial)" stroke-opacity=".45" stroke-width="1.3" stroke-dasharray="1 8"/></g>' +
      '<g class="r-comets" filter="url(#agGlowGold)">' + comets + '</g>' +
    '</svg>';
  }

  Array.prototype.forEach.call(heroes, function (hero) {
    if (hero.querySelector('.rings')) return;
    var box = document.createElement('div');
    box.className = 'rings';
    box.setAttribute('aria-hidden', 'true');
    box.innerHTML = dial();
    hero.insertBefore(box, hero.firstChild);

    if (reduce) return;

    /* cursor parallax, a few pixels only, rAF throttled */
    var svg = box.querySelector('svg'), queued = false, px = 0, py = 0;
    hero.addEventListener('pointermove', function (e) {
      if (e.pointerType === 'touch') return;
      var r = hero.getBoundingClientRect();
      px = ((e.clientX - r.left) / r.width - 0.5) * 26;
      py = ((e.clientY - r.top) / r.height - 0.5) * 20;
      if (queued) return;
      queued = true;
      requestAnimationFrame(function () {
        svg.style.setProperty('--rx', px.toFixed(1) + 'px');
        svg.style.setProperty('--ry', py.toFixed(1) + 'px');
        queued = false;
      });
    });
    hero.addEventListener('pointerleave', function () {
      svg.style.setProperty('--rx', '0px');
      svg.style.setProperty('--ry', '0px');
    });
  });
})();
