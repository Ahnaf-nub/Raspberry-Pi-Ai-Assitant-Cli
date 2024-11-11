# OpenAI Chat Assistant for Raspberry Pi

This repository provides a simple chat assistant using OpenAI's API, tailored for Raspberry Pi. After setup, you can use this assistant by simply typing `chat` in the terminal.

## Features

- Quickly access a helpful AI assistant from the terminal.
- Answers are provided with context specifically suited for the Raspberry Pi environment.
- Simple setup that automatically adds a `chat` command alias for easy access.

## Requirements

- Raspberry Pi running a Linux-based OS (e.g., Raspberry Pi OS)
- Python 3
- OpenAI API Key

## Setup Instructions

1. **Clone the Repository**:

    ```bash
    https://github.com/Ahnaf-nub/Raspberry-Pi-Ai-Assitant-Cli.git
    cd Raspberry-Pi-Ai-Assitant-Cli
    ```

2. **Edit `chat.py`**:

    Open `chat.py` in a text editor and replace `""` with your actual OpenAI API key.

3. **Run the Setup Script**:

    Run the setup script to install dependencies:

    ```bash
    bash setup.sh
    ```

    This script will:
    - Install necessary dependencies (Python and the OpenAI Python library).
    - Add an alias `chat` to your `.bashrc` so you can run the assistant by simply typing `chat` in the terminal.

4. **Start Chatting**:

    After setup, type the following command to start the chat assistant:

    ```bash
    chat
    ```

    You can now ask questions, and the assistant will respond based on the Raspberry Pi context.

## How It Works

The setup script:
- Updates the system and installs Python dependencies.
- Adds an alias `chat` to `.bashrc` so that you can invoke the assistant with one command.
- Immediately applies the alias for the current session so that it’s ready to use without restarting the terminal.

## Example Usage

```bash
$ chat
Ask: What is the best way to interface a sensor with Raspberry Pi Zero 2W?
