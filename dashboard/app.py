import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("CI Experiment Dashboard")

df = pd.read_csv("experiment_engine/results.csv")

st.subheader("Experiment Results")
st.dataframe(df)

total_runs = len(df)
passed_runs = len(df[df["status"] == "PASSED"])
failed_runs = len(df[df["status"] == "FAILED"])

success_rate = round((passed_runs / total_runs) * 100, 2)
failure_rate = round((failed_runs / total_runs) * 100, 2)

st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Runs", total_runs)
col2.metric("Success Rate", f"{success_rate}%")
col3.metric("Failure Rate", f"{failure_rate}%")

st.subheader("Pipeline Success vs Failure")

status_counts = df["status"].value_counts()

fig1, ax1 = plt.subplots()
ax1.bar(status_counts.index, status_counts.values)
ax1.set_xlabel("Status")
ax1.set_ylabel("Count")
ax1.set_title("Pipeline Success vs Failure")
st.pyplot(fig1)

st.subheader("Average Duration by Test Type")

avg_duration = df.groupby("test_type")["duration_seconds"].mean()

fig2, ax2 = plt.subplots()
ax2.bar(avg_duration.index, avg_duration.values)
ax2.set_xlabel("Test Type")
ax2.set_ylabel("Average Duration Seconds")
ax2.set_title("Reliable vs Flaky Test Duration")
st.pyplot(fig2)

st.subheader("Duration Across Runs")

fig3, ax3 = plt.subplots()
ax3.plot(df["duration_seconds"])
ax3.set_xlabel("Run Number")
ax3.set_ylabel("Duration Seconds")
ax3.set_title("Pipeline Duration Trend")
st.pyplot(fig3)

st.subheader("Success Rate by Test Type")

success_by_type = (
    df.groupby("test_type")["status"]
    .apply(lambda x: (x == "PASSED").mean() * 100)
)

fig4, ax4 = plt.subplots()
ax4.bar(success_by_type.index, success_by_type.values)
ax4.set_xlabel("Test Type")
ax4.set_ylabel("Success Rate %")
ax4.set_title("Success Rate by Test Type")
st.pyplot(fig4)