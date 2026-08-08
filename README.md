# 📄 AI Smart Resume Screening & Candidate Ranking Tool

An AI-powered resume screening application that helps recruiters compare multiple resumes against a job description using **ATS keyword matching, resume similarity, and candidate ranking**.

The application provides a recruiter-friendly dashboard with performance metrics, candidate scores, visualizations, and downloadable reports.

## 🚀 Features

* 📤 Upload multiple resumes in PDF format
* 📝 Enter or paste a Job Description
* 📄 Automatically extract text from resumes
* 🎯 Calculate ATS keyword matching score
* 🔍 Calculate resume–job description similarity
* 🏆 Rank candidates based on their overall scores
* 📊 Interactive recruiter dashboard
* 📈 Visualize candidate performance
* 👤 Identify the top candidate
* 📥 Download candidate analysis reports
* ⚡ Simple and interactive Streamlit interface

## 🛠️ Tech Stack

* **Python**
* **Streamlit** – Web application
* **Pandas** – Data processing
* **Scikit-learn** – TF-IDF and cosine similarity
* **Plotly** – Interactive visualizations
* **pdfplumber / PyPDF2** – PDF text extraction

## 🧠 How It Works

```text
Job Description
       ↓
Resume Upload
       ↓
PDF Text Extraction
       ↓
Resume Processing
       ↓
ATS Keyword Matching
       ↓
Resume–JD Similarity
       ↓
Candidate Ranking
       ↓
Recruiter Dashboard
       ↓
Downloadable Report
```

## 📊 Candidate Evaluation

The tool evaluates candidates using two major components:

### ATS Score

Measures how well the candidate's resume matches relevant keywords and skills from the job description.

### Similarity Score

Uses **TF-IDF and Cosine Similarity** to measure how closely the resume content matches the job description.

### Overall Ranking

Candidates are ranked using their combined evaluation scores to help recruiters identify the strongest matches.

## 📁 Project Structure

```text
Smart-Resume-Screening/
│
├── app.py
├── ats.py
├── ranking.py
├── resume_parser.py
├── utils.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd Smart-Resume-Screening
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🎯 Use Case

This project can help recruiters and hiring teams reduce the time spent manually screening resumes by providing a quick comparison between candidates and a specific job description.

It can also be used as a demonstration of practical skills in:

* Python
* Data Analysis
* Natural Language Processing
* Machine Learning
* Streamlit
* Data Visualization

## 🔮 Future Improvements

* 🤖 Advanced NLP-based semantic matching
* 🧠 Integration with transformer-based models
* 📌 Skill-gap analysis
* 💡 Resume improvement suggestions
* 📧 Automated candidate communication
* 👥 Recruiter authentication
* ☁️ Cloud deployment
* 📊 Advanced candidate analytics

## 👩‍💻 Author

**Tanushri Mishra**

B.Tech – Computer Science & Engineering

---

⭐ If you find this project useful, consider giving the repository a star!
