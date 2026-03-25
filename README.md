📄 **Smart Resume Parser**
🚀 **Overview**

The Smart Resume Parser is a Python-based application that automatically extracts important information from resumes. It processes PDF and DOCX files to identify key details such as skills, education, and experience, and presents them in a structured format.

This project helps reduce manual effort in resume screening and demonstrates practical use of text processing and basic NLP techniques.

✨ **Features**
📂 Supports PDF & DOCX resume formats
🔍 Extracts Skills, Education, Experience
🧹 Cleans and processes raw text
📊 Outputs structured data in JSON format
🌐 Simple web interface using Streamlit
📥 Download extracted results

🛠️** Tech Stack**
Python
pdfplumber
python-docx
Regular Expressions (re)
JSON
Streamlit
Visual Studio Code

**Installation**
1️⃣ Clone the repository
git clone https://github.com/your-username/resume-parser.git
cd resume-parser
2️⃣ Install dependencies
pip install pdfplumber python-docx streamlit
▶️ How to Run
🔹 Run Parser (Terminal)
python parser.py
🔹 Run Web App
streamlit run app.py

OR

py -m streamlit run app.py

📸 **Usage**
Open the web app
Upload a resume (PDF/DOCX)
View extracted:
Skills
Education
Experience
Download results as JSON

📌 **Example Output**
{
    "Skills": ["Python", "SQL"],
    "Education": ["Bachelor"],
    "Experience": ["Intern", "Project"]
}

🎯 **Future Enhancements**
🤖 Advanced NLP-based skill detection
📊 Resume scoring system
💼 Job matching feature
🎨 Improved UI design
🌐 Deployment on cloud

👩‍💻 Author

Kavisri Vijayakumar

📄 **License**

This project is for educational purposes.
