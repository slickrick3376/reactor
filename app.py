import streamlit as st

st.set_page_config(page_title="Message", layout="centered")

st.title("fentreactor69000 clarification")

txt = st.text_area("Hello everyone, about fentreactor69000; wanted to clear some things up. I threw together this dark-humor project, tossing in memes and heavy-hitter names like Jeffrey Epstein and Adolf Hitler, just to test unhinged AI. Never was about supporting them; their beliefs are trash, and mine don't align. Things got too raw, too fast, and I apologize. The bots are offline now. Taken down, being reworked with strict guardrails. They'll return, but way more controlled. Thanks for understanding. 
- 🪿👑
", height=200, key="msg")

if txt.strip():
    st.markdown("---")
    st.markdown(
        f'<p style="font-size: 1.4rem; line-height: 1.7;">{txt}</p>',
        unsafe_allow_html=True
    )
