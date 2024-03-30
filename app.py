import streamlit as st
import random
import csv

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
        questions = random.sample(junior_questions, 4)
    elif position == "Mid-Level":
        questions = random.sample(mid_level_questions, 4)
    elif position == "Senior":
        questions = random.sample(senior_questions, 4)

    session_state = st.session_state.get("session_state", {"question_index": 0, "answers": []})

    if session_state["question_index"] < len(questions):
        display_question(questions, session_state)
    else:
        display_responses(session_state["answers"])

def display_question(questions, session_state):
    st.header("Interview Questions")
    current_question = questions[session_state["question_index"]]
    #st.subheader(f"Question {session_state['question_index'] + 1}")
    st.write(current_question)
    answer = st.text_area("Your Answer:", value="")
    
    if st.button("Submit"):
        st.subheader(f"Question {session_state['question_index'] + 1}")
        session_state["answers"].append(answer)
        session_state["question_index"] += 1
        if session_state["question_index"] < 4:
            st.experimental_rerun()

def display_responses(answers):
    st.header("Your Responses")
    for i, answer in enumerate(answers, start=1):
        st.write(f"Response {i}: {answer}")

    if st.button("Save Responses"):
        save_responses(answers)

def save_responses(answers):
    filename = "interview_responses.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Question", "Response"])
        for i, answer in enumerate(answers, start=1):
            writer.writerow([f"Question {i}", answer])
    st.write(f"Responses saved to {filename}")

if __name__ == "__main__":
    main()
