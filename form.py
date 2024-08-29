import streamlit as st 

st.write("1.Addition\n\n2.Subtraction ")

opt=st.number_input("Enter the Number: ",value=None, placeholder="Type the number....")

if opt == 1:
    num1 = st.number_input("Enter the first number: ", value=None, placeholder="Type the number....")
    num2 = st.number_input("Enter the second number: ", value=None, placeholder="Type the number....")

    if num1 is not None and num2 is not None:  # Check for None values
        sum = num1 + num2
        st.write("The sum of two numbers is: ", sum)
    else:
        st.error("Please enter both numbers.")
elif opt == 2:
    num1 = st.number_input("Enter the first number: ", value=None, placeholder="Type the number....")
    num2 = st.number_input("Enter the second number: ", value=None, placeholder="Type the number....")

    if num1 is not None and num2 is not None:  # Check for None values
        sum = num1 - num2
        st.write("The subtraction of two numbers is: ", sum)
    else:
        st.error("Please enter both numbers.")
else:
   st.error("Enter the Number between 1 and 2")