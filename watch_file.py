from pathlib import Path
import sys
import hashlib


def calculate_fingerprint(file_path):
    contents = file_path.read_bytes()
    return hashlib.sha256(contents).hexdigest()


project_folder = Path(__file__).resolve().parent

sample_file = project_folder / "lab" / "demo_config.txt"
try:
    fingerprint = calculate_fingerprint(sample_file)
except FileNotFoundError:
    print("ERROR: lab/demo_config.txt is missing. Cannot check the file.")
    sys.exit(1)

print(f"SHA-256: {fingerprint}")


baseline_file = project_folder / "baseline.sha256"

try:
    expected_fingerprint = baseline_file.read_text(encoding="utf-8").strip()
except FileNotFoundError:
    print("ERROR: baseline.sha256 is missing. Cannot check the file.")
    sys.exit(1)
else:
    if fingerprint == expected_fingerprint:
        print("UNCHANGED: the file matches our reference.")
    else:
        print("CHANGED: the file differs from our reference.")
        sys.exit(2)
