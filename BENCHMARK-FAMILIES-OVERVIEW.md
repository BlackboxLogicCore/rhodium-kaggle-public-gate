# Rhodium Germany — Benchmark-Familien und Nachweisregister

**Öffentliche Übersicht · 5. November 2026**

Diese Seite ist der zentrale Einstieg in die bereits veröffentlichten technischen Nachweise von Rhodium Germany. Sie verlinkt auf bestehende Register; sie stellt **keinen neuen Testlauf** und keine unabhängige Produktzertifizierung dar.

## Umfang der veröffentlichten Nachweise

| Register | Dokumentierter Umfang | Quelle |
|---|---:|---|
| Unterschiedliche Prüfzwecke | 62, plus gesonderte Profilübersicht | [Einzelregister](benchmarks/RHODIUM-ALL-DISTINCT-TESTS.md) |
| Ergänzende Messprofile | 22 | [Evidence JSON](public-evidence/2026-10-15-recovered-evidence.json) |
| Unterschiedliche ausgewählte Eingabedaten | 25 | [Roundtrip- und SHA-256-Register](benchmarks/RHODIUM-PUBLIC-BENCHMARK-RESULTS-AND-SHA256.md) |
| Historische Familiennachweise | 29 | [Familienregister](benchmarks/RHODIUM-PUBLIC-BENCHMARK-FAMILY.csv) |

**Zählregel:** Diese Register überschneiden sich. Die Zahlen sind weder zu einer Gesamtzahl unabhängiger Benchmarks addierbar noch Belege für 62 unabhängige Zertifizierungen. Registerstand überwiegend 15. Oktober 2026.

## Nachweisfamilien

| Bereich | Dokumentierte Beispiele | Nachweisgrenze |
|---|---|---|
| Datenintegrität und Wiederherstellung | Lokale bit- und hashgleiche Roundtrips, ausgewählte SHA-256-Prüfwerte, 1 MiB bis mehrere GiB | Historische lokale Berichte; erneute unabhängige Verifikation nicht pauschal erfolgt |
| Streaming und Betrieb | Zustellung, Replay, Puffer, Latenzprofile | Testaufbau und Messpunkt beachten; keine allgemeine WAN-Verfügbarkeitsgarantie |
| Cold / Warm / Delta | Unterschiedliche Übertragungsmengen bei Erstübertragung und vorhandenen Empfängerzuständen | Warm setzt vorhandene Daten voraus; kein Beleg für Rekonstruktion ohne Datenbasis |
| Sicherheits- und Eingabeprüfungen | Manipulierte Nachweise, Fehlformate, Zugriffsgrenzen | Nur jeweils geprüfte Schnittstelle / Testkonfiguration |
| Große Datenmengen | Historisch dokumentierter 100-GiB-Roundtrip und NASA-Juno-WAVES-Datenfall | Keine unabhängige Anbieterzertifizierung oder NASA-Freigabe |
| Fachliche Datensätze | Seismik, Robotik, Automotive, Sport, Forschungsdaten | Datensatzbezogene Prüfungen, keine universelle Branchenfreigabe |
| Externe Schnittstellen / Vergleich | Historische externe Proofs, Upstream-Builds und definierte lokale Vergleiche | Build-PASS ist kein Leistungsgewinn; Messpunkte können abweichen |

## Konkrete ausgewählte Ergebnisse

- **64 MiB lokaler Blackbox-Roundtrip:** 67.108.864 B Eingabe, 33.869.410 B Cold-Wire und 5.827 B Warm-Wire, mit dokumentiertem übereinstimmendem Original-/Restore-SHA-256. [Beleg und Bedingungen](benchmarks/RHODIUM-PUBLIC-BENCHMARK-RESULTS-AND-SHA256.md)
- **128 MiB Golden Roundtrip:** 134.217.728 B Eingabe, 67.737.497 B Cold-Wire und 11.270 B Warm-Wire; historischer lokaler Bericht. [Beleg und Bedingungen](benchmarks/RHODIUM-PUBLIC-BENCHMARK-RESULTS-AND-SHA256.md)
- **100 GiB Scale/Recovery:** historisch 107.374.182.400 B Eingabe, 14.476.957.280 B dokumentierte Ausgabe und zwei berichtete Restore-PASS. [Familienregister](benchmarks/RHODIUM-PUBLIC-BENCHMARK-FAMILY.csv)
- **Seismische und weitere öffentliche Datensätze:** ausgewählte historische Eingabegrößen, Transferwerte und Hash-Nachweise. [Roundtrip-Register](benchmarks/RHODIUM-PUBLIC-BENCHMARK-RESULTS-AND-SHA256.md)

## Was nicht behauptet wird

Keine universelle Ausfallverhinderung, keine garantierte Wiederherstellung beliebiger unbekannter Daten aus einem kurzen Fingerabdruck, keine pauschale P=0-Wirkung, keine unabhängige Zertifizierung aller Familien und kein nachgewiesener Sieg über Cloud-Anbieter. Die konkreten Messgrenzen, Vorbedingungen und noch offenen Prüfungen gelten weiterhin.

## Für technische Interessenten

Beginnen Sie mit dem [Einzelregister](benchmarks/RHODIUM-ALL-DISTINCT-TESTS.md), prüfen Sie die [SHA-256-Ergebnisse](benchmarks/RHODIUM-PUBLIC-BENCHMARK-RESULTS-AND-SHA256.md) und lesen Sie die [Verifikationshinweise](PUBLIC-BENCHMARK-VERIFICATION.md). Ein produktiver Einsatz erfordert eine gesonderte, schriftlich vereinbarte technische Abnahme.

**Schutzgrenze:** Diese Übersicht veröffentlicht weder Quellcode, Algorithmen, private Infrastruktur, Zugangsschlüssel noch Kundendaten. Die privaten Mama-, Forschungs- und Arbeiterbox-Bestände bleiben unverändert.
