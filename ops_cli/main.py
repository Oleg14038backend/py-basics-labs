from __future__ import annotations

# Подключаем стандартный модуль Python
import argparse
import logging

# Точкак входа
# запуск → через if __name__ == "__main__"
# CLI-программы возвращают код
# 0 = успех
# >0 = ошибка


def main() -> int:
    """
    Точка входа CLI-программы.

    Используем argparse, чтобы:
    - автоматически разбирать аргументы
    - автоматически показывать help
    - не писать ручные проверки len(argv)
    """

    # 1. Создаём объект парсера
    # 2. Как будет называться программа в help
    # 3. текст, который пользователь увидит, когда напишет --help.
    parser = argparse.ArgumentParser(
        prog="ops-cli",
        description="Учебная CLI-утилита"
    )
    logging.info("Запуск ops-cli")

    # 2. Создаём подкоманды (greet, sum и т.д.)
    # 3. Если пользователь не указал команду → Python сам напишет ошибку
    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # Создаём подкоманду greet
    greet_parser = subparsers.add_parser(
        "greet",
        help="Поздороваться с пользователем"
    )
    greet_parser.add_argument(
        "name",
        help="Имя пользователя"
    )

    # Команда sum ----------
    sum_parser = subparsers.add_parser(
        "sum",
        help="Сложить два целых числа"
    )

    # Аргументы a и b
    # type=int сам попробует превратить строку в число
    # если не получится → сам покажет ошибку
    sum_parser.add_argument(
        "a",
        type=int,
        help="Первое число"
    )
    sum_parser.add_argument(
        "b",
        type=int,
        help="Второе число"
    )

    # 3. Парсим аргументы
    args = parser.parse_args()

    # 4. Обрабатываем команды
    if args.command == "greet":
        logging.info("Привет, %!", args.name)
        return 0

    if args.command == "sum":
        print(args.a + args.b)
        return 0

    # Теоретически сюда мы не попадём,
    # но return нужен для полноты
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
