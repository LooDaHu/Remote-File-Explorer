(function () {
    var n = document.getElementsByClassName("effect");
    for (var e = 0, t = n.length; e < t; e++) {
        var a = n[e], r = a.textContent.trim();
        a.innerHTML = null;
        i(a, r)
    }

    function i(n, e) {
        for (var t in e) {
            var a = document.createElement("span");
            a.innerHTML = e[t] === " " ? "&nbsp;" : e[t];
            n.appendChild(a)
        }
    }
})();