import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import make_pipeline

train_data=pd.read_csv('file1.csv')
test_data=pd.read_csv('file3.csv')
print(test_data['Category'].value_counts())
# df['Category'].value_counts() //values of each category
train_data.dropna(inplace=True) #for droping empty rows
test_data.dropna(inplace=True) #for droping empty rows
print(test_data['Category'].value_counts())
# df.isnull().sum() #for checking if there any empty row
# df.duplicated().sum()
train_data.drop_duplicates(inplace=True)
test_data.drop_duplicates(inplace=True)
# df.duplicated().sum()
print(test_data['Category'].value_counts())
# X=df.iloc[:,0:1]
# Y=df['Category']


# Extract text and labels from the training and testing sets
train_texts = train_data['article'].values
train_labels = train_data['Category'].values
test_texts = test_data['article'].values
test_labels = test_data['Category'].values

model = make_pipeline(TfidfVectorizer(),MultinomialNB())
model.fit(train_texts,train_labels)

# Make predictions on the test set
predictions = model.predict(test_texts)
mat=confusion_matrix(test_labels,predictions)
print(mat)

# Evaluate the model
accuracy = accuracy_score(test_labels, predictions)
print(f"Accuracy: {accuracy:.2f}")

# Display classification report
print("Classification Report:\n", classification_report(test_labels, predictions))
