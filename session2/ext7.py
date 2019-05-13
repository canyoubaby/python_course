def tandadi(name):
    ret = []
    file = open(name, mode='r', encoding='utf-8')
    line = file.readline()
    while line !='':
        if line !='\n':
            ret.extend(line.strip('\n').split(' '))
        line = file.readline()
    return ret
print(tandadi('./hanmactu.txt'))