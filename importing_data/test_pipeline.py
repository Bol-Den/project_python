import pytest
from pipeline_extract import extract

@pytest.fixture
def raw_data():
    data = extract("my_data.xlsx")
    return data


def test_raw_data(raw_data):
    assert len(raw_data.columns) == 12