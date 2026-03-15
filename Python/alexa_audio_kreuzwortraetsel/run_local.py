"""Lokaler CLI-Runner für das Audio-Kreuzworträtsel.

Damit kannst du den Spielablauf in jeder IDE testen,
ohne Alexa Developer Console oder AWS.
"""

from engine import CrosswordGame


def main() -> None:
    game = CrosswordGame.with_sample_puzzle()
    print("Audio-Kreuzworträtsel (lokal) gestartet. Tippe 'hilfe' für Befehle.")

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
