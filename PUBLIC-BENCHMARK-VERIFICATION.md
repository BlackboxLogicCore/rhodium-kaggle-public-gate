# Public benchmark disclosure and verification policy

## Strict confidentiality boundary

The Rhodium internal core, Matrix algorithms, weighting, routing, reconstruction implementation, private manifests, credentials, keys, and Mama/Worker/Research control paths must never be published. Do not publish executable internal components, private file paths, or data identifying customers.

## What a publicly verifiable benchmark requires

Each claimed PASS needs:
1. Publicly identified input dataset/version, license and acquisition reference (or publicly downloadable test vector).
2. Exact uncompressed input bytes, transmission bytes, restored bytes, and clearly defined metric denominator.
3. SHA-256 digest of the original input and independently obtained restored output, with equality checked.
4. Run ID, UTC timestamp, hardware/OS profile, cold/warm cache state and baseline comparator when claiming advantage.
5. Raw machine-readable result log, verifier version and instructions for running an independent verification.
6. Independent external verification status separately from local PASS. P=0 is an internal acceptance policy, not proof of zero technical risk.

If any requirement is missing, label the measurement HISTORICAL_REPORTED or PENDING_EVIDENCE rather than EXTERNALLY_VERIFIED. Never infer an independent Kaggle certification from a local run.

## Existing currently documented test

See `README.md` and `public-evidence/2026-10-14-kaggle-rhodium-roundtrip.json` for the 2026-10-14 local roundtrip. Independent Kaggle verification remains PENDING until evidence is added.

## Historical benchmark claims awaiting source artifacts

The following figures were previously reported in Rhodium project records. They are **not independently verified by this index**. Do not relabel these rows PASS or publish them as externally validated without primary evidence and a reproducible verifier.

| Benchmark | Reported result | Public proof status |
|---|---:|---|
| NASA JUNO WAVES | 85.54% reduction | PENDING_EVIDENCE |
| Matrix cold | 81.25% reduction | PENDING_EVIDENCE |
| Matrix warm | 99.9916% reduction | PENDING_EVIDENCE |
| Matrix delta | 99.9541% reduction | PENDING_EVIDENCE |
| Evidence Gateway | 99.4021% event reduction | PENDING_EVIDENCE |
| Metrica Sports cold | 65.58% reduction | PENDING_EVIDENCE |
| Metrica Sports warm | 98.54% reduction | PENDING_EVIDENCE |
| Blackbox 64 MiB cold | 49.5306% reduction | PENDING_EVIDENCE |
| Blackbox 64 MiB warm | 99.9913% reduction | PENDING_EVIDENCE |
| WAN true-cold | 6,950 wire bytes | PENDING_EVIDENCE |

## GitHub / Kaggle publication gate

Publish sanitized evidence files and verifier instructions on GitHub first. Publish or update a Kaggle dataset/notebook only after checking dataset licensing, private-data removal, and repeatability. State clearly whether each validation occurred locally, on Kaggle, or independently. External evaluators can use a black-box interface or a sealed executable under agreed conditions; the private core is not required for publication.
