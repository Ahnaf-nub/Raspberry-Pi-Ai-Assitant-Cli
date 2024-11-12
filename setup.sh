#!/bin/bash

# Install the OpenAI library
echo "Installing the OpenAI library..."
pip3 install openai

# Get the directory of the setup script (assumes chat.py is in the same directory)
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Add an alias to .bashrc that passes all arguments to chat.py
echo "Adding alias to .bashrc..."
echo "alias chat='python3 $SCRIPT_DIR/chat.py'"' "$@"' >> ~/.bashrc

# Immediately load the new alias into the current shell session
echo "Applying alias for the current session..."
alias chat="python3 $SCRIPT_DIR/chat.py"' "$@"'

echo "Setup complete! You can now use 'chat your query' to interact with the assistant."
