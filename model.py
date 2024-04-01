import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Preprocess the answers
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    stop_words = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(text)
    filtered_tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered_tokens)

preprocessed_answers = {question: preprocess_text(answer) for question, answer in all_answers.items()}

# Vectorize the answers
vectorizer = TfidfVectorizer()
answer_vectors = vectorizer.fit_transform(preprocessed_answers.values())

# Function to get the response
def get_response(user_answer):
    preprocessed_user_answer = preprocess_text(user_answer)
    user_vector = vectorizer.transform([preprocessed_user_answer])
    similarities = cosine_similarity(user_vector, answer_vectors)
    return similarities

# Example usage
user_answer = "The Central Limit Theorem states that the sampling distribution of the sample mean approaches a normal distribution as the sample size increases, regardless of the shape of the population distribution."
similarities = get_response(user_answer)
print("Similarity scores:", similarities)
