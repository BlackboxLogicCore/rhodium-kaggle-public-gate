# Rhodium Germany – Register der unterschiedlichen Prüfungen

Stand: 15.10.2026. Dieses Register führt unterschiedliche Prüfziele einzeln auf. Datensätze, Größen, Wiederholungen und Umgebungen derselben Prüfung bleiben zugehörige Profile. Ein historisch gemeldeter PASS wird erhalten. Eine Zusammenfassung ist als solche gekennzeichnet.

[CSV](RHODIUM-ALL-DISTINCT-TESTS.csv) · [Messprofile und Beleg-Hashes](../public-evidence/2026-10-15-recovered-evidence.json) · [Quellenabgleich](../public-evidence/2026-10-15-source-reconciliation.md)

Der Geltungsbereich ist die Zusammenführung der jetzt zugänglichen gespeicherten Quellen. Vollständigkeit aller jemals erzeugten Dateien oder die aktuelle Abnahme des Gesamtsystems wird daraus nicht abgeleitet. Es wurde kein neuer Leistungstest ausgeführt.


## Daten und Integritaet

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| CHECK-01 | Strukturierte Tabellen | 8 MiB; 83.421% Reduktion; Verdichten 16.52 MiB/s; Restore 178.21 MiB/s; Original = Restore | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-02 | Zeilenorientierte Objektdaten | 8 MiB; 93.737% Reduktion; Verdichten 57.23 MiB/s; Restore 263.88 MiB/s; Original = Restore | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-03 | Zeitreihen | 8 MiB; 99.141% Reduktion; Verdichten 189.11 MiB/s; Restore 258.85 MiB/s; Original = Restore | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-04 | Zufallsdaten | Identische Rekonstruktion; -0.031% Reduktion (Ausgabe groesser); Restore 443.93 MiB/s | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. Erfolgreicher Restore, keine Reduktion dieses Zufallsdatensatzes. |
| CHECK-05 | Großer Forschungsdatensatz | 5,443,001,419 B -> 787,199,297 B; 85.54% Reduktion; Restore dokumentiert | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-06 | 100-GiB-Roundtrip | 100 GiB; 107,374,182,400 B -> 14,476,957,280 B; ca. 86.52%; 2/2 Restore-PASS | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-07 | Delta-Wiederverwendung | 64 Bloecke; 63 wiederverwendet; 1 geaendert; 98.4375% weniger Transport im dokumentierten Profil | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-08 | Beschädigungserkennung | 8 MiB; gezielt geaendertes Bit / betroffener Block erkannt | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |

## Durchfluss und Betrieb

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| CHECK-09 | End-to-End-Durchsatz | Juli-Profil: 20,000/20,000 interne Vorgaenge, 0 Fehler, 479,442.48/s; August-Profil: 54,105.74/s. Unterschiedliche historische Aufbauten, kein Versionsvergleich. | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. Lokaler Aufbau; kein Beleg fuer ein reales WAN oder Satellitennetz. |
| CHECK-10 | Latenzprofil | August-Profil: p50 17.21 us; p95 30.21 us; p99 33.81 us; zusammengehoeriger Lauf | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. Lokaler Aufbau; kein Beleg fuer ein reales WAN oder Satellitennetz. |
| CHECK-11 | Rückstaupuffer | 18,000 Ereignisse gepuffert | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. Lokaler Aufbau; kein Beleg fuer ein reales WAN oder Satellitennetz. |
| CHECK-12 | Vollständige Zustellung | 20,000/20,000 Ereignisse ausgeliefert | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. Lokaler Aufbau; kein Beleg fuer ein reales WAN oder Satellitennetz. |
| CHECK-13 | Duplikatfreiheit | 0 doppelte Auslieferungen | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. Lokaler Aufbau; kein Beleg fuer ein reales WAN oder Satellitennetz. |
| CHECK-14 | Replay-Leistung | 2,360,787 Replay-Ereignisse/s | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. Lokaler Aufbau; kein Beleg fuer ein reales WAN oder Satellitennetz. |
| CHECK-15 | Forschungsbox-Gesamttest | 2/2 PASS; beste dokumentierte Laufzeit 5.688 s (weiterer Lauf 6.514 s) | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-16 | Mutterbox-Gesamttest | 2/2 PASS; beste dokumentierte Laufzeit 6.353 s (weiterer Lauf 10.683 s) | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |

