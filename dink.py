import sys
import subprocess
import platform
from playsound import playsound

# FLAGS
toast = False
flash = False

def parse(args):
    global flash, toast
    if '--toast' in args or '-t' in args:
        toast = True
    elif '--flash' in args or '-f' in args:
        flash = True

allowed_args = {'--toast', '-t', '--flash', '-f'}

args = sys.argv[1:]

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
