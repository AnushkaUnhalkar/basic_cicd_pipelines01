import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("data/dataset.csv")

X = data.drop("target", axis=1)
y = data["target"]

model = LogisticRegression()
model.fit(X, y)

print("Model trained successfully")
