# Audio-Kreuzworträtsel für Alexa (Python)

Dieses Beispiel zeigt, wie du ein barrierearmes, sprachbasiertes Kreuzworträtsel mit Alexa bauen kannst.

## Wo kann ich das Script selbst starten?

Ja, du kannst es direkt in deiner IDE starten (z. B. VS Code, PyCharm, Thonny):

1. Projektordner öffnen: `Python/alexa_audio_kreuzwortraetsel`
2. Datei `run_local.py` als Startdatei auswählen
3. Script ausführen (Run/Start)

Oder im Terminal:

```bash
cd Python/alexa_audio_kreuzwortraetsel
python3 run_local.py
```

Damit testest du den Rätselablauf lokal per Tastatur-Eingabe (ohne Alexa Cloud).

## Inhalt

- `run_local.py`: Lokaler CLI-Start (für IDE und schnelles Testen).
- `lambda_function.py`: Alexa-Handler für Launch, Antwort, Hinweis und Hilfe.
- `engine.py`: Reine Rätsel-Logik (lokal testbar).
- `skill-interaction-model.json`: Beispiel-Intents für die Alexa Developer Console.
- `tests/test_engine.py`: Unit-Tests für die Rätsel-Logik.

## Lokal testen

```bash
cd Python/alexa_audio_kreuzwortraetsel
python3 -m pip install -r requirements.txt
python3 -m pip install pytest
PYTHONPATH=. pytest -q
python3 run_local.py
```

## Deployment zu Alexa (Kurzfassung)

1. In der Alexa Developer Console einen **Custom Skill** anlegen.
2. Das Interaction Model aus `skill-interaction-model.json` importieren.
3. AWS Lambda (Python 3.11) erstellen und den Inhalt von `lambda_function.py` + `engine.py` deployen.
4. Abhängigkeit `ask-sdk-core` als Lambda Layer oder im Deployment-Paket mitliefern.
5. Skill-Endpunkt mit der Lambda-Funktion verbinden.

## Hinweise zur Barrierefreiheit

- Sprich langsam (im Code per SSML gesetzt).
- Biete klare Sprachbefehle: „Hinweis“, „Wiederholen“, „Stop“.
- Speichere Fortschritt später in DynamoDB, damit Sitzungen fortsetzbar sind.
