import time
import os
import pandas

while True:
    if os.path.exists("files/temps_today.csv"):
        data=pandas.read_csv('files/temps_today.csv')
        print(data.mean())
    else:
        print("File doesnt exist.")

    time.sleep(10)
