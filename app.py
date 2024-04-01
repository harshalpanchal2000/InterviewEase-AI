import streamlit as st
import pandas as pd
import random 

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

def main():
    st.sidebar.title("Interview Ease AI")
    st.sidebar.write("Welcome to Interview Ease AI, your ultimate solution for data scientist hiring! With customizable interview templates and advanced NLP analysis, streamline your hiring process effortlessly. Say hello to a new era of interviews.")

    st.sidebar.title("Select Position Level")
    position = st.sidebar.radio("", ("Junior", "Mid-Level", "Senior"))

    if position == "Junior":
        questions = random.sample(junior_questions, 4)
    elif position == "Mid-Level":
        questions = random.sample(mid_level_questions, 4)
    elif position == "Senior":
        questions = random.sample(senior_questions, 4)

    session_state = st.session_state.get("session_state", {"question_index": 0, "answers": [], "show_questions": True})

    if session_state["show_questions"]:
        if session_state["question_index"] < len(questions):
            display_question(questions, session_state)
        else:
            session_state["show_questions"] = False
            display_responses(session_state["answers"])
    else:
        display_responses(session_state["answers"])

def display_question(questions, session_state):
    st.header("Interview Questions")
    current_question = questions[session_state["question_index"]]
    st.write(current_question)
    answer = st.text_area("Your Answer:", value="")
    
    if st.button("Submit"):
        session_state["answers"].append(answer)
        session_state["question_index"] += 1
        st.session_state["session_state"] = session_state
        st.experimental_rerun()

def display_responses(answers):
    st.header("Your Responses")
    for i, answer in enumerate(answers, start=1):
        st.write(f"Response {i}: {answer}")

    if st.button("Save Responses"):
        save_responses(answers)

def save_responses(answers):
    if "responses_df" not in st.session_state:
        st.session_state.responses_df = pd.DataFrame(columns=["Question", "Response"])
    
    for i, answer in enumerate(answers, start=1):
        st.session_state.responses_df = st.session_state.responses_df.append({"Question": f"Question {i}", "Response": answer}, ignore_index=True)

    st.write("Responses saved to DataFrame")

if __name__ == "__main__":
    main()
