

import logging


def run(name: str) -> int:
    """
    Команда greet.

    Args:
        name: имя пользователя.

    Returns:
        Код завершения: 0 если всё ок.
    """
    logging.info("Привет, %s!", name)

    return 0
