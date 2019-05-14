import os

home = '/home/' + os.getlogin()
print(os.listdir(home))