---
title: Phase 00 Foundations Mission
tags:
  - missions
  - phase-00
  - python-foundations
---

# Phase 00 Foundations Mission

## Learning goals

- Understand basic module and package organization
- Review functions, parameters, return values, and scope
- Compare Python built-in collections at a practical level
- Build confidence writing and running tests
- Start explaining simple time and space complexity

## Manual coding boundaries

> [!warning]
> This phase is designed for manual implementation by the learner. The framework may provide tests, placeholders, and acceptance criteria, but the learner should write the main solution code.

## Structures or utilities to implement manually

- `MissionTracker` behavior implementation
- small utility functions such as list chunking and string analysis

## Experiment target

Build a minimal CLI-oriented learning tracker and a few basic utility functions that are fully covered by tests.

## Implementation workflow

1. Read the placeholder contracts in `systems/mission_tracker.py` and `core/foundation_utils.py`
2. Open the opt-in tests in `tests/systems/test_mission_tracker.py` and `tests/core/test_foundation_utils.py`
3. Remove the module-level `pytestmark = pytest.mark.skip(...)` marker when you are ready to work on that exercise
4. Run the targeted test file and watch it fail for the expected reason
5. Implement the code manually
6. Re-run the same tests until they pass
7. Fill in `notes/complexity/phase-00-foundations.md`

## Manual acceptance checklist

- [ ] `MissionTracker` works for add / read / copy-safety behavior
- [ ] `chunk_list` handles normal and invalid inputs correctly
- [ ] `count_vowels` handles basic and empty-string inputs correctly
- [ ] You can explain the complexity of both utility functions
- [ ] You can explain why the repository is organized this way

## Exit criteria

- You can explain how the repository is organized
- You can run pytest successfully
- You have manually implemented the assigned Phase 0 targets
- You can explain at least one simple complexity tradeoff