## Schnittstelle und Datenschutz

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| CHECK-17 | Gesundheit vor Test | PASS: vor Belastung erreichbar | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-18 | Gesundheit nach Test | PASS: nach Belastung erreichbar | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-19 | Schnittstellenvertrag | PASS: Schnittstellenbeschreibung geprueft | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-20 | Reales Prozessschema | PASS: Pflichtstruktur eingehalten | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-21 | Gültige Verarbeitung | PASS: zulaessige Eingabe akzeptiert | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-22 | Kein Inhaltsecho | PASS: kein unkontrolliertes Inhaltsecho | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-23 | Verdeckter Operatorinhalt | PASS: interner Inhalt nicht offengelegt | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-24 | Deaktivierte Persistenz | PASS: keine dauerhafte Inhaltsspeicherung im Pruefpfad | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |

## Nachweise und Eingabegrenzen

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| CHECK-25 | Inhaltsfingerabdruck | PASS: Inhaltszuordnung und Integritaet | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-26 | Gültiger Nachweis | PASS: korrekte Pruefreferenz akzeptiert | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-27 | Manipulierter Nachweis | PASS: veraenderter Beleg abgewiesen | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-28 | Fehlformatierte Eingaben | PASS: 4 ungueltige Varianten abgewiesen | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-29 | Zu kurze Kennung | PASS: zu kurze Kennung abgewiesen | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-30 | Übergroße Eingabe | PASS: Groessenlimit durchgesetzt | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-31 | Berechtigungsgrenzen | PASS: Verweigern und erlaubte Aktionen getrennt geprueft | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |
| CHECK-32 | Angriffsmuster als Daten | PASS: 10 Angriffsmuster als Daten verarbeitet; keine Befehlsuebernahme protokolliert | REPORTED_PASS; sanitized_historical_summary | Interner historischer Funktionscheck; gekuerzte Zusammenfassung; keine unabhaengige Zertifizierung. |

## Daten und Integritaet

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| TYPE-BINARY-ROUNDTRIP | Binaerer Cold-/Warm-Roundtrip | Mehrere dokumentierte Profile von 6 MiB bis 8 GiB; je Profil getrennte Bytewerte und Restore-Nachweise. Kaggle-Eingabe: lokaler PASS, externe Rueckpruefung offen. | REPORTED_PASS; historical_report | Datensatz-, Groessen- und Umgebungsvarianten bleiben Profile derselben Pruefart; Warm setzt Empfaengerzustand voraus. |

## Wiedererkennung

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| TYPE-RECOGNITION | Referenzgestuetzte Wiedererkennung | 1,000,000,000 B -> 81,481 B Warm; 134,728,520 B -> 11,354 B; 1,048,576 B -> 7,151 B; jeweils im eigenen dokumentierten Profil. | REPORTED_PASS; historical_report | Datensatz-, Groessen- und Umgebungsvarianten bleiben Profile derselben Pruefart; Warm setzt Empfaengerzustand voraus. |

## Filtering

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| LEGACY-03 | Evidence Gateway | 250,000 -> 1,842; calculated reduction 99.2632%; precision 1.0; recall 1.0 | PASS; historical_report | Uses mathematically corrected reduction for 250000 -> 1842 |

## External Proof

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| LEGACY-05 | Canonical Public Proof | Signature verification and tamper rejection; 3/3 + 3/3 PASS | PASS; historical_report | Public attestation proof |
| LEGACY-06 | World Blind Proof | 4/4 + 2/2 PASS; manipulated engine blocked before execution | PASS; historical_report | Blind/integrity proof |

## Live Source

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| LEGACY-11 | Cloudflare Live Source | 6,950 B cold; 5,838 B warm; restore PASS | PASS; historical_report | Same-payload live-source measurement; not represented as symmetric Internet-path-vs-Internet-path benchmark |

