import streamlit as st
import datetime

st.title("Welcome to Student Registration Portal")

user_input = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=100)
birthdate = st.date_input("Select your birthdate:", datetime.date(2000, 1, 1))
volume = st.slider("Select Percentage:", 0, 100, 50)
option = st.selectbox("Choose a Stream:", ["Computer Science", "Electrical Engg", "Mechanical Engg"])
uploaded_file = st.file_uploader("Upload passport size Photo")
options = st.multiselect("Select your hobby:", ["Play Cricket", "Singing", "Dance", "Trekking"])
feedback = st.text_area("Additional Comment:")
choice = st.radio("Gender:", ["Male", "Female"])
agree = st.checkbox("I agree with the terms & Conditions ")

# When the user clicks the "Submit" button
if st.button("Submit"):
    if agree:
        # Creating the content of the text file
        file_content = f"""
        Name: {user_input}
        Age: {age}
        Birthdate: {birthdate}
        Percentage: {volume}
        Selected Stream: {option}
        Hobbies: {', '.join(options)}
        Gender: {choice}
        Additional Comment: {feedback}
        Agreed to Terms & Conditions: {'Yes' if agree else 'No'}
        """

        # Writing the content to a text file
        with open("student_registration.txt", "w") as file:
            file.write(file_content)

        # Providing a success message and allowing the user to download the file
        st.success("Form successfully submitted!")
        st.write("You can download your submission here:")
        st.download_button(label="Download File", data=file_content, file_name="student_registration.txt", mime="text/plain")
    else:
        st.error("You need to agree with the terms & conditions before submitting.")
