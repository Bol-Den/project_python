import pytest
from pipeline_extract import extract

# @pytest.fixture
# def raw_data():
#     data = extract("my_data.xlsx")
#     return data


def test_raw_data():
    data = extract("my_data.xlsx")
    assert len(data.columns) == 12