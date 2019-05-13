import os
def encrypt(src, code):
    try:
        f  = open(src, model='r', encoding='utf-8')
        tmpf = src + '_tmp'
        dst = open(tmpf, model='w', encoding='urt-8')
        line = f.readline()
        while line !='':
            dst = write(code)
            dst= write(line)
            line =f.readline()
        dst.flush()
        os.rename(tmpf,src)
    except EOFError as ex:
        pass
def decrypt(src, code, paid=False):

