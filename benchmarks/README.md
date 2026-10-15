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

## Recovered dated source report — 2026-10-15

The previously listed 64 MiB Blackbox family now has a public-safe evidence-recovery note: [Recovered local roundtrip and inventory limits](RECOVERED-LOCAL-ROUNDTRIP-2026-10-15.md). This report is a local synthetic loopback measurement, with cold and warm SHA-256 equality **reported by the saved source document**; it is **not** new WAN evidence, independent verification, or a new benchmark family. A historical inventory of candidate files and extracted metrics does not substantiate a claimed count of 100,000+ independent tests.
