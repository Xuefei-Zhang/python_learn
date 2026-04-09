---
title: Phase 00 Foundations Guide
date: 2026-04-09
tags:
  - python
  - phase-00
  - foundations
  - learning-guide
aliases:
  - Python Phase 0 Guide
---

# Phase 00 Foundations Guide

## What this phase is really about

Phase 0 is not just "review some basics". It is the phase where you build the mental model that will support everything later.

If Phase 0 is weak, later phases become painful because you will be fighting both:

- the data structure problem itself
- the Python syntax and runtime behavior needed to express it

So the real goal of this phase is to move from:

- "I can write some Python"

to:

- "I understand how Python code is organized, how functions and modules work, how to reason about basic data, and how to verify my code with tests"

## What you need to master in this phase

This phase focuses on five knowledge clusters:

1. module and package organization
2. function design
3. built-in collections
4. test workflow with pytest
5. basic complexity analysis

---

## 1. Module and package organization

### What is a module?

In Python, a module is usually one `.py` file.

For example:

- `systems/mission_tracker.py`
- `core/foundation_utils.py`

Each of these files is a module.

A module lets you group related code in one place.

### What is a package?

A package is a directory that Python treats as importable code.

In this repo:

- `core/`
- `systems/`
- `runtime/`
- `tests/`

are packages because they contain `__init__.py`.

That means code like this works:

```python
from core.foundation_utils import chunk_list
from systems.mission_tracker import MissionTracker
```

### Why does this matter?

When you move to later phases, you will stop writing everything in one file. You need to know:

- where code should live
- how files relate to each other
- how imports work
- how tests find your code

### Rule of thumb

- one file = one coherent responsibility
- `core/` = foundational reusable code
- `systems/` = small practical modules built on top of those foundations
- `tests/` = behavior verification
- `missions/` = what to do
- `notes/` = what you learned

### Common beginner confusion

#### Confusion 1: "Why not write everything in one file?"

Because later, the project becomes unreadable and untestable.

#### Confusion 2: "Why do we need `__init__.py`?"

Because it helps Python recognize directories as packages and supports clean imports.

#### Confusion 3: "Why does pytest sometimes fail to import my code?"

Because Python needs the repo root on its import path. In this repo, `pyproject.toml` already sets:

```toml
pythonpath = ["."]
```

That is why `pytest` from repo root works.

---

## 2. Function design

Functions are the smallest reliable unit of logic in this phase.

You need to understand:

- parameters
- return values
- scope
- validation
- side effects

### Parameters

A parameter is input to a function.

Example:

```python
def count_vowels(text: str) -> int:
    ...
```

Here:

- `text` is a parameter
- `str` is the expected input type

Another example:

```python
def chunk_list(items: list[int], size: int) -> list[list[int]]:
    ...
```

This function needs two pieces of input:

- a list
- a chunk size

### Return values

A function should return a result instead of only printing things.

Bad example:

```python
def add(a, b):
    print(a + b)
```

Better example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Why is this better?

Because return values are reusable. Tests can verify them. Other functions can consume them.

### Scope

Scope answers: where does a variable exist?

Example:

```python
def demo() -> int:
    x = 10
    return x
```

`x` only exists inside `demo`.

This is called local scope.

A common beginner bug is trying to use a local variable outside the function.

### Validation

Good functions defend their assumptions.

For example, `chunk_list` should reject invalid chunk sizes:

```python
if size <= 0:
    raise ValueError("size must be positive")
```

This matters because:

- your code becomes safer
- tests become clearer
- edge cases are handled intentionally

### Side effects

A side effect means the function changes something outside its own local result.

Examples of side effects:

- modifying a list in place
- changing object state
- writing a file
- printing

Not all side effects are bad. But in this phase, you should clearly know when a function:

- returns a new value
- mutates existing data

---

## 3. Built-in collections

You must know the practical difference between:

- `list`
- `tuple`
- `dict`
- `set`

### `list`

Ordered, mutable sequence.

Example:

```python
items = [1, 2, 3]
items.append(4)
```

Use `list` when:

- order matters
- duplicates are allowed
- you need append/remove/indexing

### `tuple`

Ordered, usually used as immutable grouped data.

Example:

```python
point = (3, 5)
```

Use `tuple` when:

- the data should not change
- you want a fixed-size grouping

### `dict`

Key-value mapping.

Example:

```python
scores = {"alice": 95, "bob": 88}
print(scores["alice"])
```

Use `dict` when:

- you need fast lookup by key
- the data has named associations

### `set`

Unordered collection of unique values.

Example:

```python
letters = {"a", "e", "i", "o", "u"}
```

Use `set` when:

- uniqueness matters
- membership testing matters

### Practical comparison

Suppose you want to count vowels.

You could write:

```python
vowels = {"a", "e", "i", "o", "u"}
count = 0
for char in text.lower():
    if char in vowels:
        count += 1
```

Why is a `set` a good choice here?

Because membership checks like `char in vowels` are conceptually what the structure is for.

### Common confusion

#### `list` vs `tuple`

- `list` changes easily
- `tuple` is for stable grouped values

#### `dict` vs `set`

- `dict` stores key -> value
- `set` stores just unique values

#### "Why not always use list?"

Because different structures communicate different intent and give different performance tradeoffs.

