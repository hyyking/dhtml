# DHtml library
# Author = Léo Duret
# Version = 0.11

#imports
from HTMLParser import HTMLParser

#Lists of tag exeptions
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
	'dccgraph':'Graph'
}

class Dhtml(object):
	'''Main Object'''
	
	#DHTML
	class dHandler(HTMLParser):
		'''Handling The Parsing of DHTML'''
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
			'''att = dict(att)
												
												dstyle = []
												did = att.get('id','')
												dclass= att.get('class','')
									
												for keys in styling:
													style.append(keys)
													print(style)
												
												attribute = 'id=\'{}\', className=\'{}\''.format(did,dclass)
												return attribute'''
			return

		def handle_starttag(self, tag, attrs):
			att = attrs
			attrib = ''
				
			if tag in headers:
				pass

			elif tag == 'body':
				ident = self.set_ident()
				attrib = '{} children=['.format(self.att_handle(tag, att))
				return Dhtml.result.write(ident + 'html.' + 'Div'+ '(' + attrib + '\n')
			
			elif tag in corecomponents:
				ident = self.set_ident()
				attrib = '{} children=['.format(self.att_handle(tag, att))
				return Dhtml.result.write(ident + 'dcc.' + corecomponents[tag] + '(' + attrib + ']),' '\n'), self.remove_ident()
				
			elif tag in selfclosing:
				ident = self.set_ident()
				attrib = '{} children=['.format(self.att_handle(tag, att))
				return Dhtml.result.write(ident + 'html.' + tag.title() + '(' + attrib + ']),' + '\n'), self.remove_ident()
				
			else:
				ident = self.set_ident()
				attrib = '{}children=['.format(self.att_handle(tag, att))
				return Dhtml.result.write(ident + 'html.' + tag.title() + '(' + attrib + '\n')
			
		def handle_endtag(self, tag):
			closing = ''
			
			if tag in headers or tag in corecomponents or tag in selfclosing:
				return

			elif tag == 'body':
				ident = self.remove_ident()
				closing = '])'
				return Dhtml.result.write(ident + closing + '\n')

			else:
				ident = self.remove_ident()
				closing = ']),'
				return Dhtml.result.write(ident + closing + '\n')

		def handle_startendtag(self, tag, attrs):
			if tag in dash_core:
				return print('found')
	#HTML
	class hHandler(HTMLParser):
		'''Handling The Parsing of HTML'''
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
			return 'attributes'

		def handle_starttag(self, tag, attrs):
			att = dict(attrs)
			attrib = ''
				
			if tag in headers or tag in corecomponents:
				pass

			elif tag == 'body':
				ident = self.set_ident()
				attrib = '{}, children=['.format(self.att_handle(tag, att))
				return Dhtml.result.write(ident + 'html.' + 'Div'+ '(' + attrib + '\n')
				
			elif tag in selfclosing:
				ident = self.set_ident()
				attrib = '{}, children=['.format(self.att_handle(tag, att))
				return Dhtml.result.write(ident + 'html.' + tag.title() + '(' + attrib + ']),' + '\n'), self.remove_ident()
				
			else:
				ident = self.set_ident()
				attrib = '{}, children=['.format(self.att_handle(tag, att))
				return Dhtml.result.write(ident + 'html.' + tag.title() + '(' + attrib + '\n')
			
		def handle_endtag(self, tag):
			closing = ''
			
			if tag in headers or tag in corecomponents or tag in selfclosing:
				return

			elif tag == 'body':
				ident = self.remove_ident()
				closing = '])'
				return Dhtml.result.write(ident + closing + '\n')

			else:
				ident = self.remove_ident()
				closing = ']),'
				return Dhtml.result.write(ident + closing + '\n')

		def handle_startendtag(self, tag, attrs):
			if tag in dash_core:
				return print('found')	
	
	#-------------------------------------------
	'''Main Object Charactristics and Commands'''
	def __init__(self, file_in, file_out='dhtmlresult.py'):
		
		self.file_in = file_in
		self.file_out = file_out

		self.openfile = open(file_in, 'r')
		type(self).result = open(file_out, 'r+')
	
	def __str__(self):
		return "<Object Dhtml | In: {}; Out: {} | call .dparse() to write file>".format(self.file_in, self.file_out)
	
	#-------------------------------------------
	'''File reading functions'''
	def dread(self):
		return self.result.read()
	
	def hread(self):
		return self.openfile.read()
	
	#-------------------------------------------
	'''File printing function'''
	def dprint(self):
		return print(self.result.read())

	def hprint(self):
		return print(self.openfile.read())
	
	#-------------------------------------------
	'''File parsing functions'''
	def dparse(self):
		dparser = self.dHandler()
		for line in self.openfile:
			dparser.feed(line)
		dparser.close()

	def hparse(self):
		hparser = self.hHandler()
		for line in self.openfile:
			hparser.feed(line)
		return hparser.close()

