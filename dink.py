import sys
import subprocess
from win32 import win32gui
from playsound import playsound

args = sys.argv[1:]
subprocess.run(args, shell=True)
# win32gui.FlashWindowEx() no idea what args are supposed to go here (well somewhat of an idea but im too lazy to add rn)
playsound('notification.wav')
