function getChartColorsArray(r) { if (null !== document.getElementById(r)) { var o = document.getElementById(r).getAttribute("data-colors"); if (o) return (o = JSON.parse(o)).map(function(r) { var o = r.replace(" ", ""); if (-1 === o.indexOf(",")) { var e = getComputedStyle(document.documentElement).getPropertyValue(o); return e || o } var t = r.split(","); return 2 != t.length ? o : "rgba(" + getComputedStyle(document.documentElement).getPropertyValue(t[0]) + "," + t[1] + ")" }) } }! function(p) {
    "use strict";

    function r() {}
    r.prototype.respChart = function(r, o, e, t) {
        Chart.defaults.global.defaultFontColor = "#9295a4", Chart.defaults.scale.gridLines.color = "rgba(166, 176, 207, 0.1)";
        var a = r.get(0).getContext("2d"),
            n = p(r).parent();

        function l() {
            r.attr("width", p(n).width());
            switch (o) {
                case "Line":
                    new Chart(a, { type: "line", data: e, options: t });
                    break;
                case "Doughnut":
                    new Chart(a, { type: "doughnut", data: e, options: t });
                    break;
                case "Pie":
                    new Chart(a, { type: "pie", data: e, options: t });
                    break;
                case "Bar":
                    new Chart(a, { type: "bar", data: e, options: t });
                    break;
                case "Radar":
                    new Chart(a, { type: "radar", data: e, options: t });
                    break;
                case "PolarArea":
                    new Chart(a, { data: e, type: "polarArea", options: t })
            }
        }
        p(window).resize(l), l()
    }, r.prototype.init = function() {
        var r, o = getChartColorsArray("lineChart");
        o && (r = { labels: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October"], datasets: [{ label: "Sales Analytics", fill: !0, lineTension: .5, backgroundColor: o[0], borderColor: o[1], borderCapStyle: "butt", borderDash: [], borderDashOffset: 0, borderJoinStyle: "miter", pointBorderColor: o[1], pointBackgroundColor: "#fff", pointBorderWidth: 1, pointHoverRadius: 5, pointHoverBackgroundColor: o[1], pointHoverBorderColor: "#fff", pointHoverBorderWidth: 2, pointRadius: 1, pointHitRadius: 10, data: [65, 59, 80, 81, 56, 55, 40, 55, 30, 80] }, { label: "Monthly Earnings", fill: !0, lineTension: .5, backgroundColor: o[2], borderColor: o[3], borderCapStyle: "butt", borderDash: [], borderDashOffset: 0, borderJoinStyle: "miter", pointBorderColor: o[3], pointBackgroundColor: "#fff", pointBorderWidth: 1, pointHoverRadius: 5, pointHoverBackgroundColor: o[3], pointHoverBorderColor: "#eef0f2", pointHoverBorderWidth: 2, pointRadius: 1, pointHitRadius: 10, data: [80, 23, 56, 65, 23, 35, 85, 25, 92, 36] }] }, this.respChart(p("#lineChart"), "Line", r, { scales: { yAxes: [{ ticks: { max: 100, min: 20, stepSize: 10 } }] } }));
        var e, t = getChartColorsArray("doughnut");
        t && (e = { labels: ["Desktops", "Tablets"], datasets: [{ data: [300, 210], backgroundColor: t, hoverBackgroundColor: t, hoverBorderColor: "#fff" }] }, this.respChart(p("#doughnut"), "Doughnut", e));
        var a, n = getChartColorsArray("pie");
        n && (a = { labels: ["Desktops", "Tablets"], datasets: [{ data: [300, 180], backgroundColor: n, hoverBackgroundColor: n, hoverBorderColor: "#fff" }] }, this.respChart(p("#pie"), "Pie", a));
        var l, i = getChartColorsArray("bar");
        i && (l = { labels: ["January", "February", "March", "April", "May", "June", "July"], datasets: [{ label: "Sales Analytics", backgroundColor: i[0], borderColor: i[0], borderWidth: 1, hoverBackgroundColor: i[1], hoverBorderColor: i[1], data: [65, 59, 81, 45, 56, 80, 50, 20] }] }, this.respChart(p("#bar"), "Bar", l, { scales: { xAxes: [{ barPercentage: .4 }] } }));
        var d, s = getChartColorsArray("radar");
        s && (d = { labels: ["Eating", "Drinking", "Sleeping", "Designing", "Coding", "Cycling", "Running"], datasets: [{ label: "Desktops", backgroundColor: s[0], borderColor: s[1], pointBackgroundColor: s[1], pointBorderColor: "#fff", pointHoverBackgroundColor: "#fff", pointHoverBorderColor: s[1], data: [65, 59, 90, 81, 56, 55, 40] }, { label: "Tablets", backgroundColor: s[2], borderColor: s[3], pointBackgroundColor: s[3], pointBorderColor: "#fff", pointHoverBackgroundColor: "#fff", pointHoverBorderColor: s[3], data: [28, 48, 40, 19, 96, 27, 100] }] }, this.respChart(p("#radar"), "Radar", d));
        var u, C = getChartColorsArray("polarArea");
        C && (u = { datasets: [{ data: [11, 16, 7, 18], backgroundColor: C, label: "My dataset", hoverBorderColor: "#fff" }], labels: ["Series 1", "Series 2", "Series 3", "Series 4"] }, this.respChart(p("#polarArea"), "PolarArea", u))
    }, p.ChartJs = new r, p.ChartJs.Constructor = r
}(window.jQuery),
function() {
    "use strict";
    window.jQuery.ChartJs.init()
}();