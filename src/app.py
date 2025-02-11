import streamlit as st
from model import generate_summary


st.set_page_config(page_title="Text Summarizer", layout="wide")

st.markdown(
    """
    <style>
        .header {
            font-size: 36px;
            font-weight: bold;
            color: #2e3a59;
            text-align: center;
            margin-bottom: 20px;
        }
        .subheader {
            font-size: 18px;
            color: #4b4b4b;
            margin-bottom: 20px;
        }
        .textarea {
            font-size: 16px;
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #cccccc;
            width: 100%;
        }
        .button {
            background-color: #5cb85c;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 8px;
            width: 100%;
        }
        .summary-box {
            background-color: #f9f9f9;
            border-radius: 8px;
            padding: 20px;
            border: 1px solid #e0e0e0;
            margin-top: 30px;
        }
    </style>
    """, unsafe_allow_html=True)


st.markdown('<div class="header">Text Summarizer</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Enter the text below to generate a concise summary.</div>', unsafe_allow_html=True)


text = st.text_area("", height=310, key="input_text", label_visibility="collapsed", help="Paste or type the text you want to summarize.")


if st.button("Generate Summary", key="generate_button", help="Click to generate summary", use_container_width=True):
    if text:
        summary = generate_summary(text)
    else:
        summary = "Please enter some text to summarize."


    st.markdown('<div class="summary-box">', unsafe_allow_html=True)
    st.write("## Summarized Text:")
    st.write(summary)
    st.markdown('</div>', unsafe_allow_html=True)

