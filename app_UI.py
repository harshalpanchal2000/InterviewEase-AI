import streamlit as st
import random 
import pandas as pd

# Define your questions lists here: junior_questions, mid_level_questions, senior_questions
# Define your correct answers lists here: junior_correct_answers, mid_level_correct_answers, senior_correct_answers

def main():
    st.sidebar.title("Interview Ease AI")
    st.sidebar.write("Welcome to Interview Ease AI, your ultimate solution for data scientist hiring! With customizable interview templates and advanced NLP analysis, streamline your hiring process effortlessly. Say hello to a new era of interviews.")

    st.sidebar.title("Select Position Level")
    position = st.sidebar.radio("", ("Junior", "Mid-Level", "Senior"))

    if position == "Junior":
        questions = random.sample(junior_questions, 4)
        correct_answers = random.sample(junior_correct_answers, 4)
    elif position == "Mid-Level":
        questions = random.sample(mid_level_questions, 4)
        correct_answers = random.sample(mid_level_correct_answers, 4)
    elif position == "Senior":
        questions = random.sample(senior_questions, 4)
        correct_answers = random.sample(senior_correct_answers, 4)

    session_state = st.session_state.get("session_state", {"question_index": 0, "answers": [], "show_questions": True})

    if session_state["show_questions"]:
        if session_state["question_index"] < len(questions):
            display_question(questions, session_state)
        else:
            session_state["show_questions"] = False
            display_responses(session_state["answers"], correct_answers)
    else:
        display_responses(session_state["answers"], correct_answers)

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

def display_responses(answers, correct_answers):
    st.header("Your Responses")
    for i, (answer, correct_answer) in enumerate(zip(answers, correct_answers), start=1):
        st.write(f"Question {i}:")
        st.write(f"Your Response: {answer}")
        st.write(f"Correct Answer: {correct_answer}")
        st.write("---")

    if st.button("Save Responses"):
        save_responses(answers, correct_answers)

def save_responses(answers, correct_answers):
    df = pd.DataFrame({"Question": [f"Question {i}" for i in range(1, len(answers)+1)], 
                       "Your Response": answers,
                       "Correct Answer": correct_answers})
    df.to_csv("responses.csv", index=False)
    st.write("Responses saved to responses.csv")

if __name__ == "__main__":
    main()
