# Rhodium Germany · Public Benchmark Index

**Published results, clear evidence status, full reported fingerprints.** Documentation updated 2026-10-15.

[Customer overview (DE/EN)](../README.md) · [Evidence status](../EVIDENCE-STATUS.md) · [Verification guide](../PUBLIC-BENCHMARK-VERIFICATION.md) · [Kaggle](https://www.kaggle.com/datasets/kaikuhnert/rhodium-germany-public-benchmark-evidence)

## Choose a view

| File | Contents | Best use |
|---|---|---|
| [Results and SHA‑256](RHODIUM-PUBLIC-BENCHMARK-RESULTS-AND-SHA256.md) | Readable table of 25 local best-of records | Inspect measured bytes and complete reported hashes |
| [Best-of CSV](RHODIUM-LOCAL-BEST-OF-ROUNDTRIPS-20261015.csv) | 25 records grouped by distinct original input SHA‑256 | Calculate and compare dataset-specific cold/warm values |
| [Family CSV](RHODIUM-PUBLIC-BENCHMARK-FAMILY.csv) | 29 historical benchmark, proof and validation entries | Inspect the wider documented evidence scope |
| [Data dictionary](DATA-DICTIONARY.md) | Every CSV field, units, counting rules and provenance | Interpret the data correctly |

## Counts and selection

The family register originally contained 27 entries and was extended with the local Rhodium/MSP360 comparison and NASA C-MAPSS FD001 pipeline result: **29 current entries**. An entry may describe a build check, proof or workload; it is not automatically a distinct performance benchmark.

The best-of table contains **25 distinct input SHA‑256 values**, selected from internally consistent stored local cold/warm reports. Cold and warm best values are profile-specific historical minima; do not assume they form one newly executed combined run. A single report fingerprint per row does not by itself establish the full lineage of both minima. Repeated inputs are grouped; the 25 records overlap with family entries and are not added to 29 as independent tests.

## Consistent status interpretation

The family CSV's `status` column preserves the **source-reported outcome**, including historical PASS labels. The best-of CSV's `validation_scope` states the consistency-check scope. **Neither field is an independent certification.** [EVIDENCE-STATUS.md](../EVIDENCE-STATUS.md) defines the publication-level interpretation for both collections.

The Kaggle-generated-input roundtrip is locally documented as PASS. The independent returned-file hash/size check on Kaggle is PENDING. Publishing these tables on Kaggle is a separate activity from executing that check.

## Scope and confidentiality

Cold and warm transfer values must be read with their receiver state and test-specific byte-measurement boundary. Byte reduction, event filtering, processing throughput and upstream compatibility are different quantities. Named providers are not endorsing or certifying Rhodium.

Full Hutter/enwik9 competition results are outside the scope of this benchmark collection. The 1 MiB row labelled “Research enwik9 local sample” is a historical sample measurement, not a full enwik9 competition submission or award.

The source tables and fingerprints are preserved. No new Rhodium workload run was performed for this documentation update. Private implementation, customer payloads, credentials, confidential paths and manifests remain excluded.
