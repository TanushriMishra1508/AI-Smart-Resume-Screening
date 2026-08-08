from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def rank_resumes(resume_text, job_description):
    """
    Calculate similarity between a resume
    and a job description.

    Returns a value between 0 and 1.
    """

    if not resume_text.strip() or not job_description.strip():
        return 0.0

    documents = [
        resume_text,
        job_description
    ]

    try:
        vectorizer = TfidfVectorizer(
            stop_words="english"
        )

        vectors = vectorizer.fit_transform(documents)

        similarity = cosine_similarity(
            vectors[0:1],
            vectors[1:2]
        )

        return float(similarity[0][0])

    except Exception:
        return 0.0