try:
    result_out = input()
    while result_out !='':
        print(result_out)
        result_out = input()
except EOFError as ex:
    pass    
    
