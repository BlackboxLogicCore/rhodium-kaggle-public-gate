# Rhodium Germany – Ergänzungsregister externer und großer Prüfungen

Stand 2026-11-02. Dieses Dokument ergänzt die vorhandenen 62 Prüfzwecke, 22 Messprofile, 25 SHA-distinkten Best-of-Fälle und 29 Familienpositionen. **Keine Addition dieser Registerzahlen:** Es gibt Überschneidungen. Alle unten genannten Ergebnisse sind aus historischen internen Inventurberichten übernommen; hier wurde kein neuer Lauf ausgeführt.

| ID | Historisch dokumentierter Prüffall | Berichtetes Ergebnis | Aussagegrenze |
|---|---|---|---|
| EXT-K26 | Golden Roundtrip, 128 MiB | Cold 67.737.497 B, Warm 11.270 B; bitidentischer Restore | Lokal; Warm nutzt Empfängerzustand |
| EXT-K27 | Kaggle-Datensatz, 698.914 B | Restore-SHA-256 identisch, Empfänger-ACK, PASS_LOCAL_ROUNDTRIP | Keine Kaggle-Zertifizierung |
| EXT-Z01 | Automotive FAST75 | 75/75 Roundtrips, null gemeldete Fehler | Keine Automotive-Sicherheitszulassung |
| EXT-Z18 | Cross-Runner-Replay, 1 GiB und weitere Größen | PASS_REAL_CROSS_RUNNER_NATIVE_PROTOCOL_REPLAY | Kein gleichzeitiger TCP-Live-Transport |
| EXT-Z21 | Externe GitHub-Runner, 1 GiB und 256 MiB | PASS_REAL_ROUNDTRIP laut historischen Berichten | Kein unabhängiges Prüflabor |
| EXT-Z22 | HTTPS-Echo, 1 MiB in 16 Paketen | Identischer Restore-Hash | Echo-Endpunkt, kein zweiter nativer Rhodium-Empfänger |
| EXT-Z23 | 8-GiB-Matrixlauf | 8.589.934.592 B Input, Cold 4.334.824.636 B, Warm 696.713 B, Hashgleichheit | Synthetische lokale Daten |
| EXT-Z24 | 4-GiB-Matrixlauf | 4.294.967.296 B Input, Cold 2.167.425.223 B, Warm 348.553 B | Synthetische lokale Daten |
| EXT-Z25 | Matrixlauf, 1 Milliarde Byte | Cold 323.250.554 B, Warm 10.592 B, Hashgleichheit | Vorbefüllter Empfänger im Warm-Lauf |
| EXT-K28 | MSP360-Vergleich, 128 MiB | Cold- und Delta-Restore bitidentisch | Unterschiedliche Messpunkte; keine Herstellerzertifizierung |
| EXT-K29 | NASA C-MAPSS FD001 | 495.144 Werte aus 20.631 Zeilen verarbeitet | Keine Prognosevalidierung oder NASA-Zertifizierung |
| EXT-Z26 | Niagara / USGS | Zwei Originaldatenberichte mit Roundtrip- und Hash-PASS | Kein Beweis für null physikalisches Rauschen |

**Quellennachweis:** historisches internes Dokument `Rhodium-Gesamtinventur-2026-10-22.md`, über das geschützte Hauptprojekt `BlackboxLogicCore/rhodium-zero-point` in `EVIDENCE-SCOPE.md` abgeglichen. Private Originalberichte, vollständige Implementierungen, Schlüssel und interne Pfade werden nicht veröffentlicht. Der öffentliche Leser kann die historischen Angaben anhand dieses Registers einordnen, aber nicht jeden Originaldurchlauf unabhängig reproduzieren.

**Deduplizierung:** EXT-K26 usw. sind Quell-IDs, keine neu gezählten Benchmarks. Vor einer Übernahme als eigenständige zusätzliche Prüfzwecke muss gegen `RHODIUM-ALL-DISTINCT-TESTS.md` anhand Prüfziel, Datensatz, Messprofil und Originalbeleg abgeglichen werden. Bestehende 62 Positionen bleiben unverändert.

**Kundenprüfung:** Derzeit ist kein allgemein erreichbarer, authentifizierter Arbeiterbox-Upload-Endpunkt durch einen vollständigen externen Ende-zu-Ende-Test nachgewiesen. Ein GitHub-Actions-Reparaturtest für die private Bridge ist kein solcher Kundentest. Dieses Register stellt keine Aufforderung zum Upload sensibler Daten dar.
