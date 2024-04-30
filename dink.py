import sys
import subprocess
import platform
from playsound import playsound

# FLAGS
toast = False
flash = False
numflash=5

def parse(args):
    global flash, toast
    if '-t' in args:
        toast = True
    elif '-f' in args:
        flash = True

allowed_args = {'-t', '-f'}

args = sys.argv[1:]

for i in range(0,len(args)):
	if args[i] not in allowed_args:
		if args[i][0] != "-" and not args[i][0] in ["1","2","3","4","5","6","7","8","9","0"]:
			command_pointer = i
			break
		elif args[i][0] in ["1","2","3","4","5","6","7","8","9","0"]:
			continue

		else:
			raise Exception(f"{args[i]} is not a valid flag")
	if args[i]=="-f":
		flash=True
		if args[i+1][0] in ["1","2","3","4","5","6","7","8","9","0"]:
			numflash=int(args[i+1])


if __name__ == '__main__':

    command = args[command_pointer:]
    parse(args[:command_pointer])

    if platform.system() == 'Windows':

        if flash:
            from win32 import win32gui
            import win32con
            cur_window = win32gui.GetForegroundWindow()
            subprocess.run(command, shell=True)
            win32gui.FlashWindowEx(cur_window, 15, numflash, 400) # Nvm i fixed it
        else:
            subprocess.run(command, shell=True)

    elif platform.system() == 'Linux':
        pass
    else:
        pass

    playsound('.\\notification.wav')

    if toast:
        from plyer import notification
        notification.notify(title="Command Finished",message=f"{}",timeout=1)
