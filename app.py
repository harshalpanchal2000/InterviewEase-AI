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

def main():
    st.sidebar.title("Interview Ease AI")
    st.sidebar.write("Welcome to Interview Ease AI, your ultimate solution for data scientist hiring! With customizable interview templates and advanced NLP analysis, streamline your hiring process effortlessly. Say hello to a new era of interviews.")

    st.sidebar.title("Select Position Level")
    position = st.sidebar.radio("", ("Junior", "Mid-Level", "Senior"))

    if position == "Junior":
        questions = junior_questions
    elif position == "Mid-Level":
        questions = mid_level_questions
    elif position == "Senior":
        questions = senior_questions

    session_state = st.session_state.get("session_state", {"question_index": 0, "responses": []})

    if session_state["question_index"] < len(questions):
        display_question(questions, session_state)
    else:
        display_responses(session_state["responses"])

def display_question(questions, session_state):
    st.header("Interview Questions")
    current_question = questions[session_state["question_index"]]
    st.write(current_question)
    answer = st.text_area("Your Answer:", value="")
    
    if st.button("Submit"):
        session_state["responses"].append(answer)
        session_state["question_index"] += 1
        st.experimental_rerun()

    if session_state["question_index"] == len(questions):
        display_responses(session_state["responses"])

def display_responses(responses):
    st.header("Your Responses")
    df = pd.DataFrame({"Question": range(1, len(responses) + 1), "Response": responses})
    st.dataframe(df)

    if st.button("Save Responses"):
        # Perform any further evaluation or processing here
        st.write("Responses saved for evaluation.")

if _name_ == "_main_":
    main()
