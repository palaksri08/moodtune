import streamlit as st
from datetime import datetime
import pandas as pd
from emotion_analysis import get_emotion
from spotify_recommender import get_tracks_for_emotion

st.title("🎵 MoodTune – Your Mood Journal with Soundtrack")

user_input = st.text_area("How are you feeling today?")

if st.button("Analyze Mood & Recommend Songs"):
    if user_input:
        with st.spinner("Analyzing mood..."):
            mood, confidence = get_emotion(user_input)
            st.success(f"Detected Mood: {mood} ({confidence*100:.1f}%)")

            st.markdown("### 🎶 Recommended Songs")
            tracks = get_tracks_for_emotion(mood)
            for track in tracks:
                st.markdown(f"- [{track['name']} by {track['artist']}]({track['url']})")

            new_entry = {"date": datetime.now(), "text": user_input, "mood": mood}
            try:
                df = pd.read_csv("mood_data.csv")
                df = df.append(new_entry, ignore_index=True)
            except:
                df = pd.DataFrame([new_entry])
            df.to_csv("mood_data.csv", index=False)

st.markdown("---")
st.markdown("### 🕒 Mood Timeline")
try:
    df = pd.read_csv("mood_data.csv")
    st.dataframe(df)
except:
    st.info("No past entries yet. Start journaling!")