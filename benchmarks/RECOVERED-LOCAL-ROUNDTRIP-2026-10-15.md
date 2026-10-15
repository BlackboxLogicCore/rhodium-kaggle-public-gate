# Recovered local roundtrip evidence — 2026-10-15 inventory update

This is an **evidence recovery and cross-check**, not a newly executed benchmark, independent certification, or validation of every past run. The measurements below originate in a dated **2026-09-04 Rhodium local report**. Its public-safe values were checked for internal consistency on 2026-10-15.

## Existing 64 MiB local test, cold and warm

- Run reference: `PRF-20260904-041012-7F9C61D6`
- Test data: synthetic; 67,108,864 input bytes (64 MiB)
- Test scope: **local loopback self-test**; **no external network** and **no third-party validation**
- Input SHA-256: `100579a3d6d02bdc61b4fda1030d0b7e680d6fbc72c2c1a137896e3b78207d7a`
- Report document SHA-256: `E1A8C4808B1D483884A89190C3726001EADE77E609794B00E3E3CADF6C4B47FC`
- Original report declares source and restored hashes identical, byte counts equal, and restore `PASS` for both modes.

| Mode | Input bytes | Wire bytes | Reduction | Blocks reused | Reported restore |
|---|---:|---:|---:|---:|---|
| Cold | 67,108,864 | 33,869,410 | 49.5306% | 0/64 | bit-identical, hash match |
| Warm | 67,108,864 | 5,827 | 99.9913% | 64/64 | bit-identical, hash match |

The warm result is a **cache/reuse measurement**, not a new-data compression ratio. Neither mode should be described as a verified WAN transmission. The source and restored binary payloads were **not freshly rehashed against one another** during the 2026-10-15 inventory: internal consistency of saved report fields was checked instead.

This **adds supporting provenance to the existing “64 MiB Blackbox” benchmark family**, not a new independent benchmark or an additional unique test family.

## Broader evidence discovery: inventory, not a test count

During the 2026-10-15 inventory, a limited index of existing JSON evidence files was checked. The **2,369** indexed distinct files all matched their indexed file SHA-256 values at recheck. Among the indexed files, **103** reports had both cold and warm sections; **91** were internally consistent under a field-level test, while **12** had missing or contradictory fields under that test. Remaining files have not been fully schema-validated. These figures describe a **subset of records**, not total execution count, globally independent runs, or third-party verification.

An earlier broader inventory dated 2026-10-08 reported **8,427 candidate files** and **7,788 extracted metrics** across an extensive disk scan. Files, metrics, report copies, and distinct executed tests are **different units**. A historical claim of 100,000+ tests is **not verified** by these inventory figures and should not be presented as an audited test count.

## Publication status

- `LOCAL_REPORTED_WITH_INTERNAL_CONSISTENCY_CHECK`: saved report fields and document SHA-256
- `PENDING_RAW_ARTIFACT_RECHECK`: independently hash original and restored binary test artifacts
- `PENDING_EXTERNAL_REPRODUCTION`: third-party execution and verification

No proprietary implementation, code, private manifest, machine path, credential, or private control information is included.
