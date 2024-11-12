#!/bin/bash

# Install the OpenAI library
echo "Installing the OpenAI library..."
pip3 install openai --break-system-packages

# Define the exact path to the `chat.py` file
SCRIPT_DIR="/home/pi/Raspberry-Pi-Ai-Assitant-Cli"

# Add an alias to .bashrc pointing to the absolute path of chat.py
echo "Adding alias to .bashrc..."
echo "alias chat='python3 \"$SCRIPT_DIR/chat.py\"'"' "$@"' >> ~/.bashrc

# Immediately load the new alias into the current shell session
echo "Applying alias for the current session..."
alias chat="python3 \"$SCRIPT_DIR/chat.py\""' "$@"'

echo "Setup complete! You can now use 'chat your query' to interact with the assistant."
