from src.decorators import log

import pytest
import tempfile


def test_log():
    """Тестирует выполнение декорированной функции"""

    @log()
    def my_function(x, y):
        return x + y

    result = my_function(2, 3)
    assert result == 5


def test_log_console_input_success(capsys):
    """Тестирует запись в консоль после успешного выполнения"""

    @log()
    def my_function(x, y):
        return x + y

    my_function(2, 3)
    captured = capsys.readouterr()
    assert captured.out == "Функция my_function выполнилась успешно. Результат ее работы - 5.\n"


def test_log_console_input_error(capsys):
    """Тестирует запись в консоль после выполнения с ошибкой"""

    @log()
    def my_function(x, y):
        return x + y

    with pytest.raises(Exception):
        my_function("2", 3)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Функция my_function не выполнилась. Тип ошибки can only concatenate str (not \"int\") to str. \nВходные данные: args = ('2', 3), kwargs = {}.\n"
    )


def test_log_file_input_success():
    """Тестирует запись в файл после успешного выполнения"""
    with tempfile.NamedTemporaryFile(delete=False) as f:
        log_file_path = f.name

    @log(file_name=log_file_path)
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    assert logs == "Функция my_function выполнилась успешно. Результат ее работы - 3."


def test_log_file_input_error():
    """Тестирует запись в файл после выполнения с ошибкой"""
    with tempfile.NamedTemporaryFile(delete=False) as f:
        log_file_path = f.name

    @log(file_name=log_file_path)
    def my_function(x, y):
        return x + y

    with pytest.raises(Exception):
        my_function("2", 3)

    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    assert (
        logs
        == "Функция my_function не выполнилась. Тип ошибки can only concatenate str (not \"int\") to str. \nВходные данные: args = ('2', 3), kwargs = {}."
    )
