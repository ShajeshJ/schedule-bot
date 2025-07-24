import logging
import discord
import discord.ext.commands

import schedule_bot.cogs


async def register_cogs(bot: discord.ext.commands.Bot):
    """Register all cogs to the bot."""
    for cog in schedule_bot.cogs.get_all_cogs():
        try:
            await bot.add_cog(cog(bot))
            logging.info(f"Added {cog.__name__} Cog to the bot.")
        except Exception:
            logging.exception(f"Failed to add {cog.__name__} Cog to the bot.")


async def create_bot() -> discord.ext.commands.Bot:
    intents = discord.Intents.default()
    intents.message_content = True
    intents.guild_messages = True

    bot = discord.ext.commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        await bot.tree.sync()
        logging.info(f"Logged in as {bot.user} (ID: {bot.user.id})")
        logging.info("-----")

    await register_cogs(bot)

    return bot
