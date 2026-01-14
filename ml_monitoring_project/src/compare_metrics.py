import pandas as pd

current = pd.read_csv("metrics/current_metrics.csv")
historical = pd.read_csv("metrics/historical_metrics.csv")

current_accuracy = current["accuracy"].mean()
historical_accuracy = historical["accuracy"].mean()

print(f"Current Accuracy: {current_accuracy}")
print(f"Historical Accuracy: {historical_accuracy}")

if current_accuracy < historical_accuracy:
    print("⚠ Performance degradation detected")
else:
    print("Performance is stable")
