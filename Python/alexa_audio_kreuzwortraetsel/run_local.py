"""Lokaler CLI-Runner für das Audio-Kreuzworträtsel.

Damit kannst du den Spielablauf in jeder IDE testen,
ohne Alexa Developer Console oder AWS.
"""

from pathlib import Path

from engine import CrosswordGame


VALID_DIFFICULTIES = {"leicht", "mittel", "schwer"}


def select_difficulty() -> str:
    raw = input("Schwierigkeit wählen (leicht/mittel/schwer, Enter=mittel): ").strip().lower()
    if not raw:
        return "mittel"
    if raw not in VALID_DIFFICULTIES:
        print("Unbekannte Auswahl, wir nehmen 'mittel'.")
        return "mittel"
    return raw


def load_game() -> CrosswordGame:
    custom = input("Eigene Fragen aus JSON laden? (j/n, Enter=n): ").strip().lower()
    if custom == "j":
        default = "custom_questions.json"
        raw_path = input(f"Pfad zur JSON-Datei (Enter={default}): ").strip()
        json_path = raw_path or default
        file_path = Path(json_path)
        if not file_path.exists():
            print(f"Datei '{json_path}' nicht gefunden. Wir starten Standardfragen.")
            return CrosswordGame.with_sample_puzzle(select_difficulty())
        return CrosswordGame.from_json_file(file_path)

    return CrosswordGame.with_sample_puzzle(select_difficulty())


def main() -> None:
    game = load_game()
    print(f"\nAudio-Kreuzworträtsel gestartet (Schwierigkeit: {game.difficulty}).")
    print("Tippe 'hilfe' für Befehle.")

    while not game.is_finished():
        clue = game.next_open_clue()
        if clue is None:
            break

        print(f"\n{game.format_clue(clue)}")
        user_input = input("Deine Antwort (oder 'hinweis'/'ende'): ").strip()

        if user_input.lower() == "ende":
            print("Spiel beendet. Du kannst später neu starten.")
            return

        if user_input.lower() == "hilfe":
            print("Befehle: 'hinweis', 'ende' oder direkt die Lösung eingeben.")
            continue

        if user_input.lower() == "hinweis":
            print(game.hint_for(clue.clue_id))
            continue

        if game.check_answer(clue.clue_id, user_input):
            print("✅ Richtig!")
        else:
            print("❌ Nicht korrekt. Versuche es nochmal oder nutze 'hinweis'.")

    print("\n🎉 Super! Du hast alle Hinweise gelöst.")


if __name__ == "__main__":
    main()
