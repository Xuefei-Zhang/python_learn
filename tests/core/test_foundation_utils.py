"""Opt-in Phase 0 practice tests for foundational utility functions.

These tests are intentionally skipped by default so the repository remains green
until the learner is ready to implement the exercise manually.
Remove or replace the module-level skip marker when you want to work on them.
"""

from __future__ import annotations

import pytest

pytestmark = pytest.mark.skip(reason="Phase 0 manual exercise: unskip when ready to implement")

from core.foundation_utils import chunk_list, count_vowels


def test_chunk_list_basic() -> None:
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_chunk_list_empty_input() -> None:
    assert chunk_list([], 3) == []


def test_chunk_list_large_chunk_size() -> None:
    assert chunk_list([1, 2], 5) == [[1, 2]]


def test_chunk_list_invalid_size() -> None:
    with pytest.raises(ValueError):
        chunk_list([1, 2, 3], 0)


def test_count_vowels_basic() -> None:
    assert count_vowels("algorithm") == 3


def test_count_vowels_empty_string() -> None:
    assert count_vowels("") == 0
