# OpenAI Chat Assistant for Raspberry Pi

This repository provides a simple chat assistant using OpenAI's API, designed for Raspberry Pi. After setup, you can use this assistant by typing `chat your query` in the terminal to get a quick response.

## Features

- Quickly access a helpful AI assistant from the terminal.
- Answers are provided with context specifically suited for the Raspberry Pi environment.
- Simple setup that automatically adds a `chat` command for easy access.

## Requirements

- Raspberry Pi running a Linux-based OS (e.g., Raspberry Pi OS)
- Python 3
- OpenAI API Key

## Setup Instructions

1. **Clone the Repository**:

    ```bash
    git clone https://github.com/Ahnaf-nub/Raspberry-Pi-Ai-Assitant-Cli.git
    cd Raspberry-Pi-Ai-Assitant-Cli
    ```

2. **Edit `chat.py`**:

    Open `chat.py` in a text editor and replace `"sk-your-api-key-here"` with your actual OpenAI API key.

3. **Run the Setup Script**:

    Run the setup script to install dependencies and set up the `chat` command:

    ```bash
    bash setup_chat.sh
    ```

    This script will:
    - Install necessary dependencies (Python and the OpenAI Python library).
    - Add an alias `chat` to your `.bashrc` so you can run the assistant by simply typing `chat your query` in the terminal.

4. **Start Chatting**:

    After setup, type the following command to start the chat assistant:

    ```bash
    chat your query
    ```

    For example:

    ```bash
    chat What is the best way to interface a sensor with Raspberry Pi Zero 2W?
    ```

    The assistant will respond directly in the terminal.

## How It Works

The setup script:
- Installs necessary dependencies.
- Adds an alias `chat` to `.bashrc` that runs `chat.py` with any query you provide.
- Run `sudo reboot` to restart and then use!!
