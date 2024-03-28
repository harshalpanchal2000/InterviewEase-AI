import streamlit as st
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

def main():
    st.title("Interview Ease AI")

    # Position level selection
    position = st.radio("Select Position Level:", ("Junior", "Mid-Level", "Senior"))

    if position == "Junior":
        user_responses = display_questions(junior_questions, position)
    elif position == "Mid-Level":
        user_responses = display_questions(mid_level_questions, position)
    elif position == "Senior":
        user_responses = display_questions(senior_questions, position)

    # Output all user responses
    st.write("User Responses:", user_responses)

def display_questions(question_pool, position):
    st.header(f"{position} Level Questions")

    user_responses = {}

    # Display questions one by one
    for i, question in enumerate(question_pool, start=1):
        st.subheader(f"Question {i}")
        st.write(question)
        answer = st.text_area(f"Your Answer for Question {i}:")  # Unique key for each text area
        user_responses[f"Question {i}"] = answer

        # Add a submit button for each question
        if st.button("Submit"):
            st.write(f"Your Answer for Question {i}: {answer}")
            st.write("Answer Submitted!")

    return user_responses

if __name__ == "__main__":
    main()
