# Public evidence verification · Rhodium Germany

[Customer overview](README.md) · [Evidence status](EVIDENCE-STATUS.md) · [Results](benchmarks/RHODIUM-PUBLIC-BENCHMARK-RESULTS-AND-SHA256.md) · [Data dictionary](benchmarks/DATA-DICTIONARY.md)

## What is already documented

The publication contains 25 SHA-distinct local best-of records, a 29-entry historical family register, and a machine-readable local roundtrip report. Historical source PASS outcomes are preserved. They must be read with the publication scope in [EVIDENCE-STATUS.md](EVIDENCE-STATUS.md).

The best-of reports were checked for internal field consistency. The family register consolidates historical outcomes with different source coverage. **A pending external check does not invalidate a reported local PASS, and a local PASS does not complete an independent check.**

## Three checks a reader can perform

### 1. Check the published measurements

Download the [best-of CSV](benchmarks/RHODIUM-LOCAL-BEST-OF-ROUNDTRIPS-20261015.csv). For each row, calculate:

`reduction_percent = 100 * (input_bytes - wire_bytes) / input_bytes`

Use cold and warm wire bytes separately. Compare with the displayed four-decimal percentage, allowing the rounding precision shown. Input bytes, transferred bytes and restored bytes must refer to the same workload and stated measurement boundaries.

This verifies the arithmetic in the publication. It does not execute Rhodium, validate the original workload, or establish elapsed-time or cost savings.

### 2. Check an actual returned artifact

The [2026-10-14 JSON](public-evidence/2026-10-14-kaggle-rhodium-roundtrip.json) records a 698,914-byte input and restore with SHA‑256:

`2C6C60142C3FD99BF25B324994D6EDD837CA6DA7326213253399BF99AC5C46BA`

If you have the actual returned file, download [verify_return.py](verify_return.py) and run it with Python 3:

```console
python verify_return.py RHODIUM-KAGGLE-ROUNDTRIP.csv
```

Exit code 0 means the supplied file's length and computed SHA‑256 match the published reference; exit code 1 means they do not. The helper's output field `bit_identical` denotes this size/hash check, not a direct byte-by-byte comparison with a second original file. The returned artifact itself is not included in this repository. The command cannot be completed from the evidence JSON alone.

For a direct bit-identity claim, independently obtain both original and restored binary files and compare all bytes as well as their length and hashes. Record who performed the check, when, and exactly which files were compared.

The independent returned-artifact check **on Kaggle remains PENDING**. Publishing the historical CSVs on Kaggle is not completion of this check.

### 3. Check report provenance

`report_sha256` fingerprints a historical report. To recompute it, the verifier needs the exact original report bytes; summaries cannot reconstruct those bytes. Raw confidential source reports are not automatically available in the public tables. The best-of cold/warm selections may come from different profiles and the single report fingerprint is not a full per-profile provenance manifest.

Do not run the legacy flat-schema `verify_public_evidence.py` against the nested roundtrip JSON. They have different schemas. Its legacy flat-record check is not the verifier for this published returned artifact.

## Evidence required for independent reproduction

A complete external validation records:

1. Exact dataset/version, acquisition reference and applicable terms or a public test vector.
2. Original, transferred and restored sizes with precise byte-measurement boundaries.
3. Independently recomputed original and restored SHA‑256, plus binary comparison when claiming bit identity.
4. Run ID/time, hardware/OS and receiver/cache state; a controlled baseline for a comparative performance claim.
5. Publicly shareable raw measurement logs, verifier version and reproduction instructions.
6. Identity and scope of the independent check, separately from the source's local PASS.

Where this material is incomplete, use HISTORICAL_REPORTED, HISTORICAL_LOCAL_REPORT_CONSISTENCY or PENDING for the publication-level scope. Preserve source statuses in their own fields; do not promote them to EXTERNALLY_VERIFIED without supporting evidence.

## Historical results and current publication scope

| Item | Stored reported result | Current public scope |
|---|---|---|
| NASA JUNO WAVES | 85.54% byte reduction | Historical family entry; independent reproduction not established here |
| Matrix cold/warm/delta | 81.2486% / 99.9916% / 99.9541% | Historical family entry; different profiles |
| Evidence Gateway | 250,000 → 1,842 events; 99.2632% | Historical event filtering result; not a byte rate |
| Metrica Sports | Cold 65.58%; warm 98.54% | Historical source record; no provider certification |
| Blackbox 64 MiB | Cold 49.5306%; warm 99.9913% | Historical family entry and best-of consistency-checked report fields with published hashes |
| WAN true-cold | 6,950 wire bytes | Historical specific session; 64 blocks, unique=1 |
| 100 GiB scale/recovery | 107,374,182,400 → 14,476,957,280 B; about 86.52%; two reported restore checks | Historical family entry; complete independent public reproduction not established |

This table and the family CSV describe historical outcomes. They do not establish a single combined “best overall system” result.

## Confidentiality and publication

Public measurements, public references and explicitly reviewed verification helpers can be shared. The proprietary core, algorithms, internal routing/control implementation, credentials, private manifests and customer payloads remain excluded. Independent evaluation can use agreed black-box conditions without publishing the core.

The [Kaggle dataset](https://www.kaggle.com/datasets/kaikuhnert/rhodium-germany-public-benchmark-evidence) hosts historical result files. The revised [dataset card](kaggle/DATA-CARD.md) is prepared here; its direct save to Kaggle has not been confirmed. Existing input-data and publication rights are not expanded by this documentation update.

## Additional public audit references (not competition certifications)

Historical Rhodium Connector Audit (2026-10-06) records the following GitHub Actions links. A successful workflow run alone does not establish independent third-party verification or competition acceptance. Full logs, licensing and verifiers require separate inspection before promotion to EXTERNALLY_VERIFIED.

- Hutter enwik9, run [36989217616](https://github.com/BlackboxLogicCore/rhodium-benchmarks/actions/runs/36989217616): source 1,000,000,000 bytes; archive 356,916,775 bytes; wrapper 2,048 bytes; reported combined 356,918,823 bytes; source/restore SHA-1 match; reported PASS_BIT_EXACT. The audit explicitly says `RHODIUM_STRICT_SELF_CONTAINED_P0_CERTIFIED=NO`. **Do not claim Hutter Prize win or certification**.
- Fingerprint one-file probe, run [36993722643](https://github.com/BlackboxLogicCore/rhodium-benchmarks/actions/runs/36993722643): source 1,048,576 bytes; fingerprint 7,151 bytes; SHA-256 match; reported bit-identical restore; restore ~62 ms.
- ULTIMO5 Ubuntu proof, run [36962456220](https://github.com/BlackboxLogicCore/rhodium-benchmarks/actions/runs/36962456220): reported PASS for eBPF/XDP canary, compile/load, SHA-NI availability, zero-copy selftest and lock-free atomic selftest. These are infrastructure tests, **not lossless-compression ratios**.

### Metric correction

An older Evidence Gateway claim used 99.4021%. The source counts 250,000 and 1,842 imply (250000-1842)/250000 * 100 = **99.2632%**, which supersedes that older figure. The numerator is an event-count reduction; do not present it as a byte compression rate.

### Additional claim boundary

The historical 64 MiB Cloudflare *live-source* figures are **not** a controlled direct comparison against Cloudflare's product or a generic ISP speed test. Cold/warm results depend on reuse, cache conditions, source characteristics and test methodology. Externally reproduced evidence remains separate from historical reports.

