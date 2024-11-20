## Overview

`discord-bot-base` is a template repository for creating Discord bots using Python 3.10. It provides a basic structure and common functionalities to help you get started quickly.

## Features

- Command handling
- Event handling
- Configuration management
- Logging
- Error handling

## Prerequisites

- Python 3.10
- pip (Python package installer)
- A Discord bot token

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/andrewgalvin/discord-bot-base.git
   cd discord-bot-base
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration

1. Open the `config.py` file.

2. Add your Discord bot token to the `config.py` file:
   ```python
   DISCORD_TOKEN = 'your-discord-bot-token'
   ```

## Usage

To start the bot, run:

```sh
cd bot
python bot.py
```

## Running Tests

To run the tests, in the [root directory](.) run:

```sh
python -m unittest discover -s tests -p "test_*.py"
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
