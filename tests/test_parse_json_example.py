import pytest
from src.parse_json_example import parse_json

def test_parse_json():
    sample_json = '{"name": "John", "age": 30, "city": "New York"}'
    expected_output = {"name": "John", "age": 30, "city": "New York"}
    assert parse_json(sample_json) == expected_output
