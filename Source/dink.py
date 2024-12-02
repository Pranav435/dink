import sys
import subprocess
import platform
from playsound import playsound
import pyttsx3
import os

# FLAGS
toast = False
flash = False
tts=False

numflash=5
try:
    sound_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Dink', 'notification.wav')
except:
    sound_path="notification.wav"
version_number="0.0.0 Kavin you are stupid update"

def parse(args):
    global flash, toast, numflash, tts
    if '-t' in args:
        toast = True
    if '-f' in args:
        flash = True
        index = args.index('-f')+1
        if index < len(args):
            if args[index].isnumeric():
                numflash = int(args[index])
    if '-tts' in args:
        tts=True

allowed_args = {'-t', '-f','-v','-h','-tts'}

if __name__ == '__main__':

    args = sys.argv[1:]
    if '-v' in args:
        print(f"Dink V {version_number}.")
        sys.exit()
    if '-h' in args:
        print("Run dink along with the command you want to be notified about once completed.\nFlags for configuration:\n-t: displays a toast message once the command has finished executing.\n-f: (windows only) flashes the icon of the command window on the taskbar once the command has completed execution. By default, the window will flash 5 times. Include an integer to specify the number of times you want the window to flash after the flag.\n-tts: specifies if the system tts voice should be used to notify you of command completion.\n-v: Displays the version number you are running.")
        sys.exit()
    value_flag = False

    for i in range(0, len(args)):
        if args[i] not in allowed_args:
            if args[i][0] != "-" and not args[i][0] in '1234567890':
                command_pointer = i
                break
            else:
                if not value_flag:
                    raise Exception(f"{args[i]} is not a valid flag")
                else:
                    value_flag = False
        else:
            value_flag = True

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
    try:
        playsound(sound_path)
    except:
        print("The provided notification file does not exist. Please correct the path and try again.")
        sys.exit()
    if toast:
        from plyer import notification
        notification.notify(title="Command Completed", message=f"{' '.join(command)} has completed!", timeout=0)

    if tts:
        engine=pyttsx3.init()
        engine.say("Command completed")
        engine.runAndWait()
