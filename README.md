

This repository contains a simple Python script (`APP.PY`) that provides a command-line interface to interact with the Groq API. It allows users to have a conversation with the `llama-3.3-70b-versatile` model directly from their terminal.

## Prerequisites

Before you begin, ensure you have the following:
*   Python 3.x
*   A Groq API key. You can get one from the [GroqCloud Console](https://console.groq.com/keys).

## Installation and Setup

Follow these steps to set up and run the project locally.

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/yeulsanket/gen.git
    cd gen
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # Create the virtual environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure the API Key:**
    The script requires your Groq API key to function. For security reasons, it is strongly recommended to use an environment variable instead of hardcoding the key into the script.

    First, set an environment variable named `GROQ_API_KEY`:
    *   On macOS/Linux: `export GROQ_API_KEY='your_api_key_here'`
    *   On Windows: `setx GROQ_API_KEY "your_api_key_here"` (in a new terminal) or `set GROQ_API_KEY=your_api_key_here` (for the current session)

    Next, modify the beginning of `APP.PY` to load the key from the environment:

    ```python
    import os
    from groq import Groq

    # Load API key from environment variable
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )
    # ... rest of the script
    ```

## Usage

Once the setup is complete and the API key is configured, run the application:

```sh
python APP.PY
```

The script will present a `you:` prompt. Type your message, press Enter, and the AI's response will be printed to the console. The conversation will continue in a loop until you manually exit the script (e.g., by pressing `Ctrl+C`).


