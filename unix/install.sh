#!/bin/bash

# Define the source file paths
dink_path="./dink"
wav_path="../Source/notification.wav"

# Define the target directory in the PATH (e.g., /usr/local/bin)
target_dir="/usr/local/bin"

# Copy the dink executable to the target directory
if [ -f "$dink_path" ]; then
    sudo cp "$dink_path" "$target_dir/"
    sudo chmod +x "$target_dir/dink"  # Make sure it's executable
    echo "dink executable copied successfully."
else
    echo "Error: dink executable not found."
fi

# Copy the notification.wav file to the target directory
if [ -f "$wav_path" ]; then
    sudo cp "$wav_path" "$target_dir/"
    echo "notification.wav copied successfully."
else
    echo "Error: notification.wav file not found."
fi
