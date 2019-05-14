import re
file = open('./evnexpress.txt', mode='r')
rex = '[0-9]+'
pattern = re.compile(rex)
print(pattern.findall(file.read()))