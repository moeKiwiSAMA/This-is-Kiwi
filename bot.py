import os
import time


if __name__ == "__main__":
    while True:
        with open("commits/logs", "a") as logs:
            logs.writelines(time.asctime() + "\n")
    
        os.system("git add .")
        os.system("git commit -m \"Commit Bot At " + time.asctime() + "\"")
        os.system("git push")

        time.sleep(600)
