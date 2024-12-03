# Dink - Command Line Notifier

Dink is a simple command-line tool that provides notifications when your commands finish executing. It can play a sound, show a toast notification, or, on Windows, flash the taskbar icon. It's perfect for long-running commands or background tasks, so you don't have to constantly monitor your terminal.

## Features

- **Sound notification**: Play a custom sound when the command finishes executing.
- **Toast notification**: Get a toast notification on command completion (works on both Windows and Linux).
- **Taskbar flash**: On Windows, flash the command prompt icon on the taskbar to alert you (configurable flash count).
- **Text-to-Speech**: Dink can speak a message after the command completes, for accessibility or convenience.

## Setup

### Windows

1. Download the latest release from [here](https://github.com/Pranav435/dink/releases/download/v1.0.0/dink_installer_windows.exe).
2. Run the `dink_installer.exe` file to install Dink.

### Linux

1. Download the latest release from [here](https://github.com/Pranav435/dink/releases/download/v1.0.0/dink_linux.zip).
2. Run the `install.sh` script.

Alternatively, you can build from source:

1. Clone the repository:
   ```bash
   git clone https://github.com/Pranav435/dink.git
   cd dink/Source
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure Python is installed on your system.

## Usage

To use Dink, simply run it with the command you want to be notified about. For example:
```bash
dink ls
```

By default, a sound will play as soon as the command finishes executing.

### Flags

Here are some flags you can use with Dink. Make sure these flags come **after** the word `dink` but **before** the command you want to be notified about.

- `-m`: Mutes the custom audio notification.
- `-t`: Shows a toast notification once the command completes.
- `-f`: Windows only. Flashes the command prompt icon on the taskbar. By default, it flashes the icon 5 times. You can customize the number of flashes by adding a number after the flag. Example: `-f 10` will flash the icon 10 times.
- `-tts`: Speaks a text-to-speech message once the command completes.
- `-h`: Shows a quick help message.
- `-v`: Shows the current version number of Dink.

### Example

To run the `ls` command and get a toast notification with a sound when it's done, use:
```bash
dink -t ls
```

To mute the sound but show a toast notification and flash the taskbar icon:
```bash
dink -m -t -f ls
```

## License

Dink is open-source and distributed under the **MIT License**. This means you are free to use, modify, and distribute the software, including for commercial purposes, with the following conditions:

- The software is provided "as is", without any warranty of any kind. The author(s) are not responsible for any damages, direct or indirect, arising from the use of the software.
- If you modify or distribute the software, you must include a copy of this license with the software, and provide proper attribution to the original author(s).

For more details, see the [LICENSE](LICENSE) file.

```

This expands the explanation and makes the terms of the MIT License clearer for users who may not be familiar with it.