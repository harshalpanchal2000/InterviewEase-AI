import streamlit as st
import pandas as pd
import random 

# Define question pools for each level
junior_technical_questions = [
    "What is the Central Limit Theorem?",
    "How can outlier values be treated?",
    "Explain the concept of overfitting in machine learning.",
    "Explain confidence intervals.",
    "What is the difference between supervised and unsupervised learning?"
]

junior_behavioral_questions = [
    "Can you describe a time when you had to work under pressure?",
    "How do you handle conflicts in a team?",
    "Tell us about a project you completed successfully. What challenges did you face and how did you overcome them?",
    "Describe a situation where you had to learn a new technology or tool quickly.",
    "How do you prioritize tasks when working on multiple projects?"
]

mid_level_technical_questions = [
    "What is regularization in machine learning?",
    "Explain the bias-variance tradeoff.",
    "What are the assumptions of linear regression?",
    "What is the significance of p-value?",
    "You are given a data set consisting of variables with more than 30 percent missing values. How will you deal with them?"
]

mid_level_behavioral_questions = [
    "Describe a difficult decision you had to make at work. How did you approach it?",
    "How do you handle feedback?",
    "Tell us about a time when you had to resolve a conflict within your team.",
    "Describe a project where you had to take the lead. What was your approach?",
    "How do you handle tight deadlines?"
]

senior_technical_questions = [
    "What is deep learning and how does it differ from traditional machine learning?",
    "What are some common techniques for dimensionality reduction?",
    "What are the feature selection methods used to select the right variables?",
    "Facebook composer, the posting tool, dropped from 3% posts per user last month to 2.5% posts per user today. How would you investigate what happened?",
    "If the labels are known in a clustering project, how would you evaluate the performance of the model?"
]

senior_behavioral_questions = [
    "Describe a time when you had to mentor or train a junior team member.",
    "How do you handle failure?",
    "Tell us about a project where you had to navigate ambiguity.",
    "Describe a situation where you had to influence others to adopt your ideas.",
    "How do you stay updated with the latest developments in your field?"
]

# Function to select questions based on position and type (technical or behavioral)
def select_questions(position, question_type):
    if position == "Junior":
        if question_type == "Technical":
            return random.sample(junior_technical_questions, 4)
        elif question_type == "Behavioral":
            return random.sample(junior_behavioral_questions, 4)
    elif position == "Mid-Level":
        if question_type == "Technical":
            return random.sample(mid_level_technical_questions, 4)
        elif question_type == "Behavioral":
            return random.sample(mid_level_behavioral_questions, 4)
    elif position == "Senior":
        if question_type == "Technical":
            return random.sample(senior_technical_questions, 4)
        elif question_type == "Behavioral":
            return random.sample(senior_behavioral_questions, 4)

# Main function
def main():
    st.sidebar.title("Interview Ease AI")
    st.sidebar.write("Welcome to Interview Ease AI, your ultimate solution for hiring data scientists! Select the position level and question type to get started.")

    position = st.sidebar.radio("Position Level", ("Junior", "Mid-Level", "Senior"))
    question_type = st.sidebar.radio("Question Type", ("Technical", "Behavioral"))

    questions = select_questions(position, question_type)

    session_state = st.session_state.get("session_state", {"question_index": 0, "responses": []})

    if session_state["question_index"] < len(questions):
        display_question(questions, session_state)
    else:
        display_responses(session_state["responses"])

# Function to display questions
def display_question(questions, session_state):
    st.header("Interview Questions")
    current_question = questions[session_state["question_index"]]
    st.write(current_question)
    answer = st.text_area("Your Answer:", value="")
    
    if st.button("Submit"):
        session_state["responses"].append(answer)
        session_state["question_index"] += 1
        if session_state["question_index"] < len(questions):
            st.experimental_rerun()

    if session_state["question_index"] == len(questions):
        display_responses(session_state["responses"])

# Function to display responses
def display_responses(responses):
    st.header("Your Responses")
    df = pd.DataFrame({"Question": range(1, len(responses) + 1), "Response": responses})
    st.dataframe(df)

if __name__ == "__main__":
    main()
