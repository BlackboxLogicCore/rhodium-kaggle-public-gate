# Rhodium Germany – Kaggle Public Verification Gate

Purpose:
Public-safe verification surface for externally reproducible benchmark checks.

SECURITY BOUNDARY:
This repository does NOT contain the Rhodium core, Matrix implementation,
reconstruction logic, private keys, credentials, internal control paths,
Mama/Worker/Research runtime or private manifests.

## Verified evidence currently published

### 2026-10-14 — Kaggle-generated input -> Rhodium local roundtrip

Status: **PASS_LOCAL_ROUNDTRIP**

- Input: 698,914 bytes
- Input SHA-256: `2C6C60142C3FD99BF25B324994D6EDD837CA6DA7326213253399BF99AC5C46BA`
- Wire sent: 381,517 bytes
- Transfer reduction: 45.412883416271534%
- Restored: 698,914 bytes
- Restored SHA-256: identical to input
- Bit-identical restore: PASS
- P=0: PASS
- Fresh cache: PASS
- Blocks reused: 0
- Receiver acknowledgement: PASS

Machine-readable evidence:
`public-evidence/2026-10-14-kaggle-rhodium-roundtrip.json`

Public verifier:
`verify_return.py`

### Claim boundary

The local Rhodium roundtrip above is complete and evidenced.
The independent Kaggle check of the returned artifact is still **PENDING**.
Therefore this repository does **not** claim that Kaggle has certified,
validated, or independently completed the Rhodium roundtrip.

A complete external return verification requires:
external input -> Rhodium processing -> restored artifact -> independent
SHA-256/size comparison of that returned artifact.

Only verified measurements are published here. No private Rhodium core
implementation is included.

### 2026-10-15 — Benchmark evidence register update

The [public-safe benchmark index](benchmarks/RHODIUM-PUBLIC-BENCHMARK-FAMILY.csv) currently contains **27 documented entries** spanning measured data-path results, integrity/restore proofs, validation checks and upstream compatibility. These categories are kept separate; a PASS in a build or self-inspection check is not a new end-to-end compression benchmark.

Existing internal registers inventory 2,733 reports (2,719 unique files), and a consolidated JSON evidence register covers 2,369 files arranged into 216 automatically classified groups. These counts are provided for traceability only: they do not assert 216 independently passed tests, and the inventories were not independently audited by GitHub or Kaggle.

No additional benchmark execution is claimed in this update. Existing per-test SHA-256, original/restore sizes and on-wire measurements retain their specific test and measurement boundaries. The Kaggle-generated-input local roundtrip remains verified locally, with independent Kaggle validation **PENDING**.

The proprietary core and internal agent, validation and reconstruction mechanisms remain outside this repository.
