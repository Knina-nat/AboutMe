import streamlit as st

st.title("Calculator")

st.header("Simple calculator for numbers <=100")

num1 = st.number_input("Enter first number:", min_vale = 0, max_value=100 )
num2 = st.number_input("Enter second number:", min_vale = 0, max_value=100 )

drop_down = st.selectbox("Choose an operation:",("Add","Subtract","Multiply","Divide"))

if st.button("Calculate"):
    if drop_down == "Add":
        result = num1 + num2
        st.success(f"Your result is: {result}")

    elif drop_down == "Subtract":
        result = num1 - num2
        st.success(f"Your result is: {result}")

    elif drop_down == "Multiply":
        result = num1 * num2
        st.success(f"Your result is: {result}")

    elif drop_down == "Divide":
        if num1 or num2 == 0:
            st.error("You cannot divide by zero")
        else:
            result = num1 / num2
        st.success(f"Your result is: {result}")

