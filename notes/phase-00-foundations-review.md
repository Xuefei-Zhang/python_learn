---
title: Phase 00 Foundations Review
date: 2026-04-10
tags:
  - python
  - phase-00
  - review
  - mission-tracker
aliases:
  - Phase 0 Review
  - MissionTracker Review
---

# Phase 00 Foundations Review

This note collects the main concepts that came up while manually working through `[[missions/phase-00-foundations|Phase 00 Foundations Mission]]`, especially around `[[systems/mission_tracker.py]]`.

Use it as a repetition note after finishing the experiment, not as a replacement for hand-implementing the code.

## What this phase is trying to train

Phase 0 is not mainly about solving a hard algorithm. It is about building a stable mental model for:

- how Python files and modules are organized
- how functions and methods receive input and return output
- how built-in data structures behave
- how object state works inside a class
- how tests define the behavior contract
- how to protect internal mutable data from accidental outside mutation

If these basics feel fuzzy, later phases will feel much harder than they should.

## The real role of `MissionTracker`

`MissionTracker` is a very small class, but it teaches several important things at once:

- class syntax
- `__init__`
- `self`
- dictionary storage
- list mutation with `append`
- method design
- safe return values

The class is essentially storing this relationship:

```python
phase_name -> list of mission items
```

A concrete example looks like this:

```python
{
    "phase-00": ["finish variables review", "practice scopes"],
    "phase-01": ["implement stack"]
}
```

That is why the storage type is written like this:

```python
self.phase: dict[str, list[str]] = {}
```

Read it from right to left:

- `{}` means the actual starting value is an empty dictionary
- `dict[str, list[str]]` means each key should be a string and each value should be a list of strings

## Why there is a colon after the variable name

In Python, this form:

```python
name: SomeType = value
```

means:

- `name` is the variable
- `SomeType` is the type hint
- `value` is the actual assigned value

Example:

```python
count: int = 0
name: str = "alice"
items: list[str] = []
```

This does **not** mean Python becomes a strict compile-time typed language like C++ or Rust.

It means:

- readers can understand the expected data shape
- editors can give better completion and warnings
- static tools can catch mistakes earlier
- your own thinking becomes clearer

## Type expression vs real runtime value

One of the easiest beginner mistakes is confusing a **type description** with a **real value**.

These are different things:

```python
dict[str, list[str]]
```

and:

```python
{}
```

The first one is only describing the shape.
The second one is the actual object created at runtime.

The full line combines both:

```python
self.phase: dict[str, list[str]] = {}
```

A good mental model is:

> “Create an empty dictionary now, and document that it is supposed to map strings to lists of strings.”

## Understanding `self`

Inside a class, `self` refers to the current object instance.

Example:

```python
tracker = MissionTracker()
```

When the object is created, `__init__` runs, and:

```python
self.phase = {}
```

means the object now owns an internal dictionary.

So when you later write:

```python
self.phase[phase]
```

you are saying:

> “Go into this object’s internal storage, look up the entry for this phase.”

## Why `add()` has to initialize before append

This code is the key:

```python
if phase not in self.phase:
    self.phase[phase] = []
self.phase[phase].append(item)
```

This happens in two stages.

### Stage 1: make sure the key exists

If the phase has never appeared before, the dictionary has no list stored under that key yet.
So we create one:

```python
self.phase[phase] = []
```

### Stage 2: append into that list

Now the key definitely exists, so:

```python
self.phase[phase]
```

is a list.

That is why this works:

```python
self.phase[phase].append(item)
```

A concrete example:

```python
self.phase = {}
phase = "phase-00"
item = "practice scopes"
```

After the `if` block:

```python
self.phase == {"phase-00": []}
```

After append:

```python
self.phase == {"phase-00": ["practice scopes"]}
```

## Why `.append()` sometimes did not show up in completion

The logic was fine. The likely problem was not the Python code itself, but editor tooling.

We already checked that the local Python LSP setup was not healthy in this environment, so completion quality was unreliable.

That matters because editor completion is only a helper. It is not the source of truth.

The source of truth is still your reasoning about the data shape:

- `self.phase` is a dictionary
- `self.phase[phase]` is a list
- lists have `.append(...)`

## `dict.get()` explained with the real code

This line is very important:

```python
self.phase.get(phase, [])
```

General form:

```python
dictionary.get(key, default_value)
```

Meaning:

