import streamlit as st
import pandas as pd
# ---- PAGE CONFIG ----
st.set_page_config(page_title="Chatbot Conversation Dashboard", page_icon="🤖", layout="wide")

# ---- HEADER ----
st.title("🤖 Chatbot Conversation Analysis Dashboard")
st.markdown("""
This dashboard presents a full overview of chatbot activity, sentiment, topics, and user behavior.  
It highlights trends, performance metrics, and insights derived from message and user data.
""")

st.markdown("---")

# ---- KPI SECTION ----
st.subheader("📈 Key Performance Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Users", "1,066")
col2.metric("Total Messages", "≈ 10,000")
col3.metric("Positive Sentiment", "87%")

st.markdown("---")

# ---- SECTION 1: CONVERSATION VOLUME ----
st.subheader("💬 Conversation Volume Trends")
col1, col2 = st.columns(2)
with col1:
    st.image("plots/messages_per_day.png", caption="Messages per Day", use_container_width=True)
with col2:
    st.image("plots/messages_per_week.png", caption="Messages per Week", use_container_width=True)

st.markdown("---")

# ---- SECTION 2: SENTIMENT ANALYSIS ----
st.subheader("😊 Sentiment Analysis")
col1, col2 = st.columns(2)
with col1:
    st.image("plots/Bar_plot.png", caption="Sentiment Distribution", use_container_width=True)
with col2:
    st.image("plots/Pie_chart.png", caption="Sentiment Breakdown", use_container_width=True)

st.markdown("---")

# ---- SECTION 3: TOPICS & INTENTS ----
st.subheader("🧠 Topic & Intent Insights")
st.image("plots/topic.png", caption="Most Frequent Topics in User Questions", use_container_width=True)

st.markdown("---")

# ---- SECTION 4: USER SEGMENTATION ----
st.subheader("👥 User Segmentation")
st.image("plots/user_segments.png", caption="User Segments by Satisfaction & Activity", use_container_width=True)

st.markdown("---")

# ---- SECTION 5: FORECASTING CHAT VOLUME ----
st.subheader("📅 Chat Volume Forecast")
st.image("plots/chat_volume_forecast.png", caption="Predicted Message Volume - Next 30 Days", use_container_width=True)
st.image("plots/trend-weekly-daily.png", caption="Trend and Seasonality Components", use_container_width=True)
st.markdown("---")

# ---- SECTION 6: TOPIC Recommendations ----
topic_perf = pd.read_csv("cleaned_data/topic_performance.csv")
st.subheader("💡 Topic Recommendations")
st.image("plots/topic_recommendations.png", caption="Topic Performance: Sentiment vs Satisfaction", use_container_width=True)
st.dataframe(
    topic_perf.style.highlight_max(subset=["message_count"], color="#a5d6a7")
              .highlight_min(subset=["avg_satisfaction"], color="#ef9a9a")
              .format({"avg_sentiment": "{:.2f}", "avg_satisfaction": "{:.2f}"})
)
st.markdown("---")

# ---- FOOTER ----
st.markdown("""
### 🧾 Summary of Findings
- Most conversations are text-based and occur during specific high-activity periods.
- Sentiment distribution shows **neutral** dominance with smaller positive and negative shares.
- Topic analysis highlights frequent use of terms like *image, result, analysis, lebanon*.
- User segmentation identifies:
  - 🟢 Active & Positive Users (majority)
  - 🟣 Happy Users with high satisfaction
  - 🟠 Low-Engagement Users with low activity
  - 🔴 Power Users (very high activity)
""")

st.caption("Built by **Kamel Hawila** — Project 2025 🚀")
