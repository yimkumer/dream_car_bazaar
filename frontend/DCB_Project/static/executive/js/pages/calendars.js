"use strict";
var CalendarList = [];

function CalendarInfo() { this.id = null, this.name = null, this.checked = !0, this.color = null, this.bgColor = null, this.borderColor = null, this.dragBgColor = null }

function addCalendar(r) { CalendarList.push(r) }

function findCalendar(a) { var o; return CalendarList.forEach(function(r) { r.id === a && (o = r) }), o || CalendarList[0] }

function hexToRGBA(r) { return "rgba(" + parseInt(r.slice(1, 3), 16) + ", " + parseInt(r.slice(3, 5), 16) + ", " + parseInt(r.slice(5, 7), 16) + ", " + (parseInt(r.slice(7, 9), 16) / 255 || 1) + ")" }! function() { var r = new CalendarInfo;
    r.id = String(1), r.name = "My Calendar", r.color = "#ffffff", r.bgColor = "#556ee6", r.dragBgColor = "#556ee6", r.borderColor = "#556ee6", addCalendar(r), (r = new CalendarInfo).id = String(2), r.name = "Company", r.color = "#ffffff", r.bgColor = "#50a5f1", r.dragBgColor = "#50a5f1", r.borderColor = "#50a5f1", addCalendar(r), (r = new CalendarInfo).id = String(3), r.name = "Family", r.color = "#ffffff", r.bgColor = "#f46a6a", r.dragBgColor = "#f46a6a", r.borderColor = "#f46a6a", addCalendar(r), (r = new CalendarInfo).id = String(4), r.name = "Friend", r.color = "#ffffff", r.bgColor = "#34c38f", r.dragBgColor = "#34c38f", r.borderColor = "#34c38f", addCalendar(r), (r = new CalendarInfo).id = String(5), r.name = "Travel", r.color = "#ffffff", r.bgColor = "#bbdc00", r.dragBgColor = "#bbdc00", r.borderColor = "#bbdc00", addCalendar(r), (r = new CalendarInfo).id = String(6), r.name = "Birthdays", r.color = "#ffffff", r.bgColor = "#f1b44c", r.dragBgColor = "#f1b44c", r.borderColor = "#f1b44c", addCalendar(r), (r = new CalendarInfo).id = String(7), r.name = "National Holidays", r.color = "#ffffff", r.bgColor = "#ff4040", r.dragBgColor = "#ff4040", r.borderColor = "#ff4040", addCalendar(r) }();