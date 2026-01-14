from sklearn.linear_model import LogisticRegression

def test_model_initialization():
    model = LogisticRegression()
    assert model is not None
