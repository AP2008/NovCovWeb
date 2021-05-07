template = """
<html>
  <head>
    <style>
      html, body {{
        border: 0px;
        margin: 0px;
        padding: 0px;
      }}
    </style>
<style type="text/css">input:invalid {{
    outline: solid red;
}}

input:valid {{
    outline: none black;
}}</style><style type="text/css">.Select,.Select-control{{position:relative}}.Select-control,.Select-input>input{{width:100%;cursor:default;outline:0}}.Select-arrow-zone,.Select-clear-zone,.Select-loading-zone{{text-align:center;cursor:pointer}}.Select,.Select div,.Select input,.Select span{{-webkit-box-sizing:border-box;-moz-box-sizing:border-box;box-sizing:border-box}}.Select.is-disabled>.Select-control{{background-color:#f9f9f9}}.Select.is-disabled>.Select-control:hover{{box-shadow:none}}.Select.is-disabled .Select-arrow-zone{{cursor:default;pointer-events:none;opacity:.35}}.Select-control{{background-color:#fff;border-radius:4px;border:1px solid #ccc;color:#333;display:table;border-spacing:0;border-collapse:separate;height:36px;overflow:hidden}}.is-searchable.is-focused:not(.is-open)>.Select-control,.is-searchable.is-open>.Select-control{{cursor:text}}.Select-control:hover{{box-shadow:0 1px 0 rgba(0,0,0,.06)}}.Select-control .Select-input:focus{{outline:0}}.is-open>.Select-control{{border-bottom-right-radius:0;border-bottom-left-radius:0;background:#fff;border-color:#b3b3b3 #ccc #d9d9d9}}.is-open>.Select-control .Select-arrow{{top:-2px;border-color:transparent transparent #999;border-width:0 5px 5px}}.is-focused:not(.is-open)>.Select-control{{border-color:#007eff;box-shadow:inset 0 1px 1px rgba(0,0,0,.075),0 0 0 3px rgba(0,126,255,.1)}}.Select--single>.Select-control .Select-value,.Select-placeholder{{bottom:0;color:#aaa;left:0;line-height:34px;padding-left:10px;padding-right:10px;position:absolute;right:0;top:0;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}.has-value.Select--single>.Select-control .Select-value .Select-value-label,.has-value.is-pseudo-focused.Select--single>.Select-control .Select-value .Select-value-label{{color:#333}}.has-value.Select--single>.Select-control .Select-value a.Select-value-label,.has-value.is-pseudo-focused.Select--single>.Select-control .Select-value a.Select-value-label{{cursor:pointer;text-decoration:none}}.has-value.Select--single>.Select-control .Select-value a.Select-value-label:focus,.has-value.Select--single>.Select-control .Select-value a.Select-value-label:hover,.has-value.is-pseudo-focused.Select--single>.Select-control .Select-value a.Select-value-label:focus,.has-value.is-pseudo-focused.Select--single>.Select-control .Select-value a.Select-value-label:hover{{color:#007eff;outline:0;text-decoration:underline}}.Select-input{{height:34px;padding-left:10px;padding-right:10px;vertical-align:middle}}.Select-input>input{{background:none;border:0;box-shadow:none;display:inline-block;font-family:inherit;font-size:inherit;margin:0;line-height:14px;padding:8px 0 12px;-webkit-appearance:none}}.Select-loading,.Select-loading-zone{{width:16px;position:relative;vertical-align:middle}}.is-focused .Select-input>input{{cursor:text}}.has-value.is-pseudo-focused .Select-input{{opacity:0}}.Select-control:not(.is-searchable)>.Select-input{{outline:0}}.Select-loading-zone{{display:table-cell}}.Select-loading{{-webkit-animation:Select-animation-spin .4s infinite linear;-o-animation:Select-animation-spin .4s infinite linear;animation:Select-animation-spin .4s infinite linear;height:16px;box-sizing:border-box;border-radius:50%;border:2px solid #ccc;border-right-color:#333;display:inline-block}}.Select-clear-zone{{-webkit-animation:Select-animation-fadeIn .2s;-o-animation:Select-animation-fadeIn .2s;animation:Select-animation-fadeIn .2s;color:#999;display:table-cell;position:relative;vertical-align:middle;width:17px}}.Select-clear-zone:hover{{color:#D0021B}}.Select-clear{{display:inline-block;font-size:18px;line-height:1}}.Select--multi .Select-clear-zone{{width:17px}}.Select-arrow-zone{{display:table-cell;position:relative;vertical-align:middle;width:25px;padding-right:5px}}.Select--multi .Select-multi-value-wrapper,.Select-arrow{{display:inline-block}}.Select-arrow{{border-color:#999 transparent transparent;border-style:solid;border-width:5px 5px 2.5px;height:0;width:0;position:relative}}.Select-arrow-zone:hover>.Select-arrow,.is-open .Select-arrow{{border-top-color:#666}}.Select .Select-aria-only{{display:inline-block;height:1px;width:1px;margin:-1px;clip:rect(0,0,0,0);overflow:hidden;float:left}}.Select-noresults,.Select-option{{box-sizing:border-box;display:block;padding:8px 10px}}@-webkit-keyframes Select-animation-fadeIn{{from{{opacity:0}}to{{opacity:1}}}}@keyframes Select-animation-fadeIn{{from{{opacity:0}}to{{opacity:1}}}}.Select-menu-outer{{border-bottom-right-radius:4px;border-bottom-left-radius:4px;background-color:#fff;border:1px solid #ccc;border-top-color:#e6e6e6;box-shadow:0 1px 0 rgba(0,0,0,.06);box-sizing:border-box;margin-top:-1px;max-height:200px;position:absolute;top:100%;width:100%;z-index:1;-webkit-overflow-scrolling:touch}}.Select-menu{{max-height:198px;overflow-y:auto}}.Select-option{{background-color:#fff;color:#666;cursor:pointer}}.Select-option:last-child{{border-bottom-right-radius:4px;border-bottom-left-radius:4px}}.Select-option.is-selected{{background-color:#f5faff;background-color:rgba(0,126,255,.04);color:#333}}.Select-option.is-focused{{background-color:#ebf5ff;background-color:rgba(0,126,255,.08);color:#333}}.Select-option.is-disabled{{color:#ccc;cursor:default}}.Select-noresults{{color:#999;cursor:default}}.Select--multi .Select-input{{vertical-align:middle;margin-left:10px;padding:0}}.Select--multi.has-value .Select-input{{margin-left:5px}}.Select--multi .Select-value{{background-color:#ebf5ff;background-color:rgba(0,126,255,.08);border-radius:2px;border:1px solid #c2e0ff;border:1px solid rgba(0,126,255,.24);color:#007eff;display:inline-block;font-size:.9em;line-height:1.4;margin-left:5px;margin-top:5px;vertical-align:top}}.Select--multi .Select-value-icon,.Select--multi .Select-value-label{{display:inline-block;vertical-align:middle}}.Select--multi .Select-value-label{{border-bottom-right-radius:2px;border-top-right-radius:2px;cursor:default;padding:2px 5px}}.Select--multi a.Select-value-label{{color:#007eff;cursor:pointer;text-decoration:none}}.Select--multi a.Select-value-label:hover{{text-decoration:underline}}.Select--multi .Select-value-icon{{cursor:pointer;border-bottom-left-radius:2px;border-top-left-radius:2px;border-right:1px solid #c2e0ff;border-right:1px solid rgba(0,126,255,.24);padding:1px 5px 3px}}.Select--multi .Select-value-icon:focus,.Select--multi .Select-value-icon:hover{{background-color:#d8eafd;background-color:rgba(0,113,230,.08);color:#0071e6}}.Select--multi .Select-value-icon:active{{background-color:#c2e0ff;background-color:rgba(0,126,255,.24)}}.Select--multi.is-disabled .Select-value{{background-color:#fcfcfc;border:1px solid #e3e3e3;color:#333}}.Select--multi.is-disabled .Select-value-icon{{cursor:not-allowed;border-right:1px solid #e3e3e3}}.Select--multi.is-disabled .Select-value-icon:active,.Select--multi.is-disabled .Select-value-icon:focus,.Select--multi.is-disabled .Select-value-icon:hover{{background-color:#fcfcfc}}@keyframes Select-animation-spin{{to{{transform:rotate(1turn)}}}}@-webkit-keyframes Select-animation-spin{{to{{-webkit-transform:rotate(1turn)}}}}</style><style type="text/css">.dash-logout-btn {{
    padding: 1rem;
    background-color: #119DFF;
    border: 1px solid #119DFF;
    color: #ffffff;
    outline: none;
    cursor: pointer;
    text-align: center;
}}

.dash-logout-btn:hover, .dash-logout-btn:focus {{
    background-color: #0d76bf;
    border: 1px solid #0d76bf;
}}

.dash-logout-frame {{
    display: block;
    padding: 0;
    margin: 0;
}}
</style><style type="text/css">.PresetDateRangePicker_panel {{
  padding: 0 22px 11px
}}
.PresetDateRangePicker_button {{
  position: relative;
  height: 100%;
  text-align: center;
  background: 0 0;
  border: 2px solid #00a699;
  color: #00a699;
  padding: 4px 12px;
  margin-right: 8px;
  font: inherit;
  font-weight: 700;
  line-height: normal;
  overflow: visible;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  cursor: pointer
}}
.PresetDateRangePicker_button:active {{
  outline: 0
}}
.PresetDateRangePicker_button__selected {{
  color: #fff;
  background: #00a699
}}
.SingleDatePickerInput {{
  display: inline-block;
  background-color: #fff
}}
.SingleDatePickerInput__withBorder {{
  border-radius: 2px;
  border: 1px solid #dbdbdb
}}
.SingleDatePickerInput__rtl {{
  direction: rtl
}}
.SingleDatePickerInput__disabled {{
  background-color: #f2f2f2
}}
.SingleDatePickerInput__block {{
  display: block
}}
.SingleDatePickerInput__showClearDate {{
  padding-right: 30px
}}
.SingleDatePickerInput_clearDate {{
  background: 0 0;
  border: 0;
  color: inherit;
  font: inherit;
  line-height: normal;
  overflow: visible;
  cursor: pointer;
  padding: 10px;
  margin: 0 10px 0 5px;
  position: absolute;
  right: 0;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%)
}}
.SingleDatePickerInput_clearDate__default:focus,
.SingleDatePickerInput_clearDate__default:hover {{
  background: #dbdbdb;
  border-radius: 50%
}}
.SingleDatePickerInput_clearDate__small {{
  padding: 6px
}}
.SingleDatePickerInput_clearDate__hide {{
  visibility: hidden
}}
.SingleDatePickerInput_clearDate_svg {{
  fill: #82888a;
  height: 12px;
  width: 15px;
  vertical-align: middle
}}
.SingleDatePickerInput_clearDate_svg__small {{
  height: 9px
}}
.SingleDatePickerInput_calendarIcon {{
  background: 0 0;
  border: 0;
  color: inherit;
  font: inherit;
  line-height: normal;
  overflow: visible;
  cursor: pointer;
  display: inline-block;
  vertical-align: middle;
  padding: 10px;
  margin: 0 5px 0 10px
}}
.SingleDatePickerInput_calendarIcon_svg {{
  fill: #82888a;
  height: 15px;
  width: 14px;
  vertical-align: middle
}}
.SingleDatePicker {{
  position: relative;
  display: inline-block
}}
.SingleDatePicker__block {{
  display: block
}}
.SingleDatePicker_picker {{
  z-index: 1;
  background-color: #fff;
  position: absolute
}}
.SingleDatePicker_picker__rtl {{
  direction: rtl
}}
.SingleDatePicker_picker__directionLeft {{
  left: 0
}}
.SingleDatePicker_picker__directionRight {{
  right: 0
}}
.SingleDatePicker_picker__portal {{
  background-color: rgba(0,0,0,.3);
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%
}}
.SingleDatePicker_picker__fullScreenPortal {{
  background-color: #fff
}}
.SingleDatePicker_closeButton {{
  background: 0 0;
  border: 0;
  color: inherit;
  font: inherit;
  line-height: normal;
  overflow: visible;
  cursor: pointer;
  position: absolute;
  top: 0;
  right: 0;
  padding: 15px;
  z-index: 2
}}
.SingleDatePicker_closeButton:focus,
.SingleDatePicker_closeButton:hover {{
  color: darken(#cacccd,10%);
  text-decoration: none
}}
.SingleDatePicker_closeButton_svg {{
  height: 15px;
  width: 15px;
  fill: #cacccd
}}
.DayPickerKeyboardShortcuts_buttonReset {{
  background: 0 0;
  border: 0;
  border-radius: 0;
  color: inherit;
  font: inherit;
  line-height: normal;
  overflow: visible;
  padding: 0;
  cursor: pointer;
  font-size: 14px
}}
.DayPickerKeyboardShortcuts_buttonReset:active {{
  outline: 0
}}
.DayPickerKeyboardShortcuts_show {{
  width: 33px;
  height: 26px;
  position: absolute;
  z-index: 2
}}
.DayPickerKeyboardShortcuts_show::before {{
  content: "";
  display: block;
  position: absolute
}}
.DayPickerKeyboardShortcuts_show__bottomRight {{
  bottom: 0;
  right: 0
}}
.DayPickerKeyboardShortcuts_show__bottomRight::before {{
  border-top: 26px solid transparent;
  border-right: 33px solid #00a699;
  bottom: 0;
  right: 0
}}
.DayPickerKeyboardShortcuts_show__bottomRight:hover::before {{
  border-right: 33px solid #008489
}}
.DayPickerKeyboardShortcuts_show__topRight {{
  top: 0;
  right: 0
}}
.DayPickerKeyboardShortcuts_show__topRight::before {{
  border-bottom: 26px solid transparent;
  border-right: 33px solid #00a699;
  top: 0;
  right: 0
}}
.DayPickerKeyboardShortcuts_show__topRight:hover::before {{
  border-right: 33px solid #008489
}}
.DayPickerKeyboardShortcuts_show__topLeft {{
  top: 0;
  left: 0
}}
.DayPickerKeyboardShortcuts_show__topLeft::before {{
  border-bottom: 26px solid transparent;
  border-left: 33px solid #00a699;
  top: 0;
  left: 0
}}
.DayPickerKeyboardShortcuts_show__topLeft:hover::before {{
  border-left: 33px solid #008489
}}
.DayPickerKeyboardShortcuts_showSpan {{
  color: #fff;
  position: absolute
}}
.DayPickerKeyboardShortcuts_showSpan__bottomRight {{
  bottom: 0;
  right: 5px
}}
.DayPickerKeyboardShortcuts_showSpan__topRight {{
  top: 1px;
  right: 5px
}}
.DayPickerKeyboardShortcuts_showSpan__topLeft {{
  top: 1px;
  left: 5px
}}
.DayPickerKeyboardShortcuts_panel {{
  overflow: auto;
  background: #fff;
  border: 1px solid #dbdbdb;
  border-radius: 2px;
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  z-index: 2;
  padding: 22px;
  margin: 33px;
  text-align: left
}}
.DayPickerKeyboardShortcuts_title {{
  font-size: 16px;
  font-weight: 700;
  margin: 0
}}
.DayPickerKeyboardShortcuts_list {{
  list-style: none;
  padding: 0;
  font-size: 14px
}}
.DayPickerKeyboardShortcuts_close {{
  position: absolute;
  right: 22px;
  top: 22px;
  z-index: 2
}}
.DayPickerKeyboardShortcuts_close:active {{
  outline: 0
}}
.DayPickerKeyboardShortcuts_closeSvg {{
  height: 15px;
  width: 15px;
  fill: #cacccd
}}
.DayPickerKeyboardShortcuts_closeSvg:focus,
.DayPickerKeyboardShortcuts_closeSvg:hover {{
  fill: #82888a
}}
.CalendarDay {{
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  cursor: pointer;
  font-size: 14px;
  text-align: center
}}
.CalendarDay:active {{
  outline: 0
}}
.CalendarDay__defaultCursor {{
  cursor: default
}}
.CalendarDay__default {{
  border: 1px solid #e4e7e7;
  color: #484848;
  background: #fff
}}
.CalendarDay__default:hover {{
  background: #e4e7e7;
  border: 1px solid #e4e7e7;
  color: inherit
}}
.CalendarDay__hovered_offset {{
  background: #f4f5f5;
  border: 1px double #e4e7e7;
  color: inherit
}}
.CalendarDay__outside {{
  border: 0;
  background: #fff;
  color: #484848
}}
.CalendarDay__outside:hover {{
  border: 0
}}
.CalendarDay__blocked_minimum_nights {{
  background: #fff;
  border: 1px solid #eceeee;
  color: #cacccd
}}
.CalendarDay__blocked_minimum_nights:active,
.CalendarDay__blocked_minimum_nights:hover {{
  background: #fff;
  color: #cacccd
}}
.CalendarDay__highlighted_calendar {{
  background: #ffe8bc;
  color: #484848
}}
.CalendarDay__highlighted_calendar:active,
.CalendarDay__highlighted_calendar:hover {{
  background: #ffce71;
  color: #484848
}}
.CalendarDay__selected_span {{
  background: #66e2da;
  border: 1px double #33dacd;
  color: #fff
}}
.CalendarDay__selected_span:active,
.CalendarDay__selected_span:hover {{
  background: #33dacd;
  border: 1px double #33dacd;
  color: #fff
}}
.CalendarDay__selected,
.CalendarDay__selected:active,
.CalendarDay__selected:hover {{
  background: #00a699;
  border: 1px double #00a699;
  color: #fff
}}
.CalendarDay__hovered_span,
.CalendarDay__hovered_span:hover {{
  background: #b2f1ec;
  border: 1px double #80e8e0;
  color: #007a87
}}
.CalendarDay__hovered_span:active {{
  background: #80e8e0;
  border: 1px double #80e8e0;
  color: #007a87
}}
.CalendarDay__blocked_calendar,
.CalendarDay__blocked_calendar:active,
.CalendarDay__blocked_calendar:hover {{
  background: #cacccd;
  border: 1px solid #cacccd;
  color: #82888a
}}
.CalendarDay__blocked_out_of_range,
.CalendarDay__blocked_out_of_range:active,
.CalendarDay__blocked_out_of_range:hover {{
  background: #fff;
  border: 1px solid #e4e7e7;
  color: #cacccd
}}
.CalendarDay__hovered_start_first_possible_end {{
  background: #eceeee;
  border: 1px double #eceeee
}}
.CalendarDay__hovered_start_blocked_min_nights {{
  background: #eceeee;
  border: 1px double #e4e7e7
}}
.CalendarMonth {{
  background: #fff;
  text-align: center;
  vertical-align: top;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none
}}
.CalendarMonth_table {{
  border-collapse: collapse;
  border-spacing: 0
}}
.CalendarMonth_verticalSpacing {{
  border-collapse: separate
}}
.CalendarMonth_caption {{
  color: #484848;
  font-size: 18px;
  text-align: center;
  padding-top: 22px;
  padding-bottom: 37px;
  caption-side: initial
}}
.CalendarMonth_caption__verticalScrollable {{
  padding-top: 12px;
  padding-bottom: 7px
}}
.CalendarMonthGrid {{
  background: #fff;
  text-align: left;
  z-index: 0
}}
.CalendarMonthGrid__animating {{
  z-index: 1
}}
.CalendarMonthGrid__horizontal {{
  position: absolute;
  left: 9px
}}
.CalendarMonthGrid__vertical {{
  margin: 0 auto
}}
.CalendarMonthGrid__vertical_scrollable {{
  margin: 0 auto;
  overflow-y: scroll
}}
.CalendarMonthGrid_month__horizontal {{
  display: inline-block;
  vertical-align: top;
  min-height: 100%
}}
.CalendarMonthGrid_month__hideForAnimation {{
  position: absolute;
  z-index: -1;
  opacity: 0;
  pointer-events: none
}}
.CalendarMonthGrid_month__hidden {{
  visibility: hidden
}}
.DayPickerNavigation {{
  position: relative;
  z-index: 2
}}
.DayPickerNavigation__horizontal {{
  height: 0
}}
.DayPickerNavigation__verticalDefault {{
  position: absolute;
  width: 100%;
  height: 52px;
  bottom: 0;
  left: 0
}}
.DayPickerNavigation__verticalScrollableDefault {{
  position: relative
}}
.DayPickerNavigation_button {{
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  border: 0;
  padding: 0;
  margin: 0
}}
.DayPickerNavigation_button__default {{
  border: 1px solid #e4e7e7;
  background-color: #fff;
  color: #757575
}}
.DayPickerNavigation_button__default:focus,
.DayPickerNavigation_button__default:hover {{
  border: 1px solid #c4c4c4
}}
.DayPickerNavigation_button__default:active {{
  background: #f2f2f2
}}
.DayPickerNavigation_button__disabled {{
  cursor: default;
  border: 1px solid #f2f2f2
}}
.DayPickerNavigation_button__disabled:focus,
.DayPickerNavigation_button__disabled:hover {{
  border: 1px solid #f2f2f2
}}
.DayPickerNavigation_button__disabled:active {{
  background: 0 0
}}
.DayPickerNavigation_button__horizontalDefault {{
  position: absolute;
  top: 18px;
  line-height: .78;
  border-radius: 3px;
  padding: 6px 9px
}}
.DayPickerNavigation_leftButton__horizontalDefault {{
  left: 22px
}}
.DayPickerNavigation_rightButton__horizontalDefault {{
  right: 22px
}}
.DayPickerNavigation_button__verticalDefault {{
  padding: 5px;
  background: #fff;
  box-shadow: 0 0 5px 2px rgba(0,0,0,.1);
  position: relative;
  display: inline-block;
  text-align: center;
  height: 100%;
  width: 50%
}}
.DayPickerNavigation_nextButton__verticalDefault {{
  border-left: 0
}}
.DayPickerNavigation_nextButton__verticalScrollableDefault {{
  width: 100%
}}
.DayPickerNavigation_svg__horizontal {{
  height: 19px;
  width: 19px;
  fill: #82888a;
  display: block
}}
.DayPickerNavigation_svg__vertical {{
  height: 42px;
  width: 42px;
  fill: #484848
}}
.DayPickerNavigation_svg__disabled {{
  fill: #f2f2f2
}}
.DayPicker {{
  background: #fff;
  position: relative;
  text-align: left
}}
.DayPicker__horizontal {{
  background: #fff
}}
.DayPicker__verticalScrollable {{
  height: 100%
}}
.DayPicker__hidden {{
  visibility: hidden
}}
.DayPicker__withBorder {{
  box-shadow: 0 2px 6px rgba(0,0,0,.05),0 0 0 1px rgba(0,0,0,.07);
  border-radius: 3px
}}
.DayPicker_portal__horizontal {{
  box-shadow: none;
  position: absolute;
  left: 50%;
  top: 50%
}}
.DayPicker_portal__vertical {{
  position: initial
}}
.DayPicker_focusRegion {{
  outline: 0
}}
.DayPicker_calendarInfo__horizontal,
.DayPicker_wrapper__horizontal {{
  display: inline-block;
  vertical-align: top
}}
.DayPicker_weekHeaders {{
  position: relative
}}
.DayPicker_weekHeaders__horizontal {{
  margin-left: 9px
}}
.DayPicker_weekHeader {{
  color: #757575;
  position: absolute;
  top: 62px;
  z-index: 2;
  text-align: left
}}
.DayPicker_weekHeader__vertical {{
  left: 50%
}}
.DayPicker_weekHeader__verticalScrollable {{
  top: 0;
  display: table-row;
  border-bottom: 1px solid #dbdbdb;
  background: #fff;
  margin-left: 0;
  left: 0;
  width: 100%;
  text-align: center
}}
.DayPicker_weekHeader_ul {{
  list-style: none;
  margin: 1px 0;
  padding-left: 0;
  padding-right: 0;
  font-size: 14px
}}
.DayPicker_weekHeader_li {{
  display: inline-block;
  text-align: center
}}
.DayPicker_transitionContainer {{
  position: relative;
  overflow: hidden;
  border-radius: 3px
}}
.DayPicker_transitionContainer__horizontal {{
  -webkit-transition: height .2s ease-in-out;
  -moz-transition: height .2s ease-in-out;
  transition: height .2s ease-in-out
}}
.DayPicker_transitionContainer__vertical {{
  width: 100%
}}
.DayPicker_transitionContainer__verticalScrollable {{
  padding-top: 20px;
  height: 100%;
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  overflow-y: scroll
}}
.DateInput {{
  margin: 0;
  padding: 0;
  background: #fff;
  position: relative;
  display: inline-block;
  width: 130px;
  vertical-align: middle
}}
.DateInput__small {{
  width: 97px
}}
.DateInput__block {{
  width: 100%
}}
.DateInput__disabled {{
  background: #f2f2f2;
  color: #dbdbdb
}}
.DateInput_input {{
  font-weight: 200;
  font-size: 19px;
  line-height: 24px;
  color: #484848;
  background-color: #fff;
  width: 100%;
  padding: 11px 11px 9px;
  border: 0;
  border-top: 0;
  border-right: 0;
  border-bottom: 2px solid transparent;
  border-left: 0;
  border-radius: 0
}}
.DateInput_input__small {{
  font-size: 15px;
  line-height: 18px;
  letter-spacing: .2px;
  padding: 7px 7px 5px
}}
.DateInput_input__regular {{
  font-weight: auto
}}
.DateInput_input__readOnly {{
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none
}}
.DateInput_input__focused {{
  outline: 0;
  background: #fff;
  border: 0;
  border-top: 0;
  border-right: 0;
  border-bottom: 2px solid #008489;
  border-left: 0
}}
.DateInput_input__disabled {{
  background: #f2f2f2;
  font-style: italic
}}
.DateInput_screenReaderMessage {{
  border: 0;
  clip: rect(0,0,0,0);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px
}}
.DateInput_fang {{
  position: absolute;
  width: 20px;
  height: 10px;
  left: 22px;
  z-index: 2
}}
.DateInput_fangShape {{
  fill: #fff
}}
.DateInput_fangStroke {{
  stroke: #dbdbdb;
  fill: transparent
}}
.DateRangePickerInput {{
  background-color: #fff;
  display: inline-block
}}
.DateRangePickerInput__disabled {{
  background: #f2f2f2
}}
.DateRangePickerInput__withBorder {{
  border-radius: 2px;
  border: 1px solid #dbdbdb
}}
.DateRangePickerInput__rtl {{
  direction: rtl
}}
.DateRangePickerInput__block {{
  display: block
}}
.DateRangePickerInput__showClearDates {{
  padding-right: 30px
}}
.DateRangePickerInput_arrow {{
  display: inline-block;
  vertical-align: middle;
  color: #484848
}}
.DateRangePickerInput_arrow_svg {{
  vertical-align: middle;
  fill: #484848;
  height: 24px;
  width: 24px
}}
.DateRangePickerInput_clearDates {{
  background: 0 0;
  border: 0;
  color: inherit;
  font: inherit;
  line-height: normal;
  overflow: visible;
  cursor: pointer;
  padding: 10px;
  margin: 0 10px 0 5px;
  position: absolute;
  right: 0;
  top: 50%;
  -webkit-transform: translateY(-50%);
  -ms-transform: translateY(-50%);
  transform: translateY(-50%)
}}
.DateRangePickerInput_clearDates__small {{
  padding: 6px
}}
.DateRangePickerInput_clearDates_default:focus,
.DateRangePickerInput_clearDates_default:hover {{
  background: #dbdbdb;
  border-radius: 50%
}}
.DateRangePickerInput_clearDates__hide {{
  visibility: hidden
}}
.DateRangePickerInput_clearDates_svg {{
  fill: #82888a;
  height: 12px;
  width: 15px;
  vertical-align: middle
}}
.DateRangePickerInput_clearDates_svg__small {{
  height: 9px
}}
.DateRangePickerInput_calendarIcon {{
  background: 0 0;
  border: 0;
  color: inherit;
  font: inherit;
  line-height: normal;
  overflow: visible;
  cursor: pointer;
  display: inline-block;
  vertical-align: middle;
  padding: 10px;
  margin: 0 5px 0 10px
}}
.DateRangePickerInput_calendarIcon_svg {{
  fill: #82888a;
  height: 15px;
  width: 14px;
  vertical-align: middle
}}
.DateRangePicker {{
  position: relative;
  display: inline-block
}}
.DateRangePicker__block {{
  display: block
}}
.DateRangePicker_picker {{
  z-index: 1;
  background-color: #fff;
  position: absolute
}}
.DateRangePicker_picker__rtl {{
  direction: rtl
}}
.DateRangePicker_picker__directionLeft {{
  left: 0
}}
.DateRangePicker_picker__directionRight {{
  right: 0
}}
.DateRangePicker_picker__portal {{
  background-color: rgba(0,0,0,.3);
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%
}}
.DateRangePicker_picker__fullScreenPortal {{
  background-color: #fff
}}
.DateRangePicker_closeButton {{
  background: 0 0;
  border: 0;
  color: inherit;
  font: inherit;
  line-height: normal;
  overflow: visible;
  cursor: pointer;
  position: absolute;
  top: 0;
  right: 0;
  padding: 15px;
  z-index: 2
}}
.DateRangePicker_closeButton:focus,
.DateRangePicker_closeButton:hover {{
  color: darken(#cacccd,10%);
  text-decoration: none
}}
.DateRangePicker_closeButton_svg {{
  height: 15px;
  width: 15px;
  fill: #cacccd
}}</style><style type="text/css">.DateInput_input {{
    box-sizing: border-box;
}}

.DayPickerNavigation__verticalDefault {{
    text-align: center;
    height: initial;
    padding: 10px 0px;
}}

.DayPickerNavigation_svg__vertical {{
    height: 20px;
}}
</style>
        <meta name="description" content="This website gives the latest data and visualizations of the Novel Covid 19 Virus.">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script async="" src="https://buttons-config.sharethis.com/js/60597de1f6067000116b078b.js"></script><script async="" src="https://arc.io/widget.min.js#LHbAsxJ6"></script>
        <script type="text/javascript" src="https://platform-api.sharethis.com/js/sharethis.js#property=60597de1f6067000116b078b&amp;product=sop" async="async"></script>
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async="" src="https://www.googletagmanager.com/gtag/js?id=G-BVFL2XTDQ8"></script>
        <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());

        gtag('config', 'G-BVFL2XTDQ8');
        </script>
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta charset="UTF-8">
        <title>Corona Tracker</title>
        <link rel="icon" type="image/x-icon" href="/home/assets/favicon.ico?m=1616760516.946934">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/superhero/bootstrap.min.css">
<link rel="stylesheet" href="/home/assets/styles.css?m=1617452405.4350955">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script><link href="https://gateway.arc.io" crossorigin="" rel="preconnect" id="arc-preconnect-gateway" data-arc-widget=""><link href="https://webseed.arc.io" crossorigin="" rel="preconnect" id="arc-preconnect-webseed" data-arc-widget=""><link href="https://static.arc.io/widget/js/core.js?01b7da9" rel="modulepreload" as="script" id="arc-preload-corejs" data-arc-widget=""><script src="https://static.arc.io/widget/js/core.js?01b7da9" type="module" async="" id="arc-corejs" data-arc-widget=""></script><script src="https://static.arc.io/widget/js/core-legacy.js?01b7da9" nomodule="" async="" id="arc-corejs-legacy" data-arc-widget=""></script>
    <style data-styled="" data-styled-version="4.4.0"></style><script charset="utf-8" src="https://static.arc.io/widget/js/vendors~widget-ui.js?01b7da9"></script><link rel="stylesheet" type="text/css" href="https://static.arc.io/widget/css/widget.css?01b7da9"><script charset="utf-8" src="https://static.arc.io/widget/js/widget-ui.js?01b7da9"></script><script charset="utf-8" src="https://static.arc.io/widget/js/vendors~widget-sc-client.js?01b7da9"></script><script charset="utf-8" src="https://static.arc.io/widget/js/widget-sc-client.js?01b7da9"></script>
  </head>
  <body>
    <iframe width="100%" height="100%" frameBorder="0" src="https://thunder2020.pythonanywhere.com/{}"></iframe>
  </body>
</html>
"""

pages = ['index', 'timeline', 'datatable', 'map', 'counter', 'growth', 'infocenter', 'about']


for page in pages:
  print(f"Writing {page}")
  with open(page+'.html', "w+") as f:
    f.write(template.format(page))