- if `key` exists, return its value
- if `key` does not exist, return `default_value`

Example:

```python
store = {"phase-00": ["setup"]}

store.get("phase-00", [])   # returns ["setup"]
store.get("phase-01", [])   # returns []
```

This is different from:

```python
store["phase-01"]
```

because direct indexing would raise a `KeyError` if the key does not exist.

So `get()` is a safer lookup when “missing key” is a normal case.

## Why `items()` returns `list(...)`

The method is:

```python
return list(self.phase.get(phase, []))
```

There are two ideas inside it.

### Idea 1: unknown phase should return an empty list

If the phase has never been added, return `[]`.

### Idea 2: return a copy, not the internal original list

This is the subtle but important part.

If the code were:

```python
return self.phase.get(phase, [])
```

then outside code might receive the exact same internal list object.

Example:

```python
snapshot = tracker.items("phase-00")
snapshot.append("mutated outside")
```

If `snapshot` is the original list, then the internal tracker data is accidentally modified from the outside.

That breaks encapsulation.

By writing:

```python
return list(self.phase.get(phase, []))
```

Python creates a new list object.
The caller can change that returned list without changing the tracker’s internal storage.

This is what the test means by **copy-safety**.

## Does Python have pointers?

Python does not expose C/C++-style pointer syntax.
You do not manually work with memory addresses and dereference operators.

But Python variables still behave like **references to objects**.

Example:

```python
a = [1, 2]
b = a
b.append(3)
```

Now `a` is also:

```python
[1, 2, 3]
```

because `a` and `b` refer to the same list object.

So the practical mental model is:

- Python has no explicit pointer programming interface for normal code
- Python variables do refer to objects
- mutable objects can be changed through any reference to them

That is exactly why defensive copying matters in `MissionTracker`.

## Built-in collection reminders from this exercise

### `[]`

Most commonly means a list literal:

```python
items = []
items = [1, 2, 3]
```

It is also used for indexing and slicing:

```python
items[0]
text[1:4]
```

### `()`

Can mean:

- function call
- tuple
- grouping in expressions

Examples:

```python
print("hi")
point = (3, 5)
value = (1 + 2) * 3
```

### `{}`

Most commonly means a dictionary literal:

```python
mapping = {}
mapping = {"a": 1}
```

An empty `{}` is a dictionary, not a set.

A set needs values inside or an explicit constructor:

```python
letters = {"a", "b"}
empty_set = set()
```

## Mistakes that came up during hand implementation

These were the real conceptual mistakes hidden inside the broken lines.

### 1. Using a type name where a runtime variable was needed

Wrong direction:

```python
self.phase[str]
```

Why it is wrong:

- `str` is the type object
- you actually wanted the method parameter `phase`

Correct direction:

```python
self.phase[phase]
```

### 2. Assuming a key already exists in the dictionary

Wrong mental model:

> “I can append immediately.”

Correct mental model:

> “I can append only after the dictionary already has a list at this key.”

### 3. Using non-Python ideas like `empty`

Python does not have a built-in value named `empty` for this case.
Instead, you usually check with:

```python
if phase not in self.phase:
```

or compare against actual values like `[]` if needed.

### 4. Returning the wrong attribute

Wrong direction:

```python
return self.item[str]
```

This mixes up:

- the attribute name
- the key being looked up
- the actual storage shape

The correct question is:

> “Where is the data actually stored?”

In this class, it is stored in `self.phase`.

### 5. Mixing syntax problems with logic problems

Sometimes the code failed because the Python syntax itself was invalid.
Other times the syntax was fine but the data reasoning was wrong.

These are different categories of bugs:

- **syntax bug**: Python cannot parse the code
- **logic bug**: Python runs it, but it does the wrong thing

Learning to separate those two is a big step.

## How the tests define the contract

The tests are not just there to say pass/fail. They tell you exactly what behavior the class must have.

From `[[tests/systems/test_mission_tracker.py]]`, the contract is:

1. `add(phase, item)` should store an item under that phase
2. `items(phase)` should return the stored list for known phases
3. unknown phases should return `[]`
4. `items()` should return a copy, not the original mutable internal list

This is why reading the test first is such an important habit.

## The final data-flow picture

When you call:

```python
tracker.add("phase-00", "practice scopes")
```

this is the conceptual flow:

1. check whether `"phase-00"` already exists in the dictionary
2. if not, create an empty list for it
3. append the new item to that list

