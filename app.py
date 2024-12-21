"""
Token Cost Calculator App (Streamlit)
--------------------------------------

Description:
This app calculates the token count and cost of the given text. It allows users to either:
1. Input a text directly through a text box.
2. Upload a text file containing the content.

Features:
1. Tokenization: Filters out common stop words and provides the tokenized text.
2. Customizable: Users can decide whether to include special characters in tokenization.
3. Results: Displays token count, total cost, and a list of filtered tokens.
4. The UI can be customized which supports editing the Background,Text colour and Font family.

Version: 1.0.0
Team Name : Lights with Lime
Team Members:
    Name :Raghavendra V     Email: raghavendravmurthy@gmail.com
    Name :P Tharun          Email: pulaguratharun21@gmail.com
    Name :Nikhitha Reddy B  Email: nikhithareddy204@gmail.com
    Name :M Muneendra Reddy Email: muneendraa24@gmail.com
    Name :N Dileesh Rahul   Email: dileeshrahulnallanki2003@gmail.com


Date: 2024-12-21
"""

import streamlit as st
import string

# Define a set of common stop words to be excluded from tokenization
STOP_WORDS = {
    "the", "and", "is", "in", "to", "it", "of", "a", "that", "on", "for",
    "with", "as", "was", "at", "by", "an", "be", "this", "which", "or",
    "from", "are", "but", "not", "have", "has", "they", "you", "we"
}

def tokenize_and_filter(text, include_special_chars):
    """
    Tokenizes the input text, filters out stop words, and optionally removes special characters.
    
    Parameters:
    - text (str): The input text to be tokenized.
    - include_special_chars (bool): If True, special characters are retained in tokens, otherwise they are removed.
    
    Returns:
    - list: A list of filtered tokens from the text.
    """
    # Remove punctuation if special characters are not to be included
    if not include_special_chars:
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)
    
    # Convert text to lowercase and split into tokens
    tokens = text.lower().split()
    
    # Filter out stop words
    return [word for word in tokens if word not in STOP_WORDS]

# Custom CSS for styling the user interface
st.markdown("""
<style>
body {
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f4;
}
.main {
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
h1 {
    color: #333;
    font-size: 2.5rem;
    text-align: center;
    margin-bottom: 20px;
}
button {
    background-color: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}
button:hover {
    background-color: #45a049;
}
textarea {
    width: 100%;
    height: 200px;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
    resize: none;
}
.result-container {
    margin-top: 20px;
    padding: 15px;
    background-color: #000000;
    border: 1px solid #c8e6c9;
    border-radius: 10px;
}
.result-container h3 {
    color: #2e7d32;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<h1>Enhanced Token Cost Calculator</h1>', unsafe_allow_html=True)

# Input Options
st.markdown("<h3>Input Text or Upload a File</h3>", unsafe_allow_html=True)
input_option = st.radio("Choose Input Method", ("Text Box", "Upload File"))

if input_option == "Text Box":
    text_input = st.text_area("Enter your text here", height=150)
else:
    uploaded_file = st.file_uploader("Upload a Text File", type=["txt"])
    text_input = uploaded_file.read().decode("utf-8") if uploaded_file else ""

# Token Price Input
st.markdown("<h3>Enter Token Price</h3>", unsafe_allow_html=True)
token_price = st.number_input("", min_value=0.0, step=0.01, key="token_price")

# Special Characters Toggle
include_special_chars = st.checkbox("Include Special Characters in Tokens", value=False)

# Processing Section
if st.button("Calculate"):
    if text_input and token_price > 0:
        # Call the tokenization and filtering function
        filtered_tokens = tokenize_and_filter(text_input, include_special_chars)
        
        # Calculate token count and total cost
        token_count = len(filtered_tokens)
        total_cost = token_count * token_price

        # Display Results
        st.markdown("""
        <div class="result-container">
            <h3>Results</h3>
            <p><strong>Token Count:</strong> {}</p>
            <p><strong>Total Cost:</strong> ${:.2f}</p>
        </div>
        """.format(token_count, total_cost), unsafe_allow_html=True)

        # Token Display Area
        st.markdown("<h3>Filtered Tokens (Line-by-Line)</h3>", unsafe_allow_html=True)
        st.markdown(f"<textarea readonly>{chr(10).join(filtered_tokens)}</textarea>", unsafe_allow_html=True)
    else:
        st.error("Please provide valid input text and enter a positive token price.")
