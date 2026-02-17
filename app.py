import streamlit as st

#bionic function
def bionic_converter(text):
    words = text.split()
    processed_words = []

#for loop to iterate through the words
    for word in words:
        if len(word) > 1:
            # Calculate the "fixation point" (usually the first half)
            midpoint = (len(word) // 2) + 1
            # Markdown uses ** for bold. We bold the start, keep the end normal.
            bold_part = f"**{word[:midpoint]}**"
            rest_part = word[midpoint:]
            processed_words.append(bold_part + rest_part)
        else:
            # Don't bold single letters like 'a' or 'I'
            processed_words.append(word)
            
    return " ".join(processed_words)

# --- The Web Interface ---
st.set_page_config(page_title="Bionic Reader", page_icon="📖")
st.title("Bionic Reader Converter")
st.write("Paste your text below to make it easier to read!")

# Create a text box for the user
user_input = st.text_area("Input Text", placeholder="Type or paste something here...", height=200)

if user_input:
    # Run our function and display the result
    bionic_output = bionic_converter(user_input)
    st.subheader("Result:")
    st.markdown(bionic_output)