"""Rätsel-Engine für ein sprachbasiertes Kreuzworträtsel."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class Clue:
    clue_id: str
    direction: str
    number: int
    clue_text: str
    answer: str


class CrosswordGame:
    """Hält den Rätselzustand und prüft Antworten."""

    def __init__(self, clues: List[Clue], difficulty: str = "mittel") -> None:
        self._clues: Dict[str, Clue] = {clue.clue_id: clue for clue in clues}
        self._progress: Dict[str, str] = {}
        self.difficulty = difficulty

    @classmethod
    def with_sample_puzzle(cls, difficulty: str = "mittel") -> "CrosswordGame":
        puzzles: Dict[str, List[Clue]] = {
            "leicht": [
                Clue("W1", "waagerecht", 1, "Beliebter Sprachassistent von Amazon", "alexa"),
                Clue("S1", "senkrecht", 1, "Gegenteil von dunkel", "hell"),
                Clue("W2", "waagerecht", 2, "Gerät mit dem man hört", "radio"),
            ],
            "mittel": [
                Clue("W1", "waagerecht", 1, "Programmiersprache dieser App", "python"),
                Clue("S1", "senkrecht", 1, "Cloud-Dienst für Alexa-Backend", "lambda"),
                Clue("W2", "waagerecht", 2, "Sprachbefehl zum Beenden", "stop"),
                Clue("S2", "senkrecht", 2, "Kurzer Tipp zum Rätsel", "hinweis"),
            ],
            "schwer": [
                Clue("W1", "waagerecht", 1, "Persistente AWS-NoSQL-Datenbank", "dynamodb"),
                Clue("S1", "senkrecht", 1, "Strukturierte Sprach-Ausgabe in Alexa", "ssml"),
                Clue("W2", "waagerecht", 2, "Automatische Spracherkennung", "intent"),
                Clue("S2", "senkrecht", 2, "Wiederverwendbare Softwarekomponente", "modul"),
                Clue("W3", "waagerecht", 3, "Schnittstelle zum Testen ohne GUI", "konsole"),
            ],
        }
        selected = puzzles.get(difficulty.lower(), puzzles["mittel"])
        normalized = difficulty.lower() if difficulty.lower() in puzzles else "mittel"
        return cls(selected, difficulty=normalized)

    def list_open_clues(self) -> List[Clue]:
        return [clue for clue_id, clue in self._clues.items() if clue_id not in self._progress]

    def next_open_clue(self) -> Optional[Clue]:
        open_clues = self.list_open_clues()
        return open_clues[0] if open_clues else None

    def format_clue(self, clue: Clue) -> str:
        return f"{clue.direction.capitalize()} {clue.number}: {clue.clue_text}."

    def check_answer(self, clue_id: str, spoken_answer: str) -> bool:
        clue = self._clues[clue_id]
        normalized = spoken_answer.strip().lower()
        if normalized == clue.answer:
            self._progress[clue_id] = normalized
            return True
        return False

    def solved_count(self) -> int:
        return len(self._progress)

    def total_count(self) -> int:
        return len(self._clues)

    def is_finished(self) -> bool:
        return self.solved_count() == self.total_count()

    def hint_for(self, clue_id: str) -> str:
        clue = self._clues[clue_id]
        return f"Das Wort hat {len(clue.answer)} Buchstaben und beginnt mit {clue.answer[0].upper()}."
