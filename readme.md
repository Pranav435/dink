# Dink - Command Line Notifier

Dink is a simple command-line tool that provides notifications when your commands finish executing. It can play a sound, show a toast notification, or, on Windows, flash the taskbar icon. It's perfect for long-running commands or background tasks, so you don't have to constantly monitor your terminal.

## Credits

We would like to thank [Lycanthropy3301](https://github.com/Lycanthropy3301), the co-creator of this script, for their invaluable contributions to this project.

A special thanks also goes to [Reema Sarkar](https://github.com/reema-s1) for their help in building the binaries for this project.

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
