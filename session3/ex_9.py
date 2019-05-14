import re

rex = 'frozen|snow|icy'
pattern = re.compile(rex)
def upper_string(matchobj):
    return matchobj.group(0).upper()
file = open('./frozen_bis.srt', mode='w')
file2 = open('./frozen.srt',mode='r')
file.write(pattern.sub(upper_string, file2.read()))
