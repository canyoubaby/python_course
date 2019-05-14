import re
rex = '[0-9]+'
pattern = re.compile(rex)
s = 'John was born in 1970, he joined SEAL force at the age of 30. John was killed in action in 2016.'
print(pattern.sub('dd/mm/yyyy', s))