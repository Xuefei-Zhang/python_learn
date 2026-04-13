"""Phase 0 manual exercise: implement MissionTracker yourself."""

from __future__ import annotations


class MissionTracker:
    """A tiny phase-based task tracker for learning exercises.

    Manual exercise boundary:
    - You should implement the behavior of this class yourself.
    - The framework intentionally provides only the interface contract.
    """

    def __init__(self) -> None:
        # self.phase = {}
        self.phase: dict[str, list[str]] = {}

    def add(self, phase: str, item: str) -> None:
        # if self.phase[phase] != empty:
        #     self.phase[str].
        if phase not in self.phase:
            self.phase[phase] = []
        self.phase[phase].append(item)

    def items(self, phase: str) -> list[str]:
        # return self.item[str]
        # used anther list for copy one outside function
        return list(self.phase.get(phase, []))
