# === Importing Libraries ==============================

import streamlit as st

import requests

import json


# === Page Configuration ==============================

st.set_page_config(
    page_title="Student Placement Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# === Custom CSS — One Dark Pro Theme ==============================

st.markdown("""
<style>

    /* ---- Global — One Dark Pro ---- */
    .stApp {
        background-color: #282c34;
    }

    /* Hide Streamlit top bar & footer */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        height: 0 !important;
        min-height: 0 !important;
        padding: 0 !important;
        visibility: hidden;
    }

    #MainMenu, footer, .stDeployButton {
        display: none !important;
    }

    .main .block-container {
        padding-top: 2rem;
        color: #abb2bf;
    }

    /* ---- Main Title ---- */
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #61afef, #c678dd, #61afef);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient-shift 3s ease infinite;
        margin-bottom: 0.2rem;
    }

    @keyframes gradient-shift {
        0% { background-position: 0% center; }
        50% { background-position: 100% center; }
        100% { background-position: 0% center; }
    }

    .sub-title {
        text-align: center;
        color: #5c6370;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    /* ---- Sidebar — One Dark Pro ---- */
    section[data-testid="stSidebar"] {
        background-color: #21252b;
        border-right: 1px solid #3e4452;
    }

    section[data-testid="stSidebar"] .stMarkdown h2 {
        color: #61afef;
        font-size: 1.3rem;
        border-bottom: 2px solid #3e4452;
        padding-bottom: 0.5rem;
    }

    section[data-testid="stSidebar"] .stMarkdown h4 {
        color: #c678dd;
    }

    section[data-testid="stSidebar"] hr {
        border-color: #3e4452;
    }

    /* ---- All text / labels ---- */
    .stMarkdown, .stMarkdown p, .stMarkdown li {
        color: #abb2bf;
    }

    h1, h2, h3, h4, h5, h6 {
        color: #e5c07b !important;
    }

    /* ---- Input widgets ---- */
    .stNumberInput label, .stSelectbox label, .stTextInput label {
        color: #abb2bf !important;
        font-weight: 600 !important;
    }

    .stNumberInput input {
        background-color: #1e2127 !important;
        color: #abb2bf !important;
        border: 1px solid #3e4452 !important;
        border-radius: 8px !important;
    }

    .stNumberInput button {
        background-color: #3e4452 !important;
        color: #abb2bf !important;
        border: none !important;
    }

    .stNumberInput button:hover {
        background-color: #4b5263 !important;
    }

    .stSelectbox > div > div {
        background-color: #1e2127 !important;
        color: #abb2bf !important;
        border: 1px solid #3e4452 !important;
        border-radius: 8px !important;
    }

    /* ---- Cards ---- */
    .result-card {
        background-color: #21252b;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        border: 1px solid #3e4452;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .result-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(97, 175, 239, 0.1);
    }

    .result-placed {
        border: 2px solid #98c379;
        background-color: #2a3225;
    }

    .result-not-placed {
        border: 2px solid #e06c75;
        background-color: #322525;
    }

    .result-emoji {
        font-size: 4rem;
        margin-bottom: 0.5rem;
    }

    .result-status {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }

    .result-salary {
        font-size: 1.3rem;
        color: #98c379;
        font-weight: 600;
    }

    /* ---- Metric Cards ---- */
    .metric-card {
        background-color: #21252b;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        border: 1px solid #3e4452;
    }

    .metric-label {
        color: #5c6370;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .metric-value {
        color: #e5c07b;
        font-size: 1.5rem;
        font-weight: 700;
        margin-top: 0.3rem;
    }

    /* ---- Button ---- */
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #61afef, #c678dd) !important;
        color: #282c34 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.8rem 2rem !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(97, 175, 239, 0.3) !important;
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 25px rgba(198, 120, 221, 0.4) !important;
    }

    /* ---- Divider ---- */
    .section-divider {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, #3e4452, transparent);
        margin: 2rem 0;
    }

    /* ---- Skill Bars ---- */
    .skill-bar-container {
        background-color: #21252b;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #3e4452;
    }

    .skill-row {
        display: flex;
        align-items: center;
        margin-bottom: 0.9rem;
    }

    .skill-row:last-child {
        margin-bottom: 0;
    }

    .skill-name {
        color: #abb2bf;
        font-size: 0.85rem;
        font-weight: 600;
        width: 110px;
        min-width: 110px;
    }

    .skill-track {
        flex: 1;
        height: 10px;
        background-color: #3e4452;
        border-radius: 5px;
        overflow: hidden;
        margin: 0 10px;
    }

    .skill-fill {
        height: 100%;
        border-radius: 5px;
        transition: width 0.6s ease;
    }

    .skill-value {
        color: #5c6370;
        font-size: 0.8rem;
        font-weight: 700;
        width: 36px;
        text-align: right;
    }

    /* ---- Experience Grid ---- */
    .exp-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 0.7rem;
    }

    .exp-item {
        background-color: #21252b;
        border: 1px solid #3e4452;
        border-radius: 10px;
        padding: 0.8rem 1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .exp-name {
        color: #abb2bf;
        font-size: 0.85rem;
        font-weight: 600;
    }

    .exp-badge {
        background-color: #98c379;
        color: #282c34;
        font-weight: 800;
        font-size: 0.85rem;
        padding: 0.2rem 0.65rem;
        border-radius: 20px;
    }

    /* ---- Footer ---- */
    .footer {
        text-align: center;
        color: #5c6370;
        font-size: 0.85rem;
        margin-top: 3rem;
        padding-top: 1.5rem;
        border-top: 1px solid #3e4452;
    }

    .footer strong {
        color: #61afef;
    }

</style>
""", unsafe_allow_html=True)


# === API Configuration ==============================

API_URL = "http://127.0.0.1:8000/predict"


# === Header ==============================

st.markdown('<h1 class="main-title">🎓 Student Placement Predictor</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Powered by Stacking Ensemble ML — Predict your placement & expected salary</p>', unsafe_allow_html=True)
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)


