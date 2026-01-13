import logging

from ops_cli.commands import greet


def test_greet_returns_zero() -> None:
    """
    Проверяем базовое правило CLI:
    успешная команда возвращает код 0.
    """
    exit_code = greet.run("Test")
    assert exit_code == 0


def test_greet_logs_message(caplog) -> None:
    """
    Проверяем, что greet пишет ожидаемое сообщение в лог.

    caplog — это “ловушка” логов из pytest.
    Она собирает сообщения logging.* во время теста.
    """
    with caplog.at_level(logging.INFO):
        greet.run("Test")

    # caplog.text — это общий текст всех собранных логов
    assert "Привет, Test!" in caplog.text
