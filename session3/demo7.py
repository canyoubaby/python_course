import re
rex = 'Regular expression'
pattern = re.compile(rex)
s = 'input string'
pattern.search(s)
pattern.match(s)
pattern.findall(s)