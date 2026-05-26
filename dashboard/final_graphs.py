import pandas as pd
import matplotlib.pyplot as plt

unmitigated = pd.read_csv("experiment_engine/unmitigated_results.csv")
mitigated = pd.read_csv("experiment_engine/mitigated_results.csv")

unmitigated["condition"] = "Unmitigated"
mitigated["condition"] = "Mitigated"

df = pd.concat([unmitigated, mitigated], ignore_index=True)

df["run_number"] = df.groupby("condition").cumcount() + 1
df["success_value"] = df["status"].apply(lambda x: 100 if x == "PASSED" else 0)
df["failure_value"] = df["status"].apply(lambda x: 100 if x == "FAILED" else 0)

# 1. Unmitigated success over runs
plt.figure(figsize=(8, 4))
temp = df[df["condition"] == "Unmitigated"]
plt.plot(temp["run_number"], temp["success_value"], marker="o")
plt.title("Unmitigated Pipeline - Success Rate Over Runs")
plt.xlabel("Run Number")
plt.ylabel("Success Rate (%)")
plt.savefig("dashboard/graph1_unmitigated_success.png")
plt.close()

# 2. Unmitigated duration distribution
plt.figure(figsize=(8, 4))
plt.hist(temp["duration_seconds"], bins=10)
plt.title("Unmitigated Pipeline - Duration Distribution")
plt.xlabel("Duration Seconds")
plt.ylabel("Frequency")
plt.savefig("dashboard/graph2_unmitigated_duration.png")
plt.close()

# 3. Unmitigated failure over runs
plt.figure(figsize=(8, 4))
plt.plot(temp["run_number"], temp["failure_value"], marker="o")
plt.title("Unmitigated Pipeline - Failure Rate Over Runs")
plt.xlabel("Run Number")
plt.ylabel("Failure Rate (%)")
plt.savefig("dashboard/graph3_unmitigated_failure.png")
plt.close()

# 4. Mitigated success over runs
plt.figure(figsize=(8, 4))
temp = df[df["condition"] == "Mitigated"]
plt.plot(temp["run_number"], temp["success_value"], marker="o")
plt.title("Mitigated Pipeline - Success Rate Over Runs")
plt.xlabel("Run Number")
plt.ylabel("Success Rate (%)")
plt.savefig("dashboard/graph4_mitigated_success.png")
plt.close()

# 5. Mitigated duration distribution
plt.figure(figsize=(8, 4))
plt.hist(temp["duration_seconds"], bins=10)
plt.title("Mitigated Pipeline - Duration Distribution")
plt.xlabel("Duration Seconds")
plt.ylabel("Frequency")
plt.savefig("dashboard/graph5_mitigated_duration.png")
plt.close()

# 6. Mitigated failure over runs
plt.figure(figsize=(8, 4))
plt.plot(temp["run_number"], temp["failure_value"], marker="o")
plt.title("Mitigated Pipeline - Failure Rate Over Runs")
plt.xlabel("Run Number")
plt.ylabel("Failure Rate (%)")
plt.savefig("dashboard/graph6_mitigated_failure.png")
plt.close()

print("6 final graphs generated in dashboard folder.")