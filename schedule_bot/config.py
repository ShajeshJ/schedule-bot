import os


class Config:
    __sentinel: "Config | None" = None

    def __new__(cls, *args, **kwargs):
        if cls.__sentinel:
            return cls.__sentinel

        cls.__sentinel = super().__new__(cls, *args, **kwargs)
        return cls.__sentinel

    def __init__(self):
        try:
            self.BOT_TOKEN = os.environ["BOT_TOKEN"]
        except KeyError:
            raise

        self.LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
