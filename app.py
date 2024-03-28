import streamlit as st
import random

# Define question pools for each level
junior_questions = [
    "What is the Central Limit Theorem?",
    "Explain the concept of overfitting in machine learning.",
    "What is the difference between supervised and unsupervised learning?"
]

mid_level_questions = [
    "What is regularization in machine learning?",
    "Explain the bias-variance tradeoff.",
    "What are the assumptions of linear regression?"
]

senior_questions = [
    "What is deep learning and how does it differ from traditional machine learning?",
    "What are some common techniques for dimensionality reduction?",
    "Explain the concept of ensemble learning."
]

def main():
    st.title("Interview Ease AI")

    # Position level selection
    position = st.radio("Select Position Level:", ("Junior", "Mid-Level", "Senior"))

    if position == "Junior":
        display_questions(junior_questions, position)
    elif position == "Mid-Level":
        display_questions(mid_level_questions, position)
    elif position == "Senior":
        display_questions(senior_questions, position)

def display_questions(question_pool, position):
    st.header(f"{position} Level Questions")

    # Display questions one by one
    for i, question in enumerate(question_pool, start=1):
        st.subheader(f"Question {i}")
        st.write(question)
        answer = st.text_area(f"Your Answer for Question {i}:")  # Unique key for each text area
        st.write(f"Your Answer for Question {i}: {answer}")

if __name__ == "__main__":
    main()
