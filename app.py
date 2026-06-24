import streamlit as st
import random

st.set_page_config(
    page_title="Science Apparatus Challenge",
    page_icon="🔬",
    layout="centered"
)

# Question Bank
QUESTION_BANK = [
    {
        "apparatus": "Beaker",
        "question": "Which apparatus is best for holding and mixing liquids?",
        "options": ["Beaker", "Thermometer", "Ruler", "Stopwatch"],
        "answer": "Beaker",
        "explanation": "A beaker is used to hold, mix and sometimes heat liquids."
    },
    {
        "apparatus": "Thermometer",
        "question": "Which apparatus is used to measure temperature?",
        "options": ["Measuring Cylinder", "Thermometer", "Balance", "Magnifying Glass"],
        "answer": "Thermometer",
        "explanation": "A thermometer measures how hot or cold something is."
    },
    {
        "apparatus": "Measuring Cylinder",
        "question": "Which apparatus measures the volume of liquids accurately?",
        "options": ["Beaker", "Thermometer", "Measuring Cylinder", "Stopwatch"],
        "answer": "Measuring Cylinder",
        "explanation": "A measuring cylinder helps scientists measure liquid volume accurately."
    },
    {
        "apparatus": "Stopwatch",
        "question": "Which apparatus measures time during an experiment?",
        "options": ["Balance", "Stopwatch", "Ruler", "Beaker"],
        "answer": "Stopwatch",
        "explanation": "A stopwatch is used to measure time intervals."
    },
    {
        "apparatus": "Ruler",
        "question": "Which apparatus is used to measure length?",
        "options": ["Ruler", "Thermometer", "Balance", "Beaker"],
        "answer": "Ruler",
        "explanation": "A ruler measures the length of an object."
    },
    {
        "apparatus": "Electronic Balance",
        "question": "Which apparatus measures mass?",
        "options": ["Stopwatch", "Measuring Cylinder", "Electronic Balance", "Beaker"],
        "answer": "Electronic Balance",
        "explanation": "An electronic balance measures the mass of an object."
    },
    {
        "apparatus": "Magnifying Glass",
        "question": "Which apparatus helps scientists observe small details?",
        "options": ["Magnifying Glass", "Ruler", "Beaker", "Balance"],
        "answer": "Magnifying Glass",
        "explanation": "A magnifying glass enlarges objects so we can see details clearly."
    }
]

TOTAL_QUESTIONS = 5

# Session State
if "started" not in st.session_state:
    st.session_state.started = False

if "score" not in st.session_state:
    st.session_state.score = 0

if "question_num" not in st.session_state:
    st.session_state.question_num = 0

if "questions" not in st.session_state:
    st.session_state.questions = random.sample(
        QUESTION_BANK,
        TOTAL_QUESTIONS
    )

if "answered" not in st.session_state:
    st.session_state.answered = False

if "selected" not in st.session_state:
    st.session_state.selected = None

# Title Screen
if not st.session_state.started:

    st.title("🔬 Science Apparatus Challenge")

    st.markdown("""
    Welcome, Young Scientist! 👩‍🔬👨‍🔬

    Your mission:
    - Read each science scenario.
    - Choose the correct scientific apparatus.
    - Earn points for correct answers.
    - Learn how scientists think and work!

    Can you score full marks? 🌟
    """)

    if st.button("🚀 Start Game"):
        st.session_state.started = True
        st.rerun()

# Game Screen
else:

    if st.session_state.question_num < TOTAL_QUESTIONS:

        q = st.session_state.questions[
            st.session_state.question_num
        ]

        st.title("🔬 Science Apparatus Challenge")

        st.progress(
            (st.session_state.question_num) / TOTAL_QUESTIONS
        )

        st.metric("⭐ Score", st.session_state.score)

        st.subheader(
            f"Question {st.session_state.question_num + 1}"
        )

        st.write(q["question"])

        choice = st.radio(
            "Choose your answer:",
            q["options"],
            key=f"q_{st.session_state.question_num}"
        )

        if not st.session_state.answered:

            if st.button("Submit Answer"):

                st.session_state.selected = choice
                st.session_state.answered = True

                if choice == q["answer"]:
                    st.session_state.score += 1

                st.rerun()

        else:

            if st.session_state.selected == q["answer"]:

                st.success(
                    f"✅ Correct! The answer is {q['answer']}."
                )

                st.info(
                    f"💡 {q['explanation']}"
                )

                st.balloons()

            else:

                st.error(
                    f"❌ Not quite. The correct answer is {q['answer']}."
                )

                st.info(
                    f"💡 {q['explanation']}"
                )

            st.markdown(
                """
                **Ways of Thinking and Doing Science 🧠**
                
                Scientists choose the correct apparatus to make
                accurate observations and measurements.
                """
            )

            if st.button("Next Question ➡️"):

                st.session_state.question_num += 1
                st.session_state.answered = False
                st.session_state.selected = None
                st.rerun()

    else:

        st.title("🏆 Game Complete!")

        st.metric(
            "Final Score",
            f"{st.session_state.score}/{TOTAL_QUESTIONS}"
        )

        percentage = (
            st.session_state.score / TOTAL_QUESTIONS
        ) * 100

        if percentage == 100:
            st.success(
                "🌟 Outstanding! You are a Science Apparatus Expert!"
            )

        elif percentage >= 80:
            st.success(
                "🎉 Great job! You know your science tools well!"
            )

        elif percentage >= 60:
            st.info(
                "👍 Good effort! Keep practising to become a scientist."
            )

        else:
            st.warning(
                "💪 Keep learning! Scientists improve through practice."
            )

        if st.button("🔄 Play Again"):

            st.session_state.started = False
            st.session_state.score = 0
            st.session_state.question_num = 0
            st.session_state.answered = False
            st.session_state.selected = None
            st.session_state.questions = random.sample(
                QUESTION_BANK,
                TOTAL_QUESTIONS
            )

            st.rerun()
