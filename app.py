# app.py
import streamlit as st
from recommender import get_recommendations

st.set_page_config(page_title="HelperBuddy", layout="centered")

# Title and description
st.markdown("<h1 style='text-align: center; color: #4B0082;'>📚 HelperBuddy</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Select a technology topic and get recommended learning resources with useful links!</p>", unsafe_allow_html=True)
st.markdown("---")

# 15 topics
topics = [
    "Python", "AI/ML", "Data Science", "Web Development", "Cloud Computing",
    "Cybersecurity", "Blockchain", "Databases", "DevOps", "Mobile Development",
    "IoT", "Networking", "Big Data", "UI/UX", "Game Development"
]

# Dropdown menu
selected_topic = st.selectbox("Select a Topic", topics)

# Button to get recommendations
if st.button("Get Recommendations"):
    recs = get_recommendations(selected_topic)
    
    if recs:
        for r in recs:
            with st.container():
                # Resource title with icon
                st.markdown(f"<h3 style='color: #4B0082;'>📘 {r['title']}</h3>", unsafe_allow_html=True)
                
                # Description
                st.markdown(f"<p style='font-size:16px;'>{r['description']}</p>", unsafe_allow_html=True)
                
                # Clickable button
                st.markdown(
                    f"<a href='{r['url']}' target='_blank'>"
                    f"<button style='background-color:#6A5ACD;color:white;padding:6px 12px;"
                    f"border:none;border-radius:4px;cursor:pointer;'>Visit Resource</button></a>", 
                    unsafe_allow_html=True
                )
                st.markdown("<hr>", unsafe_allow_html=True)
    else:
        st.info("No recommendations available for this topic.")
