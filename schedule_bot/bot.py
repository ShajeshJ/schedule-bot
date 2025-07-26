import logging
import hikari
import arc

from schedule_bot.config import Config


async def on_start(event: hikari.StartedEvent) -> None:
    logging.info("Bot has booted up")


def create_bot() -> hikari.GatewayBot:
    bot = hikari.GatewayBot(
        token=Config().BOT_TOKEN, logs=None, intents=hikari.Intents.ALL
    )
    bot.listen()(on_start)

    client = arc.GatewayClient(bot)
    client.load_extensions_from("schedule_bot/plugins")

    return bot
