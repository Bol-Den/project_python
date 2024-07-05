import pytest
from importing_data.from_file.pipeline_extract import extract

@pytest.fixture
def raw_data():
    data = extract("my_data.xlsx")
    return data


def test_raw_data_columns(raw_data):
    assert len(raw_data.columns) == 12

def test_raw_data(raw_data):
    # data = extract("my_data.xlsx")
    assert raw_data["Quantity"].sum() == 1947