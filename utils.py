import re


def clean_text(text):
    """Clean and normalize text."""

    if not text:
        return ""

    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Keep common programming symbols such as + and #
    text = re.sub(r"[^a-zA-Z0-9+#.\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_skills(text):
    """Extract known technical skills from text."""

    skills = [
        "python",
        "java",
        "c++",
        "c",
        "sql",
        "mysql",
        "excel",
        "power bi",
        "tableau",
        "machine learning",
        "deep learning",
        "data analysis",
        "pandas",
        "numpy",
        "matplotlib",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "html",
        "css",
        "javascript",
        "react",
        "node",
        "git",
        "github",
        "docker",
        "linux",
        "aws",
        "azure",
        "streamlit",
        "nlp",
        "flask",
        "statistics",
        "data visualization"
    ]

    text = text.lower()

    found = []

    for skill in skills:
        if skill in text:
            found.append(skill)

    return sorted(set(found))