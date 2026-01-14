import pandas as pd

def test_data_not_empty():
    df = pd.read_csv("data/dataset.csv")
    assert not df.empty

def test_no_missing_values():
    df = pd.read_csv("data/dataset.csv")
    assert df.isnull().sum().sum() == 0
