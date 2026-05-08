import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Page title
st.title("CI Experiment Dashboard")

# Load CSV
df = pd.read_csv("experiment_engine/results.csv")

# Show raw data
st.subheader("Experiment Results")
st.dataframe(df)

# -------------------------------
# Success vs Failure Count
# -------------------------------

st.subheader("Pipeline Success vs Failure")

status_counts = df["status"].value_counts()

fig1, ax1 = plt.subplots()

ax1.bar(
    status_counts.index,
    status_counts.values
)

ax1.set_xlabel("Status")
ax1.set_ylabel("Count")
ax1.set_title("Pipeline Success vs Failure")

st.pyplot(fig1)

# -------------------------------
# Average Duration by Test Type
# -------------------------------

st.subheader("Average Duration by Test Type")

avg_duration = (
    df.groupby("test_type")["duration_seconds"]
    .mean()
)

fig2, ax2 = plt.subplots()

ax2.bar(
    avg_duration.index,
    avg_duration.values
)

ax2.set_xlabel("Test Type")
ax2.set_ylabel("Average Duration")
ax2.set_title("Average Pipeline Duration")

st.pyplot(fig2)

# -------------------------------
# Duration Distribution
# -------------------------------

st.subheader("Pipeline Duration Distribution")

fig3, ax3 = plt.subplots()

ax3.plot(df["duration_seconds"])

ax3.set_xlabel("Run Number")
ax3.set_ylabel("Duration")
ax3.set_title("Pipeline Duration Across Runs")

st.pyplot(fig3)