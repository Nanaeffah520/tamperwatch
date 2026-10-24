# TamperWatch

A Python security tool that checks whether a practice file has changed
by comparing its SHA-256 fingerprint with a saved baseline.

## What it does

- Reports when a file matches its baseline.
- Detects when the file's contents differ from the baseline.
- Reports a missing practice file or baseline.
- Returns exit codes that other programs can interpret.
- Finds its files even when launched from another folder.

## Project scope

This is a local learning project using a fictional configuration file.
It checks the file when the program is run.

A change alert means the contents differ from the saved reference.
It does not establish who changed the file or whether the change
was malicious.
## Requirements

- Python 3.
- No additional Python packages are required.
- The practice file: lab/demo_config.txt.
- The reference fingerprint: baseline.sha256.

## Run the checker

Open a terminal in the tamperwatch project folder and run:

```powershell
python watch_file.py
```

In PowerShell, inspect the exit code immediately afterwards:

```powershell
$LASTEXITCODE
```

## Exit codes

| Code | Meaning |
|---|---|
| 0 | The file matches the baseline |
| 1 | A required file is missing, so the check cannot complete |
| 2 | The file differs from the baseline |

## Manual testing

The following cases have been tested:

- File matches the baseline.
- File contents have changed.
- Practice file is missing.
- Baseline file is missing.
- Program is launched from the parent folder.

See [the test results](docs/test-results.md) for the recorded outcomes.
## Limitations

- Checks one configured file each time the program runs.
- Does not continuously monitor the file.
- Detects differences but does not prevent changes.
- Trusts the saved baseline. Someone who can replace both the file
  and its baseline could make an altered file pass the check.
- Reads the entire file into memory, so this version is intended
  for small practice files.
- Handles missing-file errors, but other reading errors may still
  produce a Python traceback.
- Does not yet validate the baseline's format.

## Planned improvements

- Validate the baseline before comparing fingerprints.
- Handle file-access permission errors clearly.
- Add automated tests.