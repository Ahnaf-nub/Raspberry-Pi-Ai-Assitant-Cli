#!/bin/bash

# Install the OpenAI library
echo "Installing the OpenAI library..."
pip3 install openai --break-system-packages

# Get the absolute directory path of the setup script (assuming chat.py is in the same directory)
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Add an alias to .bashrc that points to the absolute path of chat.py
echo "Adding alias to .bashrc..."
echo "alias chat='python3 \"$SCRIPT_DIR/chat.py\"'"' "$@"' >> ~/.bashrc

# Immediately load the new alias into the current shell session
echo "Applying alias for the current session..."
alias chat="python3 \"$SCRIPT_DIR/chat.py\""' "$@"'

echo "Setup complete! You can now use 'chat your query' to interact with the assistant."
