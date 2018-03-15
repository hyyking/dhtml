#Lib------------------------------------------------------------------------------------------------------------------------------------------------------

from HTMLParser import HTMLParser

#Samplepage------------------------------------------------------------------------------------------------------------------------------------------------------

page = open('YOUR HTML FILE HERE', 'r')

#Tag lists------------------------------------------------------------------------------------------------------------------------------------------------------

useless_headers = ['html','head','meta', 'link', 'title', 'base','style', 'script', '!DOCTYPE html']
selfclosing = ['area','base','br','col', 'command', 'embed', 'hr','input', 'keygen', 'link', 'menuitem', 'meta', 'param','source', 'track', 'wbr']
body = ['body']
link = ['a']

#Idents------------------------------------------------------------------------------------------------------------------------------------------------------

ident_text = '	'
ident_lvl = 0

#Writing Fs------------------------------------------------------------------------------------------------------------------------------------------------------

def input(tag, attrs):
	global ident_lvl 
	
	att = dict(attrs)
	
	start = ''
	
	#if useless
	if tag in useless_headers or tag in selfclosing:
		ident_lvl = ident_lvl
		return
	
	#if the tag is the body
	elif tag in body:
		ident = ident_text * ident_lvl

		start = '(id=\''+ att.get('id','') +'\', className=\''+ att.get('class','') +'\',style={}, children=['
		
		ident_lvl = ident_lvl + 1
		return parser.result.write('app.layout = ' + ident + 'html.' + 'div'.title() + start + '\n')

	elif tag in link:
			ident = ident_text * ident_lvl
			start = '(id=\''+ att.get('id','') +'\', className=\''+ att.get('class','') +'\', href=\''+ att.get('href','') +'\', style={}, children=['
			ident_lvl = ident_lvl + 1
			return parser.result.write(ident + 'html.' + tag.title() + start + '\n')
		
	else:
		if tag != 'img':
			ident = ident_text * ident_lvl
			
			start = '(id=\''+ att.get('id','') +'\', className=\''+ att.get('class','') +'\',style={}, children=['
			ident_lvl = ident_lvl + 1
			return parser.result.write(ident + 'html.' + tag.title() + start + '\n')
		else:
			nonclosing(tag, attrs)

def output(tag):
	global ident_lvl
	end = ''
	
	if tag in useless_headers or tag in selfclosing:
		return
	
	elif tag == 'img':
		print(tag)
		ident_lvl = ident_lvl - 1
		return

	elif tag in body:
		ident_lvl = ident_lvl - 1
		ident = ident_text * ident_lvl
		end = '])'
		return parser.result.write(ident + end + '\n')

	else:
		ident_lvl = ident_lvl - 1
		ident = ident_text * ident_lvl
		end = ']),'
		return parser.result.write(ident + end + '\n')

def nonclosing(tag, attrs):
	global ident_lvl
	
	att = dict(attrs)
	
	if tag == 'img':
		ident = ident_text * ident_lvl
		nonclosed = '(id=\''+ att.get('id','') +'\', className=\''+ att.get('class','') +'\', src=\''+ att.get('src','') +'\'),'
		return parser.result.write(ident +'html.' + tag.title() + nonclosed + '\n' )
	else:
		return
#Parser------------------------------------------------------------------------------------------------------------------------------------------------------

class GetTags(HTMLParser):
	result = open('result.py', 'w')

	def handle_starttag(self, tag, attrs):
		return input(tag, attrs)

	def handle_endtag(self, tag):
		return output(tag)

	def handle_startendtag(self, tag):
		return nonclosing(tag)

#Create Object------------------------------------------------------------------------------------------------------------------------------------------------------

parser = GetTags()

#Write imports------------------------------------------------------------------------------------------------------------------------------------------------------

parser.result.write('import dash\nimport dash_core_components as dcc\nimport dash_html_components as html\n\n')

parser.result.write('app = dash.Dash(__name__)\n\n')

#write html------------------------------------------------------------------------------------------------------------------------------------------------------

for line in page:
	parser.feed(line)

#Dash Server------------------------------------------------------------------------------------------------------------------------------------------------------

parser.result.write('\n\nif __name__ == \'__main__\':\n'+ ident_text +'app.run_server(debug=True)')

#End of Programme------------------------------------------------------------------------------------------------------------------------------------------------------
page.close()
print('done')
