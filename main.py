import asyncio
from dotenv import load_dotenv

from schedule_bot import create_bot
from schedule_bot.config import Config
from schedule_bot.logging import configure_logger


async def main():
    load_dotenv()
    configure_logger()
    bot = await create_bot()
    await bot.start(Config().BOT_TOKEN)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
