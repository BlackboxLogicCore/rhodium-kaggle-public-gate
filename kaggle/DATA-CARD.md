# Rhodium Germany Benchmark Evidence SHA256

Historical transfer measurements, restoration fingerprints and explicit verification scope.

## Project description

Rhodium Germany develops the Rhodium Box for data optimization, verifiable reconstruction and controlled technical workflows. Published tests document specific results and their conditions. These records illustrate the applications that can be investigated today and the development directions that may follow.

The current GitHub register contains **63 entries: 62 documented test purposes and one profile summary**, with **22 additional measurement profiles** in its evidence JSON. The 25 best-of input records and 29 historical evidence entries overlap with this register. These figures must not be added as independent benchmark counts. Source register date: **2026-10-15**.

[Current test register](https://github.com/BlackboxLogicCore/rhodium-kaggle-public-gate/blob/main/benchmarks/RHODIUM-ALL-DISTINCT-TESTS.md) · [Measurement profiles](https://github.com/BlackboxLogicCore/rhodium-kaggle-public-gate/blob/main/public-evidence/2026-10-15-recovered-evidence.json)

This data card is maintained in GitHub. A change to this file alone does not update or verify the live Kaggle dataset. Dataset file availability must be checked separately.

## Overview

This dataset publishes Rhodium Germany's stored benchmark-result summaries for readers evaluating transfer volume and lossless reconstruction. It contains **25 best-of records grouped by distinct input SHA‑256** and a **29-entry register of historical benchmark, proof and validation families**. The groups overlap; they are not 54 independent benchmarks.

The intended use is to inspect dataset-specific cold/warm byte measurements, recompute displayed reduction percentages, and identify the reported original/restore and evidence-report fingerprints. It is a result collection, not a downloadable Rhodium engine or a claim of independent Kaggle certification.

## Customer relevance

Lower transferred byte counts may reduce bandwidth demand for a defined workload. Warm transfer results depend on retained receiver state. Actual elapsed-time and cost benefits must be measured in the intended environment; they are not established by a percentage alone.

For example, the stored 64 MiB local report records 67,108,864 B input, 33,869,410 B cold wire and 5,827 B warm wire, with matching source/restored SHA‑256 reported. Other datasets have substantially different cold reductions. Inspect all rows before drawing conclusions.

## Files

| File | Contents |
|---|---|
| RHODIUM-LOCAL-BEST-OF-ROUNDTRIPS-20261015.csv | 25 input-hash-distinct best-of rows, with cold/warm bytes, reductions and complete reported SHA‑256 |
| RHODIUM-PUBLIC-BENCHMARK-FAMILY.csv | 29 historical benchmark, proof and validation entries with source-reported statuses and claim limits |
| RHODIUM-PUBLIC-BENCHMARK-RESULTS-AND-SHA256.md | Readable presentation of the 25 best-of rows |

The published version inspected on 2026-10-15 has these three files. The current [data dictionary](https://github.com/BlackboxLogicCore/rhodium-kaggle-public-gate/blob/main/benchmarks/DATA-DICTIONARY.md) and [evidence-status guide](https://github.com/BlackboxLogicCore/rhodium-kaggle-public-gate/blob/main/EVIDENCE-STATUS.md) explain their interpretation.

## Fields and units

Byte columns are integer bytes. 1 MiB = 1,048,576 B; 1 GiB = 1,073,741,824 B.

- test_case: workload/source label.
- input_bytes: original size.
- best_cold_wire_bytes / best_warm_wire_bytes: selected historical minima at the underlying test's measurement point.
- cold_reduction_percent / warm_reduction_percent: 100 × (1 − wire_bytes / input_bytes), displayed to four decimal places.
- source_restore_sha256: reported matching original/restored SHA‑256.
- report_sha256: fingerprint of a referenced historical report.
- consistent_report_count: number of stored internally consistent reports for the input, not independent verifiers.
- integrity / validation_scope / claim_boundary: recorded integrity statement and the limits of the check.

The family table uses family, test_or_proof, input_or_scope, result, status and public_claim_boundary. Its status is the historical source outcome. Build tests, event filtering, throughput and transfer reduction are different measurements.

## Provenance and methodology

The tables were consolidated from existing Rhodium Germany reports. Best-of inputs are deduplicated by original SHA‑256, and available stored report fields were checked for consistency. Cold and warm minima may originate from different profiles; a row is not necessarily one combined run. The single report hash is not a complete per-profile provenance manifest.

These are historical results. This publication did not rerun Rhodium workloads or independently recompute every original/restored binary pair. Original payloads and confidential source reports are not part of the download. Source versions, acquisition references, hardware and timestamps are not uniform across the summary rows.

## Verification

Readers can recalculate reduction percentages and inspect hash formats directly from the CSV files. To independently confirm reconstruction, obtain the exact original input and returned artifact and recompute both hashes and lengths; use a byte-for-byte comparison when claiming bit identity.

The separate 2026-10-14 Kaggle-generated-input → local Rhodium roundtrip has a documented local PASS. Its independent returned-artifact verification on Kaggle remains **PENDING**. Hosting this dataset on Kaggle does not complete that check.

[Verification instructions](https://github.com/BlackboxLogicCore/rhodium-kaggle-public-gate/blob/main/PUBLIC-BENCHMARK-VERIFICATION.md)

## Limitations

- Warm results require prior receiver state and are not first-transfer compression ratios.
- Wire-byte boundaries are test-specific and do not automatically include every network/control overhead.
- Historical PASS, matching reported hashes and report fingerprints do not equal independent certification.
- Provider/brand names identify test context, not customer relationships or endorsements.
- No universal ratio, general one-byte transfer, complete eight-lever validation, or competition victory is established.
- Full Hutter/enwik9 competition results are outside this dataset's scope; the named 1 MiB research sample is not a competition result.

## Confidentiality

Only result summaries, fingerprints and claim boundaries are published. No proprietary Rhodium core, internal processing methods, credentials, private keys, customer inputs or confidential paths are included.

## Usage terms and updates

This documentation update grants no new general redistribution or software license. Existing terms and third-party rights remain unchanged. Underlying input datasets are not distributed here and must be obtained under their own applicable terms. Reuse and evaluation questions: [Rhodium Germany](https://rhodium-germany.de).

The existing license category is “Other (specified in description)”; it must not be read as an open license for the proprietary core or third-party source data. Documentation and evidence are updated when reviewed records or corrections are available; no fixed update schedule is promised.

Maintainer: **Rhodium Germany · Kai Kuhnert**.  
Canonical publication: [GitHub evidence repository](https://github.com/BlackboxLogicCore/rhodium-kaggle-public-gate).  
Documentation date: **2026-10-16**.
