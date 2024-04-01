import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Define question pools for each level
junior_questions = [
    "What is the Central Limit Theorem?",
    "How can outlier values be treated?",
    "Explain the concept of overfitting in machine learning.",
    "Explain confidence intervals.",
    "What is the difference between supervised and unsupervised learning?"
]

mid_level_questions = [
    "What is regularization in machine learning?",
    "Explain the bias-variance tradeoff.",
    "What are the assumptions of linear regression?",
    "What is the significance of p-value?",
    "You are given a data set consisting of variables with more than 30 percent missing values. How will you deal with them?"
]

senior_questions = [
    "What is deep learning and how does it differ from traditional machine learning?",
    "What are some common techniques for dimensionality reduction?",
    "What are the feature selection methods used to select the right variables?",
    "Facebook composer, the posting tool, dropped from 3% posts per user last month to 2.5% posts per user today. How would you investigate what happened?",
    "If the labels are known in a clustering project, how would you evaluate the performance of the model?"
]

# Define correct answers for each level
junior_answers = {
    "What is the Central Limit Theorem?": "The Central Limit Theorem states that the sampling distribution of the sample mean approaches a normal distribution as the sample size increases, regardless of the shape of the population distribution.",
    "How can outlier values be treated?": "Outlier values can be treated by either removing them if they are due to errors or extreme noise, or by transforming them using techniques like winsorization or logarithmic transformation.",
    "Explain the concept of overfitting in machine learning.": "Overfitting occurs when a model learns to capture noise or random fluctuations in the training data rather than the underlying pattern. This leads to poor performance on new, unseen data.",
    "Explain confidence intervals.": "Confidence intervals are a range of values calculated from sample data that is likely to contain the true population parameter with a certain level of confidence. It provides a measure of the uncertainty associated with the estimate.",
    "What is the difference between supervised and unsupervised learning?": "In supervised learning, the model is trained on labeled data where each input-output pair is provided, and the model learns to predict the output from the input data. In unsupervised learning, the model is trained on unlabeled data and aims to find hidden patterns or structures in the data."
}

mid_level_answers = {
    "What is regularization in machine learning?": "Regularization is a technique used to prevent overfitting by adding a penalty term to the loss function, which discourages overly complex models. It helps to generalize the model to new, unseen data.",
    "Explain the bias-variance tradeoff.": "The bias-variance tradeoff refers to the balance between the model's ability to capture the true underlying pattern in the data (bias) and its sensitivity to variations in the training data (variance). A model with high bias may underfit the data, while a model with high variance may overfit the data.",
    "What are the assumptions of linear regression?": "The assumptions of linear regression include linearity (relationship between variables is linear), independence of errors (residuals are independent), homoscedasticity (constant variance of residuals), and normality of errors (residuals are normally distributed).",
    "What is the significance of p-value?": "The p-value is a measure of the strength of evidence against the null hypothesis in a statistical hypothesis test. It indicates the probability of observing the test results, or more extreme results, under the assumption that the null hypothesis is true.",
    "You are given a data set consisting of variables with more than 30 percent missing values. How will you deal with them?": "There are several methods to deal with missing values, including imputation (replacing missing values with a calculated value), deletion (removing observations or variables with missing values), or using advanced techniques like multiple imputation or predictive modeling."
}

senior_answers = {
    "What is deep learning and how does it differ from traditional machine learning?": "Deep learning is a subset of machine learning that uses artificial neural networks with multiple layers to learn hierarchical representations of data. It differs from traditional machine learning by automatically learning features from the data rather than relying on manual feature engineering.",
    "What are some common techniques for dimensionality reduction?": "Common techniques for dimensionality reduction include Principal Component Analysis (PCA), t-distributed Stochastic Neighbor Embedding (t-SNE), and Linear Discriminant Analysis (LDA). These techniques aim to reduce the number of features while preserving the most important information in the data.",
    "What are the feature selection methods used to select the right variables?": "Feature selection methods include filter methods (e.g., correlation-based feature selection), wrapper methods (e.g., recursive feature elimination), and embedded methods (e.g., Lasso regression). These methods aim to select the most relevant features for improving model performance.",
    "Facebook composer, the posting tool, dropped from 3% posts per user last month to 2.5% posts per user today. How would you investigate what happened?": "To investigate the drop in post percentage, you can analyze various factors such as changes in user behavior, platform algorithms, posting frequency, or external factors like competition or market trends. Conducting A/B testing or user surveys can also provide insights into the cause of the drop.",
    "If the labels are known in a clustering project, how would you evaluate the performance of the model?": "If the labels are known, you can use evaluation metrics like Adjusted Rand Index (ARI), Mutual Information Score (MI), or Fowlkes-Mallows Index (FMI) to measure the similarity between the true labels and the cluster assignments generated by the model. These metrics assess the quality of clustering without relying on the actual labels."
}

# Combine all questions and answers
all_questions = junior_questions + mid_level_questions + senior_questions
all_answers = {**junior_answers, **mid_level_answers, **senior_answers}

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
