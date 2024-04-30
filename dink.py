import sys
import subprocess
import platform
from playsound import playsound

# FLAGS
toast = False
flash = False
numflash=5

def parse(args):
    global flash, toast, numflash
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

parse(args[:command_pointer])

if __name__ == '__main__':
    if platform.system() == 'Windows':

        if flash:
            from win32 import win32gui
            import win32con
            cur_window = win32gui.GetForegroundWindow()
            subprocess.run(args[command_pointer:], shell=True)
            win32gui.FlashWindowEx(cur_window, 15, numflash, 400) # Nvm i fixed it
        else:
            subprocess.run(args[command_pointer:], shell=True)
        if toast:
            from plyer import notification
            notification.notify(title="Finished",message="Your command has just finished. Go suck something.",timeout=0)

    elif platform.system() == 'Linux':
        pass
    else:
        pass
    try:
        playsound('./notification.wav')
    except:
        pass