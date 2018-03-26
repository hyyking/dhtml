#Author = Léo Duret
#Version = 0.20
#

from HTMLParser import HTMLParser
import dash_core_components as dcc

selfclosing = ['img','area','base','br','col', 'command', 'embed', 'hr','input', 'keygen', 'link', 'menuitem', 'meta', 'param','source', 'track', 'wbr']
headers = ['html','head','meta', 'link', 'title', 'base','style', 'script', '!DOCTYPE html']


class Dhtml(object):
	main_children = []

	dcc_a = {'id': None, 'selectionStart': None, 'date': None, 'allowCross': None, 'max_date_allowed': None, 'style_disabled': None, 'accept': None, 'minLength': None, 'last_modified': None, 'draggable': None, 'type': None, 'class': None, 'clickData': None, 'calendar_orientation': None, 'vertical': None, 'name': None, 'end_date': None, 'rows': None, 'min': None, 'selectedData': None, 'labelClassName': None, 'readonly': None, 'max_size': None, 'clearable': None, 'first_day_of_week': None, 'tabIndex': None, 'marks': None, 'inputClassName': None, 'count': None, 'is_RTL': None, 'display_format': None, 'contentEditable': None, 'selectionDirection': None, 'className_disabled': None, 'hoverData': None, 'style_active': None, 'day_size': None, 'dir': None, 'disabled': None, 'figure': None, 'relayoutData': None, 'cols': None, 'inputStyle': None, 'config': None, 'show_outside_days': None, 'updatemode': None, 'disable_click': None, 'with_full_screen_portal': None, 'dots': None, 'spellcheck': None, 'multi': None, 'start_date': None, 'containerProps': None, 'start_date_placeholder_text': None, 'children': None, 'month_format': None, 'min_date_allowed': None, 'autocomplete': None, 'className_active': None, 'labelStyle': None, 'filename': None, 'className_reject': None, 'readOnly': None, 'title': None, 'min_size': None, 'included': None, 'hidden': None, 'stay_open_on_select': None, 'animation_options': None, 'end_date_placeholder_text': None, 'maxLength': None, 'style_reject': None, 'autofocus': None, 'clear_on_unhover': None, 'searchable': None, 'form': None, 'contents': None, 'placeholder': None, 'multiple': None, 'inputmode': None, 'step': None, 'style': None, 'options': None, 'size': None, 'pushable': None, 'with_portal': None, 'maxlength': None, 'contextMenu': None, 'required': None, 'initial_visible_month': None, 'value': None, 'max': None, 'reopen_calendar_on_clear': None, 'autoFocus': None, 'animate': None, 'spellCheck': None, 'number_of_months_shown': None, 'accessKey': None, 'pattern': None, 'lang': None, 'minlength': None, 'selectionEnd': None, 'wrap': None, 'list': None, 'minimum_nights': None}
	
	corecomponents = {
		'dccdropdown':dcc.Dropdown(className=dcc_a['class'], clearable=dcc_a['clearable'], disabled=dcc_a['disabled'], id=dcc_a['id'], multi=dcc_a['multi'], options=dcc_a['options'], placeholder=dcc_a['placeholder'], searchable=dcc_a['searchable'], value=dcc_a['value']),
		'dccslider':dcc.Slider(className=dcc_a['class'], disabled=dcc_a['disabled'], dots=dcc_a['dots'], id=dcc_a['id'], included=dcc_a['included'], marks=dcc_a['marks'], max=dcc_a['max'], min=dcc_a['min'], step=dcc_a['step'], updatemode=dcc_a['updatemode'], value=dcc_a['value'], vertical=dcc_a['vertical']),
		'dccRangeslider':dcc.RangeSlider(allowCross=dcc_a['allowCross'], className=dcc_a['class'], count=dcc_a['count'], disabled=dcc_a['disabled'], dots=dcc_a['dots'], id=dcc_a['id'], included=dcc_a['included'], marks=dcc_a['marks'], max=dcc_a['max'], min=dcc_a['min'], pushable=dcc_a['pushable'], step=dcc_a['step'], updatemode=dcc_a['updatemode'], value=dcc_a['value'], vertical=dcc_a['vertical']),
		'dccinput':dcc.Input(autocomplete=dcc_a['autocomplete'], autofocus=dcc_a['autofocus'], className=dcc_a['class'], id=dcc_a['id'], inputmode=dcc_a['inputmode'], list=dcc_a['list'], max=dcc_a['max'], maxlength=dcc_a['maxlength'], min=dcc_a['min'], minlength=dcc_a['minlength'], multiple=dcc_a['multiple'], name=dcc_a['name'], pattern=dcc_a['pattern'], placeholder=dcc_a['placeholder'], readonly=dcc_a['readonly'], required=dcc_a['required'], selectionDirection=dcc_a["selectionDirection"], selectionEnd=dcc_a['selectionEnd'], selectionStart=dcc_a['selectionStart'], size=dcc_a['size'], spellcheck=dcc_a['spellcheck'], step=dcc_a['step'], style=dcc_a['style'], type=dcc_a['type'], value=dcc_a['value']),
		'dcctextarea':dcc.Textarea(accessKey=dcc_a['accessKey'],autoFocus=dcc_a['autoFocus'],className=dcc_a['class'],cols=dcc_a['cols'],contentEditable=dcc_a['contentEditable'],contextMenu=dcc_a['contextMenu'],dir=dcc_a['dir'],disabled=dcc_a['disabled'],draggable=dcc_a['draggable'],form=dcc_a['form'],hidden=dcc_a['hidden'],id=dcc_a['id'],lang=dcc_a['lang'],maxLength=dcc_a['maxLength'],minLength=dcc_a['minLength'],name=dcc_a['name'],placeholder=dcc_a['placeholder'],readOnly=dcc_a['readOnly'],required=dcc_a['required'],rows=dcc_a['rows'],spellCheck=dcc_a['spellCheck'],style=dcc_a['style'],tabIndex=dcc_a['tabIndex'],title=dcc_a['title'],value=dcc_a['value'],wrap=dcc_a['wrap']),
		'dccradioitems':dcc.RadioItems(className=dcc_a['class'],id=dcc_a['id'],inputClassName=dcc_a['inputClassName'],inputStyle=dcc_a['inputStyle'],labelClassName=dcc_a['labelClassName'],labelStyle=dcc_a['labelStyle'],options=dcc_a['options'],style=dcc_a['style'],value=dcc_a['value']),
		'dccdatepickersingle':dcc.DatePickerSingle(calendar_orientation=dcc_a['calendar_orientation'],clearable=dcc_a['clearable'],date=dcc_a['date'],day_size=dcc_a['day_size'],disabled=dcc_a['disabled'],display_format=dcc_a['display_format'],first_day_of_week=dcc_a['first_day_of_week'],id=dcc_a['id'],initial_visible_month=dcc_a['initial_visible_month'],is_RTL=dcc_a['is_RTL'],max_date_allowed=dcc_a['max_date_allowed'],min_date_allowed=dcc_a['min_date_allowed'],month_format=dcc_a['month_format'],number_of_months_shown=dcc_a['number_of_months_shown'],placeholder=dcc_a['placeholder'],reopen_calendar_on_clear=dcc_a['reopen_calendar_on_clear'],show_outside_days=dcc_a['show_outside_days'],stay_open_on_select=dcc_a['stay_open_on_select'],with_full_screen_portal=dcc_a['with_full_screen_portal'],with_portal=dcc_a['with_portal']),
		'dccdatepickerrange':dcc.DatePickerRange(calendar_orientation=dcc_a['calendar_orientation'],clearable=dcc_a['clearable'],day_size=dcc_a['day_size'],disabled=dcc_a['disabled'],display_format=dcc_a['display_format'],end_date=dcc_a['end_date'],end_date_placeholder_text=dcc_a['end_date_placeholder_text'],first_day_of_week=dcc_a['first_day_of_week'],id=dcc_a['id'],initial_visible_month=dcc_a['initial_visible_month'],is_RTL=dcc_a['is_RTL'],max_date_allowed=dcc_a['max_date_allowed'],min_date_allowed=dcc_a['min_date_allowed'],minimum_nights=dcc_a['minimum_nights'],month_format=dcc_a['month_format'],number_of_months_shown=dcc_a['number_of_months_shown'],reopen_calendar_on_clear=dcc_a['reopen_calendar_on_clear'],show_outside_days=dcc_a['show_outside_days'],start_date=dcc_a['start_date'],start_date_placeholder_text=dcc_a['start_date_placeholder_text'],stay_open_on_select=dcc_a['stay_open_on_select'],with_full_screen_portal=dcc_a['with_full_screen_portal'],with_portal=dcc_a['with_portal']),
		'dccmarkdown':dcc.Markdown(children=dcc_a['children'],className=dcc_a['class'],containerProps=dcc_a['containerProps'],id=dcc_a['id']),
		'dccuploadcomponent':dcc.Upload(accept=dcc_a['accept'],children=dcc_a['children'],className=dcc_a['class'],className_active=dcc_a['className_active'],className_disabled=dcc_a['className_disabled'],className_reject=dcc_a['className_reject'],contents=dcc_a['contents'],disable_click=dcc_a['disable_click'],disabled=dcc_a['disabled'],filename=dcc_a['filename'],id=dcc_a['id'],last_modified=dcc_a['last_modified'],max_size=dcc_a['max_size'],min_size=dcc_a['min_size'],multiple=dcc_a['multiple'],style=dcc_a['style'],style_active=dcc_a['style_active'],style_disabled=dcc_a['style_disabled'],style_reject=dcc_a['style_reject']),
		'dccgraph':dcc.Graph(animate=dcc_a['animate'],animation_options=dcc_a['animation_options'],className=dcc_a['class'],clear_on_unhover=dcc_a['clear_on_unhover'],clickData=dcc_a['clickData'],config=dcc_a['config'],figure=dcc_a['figure'],hoverData=dcc_a['hoverData'],id=dcc_a['id'],relayoutData=dcc_a['relayoutData'],selectedData=dcc_a['selectedData'],style=dcc_a['style']),
	}	
	
	def __init__(self, file_in, file_out='result.py'):
		self.file_in = file_in
		self.file_out = file_out
		self.opened = open(file_in, 'r')

	def __str__(self):
		return "<Object Dhtml | In: {}; Out: {} | call .dparse() to write file>".format(self.file_in, self.file_out) 

	class dHandler(HTMLParser):

		def updatedcc_a(self, dic):
			for key in dic:
				Dhtml.dcc_a[key] = dic.get(key, None)

		def resetdcc_a(self):
			a = {'id': None, 'selectionStart': None, 'date': None, 'allowCross': None, 'max_date_allowed': None, 'style_disabled': None, 'accept': None, 'minLength': None, 'last_modified': None, 'draggable': None, 'type': None, 'class': None, 'clickData': None, 'calendar_orientation': None, 'vertical': None, 'name': None, 'end_date': None, 'rows': None, 'min': None, 'selectedData': None, 'labelClassName': None, 'readonly': None, 'max_size': None, 'clearable': None, 'first_day_of_week': None, 'tabIndex': None, 'marks': None, 'inputClassName': None, 'count': None, 'is_RTL': None, 'display_format': None, 'contentEditable': None, 'selectionDirection': None, 'className_disabled': None, 'hoverData': None, 'style_active': None, 'day_size': None, 'dir': None, 'disabled': None, 'figure': None, 'relayoutData': None, 'cols': None, 'inputStyle': None, 'config': None, 'show_outside_days': None, 'updatemode': None, 'disable_click': None, 'with_full_screen_portal': None, 'dots': None, 'spellcheck': None, 'multi': None, 'start_date': None, 'containerProps': None, 'start_date_placeholder_text': None, 'children': None, 'month_format': None, 'min_date_allowed': None, 'autocomplete': None, 'className_active': None, 'labelStyle': None, 'filename': None, 'className_reject': None, 'readOnly': None, 'title': None, 'min_size': None, 'included': None, 'hidden': None, 'stay_open_on_select': None, 'animation_options': None, 'end_date_placeholder_text': None, 'maxLength': None, 'style_reject': None, 'autofocus': None, 'clear_on_unhover': None, 'searchable': None, 'form': None, 'contents': None, 'placeholder': None, 'multiple': None, 'inputmode': None, 'step': None, 'style': None, 'options': None, 'size': None, 'pushable': None, 'with_portal': None, 'maxlength': None, 'contextMenu': None, 'required': None, 'initial_visible_month': None, 'value': None, 'max': None, 'reopen_calendar_on_clear': None, 'autoFocus': None, 'animate': None, 'spellCheck': None, 'number_of_months_shown': None, 'accessKey': None, 'pattern': None, 'lang': None, 'minlength': None, 'selectionEnd': None, 'wrap': None, 'list': None, 'minimum_nights': None}
			Dhtml.dcc_a = a

		def updatedcc(self):
			b = {
				'dccdropdown':dcc.Dropdown(className=Dhtml.dcc_a['class'], clearable=Dhtml.dcc_a['clearable'], disabled=Dhtml.dcc_a['disabled'], id=Dhtml.dcc_a['id'], multi=Dhtml.dcc_a['multi'], options=Dhtml.dcc_a['options'], placeholder=Dhtml.dcc_a['placeholder'], searchable=Dhtml.dcc_a['searchable'], value=Dhtml.dcc_a['value']),
				'dccslider':dcc.Slider(className=Dhtml.dcc_a['class'], disabled=Dhtml.dcc_a['disabled'], dots=Dhtml.dcc_a['dots'], id=Dhtml.dcc_a['id'], included=Dhtml.dcc_a['included'], marks=Dhtml.dcc_a['marks'], max=Dhtml.dcc_a['max'], min=Dhtml.dcc_a['min'], step=Dhtml.dcc_a['step'], updatemode=Dhtml.dcc_a['updatemode'], value=Dhtml.dcc_a['value'], vertical=Dhtml.dcc_a['vertical']),
				'dccRangeslider':dcc.RangeSlider(allowCross=Dhtml.dcc_a['allowCross'], className=Dhtml.dcc_a['class'], count=Dhtml.dcc_a['count'], disabled=Dhtml.dcc_a['disabled'], dots=Dhtml.dcc_a['dots'], id=Dhtml.dcc_a['id'], included=Dhtml.dcc_a['included'], marks=Dhtml.dcc_a['marks'], max=Dhtml.dcc_a['max'], min=Dhtml.dcc_a['min'], pushable=Dhtml.dcc_a['pushable'], step=Dhtml.dcc_a['step'], updatemode=Dhtml.dcc_a['updatemode'], value=Dhtml.dcc_a['value'], vertical=Dhtml.dcc_a['vertical']),
				'dccinput':dcc.Input(autocomplete=Dhtml.dcc_a['autocomplete'], autofocus=Dhtml.dcc_a['autofocus'], className=Dhtml.dcc_a['class'], id=Dhtml.dcc_a['id'], inputmode=Dhtml.dcc_a['inputmode'], list=Dhtml.dcc_a['list'], max=Dhtml.dcc_a['max'], maxlength=Dhtml.dcc_a['maxlength'], min=Dhtml.dcc_a['min'], minlength=Dhtml.dcc_a['minlength'], multiple=Dhtml.dcc_a['multiple'], name=Dhtml.dcc_a['name'], pattern=Dhtml.dcc_a['pattern'], placeholder=Dhtml.dcc_a['placeholder'], readonly=Dhtml.dcc_a['readonly'], required=Dhtml.dcc_a['required'], selectionDirection=Dhtml.dcc_a["selectionDirection"], selectionEnd=Dhtml.dcc_a['selectionEnd'], selectionStart=Dhtml.dcc_a['selectionStart'], size=Dhtml.dcc_a['size'], spellcheck=Dhtml.dcc_a['spellcheck'], step=Dhtml.dcc_a['step'], style=Dhtml.dcc_a['style'], type=Dhtml.dcc_a['type'], value=Dhtml.dcc_a['value']),
				'dcctextarea':dcc.Textarea(accessKey=Dhtml.dcc_a['accessKey'],autoFocus=Dhtml.dcc_a['autoFocus'],className=Dhtml.dcc_a['class'],cols=Dhtml.dcc_a['cols'],contentEditable=Dhtml.dcc_a['contentEditable'],contextMenu=Dhtml.dcc_a['contextMenu'],dir=Dhtml.dcc_a['dir'],disabled=Dhtml.dcc_a['disabled'],draggable=Dhtml.dcc_a['draggable'],form=Dhtml.dcc_a['form'],hidden=Dhtml.dcc_a['hidden'],id=Dhtml.dcc_a['id'],lang=Dhtml.dcc_a['lang'],maxLength=Dhtml.dcc_a['maxLength'],minLength=Dhtml.dcc_a['minLength'],name=Dhtml.dcc_a['name'],placeholder=Dhtml.dcc_a['placeholder'],readOnly=Dhtml.dcc_a['readOnly'],required=Dhtml.dcc_a['required'],rows=Dhtml.dcc_a['rows'],spellCheck=Dhtml.dcc_a['spellCheck'],style=Dhtml.dcc_a['style'],tabIndex=Dhtml.dcc_a['tabIndex'],title=Dhtml.dcc_a['title'],value=Dhtml.dcc_a['value'],wrap=Dhtml.dcc_a['wrap']),
				'dccradioitems':dcc.RadioItems(className=Dhtml.dcc_a['class'],id=Dhtml.dcc_a['id'],inputClassName=Dhtml.dcc_a['inputClassName'],inputStyle=Dhtml.dcc_a['inputStyle'],labelClassName=Dhtml.dcc_a['labelClassName'],labelStyle=Dhtml.dcc_a['labelStyle'],options=Dhtml.dcc_a['options'],style=Dhtml.dcc_a['style'],value=Dhtml.dcc_a['value']),
				'dccdatepickersingle':dcc.DatePickerSingle(calendar_orientation=Dhtml.dcc_a['calendar_orientation'],clearable=Dhtml.dcc_a['clearable'],date=Dhtml.dcc_a['date'],day_size=Dhtml.dcc_a['day_size'],disabled=Dhtml.dcc_a['disabled'],display_format=Dhtml.dcc_a['display_format'],first_day_of_week=Dhtml.dcc_a['first_day_of_week'],id=Dhtml.dcc_a['id'],initial_visible_month=Dhtml.dcc_a['initial_visible_month'],is_RTL=Dhtml.dcc_a['is_RTL'],max_date_allowed=Dhtml.dcc_a['max_date_allowed'],min_date_allowed=Dhtml.dcc_a['min_date_allowed'],month_format=Dhtml.dcc_a['month_format'],number_of_months_shown=Dhtml.dcc_a['number_of_months_shown'],placeholder=Dhtml.dcc_a['placeholder'],reopen_calendar_on_clear=Dhtml.dcc_a['reopen_calendar_on_clear'],show_outside_days=Dhtml.dcc_a['show_outside_days'],stay_open_on_select=Dhtml.dcc_a['stay_open_on_select'],with_full_screen_portal=Dhtml.dcc_a['with_full_screen_portal'],with_portal=Dhtml.dcc_a['with_portal']),
				'dccdatepickerrange':dcc.DatePickerRange(calendar_orientation=Dhtml.dcc_a['calendar_orientation'],clearable=Dhtml.dcc_a['clearable'],day_size=Dhtml.dcc_a['day_size'],disabled=Dhtml.dcc_a['disabled'],display_format=Dhtml.dcc_a['display_format'],end_date=Dhtml.dcc_a['end_date'],end_date_placeholder_text=Dhtml.dcc_a['end_date_placeholder_text'],first_day_of_week=Dhtml.dcc_a['first_day_of_week'],id=Dhtml.dcc_a['id'],initial_visible_month=Dhtml.dcc_a['initial_visible_month'],is_RTL=Dhtml.dcc_a['is_RTL'],max_date_allowed=Dhtml.dcc_a['max_date_allowed'],min_date_allowed=Dhtml.dcc_a['min_date_allowed'],minimum_nights=Dhtml.dcc_a['minimum_nights'],month_format=Dhtml.dcc_a['month_format'],number_of_months_shown=Dhtml.dcc_a['number_of_months_shown'],reopen_calendar_on_clear=Dhtml.dcc_a['reopen_calendar_on_clear'],show_outside_days=Dhtml.dcc_a['show_outside_days'],start_date=Dhtml.dcc_a['start_date'],start_date_placeholder_text=Dhtml.dcc_a['start_date_placeholder_text'],stay_open_on_select=Dhtml.dcc_a['stay_open_on_select'],with_full_screen_portal=Dhtml.dcc_a['with_full_screen_portal'],with_portal=Dhtml.dcc_a['with_portal']),
				'dccmarkdown':dcc.Markdown(children=Dhtml.dcc_a['children'],className=Dhtml.dcc_a['class'],containerProps=Dhtml.dcc_a['containerProps'],id=Dhtml.dcc_a['id']),
				'dccuploadcomponent':dcc.Upload(accept=Dhtml.dcc_a['accept'],children=Dhtml.dcc_a['children'],className=Dhtml.dcc_a['class'],className_active=Dhtml.dcc_a['className_active'],className_disabled=Dhtml.dcc_a['className_disabled'],className_reject=Dhtml.dcc_a['className_reject'],contents=Dhtml.dcc_a['contents'],disable_click=Dhtml.dcc_a['disable_click'],disabled=Dhtml.dcc_a['disabled'],filename=Dhtml.dcc_a['filename'],id=Dhtml.dcc_a['id'],last_modified=Dhtml.dcc_a['last_modified'],max_size=Dhtml.dcc_a['max_size'],min_size=Dhtml.dcc_a['min_size'],multiple=Dhtml.dcc_a['multiple'],style=Dhtml.dcc_a['style'],style_active=Dhtml.dcc_a['style_active'],style_disabled=Dhtml.dcc_a['style_disabled'],style_reject=Dhtml.dcc_a['style_reject']),
				'dccgraph':dcc.Graph(animate=Dhtml.dcc_a['animate'],animation_options=Dhtml.dcc_a['animation_options'],className=Dhtml.dcc_a['class'],clear_on_unhover=Dhtml.dcc_a['clear_on_unhover'],clickData=Dhtml.dcc_a['clickData'],config=Dhtml.dcc_a['config'],figure=Dhtml.dcc_a['figure'],hoverData=Dhtml.dcc_a['hoverData'],id=Dhtml.dcc_a['id'],relayoutData=Dhtml.dcc_a['relayoutData'],selectedData=Dhtml.dcc_a['selectedData'],style=Dhtml.dcc_a['style']),	
			}
			Dhtml.corecomponents = b

		def handle_starttag(self, tag, attrs):
			if tag in headers:
				pass
			
			elif tag in Dhtml.corecomponents:
				self.resetdcc_a()
				dic = dict(attrs)
				self.updatedcc_a(dic)
				self.updatedcc()
				Dhtml.main_children.append(Dhtml.corecomponents[tag])

			
			else:
				pass

		def handle_endtag(self, tag):
			if tag in headers:
				pass
			
			else:
				pass

	def dparse(self):
		dparser = self.dHandler()
		
		for line in self.opened:
			dparser.feed(line)

		dparser.close()

	def dprint(self):
		return print(self.opened.read())
