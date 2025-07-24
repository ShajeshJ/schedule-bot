import os

from schedule_bot.type_ext import singleton


@singleton
class Config:
    def __init__(self):
        try:
            self.BOT_TOKEN = os.environ["BOT_TOKEN"]
        except KeyError:
            raise

        self.LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
