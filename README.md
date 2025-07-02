# MoodTune – AI-Powered Mood Journal with Music Recommendations

## What It Does
MoodTune is an intelligent journaling tool that helps users reflect on their emotional well-being and discover music that aligns with their current mood.  
It uses Natural Language Processing to detect emotional states and Spotify’s API to recommend songs that resonate with those moods.

---

## How It Relates to MoodScale
MoodTune supports MoodScale’s mission by promoting mental and emotional wellness through:
- Mood awareness via journaling  
- Therapeutic use of music  
- Emotion tracking over time

---

## APIs, Tools & Libraries Used
- Streamlit → Frontend interface  
- HuggingFace Transformers + torch → Emotion classification  
- Spotipy → Spotify Web API integration  
- pandas → Mood journal storage  

---

## Core Functionalities
- Mood Journal: Analyze what users write  
- Emotion Detection: AI detects the mood  
- Spotify Integration: Suggests songs to match the mood  
- Mood History: Displays past mood entries over time  

---

## Challenges Faced
- Spotify requires redirect URIs even for client credentials  
- Emotion prediction can vary with short vs. long text  
- Streamlit cloud deployment required credential management via secrets.toml  

---

## What I'd Improve With More Time
- Add OpenAI-powered affirmations for each mood  
- Add mood heatmaps and charts  
- Store journal entries in a secure cloud DB  
- Add user accounts with authentication  

---
