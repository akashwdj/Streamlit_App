import streamlit as st
import pyjokes

def generate_random_joke(language='en'):
    return pyjokes.get_joke(language=language)

def generate_multiple_jokes(count=1, language='en'):
    jokes = []
    for _ in range(count):
        jokes.append(pyjokes.get_joke(language=language))
    return jokes

def main():
    st.title("Joke Generator")

    st.write("Select your preferences below:")

    # Dropdown for language selection
    language = st.selectbox("Select language:", ['en', 'es', 'de', 'it'])

    # Number input for the count of jokes
    count = st.number_input("Number of jokes to generate:", min_value=1, max_value=10, value=1)

    # Button to generate jokes
    if st.button("Generate Jokes"):
        if count == 1:
            joke = generate_random_joke(language)
            st.write(joke)
        else:
            jokes = generate_multiple_jokes(count, language)
            for joke in jokes:
                st.write(joke)
                st.write('-' * 30)

if __name__ == '__main__':
    main()
