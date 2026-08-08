from utils import extract_skills


def calculate_ats_score(resume_text, job_description):
    """
    Calculate ATS score based on matching skills.

    Returns:
        ats_score
        matched_skills
        missing_skills
    """

    resume_skills = set(
        extract_skills(resume_text)
    )

    job_skills = set(
        extract_skills(job_description)
    )

    # If no recognizable skills are found in JD
    if not job_skills:
        return 0.0, [], []

    matched_skills = sorted(
        resume_skills.intersection(job_skills)
    )

    missing_skills = sorted(
        job_skills - resume_skills
    )

    ats_score = (
        len(matched_skills)
        / len(job_skills)
    ) * 100

    return (
        round(ats_score, 2),
        matched_skills,
        missing_skills
    )