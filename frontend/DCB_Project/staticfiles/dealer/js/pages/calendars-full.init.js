!(function(g) {
    "use strict";

    function e() {}
    (e.prototype.init = function() {
        var l = g("#event-modal"),
            t = g("#modal-title"),
            a = g("#form-event"),
            i = null,
            r = null,
            s = document.getElementsByClassName("needs-validation"),
            i = null,
            r = null,
            e = new Date(),
            n = e.getDate(),
            d = e.getMonth(),
            o = e.getFullYear();
        new FullCalendarInteraction.Draggable(
            document.getElementById("external-events"), {
                itemSelector: ".external-event",
                eventData: function(e) {
                    return { title: e.innerText, className: g(e).data("class") };
                },
            }
        );
        var c = [{
                    title: "Lunch",
                    start: new Date(o, d, n, 12, 0),
                    end: new Date(o, d, n, 14, 0),
                    allDay: !1,
                    className: "bg-danger",
                },
                {
                    title: "Birthday Party",
                    start: new Date(o, d, n + 1, 19, 0),
                    end: new Date(o, d, n + 1, 22, 30),
                    allDay: !1,
                    className: "bg-success",
                },
            ],
            v =
            (document.getElementById("external-events"),
                document.getElementById("calendar"));

        function u(e) {
            l.modal("show"),
                a.removeClass("was-validated"),
                a[0].reset(),
                g("#event-title").val(),
                g("#event-category").val(),
                t.text("Add Event"),
                (r = e);
        }
        var m = new FullCalendar.Calendar(v, {
            plugins: ["bootstrap", "interaction", "dayGrid", "timeGrid"],
            editable: !0,
            droppable: !0,
            selectable: !0,
            defaultView: "dayGridMonth",
            themeSystem: "bootstrap",
            eventClick: function(e) {
                l.modal("show"),
                    a[0].reset(),
                    (i = e.event),
                    g("#event-title").val(i.title),
                    g("#event-category").val(i.classNames[0]),
                    (r = null),
                    t.text("Edit Event"),
                    (r = null);
            },
            dateClick: function(e) {
                u(e);
            },
            events: c,
        });
        m.render(),
            g(a).on("submit", function(e) {
                e.preventDefault();
                g("#form-event :input");
                var t,
                    a = g("#event-title").val(),
                    n = g("#event-category").val();
                !1 === s[0].checkValidity() ?
                    (event.preventDefault(),
                        event.stopPropagation(),
                        s[0].classList.add("was-validated")) :
                    (i ?
                        (i.setProp("title", a), i.setProp("classNames", [n])) :
                        ((t = {
                                title: a,
                                start: r.date,
                                allDay: r.allDay,
                                className: n,
                            }),
                            m.addEvent(t)),
                        l.modal("hide"));
            }),
            g("#btn-delete-event").on("click", function(e) {
                i && (i.remove(), (i = null), l.modal("hide"));
            }),
            g("#btn-new-event").on("click", function(e) {
                u({ date: new Date(), allDay: !0 });
            });
    }),
    (g.CalendarPage = new e()),
    (g.CalendarPage.Constructor = e);
})(window.jQuery),
(function() {
    "use strict";
    window.jQuery.CalendarPage.init();
})();