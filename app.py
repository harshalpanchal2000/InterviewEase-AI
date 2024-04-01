import streamlit as st
import pandas as pd
from model import preprocess_text, vectorize_text, get_response

# Load CSV files for each level
junior_file = "Questions & Answers/junior_questions_answers.csv"
mid_level_file = "Questions & Answers/mid_level_questions_answers.csv"
senior_file = "Questions & Answers/senior_questions_answers.csv"

# Define function to load CSV file based on level
def load_questions(level):
    if level == "Junior":
        return pd.read_csv(junior_file)
    elif level == "Mid-Level":
        return pd.read_csv(mid_level_file)
    elif level == "Senior":
        return pd.read_csv(senior_file)

def main():
    st.sidebar.title("Interview Ease AI")
    st.sidebar.write("Welcome to Interview Ease AI, your ultimate solution for data scientist hiring! With customizable interview templates and advanced NLP analysis, streamline your hiring process effortlessly. Say hello to a new era of interviews.")

    st.sidebar.title("Select Position Level")
    position = st.sidebar.radio("", ("Junior", "Mid-Level", "Senior"))

    # Load questions based on selected level
    questions_df = load_questions(position)

    session_state = st.session_state.get("session_state", {"question_index": 0, "answers": [], "show_questions": True})

    if session_state["show_questions"]:
        if session_state["question_index"] < len(questions_df):
            display_question(questions_df, session_state)
        else:
            session_state["show_questions"] = False
            save_responses(questions_df, session_state["answers"], position)
            display_responses(session_state["answers"], questions_df, position)
    else:
        display_responses(session_state["answers"], questions_df, position)

def display_question(questions_df, session_state):
    st.header("Interview Questions")
    current_question = questions_df.iloc[session_state["question_index"]]
    st.write(current_question["Question"])
    answer = st.text_area("Your Answer:", value="")
    
    if st.button("Submit"):
        session_state["answers"].append(answer)
        session_state["question_index"] += 1
        st.session_state["session_state"] = session_state
        st.experimental_rerun()

def display_responses(answers, questions_df, position):
    st.header("Your Responses")
    for i, answer in enumerate(answers, start=1):
        st.write(f"Response {i}: {answer}")

    # Preprocess user answers and compute similarity scores
    preprocessed_answers = {question: preprocess_text(answer) for question, answer in zip(questions_df["Question"], answers)}
    vectorizer = vectorize_text(preprocessed_answers.values())
    answer_vectors = vectorizer.transform(preprocessed_answers.values())

    correct_answers = questions_df["Answer"]
    similarities = get_response(answer_vectors, correct_answers)
    st.write("Similarity Scores:")
    st.write(similarities)

def save_responses(questions_df, answers, position):
    questions_df["Response"] = answers
    questions_df.to_csv(f"{position.lower()}_responses.csv", index=False)
    st.write("Responses saved to CSV")

if __name__ == "__main__":
    main()
