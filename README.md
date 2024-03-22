# Smart ATS - Generate Prompt for Chat GPT 

This Streamlit app is designed to evaluate resumes against job descriptions. It acts as an Application Tracking System (ATS), providing feedback on the percentage match between the resume and the job description, highlighting missing keywords, and generating a profile summary.

## How to Use

1. **Paste the Job Description**: Paste the job description into the provided text area.
2. **Upload Your Resume**: Upload your resume in PDF format using the file uploader.
3. **Evaluate Resume**: Click the "Evaluate Resume" button to trigger the evaluation process.
4. **View Results**: The app will display the evaluation results, including the percentage match, missing keywords, profile summary, and two job duties from the missing keywords.

## Installation

To run this app locally, make sure you have Python installed. Then, install the required dependencies using pip:

```pip install streamlit PyPDF2 pyperclip```

After installing the dependencies, you can run the app using the following command:

```streamlit run app.py```


## About

This app is built with Streamlit, a Python library for building interactive web applications. It uses PyPDF2 for extracting text from PDF resumes and pyperclip for copying the evaluation results to the clipboard.

## Contributors

- [Your Name](https://github.com/yourusername)

Feel free to contribute to this project by submitting bug reports, feature requests, or pull requests.




