# Rhodium Germany — Evidence inventory status (2026-10-15)

This document is a **public-safe inventory progress report**, not a new benchmark run, external certification, or complete validation of the Rhodium platform.

## Newly located historical material

A read-only inventory of existing local records identified:

| Source inventory | Recorded observation | Meaning |
|---|---:|---|
| Earlier two-drive inventory (2026-10-08) | 8,427 candidate evidence files | Candidates, **not** individual validated tests |
| Earlier inventory | 7,788 extracted metric occurrences | Metrics, **not** independent test executions |
| Mama evidence index (2026-10-15) | 2,733 report entries; 2,719 unique files | File-level index |
| Initial consolidated index | 2,369 unique JSON file hashes | Limited source directories only |
| Follow-up grouping | 216 groups | Evidence grouping, **not** verified benchmark families |

The latest limited-scope audit rehashed all 2,369 indexed JSON files successfully. Of those files, 103 were recognized as cold/warm roundtrip reports: **91 reports had internally consistent PASS, byte-count, and source/restored SHA-256 fields**, while **12 required further review** because fields were inconsistent or incomplete. This is a check of the **stored reports**, not a fresh independent comparison of original and restored binary payloads.

One separately identified research unit-test record reports **4 of 4 tests passed**. It does **not** establish a one-byte benchmark.

Additional reported PASS statuses remain **unverified** until their source-specific evidence, exact workload, restoration data, and test scope are checked. Earlier archives have been located but have not yet been fully incorporated or counted by distinct execution ID.

## Permitted claims at this stage

- Rhodium Germany has historical internal test reports that document lossless cold/warm reconstruction and matching source/restored hashes **within the reported local test scope**.
- Some stored reports have been cross-checked for internal field consistency.
- The evidence inventory is incomplete; counts of files, metrics, groups, and executions must not be conflated.

## Claims NOT established by this inventory

- More than 100,000 independently verified executions.
- Independent third-party certification of all recorded results.
- Full end-to-end validation of all eight internal levers.
- A general one-byte transport result.
- WAN or external Kaggle verification from these local inventory figures.

## Security and publication boundary

This report intentionally excludes source code, implementation details, internal algorithms, local file paths, credentials, secret fingerprints, keys, and private manifests. No original evidence has been uploaded here. The existing public Kaggle roundtrip report in this repository remains separate and retains its original claim boundaries.

Next action: reconcile older archive indexes, count unique execution IDs, verify input/restored payloads when accessible, and publish only sanitized, reproducible results after review.
