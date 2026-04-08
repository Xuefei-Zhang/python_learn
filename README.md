# Python Mastery Lab

A staged learning workspace for mastering Python through manual implementation, tests, and small systems experiments.

## What this repository is

This repository is not a finished Python project. It is a learning lab designed to help you grow from basic Python familiarity into a stronger engineer through:

- manual implementation of core exercises
- phase-by-phase progression
- small experiments and systems modules
- tests, notes, and complexity analysis

The current repository state is intentionally scaffold-first:

- the project structure is already set up
- the learning missions are already written
- Phase 0 placeholder code and tests are present
- the real exercise logic is still left for you to implement manually

## Current status

Right now the repository is in **Phase 0 setup complete** state.

That means:

- the repo structure is ready
- smoke tests pass
- Phase 0 learner exercises exist as placeholders
- Phase 0 exercise tests exist, but are skipped by default until you are ready to start
- later phases are described, but should not be implemented yet

## Repository structure

### Top-level directories

- `core/`
  - foundational learner code
  - currently contains `foundation_utils.py`, which is a Phase 0 manual exercise placeholder

- `runtime/`
  - future experiments for Python mechanisms such as iterators, generators, decorators, and context managers
  - currently only contains package scaffolding

- `systems/`
  - small practical modules built on top of earlier learning phases
  - currently contains `mission_tracker.py`, which is a Phase 0 manual exercise placeholder

- `tests/`
  - repository tests
  - contains:
    - `test_smoke.py` for scaffold verification
    - `tests/core/test_foundation_utils.py` for Phase 0 utility exercises
    - `tests/systems/test_mission_tracker.py` for Phase 0 tracker exercise

- `missions/`
  - phase documents describing what each stage is supposed to teach
  - `phase-00-foundations.md` is the one you should read first
  - `phase-01` to `phase-06` are future stages and should not be entered early

- `notes/`
  - learner notes
  - `notes/complexity/phase-00-foundations.md` is where you record complexity analysis for Phase 0
  - `notes/interview/` is reserved for later interview explanations

- `benchmarks/`
  - reserved for future performance experiments
  - currently placeholder only

- `playground/`
  - reserved for quick experiments and throwaway checks
  - currently placeholder only

- `docs/`
  - project design and planning documents
  - useful if you want to understand the long-term architecture of the learning system

## Important files

- `README.md`
  - this document

- `pyproject.toml`
  - project metadata and pytest configuration
  - important because it allows imports from the repo root during test runs

- `tests/test_smoke.py`
  - verifies that the repository scaffold and Phase 0 framework files exist
  - this is the safest first test to run

- `missions/phase-00-foundations.md`
  - the main Phase 0 guide
  - explains workflow, manual boundaries, and exit criteria

- `core/foundation_utils.py`
  - Phase 0 placeholder file
  - you are expected to implement the functions manually

- `systems/mission_tracker.py`
  - another Phase 0 placeholder file
  - you are expected to implement the class manually

- `tests/core/test_foundation_utils.py`
  - opt-in Phase 0 tests for `chunk_list` and `count_vowels`

- `tests/systems/test_mission_tracker.py`
  - opt-in Phase 0 tests for `MissionTracker`

## Build and test system

This repo does not have a complex build pipeline yet.

At the moment, the main execution system is simply:

- Python package layout
- pytest
- phase documents
- manual learner workflow

### Pytest behavior

The current pytest config in `pyproject.toml` is:

- `testpaths = ["tests"]`
- `python_files = ["test_*.py"]`
- `pythonpath = ["."]`
- `addopts = "-q"`

What this means in practice:

- running `pytest` from the repository root is the normal workflow
- tests are discovered from `tests/`
- import paths like `from core.foundation_utils import ...` work correctly
- output is quieter by default

## What passes right now

From the current scaffold state:

- smoke tests pass
- Phase 0 exercise tests are skipped by default

So a normal run currently looks like this conceptually:

