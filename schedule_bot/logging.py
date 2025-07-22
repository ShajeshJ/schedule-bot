import logging

from schedule_bot.config import Config


LOG_COLORS = {
    logging.DEBUG: "\033[90m",
    logging.INFO: "\033[96m",
    logging.WARNING: "\033[93m",
    logging.ERROR: "\033[91m",
}


RESET = "\033[0m"


class LogHandler(logging.StreamHandler):
    def format(self, record: logging.LogRecord):
        msg = super().format(record)

        if color := LOG_COLORS.get(record.levelno):
            msg = f"{color}{msg}{RESET}"

        return msg


def configure_logger():
    logging.basicConfig(
        level=Config().LOG_LEVEL,
        format=f"[%(asctime)s] %(levelname)s: %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
        handlers=[LogHandler()],
    )
