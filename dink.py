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

for i in range(0,len(args)):
	if args[i] not in allowed_args:
		if args[i][0] != "-":
			command_pointer = i
			break
		else:
			raise Exception(f"{args[i]} is not a valid flag")

parse(args[:command_pointer])

if __name__ == '__main__':
    if platform.system() == 'Windows':

        if flash:
            from win32 import win32gui
            import win32con
            cur_window = win32gui.GetForegroundWindow()
            subprocess.run(args[command_pointer:], shell=True)
            win32gui.FlashWindowEx(cur_window, 15, 5, 400) # Nvm i fixed it
        else:
            subprocess.run(args[command_pointer:], shell=True)

    elif platform.system() == 'Linux':
        pass
    else:
        pass

    playsound('notification.wav')
    if toast:
        from plyer import notification
        notification.notify(title="Command done",message="Kavin you suck",timeout=0)
