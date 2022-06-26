import os

os.system("pip install notify-py")

from notifypy import Notify
import time
import json

notif = Notify()

time.sleep(0.5)

h = input("> ")

print("What would you like the title to be?")

tprompt = input("> ")

print("What would you like the message to be?")

mprompt = input("> ")

print("Enter the path to your desired image or leave blank")

iprompt = input("> ")

notif.title = tprompt
notif.icon = iprompt
notif.message = mprompt

notif.send()

input("Press Enter to exit")

