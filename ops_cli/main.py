import logging

from ops_cli.cli import build_parser
from ops_cli.commands import greet, sum as sum_cmd


def main() -> int:
    """
    Точка входа приложения.

    Тут мы делаем только:
    1) конфигурацию логов
    2) разбор аргументов
    3) вызов нужной команды
    """
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    logging.info("Запуск ops-cli")

    parser = build_parser()
    args = parser.parse_args()

    if args.command == "greet":
        return greet.run(args.name)

    if args.command == "sum":
        return sum_cmd.run(args.a, args.b)

    # Не должно случиться из-за required=True, но оставляем как страховку
    logging.error("Неизвестная команда: %s", args.command)
    return 2