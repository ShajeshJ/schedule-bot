import discord.ext.commands
import discord.app_commands

from schedule_bot.cogs.cog_manager import CogManager


class Schedule(discord.ext.commands.Cog):
    """A cog for managing schedules."""

    def __init__(self, bot: discord.ext.commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name="schedule")
    @discord.app_commands.guild_only
    async def schedule_command(self, ctx: discord.Interaction):
        """Command to display the schedule."""
        await ctx.response.send_message("This is where the schedule will be displayed.")


CogManager().register_cog(Schedule)
