#!/bin/bash

# Install the OpenAI library
echo "Installing the OpenAI library..."
pip3 install openai

SCRIPT_DIR=$(dirname "$(realpath "$0")")

echo "Adding alias to .bashrc..."
echo "alias chat='python3 $SCRIPT_DIR/chat.py'" >> ~/.bashrc

echo "Applying alias for the current session..."
alias chat="python3 $SCRIPT_DIR/chat.py"

echo "Setup complete! You can now type 'chat' to use the assistant."
