import csv
import subprocess
import time
import uuid


def run_test(test_path, pipeline_type, test_type):

    run_id = str(uuid.uuid4())[:8]

    start_time = time.time()

    result = subprocess.run(
        ["pytest", test_path],
        capture_output=True,
        text=True
    )

    end_time = time.time()

    duration = round(end_time - start_time, 2)

    status = "PASSED" if result.returncode == 0 else "FAILED"

    with open("experiment_engine/results.csv", "a") as file:

        writer = csv.writer(file)

        writer.writerow([
            run_id,
            pipeline_type,
            test_type,
            status,
            duration
        ])

    print(f"""
Run ID: {run_id}
Pipeline: {pipeline_type}
Test Type: {test_type}
Status: {status}
Duration: {duration}s
""")


if __name__ == "__main__":

    for i in range(10):

        run_test(
            "tests/reliable",
            "simple",
            "reliable"
        )

        run_test(
            "tests/unreliable",
            "complex",
            "flaky"
        )