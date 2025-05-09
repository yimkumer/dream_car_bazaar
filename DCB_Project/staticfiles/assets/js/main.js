!(function (t) {
  "use strict";
  t("#download_btn").on("click", function () {
    var e = t("#download_section"),
      n = e.width(),
      a = e.height(),
      o = n + 80,
      d = 1.5 * o + 80,
      c = n,
      i = a,
      r = Math.ceil(a / d) - 1;
    html2canvas(e[0], { allowTaint: !0 }).then(function (t) {
      t.getContext("2d");
      var e = t.toDataURL("image/jpeg", 1),
        n = new jsPDF("p", "pt", [o, d]);
      n.addImage(e, "JPG", 40, 40, c, i);
      for (var a = 1; a <= r; a++)
        n.addPage(o, d), n.addImage(e, "JPG", 40, -d * a + 0, c, i);
      n.save("th-invoice.pdf");
    });
  }),
    t(".print_btn").on("click", function (t) {
      window.print();
    }),
    t("[data-bg-src]").length > 0 &&
      t("[data-bg-src]").each(function () {
        var e = t(this).attr("data-bg-src");
        t(this).css("background-image", "url(" + e + ")"),
          t(this).removeAttr("data-bg-src").addClass("background-image");
      }),
    window.addEventListener(
      "contextmenu",
      function (t) {
        t.preventDefault();
      },
      !1
    ),
    (document.onkeydown = function (t) {
      return (
        123 != event.keyCode &&
        (!t.ctrlKey || !t.shiftKey || t.keyCode != "I".charCodeAt(0)) &&
        (!t.ctrlKey || !t.shiftKey || t.keyCode != "C".charCodeAt(0)) &&
        (!t.ctrlKey || !t.shiftKey || t.keyCode != "J".charCodeAt(0)) &&
        (!t.ctrlKey || t.keyCode != "U".charCodeAt(0)) &&
        void 0
      );
    });
})(jQuery);
