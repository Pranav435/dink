import sys
import subprocess
from win32 import win32gui
import win32con
from playsound import playsound
cur_window = win32gui.GetForegroundWindow()

args = sys.argv[1:]
subprocess.run(args, shell=True)
win32gui.FlashWindowEx(cur_window, 0, 2, 500) # It doesn't flash but whatev
playsound('notification.wav')
