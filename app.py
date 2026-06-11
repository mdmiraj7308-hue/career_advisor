import streamlit as st

from main import run_advisor
from src.ui.report_display import render_placeholder, render_report
from src.ui.sidebar import render_sidebar

st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="briefcase",
    layout="wide",
)

st.title("AI Career Advisor")
st.caption(
    "Research 5-year market demand, required skills, and a realistic roadmap tailored to your background."
)

inputs = render_sidebar()

if inputs is None:
    render_placeholder()
else:
    with st.spinner("Researching market demand and building your personalized roadmap..."):
        try:
            report = run_advisor(
                career_goal=inputs.career_goal,
                location=inputs.location,
                background=inputs.background,
            )
            render_report(report)
        except EnvironmentError as exc:
            st.error(str(exc))
        except Exception as exc:
            st.error("Something went wrong while generating your report. Please try again.")
            st.exception(exc)
