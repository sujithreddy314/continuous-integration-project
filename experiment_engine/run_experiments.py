import csv
import subprocess
import time
import uuid
from datetime import datetime


CSV_FILE = "experiment_engine/results.csv"


def run_test(test_path, pipeline_type, test_type):
    run_id = str(uuid.uuid4())[:8]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    start_time = time.time()

    result = subprocess.run(
        ["pytest", test_path],
        capture_output=True,
        text=True
    )

    end_time = time.time()

    duration = round(end_time - start_time, 2)
    status = "PASSED" if result.returncode == 0 else "FAILED"

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            run_id,
            timestamp,
            pipeline_type,
            test_type,
            status,
            duration
        ])

    print(
        f"Run ID: {run_id} | "
        f"Pipeline: {pipeline_type} | "
        f"Test: {test_type} | "
        f"Status: {status} | "
        f"Duration: {duration}s"
    )


if __name__ == "__main__":
    for i in range(50):
        run_test("tests/reliable", "simple", "reliable")
        run_test("tests/unreliable", "complex", "flaky")