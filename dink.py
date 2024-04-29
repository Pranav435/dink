import sys
import subprocess
import platform
from playsound import playsound

toast=False
command=1
args = sys.argv[1:]
allowed_args={"--toast","-t"}
for i in range(0,len(args)):
	if args[i] not in allowed_args:
		if not args[i][0]=="-":
			command=i
			break
		else:
			raiseException(f"{args[i]} is not a valid flag")

	if args[i]=="--toast" or args[i]=="-t":
		toast=True


subprocess.run(args[command:], shell=True)

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
    if toast:
        from plyer import notification
        notification.notify(title="Command done",message="Kavin you suck",timeout=0)

        
