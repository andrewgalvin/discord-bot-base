import interactions

from commands import hello_world_command
from config import DISCORD_TOKEN
from utils.logger import logger

intent = interactions.Intents.ALL
bot = interactions.Client(token=DISCORD_TOKEN, intents=intent)

# Load commands
hello_world_command.setup(bot)


@interactions.listen()
async def on_startup():
    """
    Event listener for the bot's startup event.

    This function is called when the bot is ready and logs a message indicating
    that the bot has successfully started.

    Logs:
        "Bot is ready!" - Indicates that the bot has successfully started.
    """
    logger.info("Bot is ready!")


if __name__ == "__main__":
    bot.start()  # Start the bot
