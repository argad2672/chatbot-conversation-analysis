
# 🤖 Chatbot Conversation Analysis Project

### A complete NLP and data analytics pipeline for understanding and improving chatbot performance.

---

## 📋 Overview
This project focuses on analyzing chatbot interactions to understand user behavior, satisfaction, and topic trends.  
It transforms raw SQL chat data into actionable insights through cleaning, visualization, clustering, sentiment analysis, and machine learning models.

The project was completed as part of a **Data Science internship**, following professional analysis and modeling workflows.

---

## 🧩 Key Objectives
- Explore and understand the chatbot database (ERD, profiling, schema documentation).
- Analyze user engagement and conversation trends.
- Identify and cluster conversation topics.
- Evaluate chatbot performance using sentiment and satisfaction scores.
- Build predictive models for sentiment and satisfaction analysis.
- Develop an interactive dashboard for visualization and reporting.

---

## 🏗️ Project Workflow

### 🔹 Phase 1 – Database Understanding
- Restored SQL dump into MySQL.
- Generated ERD and schema documentation.
- Performed data profiling (counts, nulls, data types).

### 🔹 Phase 2 – Data Analysis
- **Conversation trends:** Messages per day/week/type.
- **User engagement:** Most active users, response times.
- **Topic performance:** Word clouds, top keywords, satisfaction distribution.

### 🔹 Phase 3 – Advanced Insights
- **Sentiment Analysis:** Using `cardiffnlp/twitter-roberta-base-sentiment-latest`.
- **Topic Clustering:** K-Means clustering (k=5) with TF-IDF features.
- **Intent Recognition:** Logistic Regression & LinearSVC models (99%+ accuracy).
- **User Segmentation:** Clustered by engagement and satisfaction.

### 🔹 Phase 4 – Visualization & Dashboard
- Built an interactive **Streamlit dashboard** to visualize:
  - Sentiment distribution
  - Conversation trends
  - Topic performance
  - User segmentation
  - Forecasted chat volume

### 🔹 Phase 5 – Predictive Features
- **Chat Volume Forecasting:** Prophet model to predict next 30 days of messages.
- **Topic Recommendations:** Identified topics needing improvement based on satisfaction & sentiment.
- **Feedback Classifier:** Trained SVC model to predict user satisfaction with 96% accuracy.

---

## 📊 Key Results
| Model | Accuracy | Purpose |
|--------|-----------|----------|
| Sentiment Analysis | – | Classified messages as positive/neutral/negative |
| Topic Clustering | 5 clusters | Grouped related user intents |
| Intent Classifier | 99.5% | Recognized chatbot intents |
| Feedback Classifier (SVC) | **96.3%** | Predicted satisfaction from text |
| Chat Forecast (Prophet) | – | Predicted 30-day chat volume trend |

---

## 📈 Main Insights
- 87% of chatbot interactions are **neutral**, 8% **positive**, and 5% **negative**.
- High-traffic topics (Cluster 0) show **average satisfaction**, suggesting improvement opportunities.
- Weekly usage peaks on **Tuesdays** and **Sundays**.
- User segments identified:
  - **Active & Positive Users**
  - **Low-Engagement Users**
  - **Happy Users**
  - **Power Users**

---

## 🧰 Tech Stack
**Languages:** Python, SQL  
**Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn, transformers, Prophet, streamlit  
**Models:** Logistic Regression, LinearSVC, K-Means, Roberta Sentiment Model, Prophet  
**Visualization:** Streamlit, Plotly  
**Database:** MySQL  

---

## 🖥️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/KamelHawila/chatbot-conversation-analysis.git
   cd chatbot-conversation-analysis
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit dashboard:
   ```bash
   streamlit run dashboard_app.py
   ```

---

## 📂 Project Structure
```
chatbot-conversation-analysis/
│
├── cleaned_data/                     # Final cleaned datasets
│   ├── chats_clean.csv
│   ├── chats_final.csv
│   ├── chats_final_with_clusters.csv
│   ├── chats_sentiment.csv
│   ├── chats_with_satisfaction.csv
│   ├── topic_performance.csv
│   └── users_clean.csv
│
├── uncleaned_data/                   # Raw data & SQL dump
│   └── abidjanAI.dump
│
├── code/                             # Extracting data
│   └── data.ipynb
│
├── models/                           # Trained ML models
│   ├── intent_recognition_model_svc.pkl
│   ├── svc_feedback_classifier.pkl
│   ├── tfidf_vectorizer.pkl
│   └── feedback_tfidf.pkl
│
├── plots/                            # Visualizations & charts
│   ├── messages_per_day.png
│   ├── messages_per_week.png
│   ├── topic_recommendations.png
│   ├── user_segments.png
│   ├── chat_volume_forecast.png
│   └── sentiment_vs_satisfaction.png
|    └── ....
│
├── reports/                          # Documentation and profiling reports
│   ├── *_profile.html                # Data profiling reports for each table
│
├── analysis.ipynb                    # Phase 2 - Data Analysis
├── Chat_volume_Forecasting.ipynb     # Phase 5 - Forecasting
├── dashboard_app.py                  # Streamlit Dashboard
├── datacleaning.ipynb               # Phase 1 - Cleaning
├── Feedback_Classifier.ipynb         # Phase 5 - Feedback model
├── intent_app.py                     # Intent Prediction app
├── Intent_Recognition_model.ipynb    # Phase 3 - Intent recognition
├── merge_dataset.ipynb               # Utility notebook
├── response_analysis.ipynb           # Phase 2 - Conversation volume
├── Sentiment_analysis.ipynb          # Phase 3 - Sentiment analysis
├── Sentiment_analysis_model.ipynb    # Model building
├── Topic_Clustring.ipynb             # Phase 3 - Clustering
├── Topic_performance.ipynb           # Phase 3 - Topic analysis
├── Topic_recommendation.ipynb        # Phase 5 - Recommendations
├── User_segmentation.ipynb           # Phase 4 - User segmentation
├── requirements.txt                  # Project dependencies
└── README.md  # Final project documentation


---

## 🧠 Key Learning Outcomes
- Hands-on experience with NLP, clustering, forecasting, and classification.
- End-to-end project pipeline creation (from raw data to dashboard).
- Model deployment with Streamlit.
- Real-world chatbot analytics and recommendation logic.

---

## 🏁 Final Result
A **complete chatbot intelligence system** that:
- Understands user behavior.
- Measures and predicts satisfaction.
- Recommends improvements for better chatbot performance.
