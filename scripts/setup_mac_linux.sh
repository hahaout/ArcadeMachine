#!/bin/bash
# Move to the project's root directory
cd "$(git rev-parse --show-toplevel)"

if command -v python3.13 >/dev/null 2>&1; then
    # If python3.13 is directly available
    PYTHON_CMD="python3.13"
else
    # Fall back to "python3" and check its version
    if command -v python3 >/dev/null 2>&1; then
        PY_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        IFS='.' read -ra VER <<< "$PY_VERSION"

        # Check that major version is 3 and minor is at least 13
        if [ "${VER[0]}" -eq 3 ] && [ "${VER[1]}" -ge 13 ]; then
            PYTHON_CMD="python3"
        else
            echo "Python 3.13 or newer is required. Found: $PY_VERSION"
            exit 1
        fi
    else
        echo "No suitable Python (3.13+) found. Please install Python 3.13 or newer."
        exit 1
    fi
fi

# Check if 'venv' or '.venv' directory exists
if [ -d "venv" ]; then
    echo "Activating existing venv..."
    source venv/bin/activate
elif [ -d ".venv" ]; then
    echo "Activating existing .venv..."
    source .venv/bin/activate
else
    echo "No virtual environment found. Creating one..."
    python3.13 -m venv venv
    source venv/bin/activate
fi

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete. Virtual environment is activated, and dependencies are installed."
