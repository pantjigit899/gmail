#Desktop notification using python

from plyer import notification
import time
if __name__ == "__main__":
    while True:
        notification.notify(
            title = " Take-Rest",
            message = "“Do something nice for yourself today. Find some quiet, sit in stillness, breathe. Put your problems on pause. You deserve a break.”",
            timeout = 10)
    time.sleep(20)
    
        