import sys
import subprocess
import platform
from playsound import playsound

args = sys.argv[1:]
subprocess.run(args, shell=True)

def windows_dink():
    import win32con
    from win32 import win32gui
    cur_window = win32gui.GetForegroundWindow()
    win32gui.FlashWindowEx(cur_window, 15, 5, 400) # Nvm i fixed it

def linux_dink():
    pass

def that_other_os_dink():
    pass

if __name__ == '__main__':
    if platform.system() == 'Windows':
        windows_dink()

    playsound('notification.wav')
