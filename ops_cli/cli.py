import argparse


def build_parser() -> argparse.ArgumentParser:
    """
    Собирает и возвращает парсер аргументов.

    Почему отдельная функция:
    - main() становится коротким
    - парсер можно тестировать отдельно
    """
    parser = argparse.ArgumentParser(
        prog="ops-cli",
        description="Учебная CLI-утилита",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    greet_parser = subparsers.add_parser("greet", help="Поздороваться")
    greet_parser.add_argument("name", help="Имя пользователя")

    sum_parser = subparsers.add_parser("sum", help="Сложить два целых числа")
    sum_parser.add_argument("a", type=int, help="Первое число")
    sum_parser.add_argument("b", type=int, help="Второе число")

    return parser
