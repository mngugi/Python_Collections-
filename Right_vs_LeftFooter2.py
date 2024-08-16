import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Constructing the dataset

# Right-footed (1 for right-footed, 0 for left-footed)
right_footed = np.array([[1, 1]] * 11 + [[1, 0]] * 4 + [[1, 0]] * 2)  # 11 successes, 4 misses, 2 near misses

# Left-footed (1 for success, 0 for failure)
left_footed = np.array([[0, 1]] * 10 + [[0, 0]] * 5 + [[0, 0]] * 2)  # 10 successes, 5 misses, 2 near misses

# Combine the datasets
data = np.vstack((right_footed, left_footed))

# Features and target
X = data[:, 0].reshape(-1, 1)  # Footedness
y = data[:, 1]  # Success (1) or Failure (0)

# Initialize and train the model
model = LogisticRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Evaluate the model
accuracy = accuracy_score(y, y_pred)
conf_matrix = confusion_matrix(y, y_pred)
class_report = classification_report(y, y_pred)

accuracy, conf_matrix, class_report
