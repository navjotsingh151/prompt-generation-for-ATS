import streamlit as st
import os
import PyPDF2 as pdf
import json
import clipboard

def prompt(input_text, jd):

    input_prompt=f"""
    Hey Act Like a skilled or very experience ATS(Application Tracking System)
    with a deep understanding of tech field,software engineering,data science ,data analyst
    and big data engineer. Your task is to evaluate the resume based on the given job description.
    You must consider the job market is very competitive and you should provide 
    best assistance for improving thr resumes. Assign the percentage Matching based 
    on Jd and
    the missing keywords with high accuracy
    resume:{input_text}
    description:{jd}

    I want the response in one single string having the structure
    {{"JD Match":"%","MissingKeywords:[]","Profile Summary":"","Create two Job Duties containing all MissingKeywords":""}}
    """

    return input_prompt
    

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text


## streamlit app
st.set_page_config(layout="wide")
st.title("Smart ATS - Generate Prompt for Chat GPT ")
st.markdown("Improve Your Resume with Smart Evaluation")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = prompt(input_text=text, jd=jd)
        # st.subheader("Response:")
        with st.expander("Show Response"):
            st.code(response, language='json')
        st.button("Copy", clipboard.copy(response))
       