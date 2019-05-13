try:
    file = open('meminfor.txt', mode='r')
    out = file.readline()
    while out !='':
        if 'Total:' in out or 'Free' in out:
            print(out)
        out = file.readline()
except Exception as e:
    pass