- scaffold tests: pass
- learner exercise tests: skipped until you opt in

## Recommended workflow for Phase 0

Follow this order.

### Step 1: Read the mission

Open:

- `missions/phase-00-foundations.md`

This file tells you:

- what Phase 0 is teaching
- which files are yours to implement
- what the acceptance checklist is

### Step 2: Confirm the scaffold is healthy

Run:

```bash
pytest tests/test_smoke.py -v
```

This verifies that the repository structure is correct before you start coding.

### Step 3: Choose one Phase 0 exercise

There are currently two Phase 0 learner targets:

1. `systems/mission_tracker.py`
2. `core/foundation_utils.py`

I recommend doing `MissionTracker` first because it is smaller and helps you get used to the workflow.

### Step 4: Unskip the test for the exercise you want to do

Both Phase 0 exercise test files currently contain a module-level skip marker like this:

```python
pytestmark = pytest.mark.skip(...)
```

That skip exists on purpose so the repository stays green before you start.

When you are ready, remove or replace that skip marker in exactly one exercise test file.

### Step 5: Run the targeted test and watch it fail

Examples:

```bash
pytest tests/systems/test_mission_tracker.py -v
```

or

```bash
pytest tests/core/test_foundation_utils.py -v
```

You want the test to fail for the expected reason, because the placeholder implementation currently raises `NotImplementedError`.

### Step 6: Implement manually

Now edit the matching learner file:

- `systems/mission_tracker.py`
- or `core/foundation_utils.py`

Important: these files are intentionally placeholders. The learning value comes from you writing the real logic yourself.

### Step 7: Re-run the same targeted test until it passes

Do not jump directly to later phases.

The correct loop is:

- unskip one exercise
- run its tests
- implement manually
- re-run until green
- move to the next Phase 0 exercise

### Step 8: Fill in the complexity note

After finishing the utility functions, update:

- `notes/complexity/phase-00-foundations.md`

You should record:

- time complexity
- space complexity
- your reasoning

### Step 9: Check the Phase 0 exit criteria

Go back to:

- `missions/phase-00-foundations.md`

Make sure you can honestly say:

- the manual exercise code works
- the tests pass
- you understand the structure of the repo
- you can explain the complexity tradeoffs

## Why later phase files already exist

You will see files like:

- `missions/phase-01-linear-structures.md`
- `missions/phase-02-hash-and-cache.md`
- ... up to Phase 6

These are there so the whole project has a visible roadmap.

They are **not** a signal that you should start implementing those phases now.

The intended progression is:

- finish Phase 0 manually
- confirm Phase 0 is complete
- only then start scaffolding or implementing Phase 1

## Manual-learning conventions in this repo

This repository follows a few important rules:

1. **Core learning code is intentionally not pre-solved**
   - placeholder files with `NotImplementedError` are part of the design

2. **Tests can be opt-in on purpose**
   - some learner tests are skipped until you are ready to work on them

3. **Progress is phase-gated**
   - you should not move to the next phase until the current phase is actually complete

4. **Notes are part of the learning system**
   - complexity explanations and later interview notes are first-class outputs, not optional extras

## Useful commands

Run all currently active tests:

```bash
pytest
```

Run only scaffold verification:

```bash
pytest tests/test_smoke.py -v
```

Run only the tracker exercise once you unskip it:

```bash
pytest tests/systems/test_mission_tracker.py -v
```

Run only the utility exercise once you unskip it:

```bash
pytest tests/core/test_foundation_utils.py -v
```

## If you feel confused about where to start

Start here, in this exact order:

1. read `missions/phase-00-foundations.md`
2. run `pytest tests/test_smoke.py -v`
3. open `tests/systems/test_mission_tracker.py`
4. unskip it
5. implement `systems/mission_tracker.py`
6. make its tests pass
7. then repeat the same process for `core/foundation_utils.py`

That is the intended current workflow for this repository.
