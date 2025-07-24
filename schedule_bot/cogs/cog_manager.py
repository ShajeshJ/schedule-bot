from dataclasses import dataclass, field
import importlib
import pkgutil
import logging
import sys

import discord.ext.commands

from schedule_bot.type_ext import singleton


@singleton
@dataclass
class CogManager:
    cogs: set[type[discord.ext.commands.Cog]] = field(default_factory=set)

    def register_cog(self, cog: type[discord.ext.commands.Cog]):
        """Register a cog."""
        self.cogs.add(cog)

    def get_cogs(self) -> list[type[discord.ext.commands.Cog]]:
        """Get all registered cogs."""
        return list(self.cogs)


_MODULES_LOADED = False


def get_all_cogs() -> list[type[discord.ext.commands.Cog]]:
    """Get all registered cogs from the CogManager."""
    _load_cog_modules()
    return CogManager().get_cogs()


def _load_cog_modules():
    """Dynamically import and load all cog modules"""
    global _MODULES_LOADED
    if _MODULES_LOADED:
        return

    for module in pkgutil.iter_modules(
        sys.modules[__package__].__path__, f"{__package__}."
    ):
        if module.ispkg or module.name == __name__:
            continue

        try:
            logging.info(f"Dynamically importing module {module.name}")
            importlib.import_module(module.name)
        except ImportError:
            logging.exception(f"Failed to import {module.name}")

    _MODULES_LOADED = True
