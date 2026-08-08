import streamlit as st
import pandas as pd
import time
import plotly.express as px

from resume_parser import extract_text
from ranking import rank_resumes
from ats import calculate_ats_score
from utils import clean_text, extract_skills


# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="AI Smart Resume Screening Tool",
    page_icon="📄",
    layout="wide"
)


# ============================================
# TITLE
# ============================================

st.title("📄 AI Smart Resume Screening Tool")

st.write(
    "Compare resumes with a Job Description using "
    "ATS scoring and resume similarity."
)

st.divider()


# ============================================
# JOB DESCRIPTION
# ============================================

job_description = st.text_area(
    "📋 Paste Job Description",
    height=200,
    placeholder="Paste the complete Job Description here..."
)


# ============================================
# RESUME UPLOAD
# ============================================

uploaded_files = st.file_uploader(
    "📤 Upload Resume(s)",
    type=["pdf"],
    accept_multiple_files=True
)


# ============================================
# ANALYZE BUTTON
# ============================================

if st.button("🚀 Analyze Resumes"):

    # Check resumes
    if not uploaded_files:
        st.warning("Please upload at least one resume.")
        st.stop()

    # Check job description
    if not job_description.strip():
        st.warning("Please enter a Job Description.")
        st.stop()

    # Progress bar
    progress = st.progress(0)

    results = []

    # Clean job description
    cleaned_job = clean_text(job_description)

    # ========================================
    # PROCESS EACH RESUME
    # ========================================

    for i, uploaded_file in enumerate(uploaded_files):

        # Extract text
        resume_text = extract_text(uploaded_file)

        # Check extracted text
        if not resume_text.strip():

            st.warning(
                f"Could not extract text from "
                f"{uploaded_file.name}"
            )

            continue

        # Clean resume
        cleaned_resume = clean_text(resume_text)

        # ------------------------------------
        # Similarity
        # ------------------------------------

        similarity = rank_resumes(
            cleaned_resume,
            cleaned_job
        )

        similarity_percentage = round(
            similarity * 100,
            2
        )

        # ------------------------------------
        # ATS Score
        # ------------------------------------

        ats_score, matched_skills, missing_skills = (
            calculate_ats_score(
                cleaned_resume,
                cleaned_job
            )
        )

        # ------------------------------------
        # Resume Skills
        # ------------------------------------

        skills = extract_skills(
            cleaned_resume
        )

        # ------------------------------------
        # Overall Score
        # ------------------------------------

        overall_score = round(
            (similarity_percentage * 0.6)
            +
            (ats_score * 0.4),
            2
        )

        # ------------------------------------
        # Store Result
        # ------------------------------------

        results.append(
            {
                "Resume": uploaded_file.name,
                "Similarity (%)": similarity_percentage,
                "ATS Score": ats_score,
                "Overall Score": overall_score,
                "Skills": ", ".join(skills),
                "Matched Skills": ", ".join(matched_skills),
                "Missing Skills": ", ".join(missing_skills)
            }
        )

        # Progress
        progress.progress(
            int(
                ((i + 1) / len(uploaded_files))
                * 100
            )
        )

        time.sleep(0.1)

    progress.empty()

    # ========================================
    # CHECK RESULTS
    # ========================================

    if not results:
        st.error(
            "No resume text could be extracted. "
            "Please upload valid text-based PDF resumes."
        )
        st.stop()

    # ========================================
    # DATAFRAME
    # ========================================

    df = pd.DataFrame(results)

    # Sort by overall score
    df = df.sort_values(
        by="Overall Score",
        ascending=False
    ).reset_index(drop=True)

    # Add rank
    df.insert(
        0,
        "Rank",
        range(1, len(df) + 1)
    )

    # ========================================
    # SUCCESS MESSAGE
    # ========================================

    st.success(
        "✅ Resume analysis completed successfully!"
    )

    st.divider()

    # ========================================
    # DASHBOARD
    # ========================================

    st.header("📊 Recruiter Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total Resumes",
            len(df)
        )

    with col2:
        st.metric(
            "Highest Overall Score",
            f"{df['Overall Score'].max():.2f}%"
        )

    with col3:
        st.metric(
            "Average ATS Score",
            f"{df['ATS Score'].mean():.2f}%"
        )

    with col4:
        st.metric(
            "Average Similarity",
            f"{df['Similarity (%)'].mean():.2f}%"
        )

    # ========================================
    # TOP CANDIDATE
    # ========================================

    st.divider()

    st.header("🏆 Top Candidate")

    top_candidate = df.iloc[0]

    st.success(
        f"🥇 {top_candidate['Resume']}"
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Overall Score",
            f"{top_candidate['Overall Score']:.2f}%"
        )

    with col2:
        st.metric(
            "ATS Score",
            f"{top_candidate['ATS Score']:.2f}%"
        )

    with col3:
        st.metric(
            "Similarity",
            f"{top_candidate['Similarity (%)']:.2f}%"
        )

    st.write(
        "**Matched Skills:**",
        top_candidate["Matched Skills"]
        if top_candidate["Matched Skills"]
        else "None"
    )

    st.write(
        "**Missing Skills:**",
        top_candidate["Missing Skills"]
        if top_candidate["Missing Skills"]
        else "None"
    )

    # ========================================
    # CANDIDATE RANKING
    # ========================================

    st.divider()

    st.header("📋 Candidate Ranking")

    ranking_columns = [
        "Rank",
        "Resume",
        "Similarity (%)",
        "ATS Score",
        "Overall Score"
    ]

    st.dataframe(
        df[ranking_columns],
        use_container_width=True,
        hide_index=True
    )

    # ========================================
    # DETAILED SKILLS
    # ========================================

    st.divider()

    st.header("🛠️ Candidate Skills")

    for _, row in df.iterrows():

        with st.expander(
            f"Rank {row['Rank']} - {row['Resume']}"
        ):

            st.write(
                "**Skills:**",
                row["Skills"]
                if row["Skills"]
                else "No recognized skills"
            )

            st.write(
                "**Matched Skills:**",
                row["Matched Skills"]
                if row["Matched Skills"]
                else "None"
            )

            st.write(
                "**Missing Skills:**",
                row["Missing Skills"]
                if row["Missing Skills"]
                else "None"
            )

    # ========================================
    # ATS CHART
    # ========================================

    st.divider()

    st.subheader("📈 ATS Score Comparison")

    ats_chart = px.bar(
        df,
        x="Resume",
        y="ATS Score",
        text="ATS Score",
        title="ATS Score of Candidates"
    )

    ats_chart.update_layout(
        yaxis_range=[0, 100]
    )

    st.plotly_chart(
        ats_chart,
        use_container_width=True
    )

    # ========================================
    # SIMILARITY CHART
    # ========================================

    st.subheader("🎯 Resume Similarity")

    similarity_chart = px.bar(
        df,
        x="Resume",
        y="Similarity (%)",
        text="Similarity (%)",
        title="Resume Similarity with Job Description"
    )

    similarity_chart.update_layout(
        yaxis_range=[0, 100]
    )

    st.plotly_chart(
        similarity_chart,
        use_container_width=True
    )

    # ========================================
    # OVERALL SCORE CHART
    # ========================================

    st.subheader("🏆 Overall Candidate Score")

    overall_chart = px.bar(
        df,
        x="Resume",
        y="Overall Score",
        text="Overall Score",
        title="Overall Candidate Ranking"
    )

    overall_chart.update_layout(
        yaxis_range=[0, 100]
    )

    st.plotly_chart(
        overall_chart,
        use_container_width=True
    )

    # ========================================
    # DOWNLOAD REPORT
    # ========================================

    st.divider()

    st.subheader("📥 Download Report")

    csv_file = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="Download Ranking Report",
        data=csv_file,
        file_name="resume_ranking_report.csv",
        mime="text/csv"
    )