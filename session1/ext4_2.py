odd_number = []

for i in range(1,101):
    if i % 2==1:
        odd_number.append(str(i))
print(odd_number) 

s = ':'.join(odd_number)
print(s)