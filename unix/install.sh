#!/bin/bash

# Define the source file paths
dink_path="./dink"
wav_path="../Source/notification.wav"

# Define the target directory in the PATH (e.g., /usr/local/bin)
target_dir="/usr/local/bin"

# Move the dink executable to the target directory
if [ -f "$dink_path" ]; then
    sudo mv "$dink_path" "$target_dir/"
    sudo chmod +x "$target_dir/dink"  # Make sure it's executable
    echo "dink executable moved successfully."
else
    echo "Error: dink executable not found."
fi

# Move the notification.wav file to the target directory
if [ -f "$wav_path" ]; then
    sudo mv "$wav_path" "$target_dir/"
    echo "notification.wav moved successfully."
else
    echo "Error: notification.wav file not found."
fi
