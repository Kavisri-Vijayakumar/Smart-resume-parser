import streamlit as st
import pdfplumber
import docx
import re
import json


def extract_text(file):
    text = ""

    if file.name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    return text


def clean_text(text):
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def extract_skills(text):
    skills_list = [
        "Python", "Java", "C++", "SQL",
        "Machine Learning", "HTML", "CSS",
        "JavaScript", "Data Science"
    ]

    return [skill for skill in skills_list if skill.lower() in text.lower()]


def extract_education(text):
    keywords = ["Bachelor", "B.Tech", "BSc", "BCA", "Master", "MBA"]

    return list(set([k for k in keywords if k.lower() in text.lower()]))


def extract_experience(text):
    keywords = ["Intern", "Experience", "Project", "Worked"]

    return list(set([k for k in keywords if k.lower() in text.lower()]))


st.title("📄 Smart Resume Parser")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file:
    text = extract_text(uploaded_file)
    cleaned = clean_text(text)

    result = {
        "Skills": extract_skills(cleaned),
        "Education": extract_education(cleaned),
        "Experience": extract_experience(cleaned)
    }

    st.subheader("📌 Extracted Information")
    st.json(result)

    st.download_button(
        "Download JSON",
        json.dumps(result, indent=4),
        file_name="result.json"
    )
