"""Rätsel-Engine für ein sprachbasiertes Kreuzworträtsel."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
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
                Clue("W1", "waagerecht", 1, "Hauptstadt von Deutschland", "berlin"),
                Clue("S1", "senkrecht", 1, "Gemeinsame Währung vieler EU-Staaten", "euro"),
                Clue("W2", "waagerecht", 2, "Name des Reformators Martin ...", "luther"),
            ],
            "mittel": [
                Clue("W1", "waagerecht", 1, "Vertrag von 1992 als Meilenstein der EU", "maastricht"),
                Clue("S1", "senkrecht", 1, "Staatsform Deutschlands", "demokratie"),
                Clue("W2", "waagerecht", 2, "Gründungsjahr der Bundesrepublik", "1949"),
                Clue("S2", "senkrecht", 2, "Wahlrecht für alle Erwachsenen", "allgemein"),
            ],
            "schwer": [
                Clue("W1", "waagerecht", 1, "Konferenz von 1938 zur Abtretung des Sudetenlands", "muenchen"),
                Clue("S1", "senkrecht", 1, "Widerstandsgruppe um Hans und Sophie Scholl", "weisserose"),
                Clue("W2", "waagerecht", 2, "Politik der Entspannung unter Willy Brandt", "ostpolitik"),
                Clue("S2", "senkrecht", 2, "Parlament der Europäischen Union", "euparlament"),
                Clue("W3", "waagerecht", 3, "Friedliche Revolution in der DDR im Jahr", "1989"),
            ],
        }
        selected = puzzles.get(difficulty.lower(), puzzles["mittel"])
        normalized = difficulty.lower() if difficulty.lower() in puzzles else "mittel"
        return cls(selected, difficulty=normalized)

    @classmethod
    def from_json_file(cls, json_path: str | Path, difficulty: str = "dynamisch") -> "CrosswordGame":
        data = json.loads(Path(json_path).read_text(encoding="utf-8"))
        clues = [
            Clue(
                clue_id=item["clue_id"],
                direction=item["direction"],
                number=int(item["number"]),
                clue_text=item["clue_text"],
                answer=str(item["answer"]).strip().lower(),
            )
            for item in data
        ]
        return cls(clues, difficulty=difficulty)

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
