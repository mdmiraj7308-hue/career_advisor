import streamlit as st


def render_placeholder() -> None:
    st.info(
        "Enter your career goal, location, and background in the sidebar, "
        "then click **Generate Report** to get a personalized 5-year market analysis and roadmap."
    )


def render_report(report: str) -> None:
    st.subheader("Career Research Report")
    st.markdown(report)
