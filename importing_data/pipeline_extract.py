
import pandas as pd

def extract(file_path):
    """reading data from file"""
    raw_data = pd.read_excel(file_path)
    return raw_data
