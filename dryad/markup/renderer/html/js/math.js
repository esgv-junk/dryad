var mathJaxIsLoaded = false;

function loadScript(src, innerHTML) {
  var script = document.createElement("script");
  script.type = "text/javascript";
  script.src = src;

  if (window.opera) {
    script.innerHTML = innerHTML;
  }
  else {
    script.text = innerHTML;
  }
  
  document.getElementsByTagName("head")[0].appendChild(script);
}

function loadMathJax() {
  if (mathJaxIsLoaded) {
    return;
  }
    
    //var jaxSrc = "http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML";
  var jaxSrc = "file:///D:/Dropbox/code/3rd_party/mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML";
    
  var jaxConfig = 
  'MathJax.Hub.Config({' +
    'skipStartupTypeset: true,' +
    'tex2jax: {' +
      'inlineMath: [["$", "$"]]' +
    '},' +
    '"HTML-CSS": {' +
        'scale: 100,' +
        'showMathMenu: false' +
    '},' +
    'NativeMML: {' +
        'scale: 100' +
    '},' +
    'TeX: {' +
      'noErrors: {'+
        'style: {' +
          '"font-family": "Verdana"'+
        '}' +
      '}' +
    '}' +
  '});'+
  'MathJax.Hub.Startup.onload();';
  
  loadScript(jaxSrc, jaxConfig);
  mathJaxIsLoaded = true;
}

function processAllMathElements() {
  mathElements = document.getElementsByClassName("math");

  if (mathElements.length > 0) {
    loadMathJax();

    if (typeof MathJax === 'undefined') {
      setTimeout(processAllMathElements, 10);
      return;
    }

    for (var i = 0; i < mathElements.length; ++i) {
      MathJax.Hub.Queue(
        ["Typeset", MathJax.Hub, mathElements[i]],
        ["remove", mathElements[i].classList, "preloaded"]
      )
  } }
}

window.onload = processAllMathElements;
