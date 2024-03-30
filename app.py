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
    st.write(current_question)
    answer = st.text_area("Your Answer:", value="")
    
    if st.button("Submit"):
        session_state["answers"].append(answer)
        session_state["question_index"] += 1
        if session_state["question_index"] < len(questions):
            st.experimental_rerun()

    if session_state["question_index"] == len(questions):
        display_responses(session_state["answers"])

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
