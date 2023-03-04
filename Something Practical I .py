import shutil
import time
from plyer import notification

#Redundancy below
'''total, used, free = shutil.disk_usage("/")
x = f"Total disk space: {total / (1024**3):.2f} GB"
print(x)

used, total, free = shutil.disk_usage("/")
print(f"Used disk space: {total / (1024**3):.2f} GB")

free, used, total,  = shutil.disk_usage("/")
print(f"free disk space: {total / (1024**3):.2f} GB")
'''

used, total, free = shutil.disk_usage("/")
z = total / (1024**3)

total, used, free = shutil.disk_usage("/")
y = total / (1024**3)

ab = (z / y) * 100

eminem = f"You have used {ab:.2f} % of Available space"


if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Just a reminder",
            message = eminem,
            timeout = 20
        )
        time.sleep(3600) #sets the time the dumb thing will have to wait before it sends it again