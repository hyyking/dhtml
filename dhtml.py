#DHtml library
# Author = Léo Duret
# Version = 1.1

#imports
from HTMLParser import HTMLParser

#Lists of html and dcc
selfclosing = ['img','area','base','br','col', 'command', 'embed', 'hr','input', 'keygen', 'link', 'menuitem', 'meta', 'param','source', 'track', 'wbr']
headers = ['html','head','meta', 'link', 'title', 'base','style', 'script', '!DOCTYPE html']
corecomponents = {
	'dccdropdown':'Dropdown',
	'dccslider':'Slider',
	'dccRangeslider':'RangeSlider',
	'dccinput':'Input',
	'dcctextarea':'Textarea',
	'dcccheckboxes':'Checkboxes',
	'dccradioitems':'RadioItems',
	'dccbutton':'Button',
	'dccdatepickersingle':'DatePickerSingle',
	'dccdatepickerrange':'DatePickerRange',
	'dccmarkdown':'Markdown',
	'dccuploadcomponent':'Upload',
	'dcctabs':'Tabs',
	'dccgraphs':'Graph'
}

class Dhtml(object):
	'''Object Class Class Charactristics'''
	def __init__(self, file_in, file_out='dhtmlresult.py'):
		
		self.file_in = file_in
		self.file_out = file_out

		self.openfile = open(file_in, 'r')
		type(self).result = open(file_out, 'w')
	
	def __str__(self):
		return "<Object Dhtml | In: {}; Out: {} | call .dparse() to write file>".format(self.file_in, self.file_out)
	
	class Handler(HTMLParser):
		ident_text = '	'
		ident_lvl = 0

		def set_ident(self):
			ident = self.ident_text * self.ident_lvl
			self.ident_lvl = self.ident_lvl + 1
			return ident

		def remove_ident(self):
			self.ident_lvl = self.ident_lvl - 1
			ident = self.ident_text * self.ident_lvl
			return ident

		def att_handle(self, tag, att):
			return 'yes'

		def handle_starttag(self, tag, attrs):
			att = dict(attrs)
			attrib = ''
				
			if tag in headers:
				pass

			elif tag == 'body':
				ident = self.set_ident()
				attrib = '{}, children=['.format(self.att_handle(tag, att))
				return Dhtml.result.write(ident + 'html.' + 'Div'+ '(' + attrib + '\n')
			
			elif tag in corecomponents:
				ident = self.set_ident()
				attrib = '{}, children=['.format(self.att_handle(tag, att))
				return Dhtml.result.write(ident + 'dcc.' + corecomponents[tag] + '(' + attrib + '\n')
				
			elif tag in selfclosing:
				ident = self.set_ident()
				attrib = '{}, children=['.format(self.att_handle(tag, att))
				return Dhtml.result.write(ident + 'html.' + tag.title() + '(' + attrib + '\n')
				
			else:
				ident = self.set_ident()
				attrib = '{}, children=['.format(self.att_handle(tag, att))
				Dhtml.result.write(ident + 'html.' + tag.title() + '(' + attrib + '\n')
			
		def handle_endtag(self, tag):
			return

		def handle_attribendtag(self, tag, attrs):
			if tag in dash_core:
				return print('found')	
	#-------------------------------------------
	#File reading functions
	def dread(self):
		return self.result.read()

	def hprint(self):
		return print(self.openfile.read())
	#-------------------------------------------
	#File parsing functions
	def dparse(self):
		dparser = self.Handler()
		for line in self.openfile:
			dparser.feed(line)


res = Dhtml('htmlsample.html')

res.dparse()
print(res)