## Plattformvalidierung

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| UBUNTU-01 | P0-Freigabeverhalten unter Ubuntu | Fail-closed-PASS | REPORTED_PASS; historical_suite_subcheck | Historisch gemeldeter Teilcheck aus Run 36962456220; kein isolierter Leistungsgewinn nachgewiesen. |
| UBUNTU-02 | eBPF/XDP-Canary | Canary-PASS | REPORTED_PASS; historical_suite_subcheck | Historisch gemeldeter Teilcheck aus Run 36962456220; kein isolierter Leistungsgewinn nachgewiesen. |
| UBUNTU-03 | Ubuntu Compile-/Load-Pruefung | Compile/Load-PASS | REPORTED_PASS; historical_suite_subcheck | Historisch gemeldeter Teilcheck aus Run 36962456220; kein isolierter Leistungsgewinn nachgewiesen. |
| UBUNTU-04 | SHA-NI-Ausfuehrung | SHA-NI-PASS | REPORTED_PASS; historical_suite_subcheck | Historisch gemeldeter Teilcheck aus Run 36962456220; kein isolierter Leistungsgewinn nachgewiesen. |
| UBUNTU-05 | Zero-Copy-Pruefung | Zero-Copy-PASS | REPORTED_PASS; historical_suite_subcheck | Historisch gemeldeter Teilcheck aus Run 36962456220; kein isolierter Leistungsgewinn nachgewiesen. |
| UBUNTU-06 | Lock-free-Atomic-Pruefung | Atomic-PASS | REPORTED_PASS; historical_suite_subcheck | Historisch gemeldeter Teilcheck aus Run 36962456220; kein isolierter Leistungsgewinn nachgewiesen. |

## Upstream Compatibility

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| LEGACY-13 | Cloudflare Speedtest upstream | 16/16 test files; 163/163 tests PASS | PASS; historical_report | Compatibility/build validation; not a Rhodium-vs-Cloudflare performance win |
| LEGACY-14 | Google Brotli upstream | 73/73 CTest PASS | PASS; historical_report | Compatibility/build validation; not a Rhodium-vs-Brotli performance win |
| LEGACY-15 | Meta Zstd upstream | make zstd + make check PASS | PASS; historical_report | Compatibility/build validation; not a Rhodium-vs-Zstd performance win |
| LEGACY-16 | Google Fleetbench upstream | Optimized compression benchmark build PASS | PASS; historical_report | Build validation only |
| LEGACY-17 | Microsoft NTTTCP upstream | Official build + CLI smoke PASS | PASS; historical_report | Build/smoke validation only |
| LEGACY-18 | Cloudflare zlib upstream | CMake build completed; upstream path recorded PASS | PASS; historical_report | Build validation only |

## Sport

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| LEGACY-20 | Metrica Sports Sample Game 1 | Cold 11,550,999 B (-65.58%); Warm 488,590 B (-98.54%); 123/128 blocks reused; restore hash-identical; P0 PASS | PASS; historical_report | Benchmark on sample sports data |

## Seismic

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| LEGACY-21 | EarthScope/USGS live evidence | Latency 2.4-6.3 s; accepted_records=23; P0 live evidence | PASS; historical_report | Live evidence; not an EarthScope/USGS certification |

## Relay

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| LEGACY-23 | Verify-Relay | Millisecond end-to-end path; SHA-256 seal; VERIFIZIERT_UND_VERSIEGELT | PASS; historical_report | Relay/integrity proof |

## WAN

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| LEGACY-24 | WAN TRUE-COLD | Wire 6,950 B; PASS | PASS; historical_report | Cross-network evidence; claim limited to documented session |

## Vendor Comparison

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| LEGACY-28 | Rhodium vs MSP360 sealed local comparison | Cold: Rhodium 67,157,014 B vs MSP360 77,628,710 B (-13.489463%); delta: Rhodium 8,407,583 B vs MSP360 12,608,574 B (-33.318526%); Rhodium cold/delta restore bit-identical; report SHA-256 2672A959AAC4B8E299F9174E484F7DA675B1973712AD492DFD5C1C6C6EB7F867 | PASS_FINAL_SEALED_EVIDENCE; historical_report | Historical defined local test dated 2026-09-21; MSP360 uploaded bytes vs Rhodium wire bytes are different implementation measurement points; not independent vendor certification |

## NASA Data Processing

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| LEGACY-29 | NASA C-MAPSS FD001 local data pipeline | PASS local pipeline; 495,144/495,144 values processed; P0 no drop; elapsed 147 ms; reported throughput 3,368,327 values/s; train SHA-256 963B5E22825B34D8B21C69E1AEB4AF3E647050EB672EE8834BA4B5D91D2DE0F8 | PASS_LOCAL_PIPELINE; historical_report | Historical desktop report 2026-09-23; signal detection/scoring is not externally validated predictive accuracy; failure-cycle labels used after matrix scoring; no NASA certification |

