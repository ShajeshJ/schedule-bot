import logging
import discord


def create_bot() -> discord.Client:
    intents = discord.Intents.default()
    intents.message_content = True
    intents.guild_messages = True

    bot = discord.Client(intents=intents)

    @bot.event
    async def on_ready():
        logging.info(f"Logged in as {bot.user} (ID: {bot.user.id})")
        logging.info("-----")

    return bot
