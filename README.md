# htmltodash
Current Work on a Html to Dash Library

Greatings!
There are many goals to this library, and the goal of this file is to explain them. 

/!\-------------------HISTORY-----------------------------------------------------------------
But first let me tell you why I am working on it.
Since I’ve discovered Dash not a long time ago I always thought it was frustrating to write dash apps in python
and almost everybody knows how to write HTML at this stage, and it is often faster to write it than having to think about the layout 
of the dash app. This is why, using HTMLParser, I wrote a small script that converts HTML layouts into dash layouts (with the idents).
This script wasn't flawless (didn’t support HTML styling, didn’t allow you to write dcc in it).

So to solve all these 'misses' I decided to work on a full library, which goal is to write dash apps faster and enhance
the styling process (because beautifull is amazinger).

/!\-------------------COMMANDS/SYNTAX-----------------------------------------------------------------
It's always great to have intuitive syntax so check it out:
_____IN HTML___________
Write your standart html file exactly the same way you would do for a website
When you want to insert a dash_core_components element, write it like a html tag with 'dcc' in front of it
Exemple:
to add a graph write <dccGraph style={...} id=...>
_____IN PYTHON___________
Exemple:
obj = Dhtml(input file, output file[default=dhtmlresult.py])
obj.dparse()
print(obj.dread())

Let's take a look at the syntax of dparse():
        d | p a r s e 
       ---| ---------
 file?    | Action it executes
 d=dhtml  | In this case: 
 h=html   | Parse to create the new file

so hparse return the parsing but without the dash elements

all functions are available in d and h to enhance the way you use the Lib
