from dataclasses import dataclass

import streamlit as st


@dataclass(frozen=True)
class CareerInputs:
    career_goal: str
    location: str
    background: str


def render_sidebar() -> CareerInputs | None:
    with st.sidebar:
        st.header("Your Profile")
        st.caption("Tell us about your career goal and background.")

        career_goal = st.text_input(
            "Career Goal",
            placeholder="e.g. Machine Learning Engineer",
        )
        location = st.text_input(
            "Location",
            placeholder="e.g. United States, India, Remote",
        )
        background = st.text_area(
            "Current Background",
            placeholder=(
                "Education, work experience, skills, and certifications you already have."
            ),
            height=160,
        )
        submitted = st.button("Generate Report", type="primary", use_container_width=True)

    if not submitted:
        return None

    missing_fields = []
    if not career_goal.strip():
        missing_fields.append("Career Goal")
    if not location.strip():
        missing_fields.append("Location")
    if not background.strip():
        missing_fields.append("Current Background")

    if missing_fields:
        st.sidebar.error(f"Please fill in: {', '.join(missing_fields)}")
        return None

    return CareerInputs(
        career_goal=career_goal.strip(),
        location=location.strip(),
        background=background.strip(),
    )
