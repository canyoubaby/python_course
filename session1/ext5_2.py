from time import sleep
loading = '|' *100
for i in range(100):
    print(loading[i], sep=' ', end=' ', flush=True); sleep(0.1)
