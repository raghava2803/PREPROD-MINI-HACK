# Token Cost Calculator App

## Overview

The **Token Cost Calculator App** allows users to calculate the number of tokens and the total cost of a given text. The app processes either:
- Text entered directly into a text box, or
- A text file uploaded by the user.

The app tokenizes the input text, removes common stop words, and computes the token count and total cost based on a user-defined token price.

You can access the deployed app here: [Token Cost Calculator App](https://preprod-mini-hack.onrender.com)

---

## Features

- **Text Input**: Enter a text directly into the provided textbox or upload a `.txt` file.
- **Tokenization**: The text is split into tokens, and common stop words are removed.
- **Cost Calculation**: Based on the token count and the provided token price, the app calculates the total cost.
- **Special Character Inclusion**: Users can choose whether to include special characters like commas, periods, etc., in tokenization.
- **Result Display**: The app displays:
  - Total token count
  - Total cost of tokens
  - List of filtered tokens

---

## Installation

To run this app locally, you need **Python** and **Streamlit** installed.

### Requirements

- **Python**: Version 3.7 or above.
- **Streamlit**: Version 1.0 or above.

### Install Dependencies

1. Clone or download the repository to your local machine.
2. Install the required dependencies using the following command:
   ```bash
   pip install streamlit

### Key Changes:
- To run the file use the following command:
  ```bash
  streamlit run app.py
