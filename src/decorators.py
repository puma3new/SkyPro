from datetime import datetime
from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования выполнения функций.
    :param filename: Если None - вывод в консоль, иначе - запись в файл
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Формируем информацию о вызове
            func_name = func.__name__
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            params = f"args: {args}, kwargs: {kwargs}"

            # Логируем начало выполнения
            start_message = (
                f"[{timestamp}] Функция {func_name} начата с параметрами: {params}"
            )
            log_message(start_message, filename)

            try:
                # Выполняем функцию
                result = func(*args, **kwargs)

                # Логируем успешное завершение (ИСПРАВЛЕННАЯ ЧАСТЬ)
                success_message = (
                    f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Функция "
                    f"{func_name} завершена. Результат: {result}"
                )
                log_message(success_message, filename)

                return result

            except Exception as e:
                # Логируем ошибку
                error_message = (
                    f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Ошибка в функции {func_name}:\n"
                    f"Тип: {type(e).__name__}\n"
                    f"Сообщение: {str(e)}\n"
                    f"Параметры: {params}"
                )
                log_message(error_message, filename)
                raise

        return wrapper

    return decorator


def log_message(message, filename=None):
    """Вспомогательная функция для вывода/записи лога"""
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)
