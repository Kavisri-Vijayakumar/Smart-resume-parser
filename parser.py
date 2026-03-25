import pdfplumber
import docx
import re
import json


def extract_text(file_path):
    text = ""

    if file_path.endswith(".pdf"):
        try:
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        except Exception as e:
            return f"Error reading PDF: {e}"

    elif file_path.endswith(".docx"):
        try:
            doc = docx.Document(file_path)
            for para in doc.paragraphs:
                text += para.text + "\n"
        except Exception as e:
            return f"Error reading DOCX: {e}"

    else:
        return "Unsupported file format"

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
    keywords = [
        "Bachelor", "B.Tech", "BSc", "BCA",
        "Master", "M.Tech", "MSc", "MBA"
    ]

    return list(set([k for k in keywords if k.lower() in text.lower()]))


def extract_experience(text):
    keywords = ["Intern", "Experience", "Worked", "Project"]

    return list(set([k for k in keywords if k.lower() in text.lower()]))


if __name__ == "__main__":
    file_path = "sample.pdf"

    text = extract_text(file_path)

    if "Error" in text or "Unsupported" in text:
        print(text)
    else:
        cleaned = clean_text(text)

        result = {
            "Skills": extract_skills(cleaned),
            "Education": extract_education(cleaned),
            "Experience": extract_experience(cleaned)
        }

        print("\n===== FINAL OUTPUT =====\n")
        print(json.dumps(result, indent=4))
