import streamlit as st

def main():
    st.title("Interview Ease AI")

    # Position level selection
    position = st.radio("Select Position Level:", ("Junior", "Mid-Level", "Senior"))

    if position == "Junior":
        # Display junior-level questions
        display_junior_questions()
    elif position == "Mid-Level":
        # Display mid-level questions
        display_mid_level_questions()
    elif position == "Senior":
        # Display senior-level questions
        display_senior_questions()

def display_junior_questions():
    st.header("Junior Level Questions")

    # Display theoretical questions
    for i in range(3):
        st.write(f"Theoretical Question {i+1}: ")

    # Display coding question
    st.write("Coding Question: ")

    # Display past experience question
    st.write("Past Experience Question: ")

def display_mid_level_questions():
    st.header("Mid-Level Questions")

    # Display theoretical questions
    for i in range(3):
        st.write(f"Theoretical Question {i+1}: ")

    # Display coding question
    st.write("Coding Question: ")

    # Display past experience question
    st.write("Past Experience Question: ")

def display_senior_questions():
    st.header("Senior Level Questions")

    # Display theoretical questions
    for i in range(3):
        st.write(f"Theoretical Question {i+1}: ")

    # Display coding question
    st.write("Coding Question: ")

    # Display past experience question
    st.write("Past Experience Question: ")

if __name__ == "__main__":
    main()
