import logging

from ops_cli.commands import sum as sum_cmd


def test_sum_returns_zero() -> None:
    """
    Успешная команда sum должна возвращать 0.
    """
    exit_code = sum_cmd.run(2, 3)
    assert exit_code == 0


def test_sum_logs_result(caplog) -> None:
    """
    Проверяем, что sum логирует сумму.
    """
    with caplog.at_level(logging.INFO):
        sum_cmd.run(2, 3)

    # Мы ожидаем, что в лог попадёт "Сумма: 5"
    assert "5" in caplog.text
