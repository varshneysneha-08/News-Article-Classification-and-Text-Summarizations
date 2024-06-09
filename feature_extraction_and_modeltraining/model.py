from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.metrics import confusion_matrix
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

train_data=pd.read_csv('model_dataset2.csv')

# Assuming you have your features X and labels y
X, y = train_data['article'].values, train_data['Category'].values

# Define your classifier
modelRF = make_pipeline(TfidfVectorizer(),SVC())

# Define the cross-validation strategy (StratifiedKFold is used here)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Initialize a list to store confusion matrices for each fold
confusion_matrices = []
accuracy_folds = []

# Perform cross-validation and collect confusion matrices
for train_index, test_index in cv.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

    # Train the classifier
    modelRF.fit(X_train, y_train)

    # Predict on the test set
    y_pred = modelRF.predict(X_test)

    # Compute and store the confusion matrix for this fold
    cm_fold = confusion_matrix(y_test, y_pred)
    confusion_matrices.append(cm_fold)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    accuracy_folds.append(accuracy)

# Aggregate or analyze the confusion matrices as needed