Then when you call:

```python
tracker.items("phase-00")
```

this is the conceptual flow:

1. safely look up that phase with `get`
2. fall back to `[]` if it does not exist
3. wrap in `list(...)` to return a copy

## Small self-check questions

Try answering these without looking at the solution.

1. Why is the storage type `dict[str, list[str]]` instead of `list[str]`?
2. Why can `self.phase[phase].append(item)` only happen after initialization?
3. What is the difference between `self.phase[phase]` and `self.phase.get(phase, [])`?
4. Why is `return list(...)` safer than returning the internal list directly?
5. Why can two Python variables affect the same list object?
6. Why is `str` different from the variable `phase`?

## What to review next in Phase 0

After `MissionTracker`, the next useful review area is `[[core/foundation_utils.py]]`.

That file should reinforce:

- function inputs and outputs
- input validation
- iteration patterns
- choosing the right built-in collection
- simple time and space complexity explanations

## `foundation_utils.py` is the other half of Phase 0

`[[core/foundation_utils.py]]` is still intentionally a manual exercise placeholder.

It contains two functions:

```python
def chunk_list(items: list[int], size: int) -> list[list[int]]:
    ...


def count_vowels(text: str) -> int:
    ...
```

These functions matter because they teach the non-class side of Python basics:

- plain function contracts
- input validation
- iteration over lists and strings
- building new return values
- using tests to define edge cases

So Phase 0 is really split into two complementary learning modes:

- `MissionTracker` teaches object state and methods
- `foundation_utils.py` teaches standalone function reasoning

## `chunk_list` contract and edge cases

The tests in `[[tests/core/test_foundation_utils.py]]` define the real contract.

What `chunk_list` must do:

- split the input list into sublists of at most `size`
- return a **new** nested list
- return `[]` for empty input
- raise `ValueError` when `size <= 0`

Examples from the test contract:

```python
chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
chunk_list([], 3) == []
chunk_list([1, 2], 5) == [[1, 2]]
```

The key ideas this function should teach you are:

- validation belongs near the start of the function
- you usually build a result list step by step
- the last chunk may be shorter than the others
- returning a value is different from mutating the input list

### Why the invalid-size case matters

This test is especially important:

```python
with pytest.raises(ValueError):
    chunk_list([1, 2, 3], 0)
```

It teaches a very important habit:

> invalid input should fail intentionally, not accidentally.

That is the difference between a function that merely “works sometimes” and a function with a clear contract.

## `count_vowels` contract and edge cases

`count_vowels` looks simple, but it teaches several core habits.

The contract from the tests is:

- count standard English vowels
- return an integer
- handle the empty string correctly

Examples:

```python
count_vowels("algorithm") == 3
count_vowels("") == 0
```

The important learning points are:

- iterating through a string one character at a time
- using an accumulator such as `count`
- checking membership against a vowel collection
- returning the computed result instead of printing

This is also a good place to compare collection choices.

For example, this is a natural pattern:

```python
vowels = {"a", "e", "i", "o", "u"}
```

because the job is a membership check:

```python
if char in vowels:
    ...
```

So this tiny function quietly teaches both iteration and data-structure choice.

## The actual pytest workflow in this repo

Phase 0 is not only about writing code. It is also about learning the repository workflow.

The intended loop is:

1. read `[[missions/phase-00-foundations|Phase 00 Foundations Mission]]`
2. run smoke tests first
3. unskip one learner test module
4. run the targeted tests
5. implement manually
6. re-run until green
7. fill in the complexity note

### Current Phase 0 status snapshot

Right now, the repo is in this state:

- `[[tests/systems/test_mission_tracker.py]]` is effectively active because the skip marker is commented out
- `[[tests/core/test_foundation_utils.py]]` is still skipped on purpose
- `[[core/foundation_utils.py]]` still raises `NotImplementedError`

That means the current learner progression is still phase-safe:

- one Phase 0 exercise has been activated
- the second one is still waiting for manual work

### Why the tests start skipped

The skip markers are not a hack. They are part of the teaching design.

They keep the repository green before you begin the exercise, while still preserving the behavior contract for when you are ready.

That means the test files are doing two jobs at once:

- keeping the repo stable before manual work starts
- defining what success looks like once you opt in

## Why `pythonpath = ["."]` matters here

