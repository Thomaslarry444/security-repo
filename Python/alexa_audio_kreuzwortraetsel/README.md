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

Damit testest du den echten Rätselablauf lokal per Tastatur-Eingabe (ohne Alexa Cloud). `run_local.py` ist also nicht nur Deko, sondern ein voll nutzbarer lokaler Spielmodus.


## Schwierigkeit erhöhen

Aktuell gibt es drei Stufen im Code:

- `leicht`
- `mittel`
- `schwer`

Im lokalen Runner wählst du die Stufe direkt beim Start.

Beispiel:

```bash
cd Python/alexa_audio_kreuzwortraetsel
python3 run_local.py
# dann im Prompt: schwer
```

Für Alexa (Lambda) wird aktuell standardmäßig `mittel` geladen. Du kannst später leicht erweitern, z. B. mit einem eigenen `DifficultyIntent`, der `CrosswordGame.with_sample_puzzle("schwer")` startet.

## macOS: Python-Environment sauber aufsetzen (empfohlen)

### 1) Python prüfen

```bash
python3 --version
```

Wenn Python fehlt, installiere es z. B. mit Homebrew:

```bash
brew install python
```

### 2) In den Repo-Ordner wechseln

```bash
cd /pfad/zu/deinem/repo/Uniteststore
```

### 3) Virtuelle Umgebung anlegen

```bash
python3 -m venv .venv
```

### 4) Virtuelle Umgebung aktivieren

```bash
source .venv/bin/activate
```

### 5) Abhängigkeiten installieren

Wichtig: `requirements.txt` liegt **nicht** im Repo-Root, sondern in `Python/alexa_audio_kreuzwortraetsel`.

```bash
python -m pip install --upgrade pip
python -m pip install -r Python/alexa_audio_kreuzwortraetsel/requirements.txt
python -m pip install pytest
```

### 6) Tests ausführen (aus dem Repo-Root)

```bash
PYTHONPATH=. pytest -q Python/alexa_audio_kreuzwortraetsel/tests
```

Alternative (wenn du lieber in den Projektordner wechselst):

```bash
cd Python/alexa_audio_kreuzwortraetsel
pytest -q
python run_local.py
```

### 7) Umgebung später verlassen

```bash
deactivate
```

## Häufige Fehler (genau wie in deinem Log)

- `pythonpython3: command not found`
  - Das war nur ein Tippfehler. Richtig ist: `python3 -m venv .venv`
- `Could not open requirements file: requirements.txt`
  - Du warst im Repo-Root. Nutze den Pfad:
    `python -m pip install -r Python/alexa_audio_kreuzwortraetsel/requirements.txt`
- `ModuleNotFoundError: No module named 'engine'`
  - Tritt auf, wenn Tests aus einem anderen Arbeitsordner laufen. Die Tests wurden so angepasst, dass sie das Projektverzeichnis selbst finden.

## Ist der Ordner schon in dein Git-Repo gepusht?

Das kannst du lokal so prüfen:

```bash
# Zeigt den letzten lokalen Commit
git log --oneline -n 1

# Zeigt, ob dein Branch vor/hinter origin liegt
git status -sb

# Zeigt, ob der Ordner im aktuellen Commit enthalten ist
git ls-tree --name-only -r HEAD | grep 'Python/alexa_audio_kreuzwortraetsel'
```

Wenn `git status -sb` z. B. `ahead 1` zeigt, ist es **lokal committed**, aber noch nicht auf Remote gepusht.
Dann pushst du mit:

```bash
git push origin <dein-branch>
```

## Inhalt

- `run_local.py`: Lokaler CLI-Start (für IDE und schnelles Testen).
- `lambda_function.py`: Alexa-Handler für Launch, Antwort, Hinweis und Hilfe.
- `engine.py`: Reine Rätsel-Logik (lokal testbar).
- `skill-interaction-model.json`: Beispiel-Intents für die Alexa Developer Console.
- `tests/test_engine.py`: Unit-Tests für die Rätsel-Logik.

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
