#!/bin/bash

# Set your environment name
ENV_NAME="venv"

# List of Python packages to install
PACKAGES=(
    langchain-core
    langchain-community
    langchain-ollama
)

echo "Creating virtual environment: $ENV_NAME"
python3 -m venv "$ENV_NAME"

echo "Activating virtual environment..."
source "$ENV_NAME/bin/activate"

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing packages..."
for package in "${PACKAGES[@]}"; do
    echo "Installing $package..."
    pip install "$package"
done
curl -fsSL https://ollama.com/install.sh | sh

ollama serve
ollama pull mistral
# To run in command : ollama run mistral
# ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPQM1Px+8aGdpnoz+vO26HXjy4OrL56pq79qiy/7otBD
# Error: listen tcp 127.0.0.1:11434: bind: address already in use
echo "✅ Setup complete. Virtual environment '$ENV_NAME' is ready and packages are installed."
source $ENV_NAME/bin/activate