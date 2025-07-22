from dotenv import load_dotenv

from schedule_bot.logging import configure_logger


def main():
    load_dotenv()
    configure_logger()


if __name__ == "__main__":
    main()
