import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
def preprocess_data(user_art):
  def remove_html_tags(text):
      pattern = re.compile('<.*?>')
      return pattern.sub(r'', text)

  def remove_url(text):
      pattern = re.compile(r'https?://\S+|www\.\S+')
      return pattern.sub(r'', text)

  def remove_punctuation(text):
      exclude = set(string.punctuation)
      return ''.join(ch for ch in text if ch not in exclude)

  def remove_stopwords(text):
      stop_words = set(stopwords.words('english'))
      new_text = [word for word in text.split() if word.lower() not in stop_words]
      return ' '.join(new_text)

  def lemmatize(text):
      lemmatizer = WordNetLemmatizer()
      return ' '.join([lemmatizer.lemmatize(token) for token in word_tokenize(text)])

  # Apply the preprocessing steps
  user_article = user_art
  user_article=user_article.lower()
  user_article = remove_html_tags(user_art)
  user_article = remove_url(user_article)
  user_article = remove_punctuation(user_article)
  user_article = remove_stopwords(user_article)
  user_article = lemmatize(user_article)

  # Tokenize the preprocessed user article
  user_article_tokenized = word_tokenize(user_article)

  return user_article_tokenized