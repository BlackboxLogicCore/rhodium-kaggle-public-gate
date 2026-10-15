# Rhodium Germany · Benchmark Evidence

**Weniger Daten übertragen. Wiederherstellung nachvollziehbar belegen.**

Diese öffentliche Sammlung zeigt dokumentierte Ergebnisse zur Datenübertragung, Wiederherstellung und Integrität von Rhodium Germany. Für Kunden ist die entscheidende Frage: **Wie viele Bytes werden im konkreten Anwendungsfall übertragen und bleibt der wiederhergestellte Inhalt identisch?** Hier stehen die Messwerte, SHA‑256-Fingerabdrücke und ihre jeweiligen Prüfgrenzen.

[Ergebnistabelle](benchmarks/RHODIUM-PUBLIC-BENCHMARK-RESULTS-AND-SHA256.md) · [Alle 29 Nachweiseinträge](benchmarks/RHODIUM-PUBLIC-BENCHMARK-FAMILY.csv) · [Prüfstatus](EVIDENCE-STATUS.md) · [Kaggle-Datensatz](https://www.kaggle.com/datasets/kaikuhnert/rhodium-germany-public-benchmark-evidence) · [Website](https://rhodium-germany.de)

## Was veröffentlicht ist

| Sammlung | Inhalt | Einordnung |
|---|---|---|
| 25 Best-of-Datensätze | Originalgröße, beste dokumentierte Cold-/Warm-Bytes, Einsparung, Original-/Restore-SHA‑256 und Berichts-Hash | Historische lokale Berichte; Felder auf innere Konsistenz geprüft |
| 29 Nachweiseinträge | Datenpfade, Wiederherstellung, Integrität, Live-/WAN-Berichte, Kompatibilität und lokale Vergleiche | Historisches Register mit unterschiedlichem Nachweisumfang |
| Roundtrip vom 14.10.2026 | Kaggle-generierte Eingabe → lokaler Rhodium-Lauf → dokumentierte Wiederherstellung | Lokaler PASS dokumentiert; unabhängige Rückprüfung auf Kaggle offen |

Die Sammlungen überschneiden sich. **29 + 25 sind keine 54 unabhängigen Benchmarks.** Diese Veröffentlichung ist keine Bestätigung eines vollständig ausgelesenen historischen Archivs oder eines unabhängig geprüften Gesamtsystems.

## Beispiele aus den gespeicherten lokalen Berichten

| Datensatz | Original | Cold: übertragene Bytes | Cold-Einsparung | Warm: übertragene Bytes | Warm-Einsparung |
|---|---:|---:|---:|---:|---:|
| Blackbox / Matrix local 64 MiB | 67.108.864 B | 33.869.410 B | 49,5306 % | 5.827 B | 99,9913 % |
| Matrix local 8 GiB | 8.589.934.592 B | 4.334.824.636 B | 49,5360 % | 696.713 B | 99,9919 % |
| Robotics AGIBOT sample 64 MiB | 67.108.864 B | 67.018.034 B | 0,1353 % | 5.827 B | 99,9913 % |

Alle drei Zeilen enthalten in den gespeicherten Berichten übereinstimmende Original-/Restore-SHA‑256. Sie zeigen auch, dass die Cold-Einsparung vom Datensatz abhängt. **Warm nutzt vorhandenen Zustand am Empfänger und ist kein Ersttransfer.** Die Byte-Messpunkte sind testspezifisch; ein Warm-Wert ist keine allgemeine Kompressionsgarantie.

→ [Alle 25 Datensätze mit vollständigen SHA‑256-Werten](benchmarks/RHODIUM-PUBLIC-BENCHMARK-RESULTS-AND-SHA256.md)

## Was das für Kunden bedeutet

Bei wiederkehrenden oder ähnlichen Daten können geringere Übertragungsmengen Bandbreite und Übertragungsaufwand reduzieren. Die tatsächliche Ersparnis hängt von Daten, Empfängerzustand und Messgrenze ab. Ob daraus im eigenen Betrieb Zeit- oder Kostenvorteile entstehen, muss am eigenen Anwendungsfall gemessen werden.

Die Veröffentlichung unterscheidet Übertragungsmengen, Ereignisfilterung, Verarbeitungsdurchsatz und Build-/Kompatibilitätstests. Diese Größen werden nicht zu einer gemeinsamen Leistungszahl zusammengerechnet. Produktnamen und Datenquellen bezeichnen den jeweiligen Testkontext, keine Kundenbeziehung oder Empfehlung durch den genannten Anbieter.

## So lassen sich die Nachweise einordnen und prüfen

1. Datensatz in der [Ergebnistabelle](benchmarks/RHODIUM-PUBLIC-BENCHMARK-RESULTS-AND-SHA256.md) oder im [Familienregister](benchmarks/RHODIUM-PUBLIC-BENCHMARK-FAMILY.csv) auswählen.
2. In [Prüfstatus und Grenzen](EVIDENCE-STATUS.md) nachlesen, ob ein historischer Bericht, eine Konsistenzprüfung oder eine unabhängige Reproduktion vorliegt.
3. Bytewerte und Prozentrechnung mit der [Prüfanleitung](PUBLIC-BENCHMARK-VERIFICATION.md) nachvollziehen.
4. Für eine unabhängige Inhaltsprüfung Original und zurückgelieferte Datei separat vergleichen. Ein veröffentlichter Hash allein ersetzt diese Prüfung nicht.

## English overview

Rhodium Germany publishes historical measurements for transfer volume, reconstruction and integrity. This repository contains **25 SHA-distinct local best-of records**, **29 benchmark/proof/validation entries**, and a machine-readable local roundtrip record. Entries overlap and are not a count of independent benchmark executions.

Cold and warm results are stated separately. Warm results use prior receiver state. Stored matching hashes and report checks are distinguished from independent payload verification. The returned artifact from the Kaggle-generated-input roundtrip has **not yet completed independent Kaggle verification**.

Start with the [results](benchmarks/RHODIUM-PUBLIC-BENCHMARK-RESULTS-AND-SHA256.md), [evidence status](EVIDENCE-STATUS.md), [data dictionary](benchmarks/DATA-DICTIONARY.md) and [verification guide](PUBLIC-BENCHMARK-VERIFICATION.md).

## Projekt und Veröffentlichungsumfang

**Rhodium Germany · Kai Kuhnert**  
Website: [rhodium-germany.de](https://rhodium-germany.de)  
Dokumentationsstand: **15.10.2026**. Datensatzdatum und Laufdatum sind getrennt zu betrachten.

Veröffentlicht werden Ergebnisse, Referenzen und ausdrücklich freigegebene Prüfhilfen. Der proprietäre Kern, interne Verfahren, Schlüssel und Kundeneingaben gehören nicht zu dieser Veröffentlichung. Siehe [Veröffentlichungsrichtlinie](PUBLIC-DISCLOSURE-POLICY.md). Es wird keine neue Lizenz für Software oder zugrunde liegende Eingabedaten erteilt; siehe [Nutzung und Datenherkunft](benchmarks/DATA-DICTIONARY.md#use-and-provenance).
