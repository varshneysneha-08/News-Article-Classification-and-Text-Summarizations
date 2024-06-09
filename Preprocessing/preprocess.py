import pandas as pd
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/crawling and scraping/data.csv')

def remove_html_tags(text):
    if isinstance(text, str):
        pattern = re.compile('<.*?>')
        return pattern.sub(r'', text)
    else:
        return text

def remove_url(text):
    if isinstance(text, str):
        pattern = re.compile(r'https?://\S+|www\.\S+')
        return pattern.sub(r'', text)
    else:
        return text

def remove_punctuation(text):
    if isinstance(text, str):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)
    else:
        return text
    
def remove_stopwords(text):
    if isinstance(text, str):
        new_text = [word for word in text.split() if word.lower() not in stopwords.words('english')]
        return ' '.join(new_text)
    else:
        return text


def remove_extra_spaces_numericals_special_chars(text):
    if isinstance(text, str):
        # Remove numerical values
        text_no_numericals = re.sub(r'\d+', '', text)
        # Remove special characters
        text_no_special_chars = re.sub(r'[^\w\s]', '', text_no_numericals)
        # Remove extra spaces
        cleaned_text = re.sub(r'\s+', ' ', text_no_special_chars)
        return cleaned_text.strip()
    else:
        return text

    
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])
df['article'] = df['article'].apply(remove_extra_spaces_numericals_special_chars)
df['article'] =  df['article'].str.lower()
df['article'] = df['article'].apply(remove_html_tags)
df['article'] = df['article'].apply(remove_url)
df['article'] = df['article'].apply(remove_punctuation)
df['article'] = df['article'].apply(remove_stopwords)
df['article'] = df['article'].apply(word_tokenize)



wordnet_lemmatizer=WordNetLemmatizer()
lemmatizer = WordNetLemmatizer()
df['article'] = df['article'].apply(lambda x:' '.join([lemmatizer.lemmatize(token) for token in x]) if isinstance(x, str) else x)
df.to_csv('data.csv', index=False)

user_prediction = modelSVC.predict(user_article)