In `[[pyproject.toml]]`, the pytest config includes:

```toml
pythonpath = ["."]
```

This matters because tests import modules like:

```python
from core.foundation_utils import chunk_list
from systems.mission_tracker import MissionTracker
```

For those imports to work cleanly when running `pytest` from the repo root, Python needs the repository root on its import path.

So this line supports the normal Phase 0 workflow:

```bash
pytest tests/systems/test_mission_tracker.py -v
pytest tests/core/test_foundation_utils.py -v
```

Without the correct import path setup, beginner confusion goes up for the wrong reason.

This repo intentionally removes that friction.

## Modules vs packages in this repo

Phase 0 also teaches the difference between a module and a package through the real repository structure.

### Module

A module is usually one `.py` file.

Examples in this repo:

- `[[systems/mission_tracker.py]]`
- `[[core/foundation_utils.py]]`
- `[[tests/systems/test_mission_tracker.py]]`

### Package

A package is a directory Python can import from.

In this repo, package-style directories include:

- `core/`
- `systems/`
- `tests/`

The `__init__.py` files help mark those directories as packages and reinforce import structure.

So when you write:

```python
from systems.mission_tracker import MissionTracker
```

you are importing from:

- package: `systems`
- module: `mission_tracker`
- class: `MissionTracker`

That is a very important layering idea for later phases.

## Phase-gated learning design

One of the easiest things to miss is that Phase 0 is intentionally scaffolded, not unfinished by accident.

The placeholders, skipped tests, mission files, and note files all work together as a learning system.

The design idea is:

- framework first
- learner implementation second
- phase progression third

That is why later phases may already have documents, but you should not jump into them early.

This is not a normal product repository.
It is a controlled practice environment.

So if something seems "not fully implemented yet," the first question should be:

> “Is this intentionally left for the learner?”

In Phase 0, the answer is often yes.

## Phase 0 complexity map

`[[notes/complexity/phase-00-foundations|Phase 00 Complexity Note]]` is the formal place for final complexity writeups.

But it is useful to keep a simple preview table here while studying.

| Item | Likely Time | Likely Space | Why |
|---|---|---|---|
| `MissionTracker.add` | Usually constant per add | Usually constant extra per add | Dictionary lookup/update plus one list append |
| `MissionTracker.items` | Linear in items for that phase | Linear in items for that phase | `list(...)` creates a copy of the stored list |
| `chunk_list` | Linear in input length | Linear in output size | You walk the list and build new chunks |
| `count_vowels` | Linear in string length | Usually constant extra space | You scan characters once and keep a small counter |

This table is intentionally phrased as a learning aid.

When you finish your manual implementations, you should still write the final reasoning in `[[notes/complexity/phase-00-foundations|Phase 00 Complexity Note]]` yourself.

## A repeatable Phase 0 study loop

If you want to use this note for repeated review, use this checklist.

- [ ] Explain what `MissionTracker` stores without looking at the code
- [ ] Explain why `items()` returns `list(...)` instead of the raw internal list
- [ ] Explain what `dict.get(key, default)` does
- [ ] Explain why `chunk_list(..., 0)` should raise `ValueError`
- [ ] Explain how `count_vowels` should work without writing code yet
- [ ] Explain the difference between a module and a package in this repo
- [ ] Explain why some Phase 0 tests start skipped
- [ ] Explain why `pythonpath = ["."]` helps pytest imports
- [ ] Explain the likely time and space complexity of all four Phase 0 targets

If you can answer these clearly from memory, your Phase 0 foundation is getting solid.

## Official references

- Python Tutorial: https://docs.python.org/3/tutorial/index.html
- Python Built-in Types: https://docs.python.org/3/library/stdtypes.html
- `dict.get`: https://docs.python.org/3/library/stdtypes.html#dict.get
- Python Classes: https://docs.python.org/3/tutorial/classes.html
- `typing`: https://docs.python.org/3/library/typing.html
- Python FAQ on arguments and object behavior: https://docs.python.org/3/faq/programming.html

## Related files

- [[missions/phase-00-foundations|Phase 00 Foundations Mission]]
- [[docs/2026-04-09-phase-00-foundations-guide|Phase 00 Foundations Guide]]
- [[systems/mission_tracker.py]]
- [[tests/systems/test_mission_tracker.py]]
- [[notes/complexity/phase-00-foundations|Phase 00 Complexity Note]]