## Textdaten

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| TYPE-ENWIK9-TRANSFER | Vollstaendiger enwik9-Transport | 1,000,000,000 B; Cold 323,250,554 Senderbytes / 63.5063 s; Warm 10,592 Senderbytes / 7.9804 s; Cold und Warm Restore bitidentisch. | PASS_REAL_ROUNDTRIP; stored_original_report | Textdatenprofil des binaeren Roundtrips, keine zusaetzliche unabhängige Testart; Warm mit gefuelltem Empfaengerzustand; kein Hutter-Preisresultat. |

## Isolierte Forschung

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| TYPE-RESEARCH-PACKAGE | Verlustfreier experimenteller Software-Kandidat | 1,048,576 B -> 529,880 B Paket; byte-identischer Restore; Pack 0.115248 s; Restore 0.214922 s. | PASS_RESEARCH_TEST; historical_report | Lokaler Forschungsversuch; Python-Laufzeit nicht im Paket; kein eigenstaendiges neues Codec-Verfahren oder Wettbewerbsrekord belegt. |

## Kontrollierte Ausfuehrung

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| TYPE-DETERMINISTIC-REPLAY | Deterministische Wiederholung | Zwei kanonische Ergebnisfolgen identisch; gesperrte Zielaktion in beiden Folgen nicht ausgefuehrt. | PASS_DETERMINISTIC_REPLAY; historical_report | Synthetischer lokaler Test ohne externe Wirkungen; interne Regeln und Implementierung bleiben privat. |
| TYPE-ACTION-INTERCEPTION | Abfangen unzulaessiger Werkzeugaktionen | Erlaubte Aktionen ausgefuehrt; 1/1 unzulaessige Zielaktion ohne Zielaufruf blockiert; Funktionskontrollen bestanden. | PASS_AGENTIC_TOOL_CALL_INTERCEPTION; historical_report | Synthetischer lokaler Test ohne externe Wirkungen; interne Regeln und Implementierung bleiben privat. |

## Integritaet und Last

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| TYPE-SHA-LOAD | Synthetischer SHA-256-Siegel-Lasttest | 1,000,000 Pruefvorgaenge; 0 Fehler; 1.640618 s; 609,526.48/s; p50/p95/p99 0.00183/0.00231/0.0026 ms. | ERFOLGREICH; historical_report | Ein Lasttest mit einer Million Vorgaengen, keine Million unterschiedlicher Benchmarks; lokaler synthetischer Aufbau. |

## Schnittstellenlast

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| TYPE-HTTP-LOAD | HTTP-Endpunkt-Lastprofile | 7 Endpunktprofile mit je Basis- und Doppellast; jeweils 0 HTTP-Fehler. Hoechster dokumentierter Durchsatz im Gesamtfluss-Profil: 1,052.43/s bei 200 Anfragen / 16 Verbindungen. | REPORTED_PASS; sanitized_historical_summary | Basis: 100 Anfragen / 8 Verbindungen; Doppelt: 200 / 16. Endpunkte sind Profile derselben Lastpruefart. Uebergeordnete Orchestrierung war nicht vollstaendig gesund. |

## Forschungsmessung

| ID | Prüfung | Bestes dokumentiertes Ergebnis / Profil | Status und Belegstufe | Grenze |
|---|---|---|---|---|
| TYPE-ANOMALY-MEASUREMENT | Synthetische Anomalieentscheidung | 50,000 Ereignisse; TP 299; FP 505; TN 48,999; FN 197; Recall 60.282%; Precision 37.189%; F1 ca. 46%. | MEASUREMENT_REPORTED; sanitized_historical_summary | Messlauf dokumentiert; keine produktionsreife Erkennungsqualitaet und keine Ausfallvorhersage-Zertifizierung. |

## Belegführung

Die maschinenlesbare Ergebnisdatei nennt zu jeder Quelle ihren vollständigen SHA-256-Wert. Sie enthält ausschließlich ausgewählte Ergebnisfelder. Originaldateien aus privaten Archiven bleiben privat. Die 32 historischen Funktionschecks stammen aus einer gekürzten Zusammenfassung. Ihre Originalprotokolle sind hier nicht als vollständig verfügbare Rohbelege dargestellt.

Die vorhandenen [25 Datensatzprofile](RHODIUM-PUBLIC-BENCHMARK-RESULTS-AND-SHA256.md) und [29 historischen Sammelpositionen](RHODIUM-PUBLIC-BENCHMARK-FAMILY.csv) bleiben erhalten. Ihre Anzahl wird nicht zu der Zahl dieses Registers addiert.
