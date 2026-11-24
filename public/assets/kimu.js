/* Kimu Txalaparta · menú, cabecera fija y vídeos de YouTube bajo demanda (sin cookies hasta pulsar) */
(function () {
  "use strict";

  // Menú móvil (botón "+")
  var btn = document.getElementById("plus");
  var panel = document.getElementById("panel");
  if (btn && panel) {
    var setOpen = function (open) {
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.setAttribute("aria-label", open ? btn.dataset.close : btn.dataset.open);
      panel.classList.toggle("open", open);
      document.documentElement.style.overflow = open ? "hidden" : "";
    };
    btn.addEventListener("click", function () {
      setOpen(btn.getAttribute("aria-expanded") !== "true");
    });
    panel.addEventListener("click", function (e) {
      if (e.target.closest("a")) setOpen(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && panel.classList.contains("open")) { setOpen(false); btn.focus(); }
    });
  }

  // Marca pequeña en la barra cuando el logotipo grande sale de pantalla
  var bar = document.querySelector(".bar");
  var mark = document.querySelector(".wordmark");
  if (bar && mark && "IntersectionObserver" in window) {
    new IntersectionObserver(function (entries) {
      bar.classList.toggle("stuck", !entries[0].isIntersecting);
    }).observe(mark);
  }

  // Vídeos: se carga el reproductor de youtube-nocookie solo al pulsar
  document.querySelectorAll("button.play[data-yt]").forEach(function (b) {
    b.addEventListener("click", function () {
      var id = b.dataset.yt;
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(id) + "?autoplay=1&rel=0";
      f.title = b.dataset.title || "YouTube";
      f.allow = "accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen";
      f.allowFullscreen = true;
      f.loading = "lazy";
      b.replaceWith(f);
      f.focus();
    });
  });

  // Aparición al hacer scroll (elementos .reveal / .rule); mejora progresiva
  var toReveal = document.querySelectorAll(".reveal, .rule");
  if (toReveal.length) {
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
        });
      }, { threshold: 0.16, rootMargin: "0px 0px -8% 0px" });
      toReveal.forEach(function (el) { io.observe(el); });
    } else {
      toReveal.forEach(function (el) { el.classList.add("is-in"); });
    }
  }
})();