# === Sidebar — Student Info Form ==============================

with st.sidebar:

    st.markdown("## 📝 Student Profile")

    # -- Academic Section --
    st.markdown("#### 🏫 Academic Details")

    branch = st.selectbox(
        "Engineering Branch",
        options=["CSE", "IT", "CE", "ME", "EE", "ECE", "Chemical"],
        index=0
    )

    college_tier = st.selectbox(
        "College Tier",
        options=["Tier-1", "Tier-2", "Tier-3"],
        index=0
    )

    cgpa = st.number_input("CGPA", min_value=0.1, max_value=9.9, value=8.0, step=0.1, format="%.1f")
    backlogs = st.number_input("Backlogs", min_value=0, max_value=3, value=0, step=1)

    st.markdown("---")

    # -- Skills Section --
    st.markdown("#### 💻 Technical Skills")

    coding_skills = st.number_input("Coding Skills (1–10)", min_value=0.1, max_value=9.9, value=7.0, step=0.1, format="%.1f")
    dsa_score = st.number_input("DSA Score (1–10)", min_value=0.1, max_value=9.9, value=7.0, step=0.1, format="%.1f")
    aptitude_score = st.number_input("Aptitude Score (20–100)", min_value=20.0, max_value=100.0, value=70.0, step=0.5, format="%.1f")
    communication_skills = st.number_input("Communication Skills (1–10)", min_value=0.1, max_value=9.9, value=7.0, step=0.1, format="%.1f")
    ml_knowledge = st.number_input("ML Knowledge (0–10)", min_value=0.0, max_value=9.9, value=5.0, step=0.1, format="%.1f")
    system_design = st.number_input("System Design (0–10)", min_value=0.0, max_value=9.9, value=5.0, step=0.1, format="%.1f")

    st.markdown("---")

    # -- Experience Section --
    st.markdown("#### 🏆 Experience & Activities")

    internships = st.number_input("Internships", min_value=0, max_value=3, value=1, step=1)
    projects_count = st.number_input("Projects Completed", min_value=0, max_value=5, value=3, step=1)
    certifications = st.number_input("Certifications", min_value=0, max_value=4, value=2, step=1)
    hackathons = st.number_input("Hackathons Participated", min_value=0, max_value=3, value=1, step=1)
    open_source_contributions = st.number_input("Open Source Contributions", min_value=0, max_value=2, value=1, step=1)
    extracurriculars = st.number_input("Extracurriculars", min_value=0, max_value=3, value=1, step=1)


# === Main Content — Profile Summary ==============================

