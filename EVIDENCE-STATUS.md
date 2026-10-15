# Evidence status · Rhodium Germany

Documentation date: **2026-10-15**. This page defines how to read the published collections without changing their historical outcomes.

## Two different questions

- **What did the stored run report?** Read the source `status`, byte counts, integrity fields and report fingerprints.
- **What can a reader verify from the public material today?** Read the publication scope below and the [verification guide](PUBLIC-BENCHMARK-VERIFICATION.md).

A historical PASS and a pending independent check can both be true. Pending independent verification does not erase a successful source report; a successful source report does not complete independent verification.

## Publication status

| Collection or item | Reported outcome | Publicly supported scope | Still outside that scope |
|---|---|---|---|
| 25 SHA-distinct best-of records | Stored local cold/warm PASS and equal source/restore SHA‑256 | HISTORICAL_LOCAL_REPORT_CONSISTENCY: fields in available stored reports were cross-checked; published CSV records the scope | Fresh original/restored binary comparison, independent external reproduction, and full lineage of separately selected best profiles |
| 29 family entries | Preserved source statuses such as PASS, PASS_LOCAL_PIPELINE and PASS_FINAL_SEALED_EVIDENCE | HISTORICAL_REPORTED: consolidated register with per-row claim boundaries | Uniform independent validation of all rows; availability of every underlying raw source artifact in this public repository |
| 64 MiB Blackbox and 128 MiB Golden | Local source reports record bit/hash-identical restore | Also represented in the best-of dataset table; use its complete reported hashes | No independent WAN/Kaggle validation inferred from these local records |
| Kaggle-generated-input roundtrip, 2026-10-14 | PASS_LOCAL_ROUNDTRIP; 698,914 B input → 381,517 B wire → 698,914 B restore | Public JSON records equal hashes, fresh cache, zero reused blocks, receiver acknowledgement and P0 PASS | Independent verification of the returned artifact remains PENDING |
| WAN / live-source entries | Historical session-specific PASS | Recorded session only; WAN TRUE-COLD states 64 blocks and unique=1 | General Internet acceleration, arbitrary-input transfer ratio, controlled Cloudflare product superiority |
| Upstream build/compatibility entries | Historical upstream test/build PASS | Compatibility or infrastructure checks | Rhodium performance advantage over those upstream products |
| Public Kaggle dataset | Three evidence files published as Version 1 | Hosting of historical result tables | Independent Kaggle execution or certification |

The “External Proof” family name and words such as “sealed” are historical source labels. They do not establish an independent verifier's identity, a vendor endorsement or a third-party certification on their own.

## Reading the numbers

**Cold:** use the exact underlying test's receiver/cache conditions. A cold label alone does not prove all other state and input structure were absent.  
**Warm:** uses prior receiver state; report its retained-state dependency separately.  
**Best-of:** one row per input SHA‑256 with selected best historical profile values, not a newly executed end-to-end combined run.  
**Reduction:** `100 × (input_bytes − wire_bytes) / input_bytes`. This is valid only for matching byte boundaries.  
**SHA‑256:** a reported match is an integrity claim in a stored report. An independent verifier must obtain the actual files separately to recompute it.  
**P=0:** recorded acceptance-policy outcome for the specific test, not a probability estimate or universal zero-risk guarantee.

Automotive labels, NASA and other provider names describe source/test labels. They do not demonstrate a commercial relationship, customer deployment or independent approval.

## Archive and system scope

The published inventory describes a limited-scope historical reconciliation. A finished publication of the located records does not prove that all historical C:/D: archives were exhaustively reconciled. File counts, metrics, grouped reports and executions are different counts.

This publication does not establish over 100,000 independently verified runs, a general one-byte transport result, a Hutter Prize win, or full end-to-end independent validation of all eight internal levers. No “best overall system result” is inferred by combining minima from separate tests.

## Links

[Customer overview](README.md) · [25 best-of results](benchmarks/RHODIUM-PUBLIC-BENCHMARK-RESULTS-AND-SHA256.md) · [29 family entries](benchmarks/RHODIUM-PUBLIC-BENCHMARK-FAMILY.csv) · [Stored inventory scope](public-evidence/2026-10-15-historical-inventory-status.md) · [Verification guide](PUBLIC-BENCHMARK-VERIFICATION.md)
