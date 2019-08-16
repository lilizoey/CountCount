import logging
import os, sys

from commands import *
from bot import bot

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        token = os.environ["DISCORD_TOKEN"]
    except KeyError as k:
        logger = logging.getLogger("discord")
        logger.error("DISCORD_TOKEN environment variable is not set.")
        sys.exit(1)
        
    bot.run(token) 