# Rhodium Germany — Public-Safe Benchmark Family

This directory consolidates the currently documented benchmark, proof, validation, compatibility and restore families into one public-safe index.

## Publication boundary

Published: measured results, run identifiers where already public-safe, data sizes, reductions, PASS/P0/restore/integrity status, and explicit claim limits.

Not published: Rhodium core implementation, Matrix/reconstruction logic, private keys, credentials, internal control paths, Mama/Worker/Research implementation, proprietary weighting, internal self-improvement logic, or private manifests.

The CSV intentionally distinguishes performance measurements from validation/build/compatibility checks. A validation family is not inflated into multiple independent benchmarks.

## Current consolidated index

See `RHODIUM-PUBLIC-BENCHMARK-FAMILY.csv`.

The original index documents 27 public-safe benchmark, proof and validation entries recovered from earlier Rhodium evidence. A complementary best-of CSV now adds 25 SHA-distinct local dataset records from the pre-existing research evidence register. It includes historical data-path benchmarks, proof families, recognition runs, upstream compatibility checks, sport/seismic/restore/WAN evidence, Blackbox/Golden runs, and the 2026-10-14 Kaggle-generated-input local roundtrip.

### Kaggle boundary

The 2026-10-14 Kaggle-generated-input -> Rhodium local roundtrip is PASS locally. The independent Kaggle hash/size verification of the returned restored artifact remains PENDING and is therefore not represented as an external Kaggle PASS.

### Exclusion

enwik9/Hutter is deliberately excluded from this public benchmark family. Internal implementation details and unverified historical claims are also excluded.

This is a public evidence index, not a claim of certification or endorsement by NASA, Kaggle, Cloudflare, Google, Meta, Microsoft, EarthScope, USGS, Metrica Sports, or any other named upstream/data provider.

## Best recorded successful local roundtrips

See [`RHODIUM-LOCAL-BEST-OF-ROUNDTRIPS-20261015.csv`](RHODIUM-LOCAL-BEST-OF-ROUNDTRIPS-20261015.csv).

- 25 distinct input SHA-256 values are represented, each with the strongest documented cold/warm transfer values from the internally consistent available local reports.
- Original and restored SHA-256 values are equal in the recorded cold and warm profiles; the evidence-table records that result as a historical local report, not as newly repeated third-party validation.
- Repetitions are grouped by original input SHA-256; one best row per distinct input. This CSV contains individual datasets and must not be added directly to the 29-entry family-level count as independently new benchmark families.
- No new benchmark was executed to prepare this index. Internal methods, processes, agents and reconstruction details are not included.

2026-10-15 historical Desktop reconciliation: the public family index was extended with the sealed Rhodium/MSP360 local cold/delta comparison and the NASA C-MAPSS FD001 local processing result. These are two documented historical successes, not rerun measurements or vendor certifications; underlying benchmark/test conditions and limits appear in the CSV.
