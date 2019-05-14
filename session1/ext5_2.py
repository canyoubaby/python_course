import time
loading = '|' *100
for i in range(100):
    print(loading[i], sep=' ', end=' ', flush=True); time.sleep(0.1)
;