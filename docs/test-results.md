# TamperWatch test results

Version being tested: after introducing calculate_fingerprint().

| Test | Expected message | Expected exit code | Result |
|---|---|---|---|
| File matches baseline | UNCHANGED | 0 | Passed: UNCHANGED, exit 0 |
| File contents changed | CHANGED | 2 | Passed: CHANGED, exit 2 |
| Practice file missing | ERROR | 1 | Passed: ERROR, exit 1 |
| Baseline file missing | ERROR | 1 | Passed: ERROR, exit 1 |
| Run from the parent folder | UNCHANGED | 0 | Passed: UNCHANGED, exit 0 |