import streamlit as st

def main():
    session_state = st.session_state.get("session_state", {"answers": [""] * 4})

    st.sidebar.title("Interview Ease AI")
    st.sidebar.write("Welcome to Interview Ease AI, your ultimate solution for data scientist hiring! With customizable interview templates and advanced NLP analysis, streamline your hiring process effortlessly. Say hello to a new era of interviews.")

    st.sidebar.title("Select Position Level")
    position = st.sidebar.radio("", ("Junior", "Mid-Level", "Senior"))

    questions = get_questions(position)

    for i, question in enumerate(questions, start=1):
        display_question(i, question, session_state)

    if session_state["question_index"] == 4:
        display_responses(session_state["answers"])

def get_questions(position):
    if position == "Junior":
        return [
            "What is the Central Limit Theorem?",
            "How can outlier values be treated?",
            "Explain the concept of overfitting in machine learning.",
            "Explain confidence intervals."
        ]
    elif position == "Mid-Level":
        return [
            "What is regularization in machine learning?",
            "Explain the bias-variance tradeoff.",
            "What are the assumptions of linear regression?",
            "What is the significance of p-value?"
        ]
    elif position == "Senior":
        return [
            "What is deep learning and how does it differ from traditional machine learning?",
            "What are some common techniques for dimensionality reduction?",
            "What are the feature selection methods used to select the right variables?",
            "Facebook composer, the posting tool, dropped from 3% posts per user last month to 2.5% posts per user today. How would you investigate what happened?"
        ]

def display_question(question_number, question, session_state):
    st.header("Interview Questions")
    st.subheader(f"Question {question_number}")
    st.write(question)
    answer = st.text_area(f"Your Answer for Question {question_number}:", value=session_state["answers"][question_number - 1], key=f"answer_{question_number}")
    
    if st.button("Submit"):
        session_state["answers"][question_number - 1] = answer
        session_state["question_index"] += 1
        if session_state["question_index"] < 4:
            st.experimental_rerun()

def display_responses(answers):
    st.header("Your Responses")
    for i, answer in enumerate(answers, start=1):
        st.write(f"Response {i}: {answer}")

if __name__ == "__main__":
    main()
