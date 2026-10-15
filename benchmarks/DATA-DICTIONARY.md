# Data dictionary · Rhodium Germany Benchmark Evidence

Published values describe stored historical reports. All sizes ending in `_bytes` are integer bytes (B). 1 MiB = 1,048,576 B; 1 GiB = 1,073,741,824 B. Percentages are percentage points on a 0–100 scale, rounded as displayed.

## Best-of CSV: 25 distinct input hashes

File: [RHODIUM-LOCAL-BEST-OF-ROUNDTRIPS-20261015.csv](RHODIUM-LOCAL-BEST-OF-ROUNDTRIPS-20261015.csv)

| Column | Meaning |
|---|---|
| test_case | Historical workload or dataset label; provider/brand names do not establish a commercial relationship |
| input_bytes | Original input size in bytes |
| best_cold_wire_bytes | Lowest documented cold-profile transfer byte count selected for that input; test-specific measurement boundary |
| best_warm_wire_bytes | Lowest documented warm-profile transfer byte count selected for that input; prior receiver state is required |
| cold_reduction_percent | 100 × (1 − best_cold_wire_bytes / input_bytes), displayed to four decimal places |
| warm_reduction_percent | 100 × (1 − best_warm_wire_bytes / input_bytes), displayed to four decimal places |
| source_restore_sha256 | SHA‑256 reported equal for original and restored content in the recorded profiles; 64 hexadecimal characters |
| report_sha256 | SHA‑256 fingerprint of the referenced historical evidence report; not an additional payload hash or digital signature |
| consistent_report_count | Number of stored reports accepted as internally consistent for that input; not a count of independent verifiers |
| integrity | Stored integrity statement; ORIGINAL_EQUALS_RESTORE_SHA256_COLD_AND_WARM means the reports recorded equality |
| validation_scope | Scope of validation performed on the stored reports; HISTORICAL_LOCAL_REPORT_CONSISTENCY does not mean a new payload test |
| claim_boundary | Row-specific qualification on provenance, independence and byte-measurement scope |

Cold and warm minima can come from different historical profiles/reports. The single report hash is not a complete per-profile lineage manifest. Do not assume the row is one combined run or that the cold and warm bytes are interchangeable.

## Family CSV: 29 historical entries

File: [RHODIUM-PUBLIC-BENCHMARK-FAMILY.csv](RHODIUM-PUBLIC-BENCHMARK-FAMILY.csv)

| Column | Meaning |
|---|---|
| family | Broad category: data path, filtering, restoration, compatibility, etc.; source labels are preserved |
| test_or_proof | Historical test or proof name |
| input_or_scope | Input size, session, run identifier or scope as recorded |
| result | Source-reported measurement or validation summary, with units stated within the field |
| status | Source-reported outcome; historical PASS is not independent third-party certification |
| public_claim_boundary | Per-entry limit that must accompany interpretation of the result |

Byte reduction, filtered event counts, processing throughput and build checks must not be treated as the same metric. The corrected Evidence Gateway event reduction is 99.2632% from 250,000 → 1,842 events. That is not byte compression.

The “32-Point” entry is one validation family with 32 positions, not 32 independent performance benchmarks. Do not add the 25 best-of records to 29 family entries as independent executions.

## Roundtrip JSON

[2026-10-14-kaggle-rhodium-roundtrip.json](../public-evidence/2026-10-14-kaggle-rhodium-roundtrip.json) contains input/restore byte counts and hashes, wire bytes, local acceptance checks, and a separate `external_return_verification` field. That last field remains `PENDING`. The nested JSON is different from the legacy flat schema used by `verify_public_evidence.py`; use the [verification guide](../PUBLIC-BENCHMARK-VERIFICATION.md) for the published returned-file check.

## Use and provenance

The collection publishes Rhodium Germany's historical result summaries, numerical fields and report fingerprints. Original customer payloads, confidential source reports and proprietary software are not included. Source dataset version, download reference, license, hardware and run timestamps are not uniformly available in the summary rows. A provider label alone is not enough to reproduce that input.

No new general redistribution, software or source-dataset license is granted by this documentation update. Existing applicable terms and third-party rights remain unchanged. Do not infer permission to reuse NASA, Metrica, automotive, seismic or other source payloads from these result tables. Questions about reuse or a scoped evaluation can be directed to Rhodium Germany through [rhodium-germany.de](https://rhodium-germany.de).

The existing Kaggle listing uses “Other (specified in description)”. This is not a substitute for stated reuse terms. A later license change requires a separate rights decision; this update does not silently assign an open license to the evidence or proprietary core.

## Further reading

[Evidence status](../EVIDENCE-STATUS.md) · [Verification instructions](../PUBLIC-BENCHMARK-VERIFICATION.md) · [Customer overview](../README.md)
