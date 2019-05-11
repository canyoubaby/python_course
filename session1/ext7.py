def filter(l, rex):
    list_l = list()
    for x in l:
        if x.startswith(rex):
            list_l.append(x)
    print(list_l) 
filter(['ab', 'bca', 'def' ,'a'], 'a')
