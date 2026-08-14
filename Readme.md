# 🎬 Netflix Movie & TV Show Recommendation System

An end-to-end Data Science and Machine Learning project that performs content-based recommendations on Netflix titles. Built using **TF-IDF vectorization** and **Cosine Similarity**, and fully interactive via a **Streamlit** web application.

---

## 📌 Project Overview

This project implements a complete data science pipeline:
1. **Data Collection & Cleaning:** Handling missing values, standardizing dates, and converting types.
2. **Exploratory Data Analysis (EDA):** Insights into content distribution, release trends, genres, and durations.
3. **Model Building:** Content-Based Filtering using NLP text processing on combined metadata.
4. **Deployment:** Interactive web user interface built with Streamlit.

---

## 🚀 Live Demo & Screenshots

- **Deployment Platform:** Streamlit Community Cloud
- **Input:** Selected Movie or TV Show Title + Number of Recommendations desired
- **Output:** Top content recommendations along with content details (Type, Genre, Plot Summary)

---

## 🛠️ Features

- **Interactive UI:** Dynamic dropdown search and recommendations slider.
- **NLP Vectorization:** TF-IDF text feature extraction from titles, genres, descriptions, directors, and cast.
- **Similarity Engine:** Cosine similarity scoring for fast real-time content matching.
- **Detailed Output:** Expandable cards showing genres, type, and plot summaries for predicted titles.

---

## 📁 Repository Structure

```text
├── app.py                   # Streamlit web application script
├── netflix_titles.csv       # Raw / preprocessed dataset
├── movies_dict.pkl          # Processed movie metadata dictionary
├── similarity.pkl          # Pre-computed Cosine Similarity matrix
├── requirements.txt         # Python dependency environment file
└── README.md                # Project documentation
