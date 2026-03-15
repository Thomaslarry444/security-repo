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

    def __init__(self, clues: List[Clue]) -> None:
        self._clues: Dict[str, Clue] = {clue.clue_id: clue for clue in clues}
        self._progress: Dict[str, str] = {}

    @classmethod
    def with_sample_puzzle(cls) -> "CrosswordGame":
        return cls(
            [
                Clue(
                    clue_id="W1",
                    direction="waagerecht",
                    number=1,
                    clue_text="Beliebter Sprachassistent von Amazon",
                    answer="alexa",
                ),
                Clue(
                    clue_id="S1",
                    direction="senkrecht",
                    number=1,
                    clue_text="Gegenteil von dunkel",
                    answer="hell",
                ),
                Clue(
                    clue_id="W2",
                    direction="waagerecht",
                    number=2,
                    clue_text="Gerät mit dem man hört",
                    answer="radio",
                ),
            ]
        )

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
