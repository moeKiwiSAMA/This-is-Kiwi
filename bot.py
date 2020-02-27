import os
import time

with open("commits/logs", "a") as logs:
        logs.writelines(time.asctime() + "\n")

os.system("git add .")
os.system("git commit -m \"Commit Bot" + time.asctime() + "\"")
