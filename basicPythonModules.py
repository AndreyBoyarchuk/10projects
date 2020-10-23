import time
import os
import pandas

while True:
    if os.path.exists("files/temps_today.csv"):
        with open("files/temps_today.csv") as file:
            print(file.read())
            time.sleep(10)
    else:
        print("File doesnt exist.")

    time.sleep(10)
