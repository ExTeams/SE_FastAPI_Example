import subprocess
import sys

def run_tests():
    print("Starting FastAPI application...")
    subprocess.Popen(["uvicorn", "main:app", "--reload"])

    print("Running tests...")
    subprocess.run(["pytest", "test.py"])

if __name__ == "__main__":
    run_tests()
