(function(){
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Slow reveal on scroll */
  var els = document.querySelectorAll('.reveal');
  if (rm || !('IntersectionObserver' in window)) {
    els.forEach(function(e){ e.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if (en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin:'0px 0px -12% 0px', threshold:0.08 });
    els.forEach(function(e){ io.observe(e); });
  }

  /* Mobile navigation — no library, focus-aware, ESC to close */
  var toggle = document.getElementById('navToggle');
  var menu   = document.getElementById('mobileNav');
  var closeB = document.getElementById('navClose');
  var lastFocused = null;

  function setMenu(open){
    menu.dataset.open = open ? 'true' : 'false';
    menu.setAttribute('aria-hidden', open ? 'false' : 'true');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    /* Labels come from the markup so one script serves both languages. */
    toggle.setAttribute('aria-label', open ? (toggle.dataset.labelClose || 'Close menu')
                                          : (toggle.dataset.labelOpen  || 'Open menu'));
    document.body.dataset.menuOpen = open ? 'true' : 'false';
    if (open){ lastFocused = document.activeElement; closeB.focus(); }
    else if (lastFocused){ lastFocused.focus(); }
  }

  if (toggle && menu && closeB){
    toggle.addEventListener('click', function(){
      setMenu(menu.dataset.open !== 'true');
    });
    closeB.addEventListener('click', function(){ setMenu(false); });

    /* Any link inside closes the menu — in-page anchors need it, and
       page links look less abrupt if the overlay dismisses first. */
    menu.querySelectorAll('a').forEach(function(a){
      a.addEventListener('click', function(){ setMenu(false); });
    });

    document.addEventListener('keydown', function(e){
      if (e.key === 'Escape' && menu.dataset.open === 'true') setMenu(false);
      /* Keep tab focus inside the overlay while it is open. */
      if (e.key === 'Tab' && menu.dataset.open === 'true'){
        var f = menu.querySelectorAll('a[href], button');
        if (!f.length) return;
        var first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first){ e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last){ e.preventDefault(); first.focus(); }
      }
    });

    /* Close if the viewport grows into the desktop nav breakpoint. */
    window.matchMedia('(min-width: 1240px)').addEventListener('change', function(ev){
      if (ev.matches && menu.dataset.open === 'true') setMenu(false);
    });
  }

  /* Nav state */
  var nav = document.getElementById('nav');
  /* Gentle parallax */
  var hero = document.getElementById('heroImg');
  var closeI = document.getElementById('closeImg');
  var ticking = false;

  function frame(){
    var y = window.pageYOffset || document.documentElement.scrollTop;
    nav.classList.toggle('stuck', y > 60);
    if (!rm){
      if (hero && y < window.innerHeight * 1.3){
        hero.style.transform = 'translate3d(0,' + (y * 0.16).toFixed(2) + 'px,0) scale(1.02)';
      }
      if (closeI){
        var r = closeI.getBoundingClientRect();
        if (r.bottom > 0 && r.top < window.innerHeight){
          var p = (window.innerHeight - r.top) / (window.innerHeight + r.height);
          closeI.style.transform = 'translate3d(0,' + ((p - .5) * 70).toFixed(2) + 'px,0) scale(1.02)';
        }
      }
    }
    ticking = false;
  }
  window.addEventListener('scroll', function(){
    if (!ticking){ ticking = true; window.requestAnimationFrame(frame); }
  }, { passive:true });
  frame();
})();
