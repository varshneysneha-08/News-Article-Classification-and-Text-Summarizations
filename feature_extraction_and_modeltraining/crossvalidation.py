import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from joblib import dump

# Instantiate the Multinomial Naive Bayes model
#model = Pipeline([('vectorizer', TfidfVectorizer()),('classifier', MultinomialNB())])
model = make_pipeline(TfidfVectorizer(),RandomForestClassifier())

train_data=pd.read_csv('model_dataset.csv')
train_texts = train_data['article'].values
train_labels = train_data['Category'].values

# Perform cross-validation
cross_val_scores = cross_val_score(model, train_texts, train_labels, cv=5,error_score='raise')  # cv=5 means 5-fold cross-validation
model.fit(train_texts,train_labels)

# Print the cross-validation scores
print("Cross-Validation Scores:", cross_val_scores)

# Print the average accuracy
print("Average Accuracy:", cross_val_scores.mean())
joblib.dump(model, 'classification_model.joblib')