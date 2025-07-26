import logging
import hikari
import arc

from schedule_bot.config import Config


async def on_start(client: arc.GatewayClient) -> None:
    user = client.app.get_me()
    if not user:
        logging.info("Bot is booted up...")
        return

    logging.info(f"Logged in as {user.username} ({user.id})")


def create_bot() -> hikari.GatewayBot:
    bot = hikari.GatewayBot(
        token=Config().BOT_TOKEN, logs=None, intents=hikari.Intents.ALL
    )

    client = arc.GatewayClient(bot)
    client.add_startup_hook(on_start)
    client.load_extensions_from("schedule_bot/plugins")

    return bot
