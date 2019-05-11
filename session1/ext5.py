# importing time module
import time
printarray = []
for i in range(0,100):
    printarray.append(str('|'))
print(printarray)
s =' '.join(printarray)
time.sleep(1)
print(s)