st.markdown("### 📊 Your Profile Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🏫 Branch</div>
        <div class="metric-value">{branch}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">🏆 College Tier</div>
        <div class="metric-value">{college_tier}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">📈 CGPA</div>
        <div class="metric-value">{cgpa}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    avg_skills = round((coding_skills + dsa_score + (aptitude_score / 10) + communication_skills + ml_knowledge + system_design) / 6, 1)
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">💡 Avg Skills</div>
        <div class="metric-value">{avg_skills}/10</div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("")


# === Skills & Experience Visuals ==============================

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.markdown("#### 💻 Skills Breakdown")

    skills = [
        ("Coding", coding_skills, 10, "#61afef"),
        ("DSA", dsa_score, 10, "#c678dd"),
        ("Aptitude", aptitude_score, 100, "#e5c07b"),
        ("Comm.", communication_skills, 10, "#56b6c2"),
        ("ML", ml_knowledge, 10, "#98c379"),
        ("Sys Design", system_design, 10, "#e06c75"),
    ]

    bars_html = ""
    for name, val, max_val, color in skills:
        pct = (val / max_val) * 100
        display = f"{val}" if max_val == 10 else f"{val}"
        bars_html += f"""
        <div class="skill-row">
            <span class="skill-name">{name}</span>
            <div class="skill-track">
                <div class="skill-fill" style="width: {pct}%; background-color: {color};"></div>
            </div>
            <span class="skill-value">{display}</span>
        </div>"""

    st.markdown(f'<div class="skill-bar-container">{bars_html}</div>', unsafe_allow_html=True)

with col_chart2:
    st.markdown("#### 🏆 Experience Overview")

    experiences = [
        ("🏢 Internships", internships),
        ("📂 Projects", projects_count),
        ("📜 Certifications", certifications),
        ("💡 Hackathons", hackathons),
        ("🌍 Open Source", open_source_contributions),
        ("🎭 Extracurriculars", extracurriculars),
    ]

    exp_html = ""
    for name, val in experiences:
        exp_html += f"""
        <div class="exp-item">
            <span class="exp-name">{name}</span>
            <span class="exp-badge">{val}</span>
        </div>"""

    st.markdown(f'<div class="exp-grid">{exp_html}</div>', unsafe_allow_html=True)


st.markdown('<hr class="section-divider">', unsafe_allow_html=True)


# === Prediction Button ==============================

predict_btn = st.button("🔮 Predict My Placement", use_container_width=True)

if predict_btn:

    # Build Payload
    payload = {
        "branch": branch,
        "college_tier": college_tier,
        "cgpa": cgpa,
        "backlogs": backlogs,
        "coding_skills": coding_skills,
        "dsa_score": dsa_score,
        "aptitude_score": aptitude_score,
        "communication_skills": communication_skills,
        "ml_knowledge": ml_knowledge,
        "system_design": system_design,
        "internships": internships,
        "projects_count": projects_count,
        "certifications": certifications,
        "hackathons": hackathons,
        "open_source_contributions": open_source_contributions,
        "extracurriculars": extracurriculars,
    }

    with st.spinner("🔄 Analyzing your profile..."):

        try:
            response = requests.post(API_URL, json=payload, timeout=10)

            if response.status_code == 200:

                result = response.json().get("response", "")

                st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
                st.markdown("### 🎯 Prediction Result")

                if result.startswith("Yes"):

                    # Extract salary
                    salary = result.split("Expected Salary: ")[1] if "Expected Salary:" in result else "N/A"

                    col_r1, col_r2, col_r3 = st.columns([1, 2, 1])

                    with col_r2:
                        st.markdown(f"""
                        <div class="result-card result-placed">
                            <div class="result-emoji">🎉</div>
                            <div class="result-status" style="color: #98c379;">PLACED!</div>
                            <div class="result-salary">💰 Expected Salary: {salary}</div>
                            <p style="color: #5c6370; margin-top: 1rem; font-size: 0.95rem;">
                                Congratulations! Based on your profile, the model predicts a successful placement.
                            </p>
                        </div>
                        """, unsafe_allow_html=True)

                    st.balloons()

                else:

                    col_r1, col_r2, col_r3 = st.columns([1, 2, 1])

                    with col_r2:
                        st.markdown("""
                        <div class="result-card result-not-placed">
                            <div class="result-emoji">📚</div>
                            <div class="result-status" style="color: #e06c75;">NOT PLACED</div>
                            <p style="color: #5c6370; margin-top: 1rem; font-size: 0.95rem;">
                                Don't worry! Focus on improving your skills, work on projects,
                                and practice DSA. You've got this! 💪
                            </p>
                        </div>
                        """, unsafe_allow_html=True)

            else:
                st.error(f"❌ API returned status code: {response.status_code}")

        except requests.exceptions.ConnectionError:
            st.error("⚠️ Could not connect to the FastAPI backend. Make sure it's running on **http://127.0.0.1:8000**")
            st.info("💡 Start the backend with: `uvicorn backend.main:app --reload`")

        except requests.exceptions.Timeout:
            st.error("⏱️ Request timed out. The server might be overloaded.")

        except Exception as e:
            st.error(f"❌ Unexpected Error: {str(e)}")


# === Footer ==============================

st.markdown("""
<div class="footer">
    <p>Built with ❤️ using <strong>Streamlit</strong> + <strong>FastAPI</strong> + <strong>Scikit-Learn</strong></p>
    <p>🎓 Student Placement Prediction Model — Stacking Ensemble ML</p>
</div>
""", unsafe_allow_html=True)
