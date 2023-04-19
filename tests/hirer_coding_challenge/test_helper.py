import os
from src.hirer_coding_challenge.helper import read_spark_config_file

filepath = "config/spark_config.json"

def test_read_spark_config_file_valid_file():
    data = read_spark_config_file(filepath)
    assert isinstance(data, dict)

def test_read_spark_config_file_invalid_file():
    data = read_spark_config_file(filepath)
    assert data is None

def test_read_spark_config_file_invalid_input():
    data = read_spark_config_file(filepath)
    assert data is None

def test_read_spark_config_file_empty_input():
    data = read_spark_config_file(filepath)
    assert data is None

def test_read_spark_config_file_nonexistent_file():
    data = read_spark_config_file(filepath)
    assert data is None

