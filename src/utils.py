import json
import logging
from typing import Dict, List

logger = logging.getLogger("__name__")
file_handler = logging.FileHandler('logs/utils.log', mode='w')
file_formatter = logging.Formatter("[%(asctime)s] at %(name)s: %(levelname)s - %(message)s")
logger.addHandler(file_handler)
file_handler.setFormatter(file_formatter)
logger.setLevel(logging.DEBUG)


def get_operations_from_json(route_to_JSON: str) -> List[Dict]:
    """Получает путь до JSON (на входе) и возвращает список операций (Dict).
    В случае ошибки чтения файла или декодирования — возвращает пустой список.
    """
    logger.debug('Запущена функция "get_operations_from_json"')
    try:
        with open(route_to_JSON, "r", encoding="utf-8") as f:
            operations_data = json.load(f)
            logger.debug(f'Функция "get_operations_from_json" успешно отработала с результатом:\n\n{operations_data}')
        return operations_data
    except FileNotFoundError:
        print(f"[Предупреждение] Файл не найден: {route_to_JSON}")
        logger.error('Возникла ошибка: FileNotFoundError')
        return []
    except json.JSONDecodeError:
        print(f"[Предупреждение] Файл содержит некорректный JSON: {route_to_JSON}")
        logger.error('Возникла ошибка: JSONDecodeError')
        return []
