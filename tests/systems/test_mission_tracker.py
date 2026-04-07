"""Opt-in Phase 0 practice tests for MissionTracker.

These tests are intentionally skipped by default so the repository remains green
until the learner is ready to implement the exercise manually.
Remove or replace the module-level skip marker when you want to work on them.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.skip(reason="Phase 0 manual exercise: unskip when ready to implement")

from systems.mission_tracker import MissionTracker


def test_add_mission_item() -> None:
    tracker = MissionTracker()
    tracker.add("phase-00", "finish variables review")
    assert tracker.items("phase-00") == ["finish variables review"]


def test_items_for_unknown_phase_are_empty() -> None:
    tracker = MissionTracker()
    assert tracker.items("phase-00") == []


def test_items_returns_a_copy() -> None:
    tracker = MissionTracker()
    tracker.add("phase-00", "practice scopes")
    snapshot = tracker.items("phase-00")
    snapshot.append("mutated outside")
    assert tracker.items("phase-00") == ["practice scopes"]
