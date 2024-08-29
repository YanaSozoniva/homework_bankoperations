import os
from functools import wraps
from typing import Any, Callable


def log(file_name: Any = None) -> Callable:
    """Декоратор регистрирует детали выполнения функций: имя функции,
    передаваемые аргументы, результат выполнения и информация об ошибках.
    Имя функции, тип возникшей ошибки и входные параметры, если выполнение функции привело к ошибке."""

    def wrapper(func: Any) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                message = (
                    f"Функция {func.__name__} не выполнилась. Тип ошибки {e}. \n"
                    f"Входные данные: args = {args}, kwargs = {kwargs}."
                )
                if file_name:
                    base_path = r"C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\logs"
                    full_path = os.path.join(base_path, file_name)

                    with open(full_path, "w", encoding="utf-8") as f:
                        f.write(message)
                else:
                    print(message)
            else:
                message = f"Функция {func.__name__} выполнилась успешно. Результат ее работы - {result}."
                if file_name:
                    base_path = r"C:\Users\user\Desktop\skyPro\practic\Home_work\ClientBankOperations\logs"
                    full_path = os.path.join(base_path, file_name)

                    with open(full_path, "w", encoding="utf-8") as f:
                        f.write(message)
                else:
                    print(message)
            return result

        return inner

    return wrapper


# if __name__ == "__main__":
#
#     @log()
#     def my_function(x, y):
#         return x + y
#
#     my_function("2", 3)
