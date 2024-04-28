import sys
import subprocess
from win32 import win32gui
import win32con
from playsound import playsound
cur_window = win32gui.GetForegroundWindow()

args = sys.argv[1:]
subprocess.run(args, shell=True)
win32gui.FlashWindowEx(cur_window, 15, 5, 400) # Nvm i fixed it
playsound('notification.wav')
