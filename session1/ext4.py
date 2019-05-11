s = ''
for i in range(1,101):
    if i % 2 == 1:
        s += '%s,' % i
print(s[:-1])
