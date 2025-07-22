from dotenv import load_dotenv

from schedule_bot import create_bot
from schedule_bot.config import Config
from schedule_bot.logging import configure_logger


def main():
    load_dotenv()
    configure_logger()
    create_bot().run(Config().BOT_TOKEN, log_handler=None)


if __name__ == "__main__":
    main()
