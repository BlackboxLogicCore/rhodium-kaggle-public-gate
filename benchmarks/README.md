# Rhodium Germany — Public-Safe Benchmark Family

This directory consolidates the currently documented benchmark, proof, validation, compatibility and restore families into one public-safe index.

## Publication boundary

Published: measured results, run identifiers where already public-safe, data sizes, reductions, PASS/P0/restore/integrity status, and explicit claim limits.

Not published: Rhodium core implementation, Matrix/reconstruction logic, private keys, credentials, internal control paths, Mama/Worker/Research implementation, proprietary weighting, internal self-improvement logic, or private manifests.

The CSV intentionally distinguishes performance measurements from validation/build/compatibility checks. A validation family is not inflated into multiple independent benchmarks.

## Current consolidated index

See `RHODIUM-PUBLIC-BENCHMARK-FAMILY.csv`.

The index currently contains 27 documented public-safe entries/families recovered from the Rhodium evidence history and benchmark materials. It includes historical data-path benchmarks, proof families, recognition runs, upstream compatibility checks, sport/seismic/restore/WAN evidence, Blackbox/Golden runs, and the 2026-10-14 Kaggle-generated-input local roundtrip.

### Kaggle boundary

The 2026-10-14 Kaggle-generated-input -> Rhodium local roundtrip is PASS locally. The independent Kaggle hash/size verification of the returned restored artifact remains PENDING and is therefore not represented as an external Kaggle PASS.

### Exclusion

enwik9/Hutter is deliberately excluded from this public benchmark family. Internal implementation details and unverified historical claims are also excluded.

This is a public evidence index, not a claim of certification or endorsement by NASA, Kaggle, Cloudflare, Google, Meta, Microsoft, EarthScope, USGS, Metrica Sports, or any other named upstream/data provider.

## Evidence inventory reconciliation — 2026-10-15

The current public index contains **27 documented benchmark/proof/validation entries**, not 27 independently certified benchmark results. Historic PASS labels are retained as Rhodium-recorded outcomes and must be read together with each row's claim boundary.

A separate internal evidence inventory reports **2,733 indexed reports (2,719 unique files)**; a consolidated JSON register lists **2,369 evidence files in 216 automatically classified test groups**. These are inventory counts, **not** proof that all files/groups passed, and **not** 216 independent benchmark victories. No new experimental runs were required to reconcile these counts.

Publication rule: report input size, on-wire bytes, restored size and matching SHA-256 only where supported by the original evidence. Published on-wire figures must clearly state their measurement boundary; overhead not separately evidenced must not be assumed included or excluded. Previous outcomes are not a substitute for missing end-to-end payload evidence.

Current external verification distinction: the Kaggle-generated-input local roundtrip remains `PASS_LOCAL_ROUNDTRIP`; independent Kaggle return validation remains `PENDING`. Neither upstream compatibility checks nor internal self-inspection constitute independent performance certification.

Protected implementation, proprietary processing and reconstruction methods, internal agent/control architecture and private artifacts remain excluded from this public repository.
