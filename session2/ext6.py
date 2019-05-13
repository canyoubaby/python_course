try:
    file = open('hanmactu.txt', mode='r')
    out = file.readline()
    index =1
    file_write = open('./output_' + str(index) + '.txt', mode='w+')
    while out !='':
        if out == '\n':
            index = index+1
            file_write = open('./output_' + str(index) + '.txt', mode='w+')
        else:
            file_write.write(out)
        out = file.readline()
except EOFError as ex :
    pass