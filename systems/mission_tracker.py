"""Phase 0 manual exercise: implement MissionTracker yourself."""

from __future__ import annotations


class MissionTracker:
    """A tiny phase-based task tracker for learning exercises.

    Manual exercise boundary:
    - You should implement the behavior of this class yourself.
    - The framework intentionally provides only the interface contract.
    """

    def __init__(self) -> None:
        raise NotImplementedError("Manual exercise: implement MissionTracker.__init__")

    def add(self, phase: str, item: str) -> None:
        raise NotImplementedError("Manual exercise: implement MissionTracker.add")

    def items(self, phase: str) -> list[str]:
        raise NotImplementedError("Manual exercise: implement MissionTracker.items")
