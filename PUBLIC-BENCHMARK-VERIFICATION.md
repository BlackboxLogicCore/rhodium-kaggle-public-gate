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
| Evidence Gateway | 250,000 -> 1,842 events = **99.2632%** reduction | PENDING_EVIDENCE; older 99.4021% claim superseded |
| Metrica Sports cold | 65.58% reduction | PENDING_EVIDENCE |
| Metrica Sports warm | 98.54% reduction | PENDING_EVIDENCE |
| Blackbox 64 MiB cold | 49.5306% reduction | PENDING_EVIDENCE |
| Blackbox 64 MiB warm | 99.9913% reduction | PENDING_EVIDENCE |
| WAN true-cold | 6,950 wire bytes | PENDING_EVIDENCE |
| 100 GiB scale/recovery | 107,374,182,400 -> 14,476,957,280 bytes (~86.52% reduction), two reported restore checks | PENDING_EVIDENCE |

## GitHub / Kaggle publication gate

Publish sanitized evidence files and verifier instructions on GitHub first. Publish or update a Kaggle dataset/notebook only after checking dataset licensing, private-data removal, and repeatability. State clearly whether each validation occurred locally, on Kaggle, or independently. External evaluators can use a black-box interface or a sealed executable under agreed conditions; the private core is not required for publication.

## Additional public audit references (not competition certifications)

Historical Rhodium Connector Audit (2026-10-06) records the following GitHub Actions links. A successful workflow run alone does not establish independent third-party verification or competition acceptance. Full logs, licensing and verifiers require separate inspection before promotion to EXTERNALLY_VERIFIED.

- Hutter enwik9, run [36989217616](https://github.com/BlackboxLogicCore/rhodium-benchmarks/actions/runs/36989217616): source 1,000,000,000 bytes; archive 356,916,775 bytes; wrapper 2,048 bytes; reported combined 356,918,823 bytes; source/restore SHA-1 match; reported PASS_BIT_EXACT. The audit explicitly says `RHODIUM_STRICT_SELF_CONTAINED_P0_CERTIFIED=NO`. **Do not claim Hutter Prize win or certification**.
- Fingerprint one-file probe, run [36993722643](https://github.com/BlackboxLogicCore/rhodium-benchmarks/actions/runs/36993722643): source 1,048,576 bytes; fingerprint 7,151 bytes; SHA-256 match; reported bit-identical restore; restore ~62 ms.
- ULTIMO5 Ubuntu proof, run [36962456220](https://github.com/BlackboxLogicCore/rhodium-benchmarks/actions/runs/36962456220): reported PASS for eBPF/XDP canary, compile/load, SHA-NI availability, zero-copy selftest and lock-free atomic selftest. These are infrastructure tests, **not lossless-compression ratios**.

### Metric correction

An older Evidence Gateway claim used 99.4021%. The source counts 250,000 and 1,842 imply (250000-1842)/250000 * 100 = **99.2632%**, which supersedes that older figure. The numerator is an event-count reduction; do not present it as a byte compression rate.

### Additional claim boundary

The historical 64 MiB Cloudflare *live-source* figures are **not** a controlled direct comparison against Cloudflare's product or a generic ISP speed test. Cold/warm results depend on reuse, cache conditions, source characteristics and test methodology. Externally reproduced evidence remains separate from historical reports.
