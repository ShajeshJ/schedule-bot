from dotenv import load_dotenv

from schedule_bot import create_bot
from schedule_bot.logging import configure_logger


def main():
    load_dotenv()
    configure_logger()
    bot = create_bot()
    bot.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
