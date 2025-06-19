import json
import os
from src.utils import get_operations_from_json

def test_get_operations_valid(tmp_path):
    file_path = tmp_path / "test.json"
    test_data = [{"id": 1}, {"id": 2}]
    file_path.write_text(json.dumps(test_data), encoding='utf-8')
    result = get_operations_from_json(str(file_path))
    assert result == test_data

def test_get_operations_file_not_found():
    result = get_operations_from_json("non_existent_file.json")
    assert result == []  # Проверяем возврат пустого списка при отсутствии файла

def test_get_operations_invalid_json(tmp_path):
    file_path = tmp_path / "invalid.json"
    file_path.write_text("{bad json}", encoding='utf-8')
    result = get_operations_from_json(str(file_path))
    assert result == []  # Проверяем возврат пустого списка при невалидном JSON