---

## 4. Type hints

You already see hints like this in the repo:

```python
def count_vowels(text: str) -> int:
```

This does not force Python at runtime in the same way some languages do, but it helps:

- readers understand expectations
- editors provide better suggestions
- static tools catch mistakes
- your own thinking becomes clearer

### Basic examples

```python
def greet(name: str) -> str:
    return f"Hello, {name}"


def total(values: list[int]) -> int:
    return sum(values)
```

### Why they matter in this repo

Later phases become more abstract. Without type hints, your code will become much harder to reason about.

---

## 5. Classes and object state

Phase 0 includes `MissionTracker`, so you need the basics of classes.

### What is a class?

A class is a blueprint for objects.

Example:

```python
class Counter:
    def __init__(self) -> None:
        self.value = 0

    def increment(self) -> None:
        self.value += 1
```

### `__init__`

`__init__` runs when an object is created.

```python
tracker = MissionTracker()
```

That means `MissionTracker.__init__()` runs.

### `self`

`self` refers to the current object instance.

Example:

```python
self._store = {}
```

means:

- this object has internal storage
- every instance can keep its own data

### Why `MissionTracker` matters

It teaches you:

- object state
- methods
- data mutation
- returning safe copies

One of the tests checks copy-safety. That means if you return a list to the outside world, the caller should not accidentally mutate your internal storage.

Conceptually:

```python
return list(self._store.get(phase, []))
```

is safer than returning the exact internal list object.

---

## 6. pytest workflow

This repo uses `pytest` as the verification tool.

### What pytest does here

- discovers tests in `tests/`
- runs functions whose names start with `test_`
- shows pass/fail information

### Current repo behavior

If you run:

```bash
pytest
```

right now, you get:

- scaffold tests passing
- Phase 0 learner tests skipped

That is intentional.

### Why are some tests skipped?

Because the repo is designed to stay green before you start a manual exercise.

In the Phase 0 test files you will see:

```python
pytestmark = pytest.mark.skip(reason="...")
```

That means:

- pytest sees the test file
- but chooses not to execute those tests yet

### Your actual workflow

1. choose one exercise
2. remove the skip marker for that exercise
3. run its tests
4. watch them fail
5. implement manually
6. run them again until they pass

This is a beginner-friendly form of test-driven learning.

---

## 7. Basic complexity analysis

You do not need advanced algorithm theory yet, but you do need the habit of asking:

- how many steps does this take as input grows?
- how much extra memory does this use?

### Time complexity intuition

#### `count_vowels`

If you scan every character once, the work grows with the length of the string.

That is why the time complexity is usually described as linear in input size.

#### `chunk_list`

If you walk through the list and build chunks, the total work also grows with the number of elements.

Again, that is usually linear.

### Space complexity intuition

- if you create a new result list, that uses extra memory
- if you only count with one integer, that uses very little extra memory

### What matters for Phase 0

You should be able to say things like:

- "This function touches each input element once, so the time grows linearly."
- "This function builds a new nested list, so it uses extra memory proportional to the output size."

That is already a good start.

---

## How this phase connects to your current tasks

### `MissionTracker`

This exercise teaches:

- class basics
- internal state
- methods
- dictionary usage
- defensive copying
- simple test-driven workflow

### `chunk_list`

This exercise teaches:

- iteration
- input validation
- list construction
- returning structured output
- simple complexity explanation

### `count_vowels`

This exercise teaches:

- string traversal
- membership checks
- basic accumulator patterns
- choosing a useful built-in collection

---

## Common mistakes in this phase

### Mistake 1: Writing code before reading the test

The test is telling you the contract. Read it first.

### Mistake 2: Returning internal mutable state directly

If outside code can mutate your internals, bugs become hard to understand.

### Mistake 3: Ignoring invalid input

If `chunk_list(..., 0)` is invalid, handle it explicitly.

### Mistake 4: Confusing printing with returning

Tests usually check returned values, not terminal output.

### Mistake 5: Jumping to Phase 1 too early

If Phase 0 still feels shaky, later data structures will feel much harder than they need to.

---

## Self-check questions

Try to answer these without looking anything up.

1. What is the difference between a module and a package?
2. Why does this repo have `__init__.py` files?
3. When should you use `list` vs `set`?
4. Why is it useful to return a copy instead of internal storage?
5. What is the difference between a parameter and a return value?
6. Why do the Phase 0 test files start as skipped?
7. Why does `pythonpath = ["."]` matter in `pyproject.toml`?
8. What does it mean to say a function is linear in input size?

If you can explain these clearly, you are building the right base.

---

## Suggested learning order for you right now

1. Read `missions/phase-00-foundations.md`
2. Read this guide once without coding
3. Open `tests/systems/test_mission_tracker.py`
4. Unskip it
5. Implement `systems/mission_tracker.py`
6. Make the tests pass
7. Repeat for `core/foundation_utils.py`
8. Fill in `notes/complexity/phase-00-foundations.md`

That is the correct way to use this phase.

## Official references

- Python Tutorial: https://docs.python.org/3/tutorial/index.html
- Python Data Model: https://docs.python.org/3/reference/datamodel.html
- Built-in Types: https://docs.python.org/3/library/stdtypes.html
- typing: https://docs.python.org/3/library/typing.html
