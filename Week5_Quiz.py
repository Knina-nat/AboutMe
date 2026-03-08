import streamlit as st

st.title("Mini Quiz")

st.header("Capital Cities in Asia")

score =0

Q1 = st.radio("1. What is the capital city of Singapore?",
              ["Kuala Lumpur", "Jakarta", "Ho Chi Minh", "Singapore"])

st.divider()

Q2 = st.radio("2. What is the capital city of Korea?",
              ["Bei Jing", "Seoul","Tokyo","Manila"])

st.divider()

Q3 = st.radio("3. What is the capital city of India?",
              ["Kathmandu","Phnom Penh","New Delhi","Tehran"])

if st.button("Submit"):
    if Q1 == "Singapore":
        st.success("Correct!")
        score +=1
    else: st.error("Wrong... Correct answer is Singapore")

    if Q2 == "Seoul":
        st.success("Correct!")
        score +=1
    else: st.error("Wrong... Correct answer is Seoul")

    if Q3 == "New Delhi":
        st.success("Correct!")
        score +=1
    else: st.error("Wrong... Correct answer is New Delhi")

st.header(f"Total Score: {score}/3")