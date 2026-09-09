import streamlit as st
from utils.extractor import load_skill_list, extract_skills
from utils.normalizer import normalize_skill

from utils.database import (
    register_user,
    login_user
)



# Page Configuration

st.set_page_config(
    page_title="Job Skill Extraction",
    page_icon="💼",
    layout="wide"
)



# Session State

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_name" not in st.session_state:
    st.session_state.user_name = ""



# Login / Register Page

if not st.session_state.logged_in:

    st.title("💼 Job Skill Extraction")

    st.write(
        "Extract skills from job descriptions using NLP and Machine Learning."
    )

    login_tab, register_tab = st.tabs(
        ["🔐 Login", "📝 Register"]
    )

    
    # LOGIN
  
    with login_tab:

        st.subheader("Login")

        email = st.text_input(
            "Email ID",
            key="login_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="login_password"
        )

        if st.button(
            "Login",
            type="primary"
        ):

            if not email or not password:

                st.warning(
                    "Please enter email and password."
                )

            else:

                user = login_user(
                    email,
                    password
                )

                if user:

                    st.session_state.logged_in = True
                    st.session_state.user_name = user["name"]
                    st.session_state.user_email = user["email"]

                    st.success(
                        f"Welcome {user['name']}!"
                    )

                    st.rerun()

                else:

                    st.error(
                        "Invalid email or password."
                    )


  
    # REGISTER
   
    with register_tab:

        st.subheader("Create Account")

        name = st.text_input(
            "Name",
            key="register_name"
        )

        email = st.text_input(
            "Email ID",
            key="register_email"
        )

        password = st.text_input(
            "Password",
            type="password",
            key="register_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            key="confirm_password"
        )

        if st.button(
            "Create Account",
            type="primary"
        ):

            if not name or not email or not password:

                st.warning(
                    "Please fill all fields."
                )

            elif password != confirm_password:

                st.error(
                    "Passwords do not match."
                )

            elif len(password) < 6:

                st.error(
                    "Password must contain at least 6 characters."
                )

            else:

                success, message = register_user(
                    name,
                    email,
                    password
                )

                if success:

                    st.success(message)
                    st.info(
                        "You can now login."
                    )

                else:

                    st.error(message)



# Main Application

else:

    st.title(
        f"Welcome, {st.session_state.user_name} 👋"
    )

    st.write(
        "You are successfully logged into the Job Skill Extraction system."
    )

    if st.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.user_name = ""
        st.rerun()

    st.divider()

    st.header("🔍 Job Skill Extractor")

    st.write(
        "Paste a job description below and detect the skills it requires, "
        "mapped to their categories."
    )

    # Load taxonomy once (cached so it doesn't reload on every interaction)
    @st.cache_data
    def get_skill_data():
        return load_skill_list()

    skill_lookup, category_lookup = get_skill_data()

    job_description = st.text_area(
        "Paste Job Description",
        height=200,
        placeholder=(
            "Looking for Data Analyst with SQL, "
            "Python, Power BI and Excel experience."
        )
    )

    if st.button(
        "Extract Skills",
        type="primary"
    ):

        if not job_description.strip():

            st.warning(
                "Please paste a job description first."
            )

        else:

            # --- Preprocessing + Skill Extraction (Day 7) ---
            raw_skills = extract_skills(job_description, skill_lookup)

            # --- Skill Normalization (Day 17) ---
            # (extract_skills already returns canonical names, but we re-run
            # normalize_skill here to demonstrate the full pipeline explicitly,
            # and to catch any raw variant text a user might paste directly)
            normalized_skills = sorted(set(
                normalize_skill(s, skill_lookup) or s for s in raw_skills
            ))

            if not normalized_skills:
                st.info("No known skills were detected in this text.")
            else:
                st.subheader("Detected Skills")
                for skill in normalized_skills:
                    st.markdown(f"- **{skill}**")

                # --- Category Mapping ---
                st.subheader("Categories")
                for skill in normalized_skills:
                    category = category_lookup.get(skill, "Unknown")
                    st.markdown(f"**{category}** → {skill}")

    st.divider()
    st.caption(
        "Built on the Job Skill Extraction pipeline: rule-based matching + "
        "taxonomy-driven normalization."
    )
