import pytest
from src import processing

# Тесты для filter_by_state
@pytest.mark.parametrize("state, expected_count, expected_ids", [
    ("EXECUTED", 2, [41428829, 939719570]),
    ("CANCELED", 2, [594226727, 615064591]),
    ("PENDING", 0, []),
])
def test_filter_by_state(test_state, state, expected_count, expected_ids):
    result = processing.filter_by_state(test_state, state)
    assert len(result) == expected_count
    assert [item['id'] for item in result] == expected_ids
    
# Тесты для sort_by_date
def test_sort_by_date_descending(test_state):
    result = processing.sort_by_date(test_state)
    dates = [item['date'] for item in result]
    assert dates == [
        '2019-07-03T18:35:29.512364',
        '2018-10-14T08:21:33.419441',
        '2018-09-12T21:27:25.241689',
        '2018-06-30T02:08:58.425572'
    ]

def test_sort_by_date_ascending(test_state):
    result = processing.sort_by_date(test_state, descending=False)
    dates = [item['date'] for item in result]
    assert dates == [
        '2018-06-30T02:08:58.425572',
        '2018-09-12T21:27:25.241689',
        '2018-10-14T08:21:33.419441',
        '2019-07-03T18:35:29.512364'
    ]
