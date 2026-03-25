import streamlit as st
import pdfplumber
import docx
import re
import json
import tempfile


# ===== Extract Text =====
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


# ===== Clean Text =====
def clean_text(text):
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


# ===== Extract Skills =====
def extract_skills(text):
    skills_list = [
        "Python", "Java", "C++", "SQL",
        "Machine Learning", "HTML", "CSS",
        "JavaScript", "Data Science"
    ]

    found_skills = []

    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills


# ===== Extract Education =====
def extract_education(text):
    keywords = ["Bachelor", "B.Tech", "BSc", "BCA", "Master", "MBA"]

    found = []
    for word in keywords:
        if word.lower() in text.lower():
            found.append(word)

    return list(set(found))


# ===== Extract Experience =====
def extract_experience(text):
    keywords = ["Intern", "Experience", "Project", "Worked"]

    found = []
    for word in keywords:
        if word.lower() in text.lower():
            found.append(word)

    return list(set(found))


# ===== UI =====
st.title("📄 Smart Resume Parser")

uploaded_file = st.file_uploader("Upload your Resume", type=["pdf", "docx"])

if uploaded_file is not None:
    text = extract_text(uploaded_file)
    cleaned = clean_text(text)

    skills = extract_skills(cleaned)
    education = extract_education(cleaned)
    experience = extract_experience(cleaned)

    result = {
        "Skills": skills,
        "Education": education,
        "Experience": experience
    }

    st.subheader("📌 Extracted Information")
    st.json(result)

    st.download_button(
        "Download Result",
        json.dumps(result, indent=4),
        file_name="result.json"
    )