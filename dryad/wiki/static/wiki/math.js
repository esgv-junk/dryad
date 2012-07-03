(function ($) {
  $.fn.typeset = function () {
    return this.each(function () {
      MathJax.Hub.Queue(["Typeset", MathJax.Hub, this]);
    });
  };
})(jQuery);
