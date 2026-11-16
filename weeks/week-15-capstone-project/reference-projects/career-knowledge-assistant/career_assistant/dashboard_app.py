"""Optional local Streamlit UI; install the dashboard extra to use."""

from __future__ import annotations

import os
from pathlib import Path

import streamlit as st

from career_assistant import service

db = Path(os.environ.get("CAREER_ASSISTANT_DB", "career.db"))
st.set_page_config(page_title="Career Knowledge Assistant")
st.title("Career Knowledge Assistant")
st.caption("Local-first learning project. No hosted AI or account needed.")

with st.form("new_note"):
    title = st.text_input("Title")
    body = st.text_area("Content")
    tags = st.text_input("Tags (comma separated)")
    if st.form_submit_button("Add note"):
        try:
            service.add_note(db, title, body, tags)
            st.success("Note saved")
        except ValueError as error:
            st.error(str(error))

query = st.text_input("Search")
notes = service.search_notes(db, query) if query.strip() else service.list_notes(db)
st.subheader("Notes")
for note in notes:
    st.markdown(f"**{note['title']}**")
    st.write(note["body"])
    st.caption(", ".join(note["tags"]))

st.subheader("Skills")
with st.form("new_skill"):
    skill = st.text_input("Skill")
    level = st.slider("Level", 0, 5, 0)
    if st.form_submit_button("Save skill"):
        try:
            service.set_skill(db, skill, level)
            st.success("Skill saved")
        except ValueError as error:
            st.error(str(error))

st.dataframe(service.list_skills(db), use_container_width=True)
st.json(service.summary(db))
