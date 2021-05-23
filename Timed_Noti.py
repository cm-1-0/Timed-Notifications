import pync
import datetime
import time


def noti():
    message = input("What is the notification that you wish to send: ")
    pync.notify(message)


def execute():
    noti_run = datetime.datetime(2021, 6, 1, 0, 0, 0)
    while datetime.datetime.now() < noti_run:
        time.sleep(1)

