---
title: Phase 00 Foundations Complexity Notes
date: 2026-04-10
tags:
  - notes
  - complexity
  - phase-00
aliases:
  - Phase 0 Complexity
---

# Phase 00 Foundations Complexity Notes

Use this note while you finish the manual implementations.

This file is for complexity-focused review, not for replacing your own reasoning work.

Use `[[notes/phase-00-foundations-review|Phase 00 Foundations Review]]` for the broader concepts, and use this note to practice explaining time and space cost clearly.

## What complexity analysis means in Phase 0

At this stage, complexity analysis is not about advanced proofs.

It is about learning to ask:

- how many elements do I touch as input grows?
- do I build a new result object?
- am I storing extra data or just reusing a few variables?

That is enough to build the right habit.

## Quick mental model

When you estimate complexity in Phase 0, use this checklist:

1. Look at the main loop or traversal
2. Ask whether each element is visited once or many times
3. Ask whether the function builds a new result
4. Separate **time** from **space**
5. Explain the reason in plain English

Good beginner phrasing sounds like this:

> “This function walks the input once, so time grows linearly with input size.”

or:

> “This function builds a new output list, so extra space grows with the size of the returned data.”

## Functions to analyze

### `chunk_list`

Contract reminder from `[[tests/core/test_foundation_utils.py]]`:

- split a list into chunks of at most `size`
- return a **new** nested list
- return `[]` for empty input
- raise `ValueError` when `size <= 0`

Likely reasoning shape:

- you examine the input list from left to right
- each input element should end up in exactly one chunk
- the function builds a new nested list for the result

Study hint:

> If every element is processed once, the time is usually linear in the number of elements.

> If you build a brand new output structure containing those elements, the extra space usually scales with the output size.

Fill in after your implementation and after you can explain the logic in your own words:

- Time complexity:
- Space complexity:
- Why:

Example sentence starter:

- Time complexity: `O(?)`
- Space complexity: `O(?)`
- Why: “I iterate through the list ___ and create ___, so ___.”

### `count_vowels`

Contract reminder from `[[tests/core/test_foundation_utils.py]]`:

- count standard English vowels
- return the count as an integer
- handle `""` correctly

Likely reasoning shape:

- you scan the string character by character
- you keep a small counter
- you probably use a small fixed collection of vowels for membership tests

Study hint:

> If you scan each character once, time usually grows linearly with string length.

> If you only keep a counter and a tiny fixed vowel collection, the extra space is usually constant.

Fill in after your implementation:

- Time complexity:
- Space complexity:
- Why:

Example sentence starter:

- Time complexity: `O(?)`
- Space complexity: `O(?)`
- Why: “I check each character ___ and only keep ___, so ___.”

## Phase 0 mini complexity map

Even though this file officially asks for `chunk_list` and `count_vowels`, it helps to compare them with `MissionTracker` too.

| Item | Likely Time | Likely Space | Main reason |
|---|---|---|---|
| `MissionTracker.add` | Usually constant per call | Usually constant extra per call | One dictionary access/update and one list append |
| `MissionTracker.items` | Linear in items for that phase | Linear in items for that phase | `list(...)` copies the stored list |
| `chunk_list` | Linear in number of input items | Linear in output size | Touch each item and build a new nested list |
| `count_vowels` | Linear in string length | Usually constant extra space | Scan once and keep a small counter |

Important note:

These are learning-level summaries, not substitutes for your own final explanation.

## How to explain complexity in an interview

In interviews, avoid just saying `O(n)` with no reason.

Better pattern:

1. State what the function does at a high level
2. State how many times it touches the input
3. State whether it allocates new result memory
4. Then give time and space complexity

Example pattern for `chunk_list`:

> “I traverse the list once and place each element into exactly one output chunk. That makes the time linear in the input length. Because I build a new nested list for the return value, the extra space grows with the size of the produced output.”

Example pattern for `count_vowels`:

> “I scan the string once and increment a counter when a character is a vowel. That makes the time linear in the string length. I only keep a small counter and a fixed vowel collection, so the extra space is constant.”

## Common beginner mistakes in complexity analysis

### Mistake 1: saying the answer without describing the work

Bad:

- “This is `O(n)`.”

Better:

- “This is `O(n)` because it visits each input element once.”

### Mistake 2: confusing input size with output size

If a function builds a new structure, that usually affects space complexity.

### Mistake 3: mixing time and space together

Time answers:

> how much work is done?

Space answers:

> how much extra memory is allocated?

### Mistake 4: ignoring validation cost

For Phase 0 functions, validation is usually tiny compared with the main traversal.

For example, checking `size <= 0` is constant work.

## Fill-this-in-yourself block

After your manual implementation is complete, rewrite this section in your own words without copying the hints above.

### My final explanation for `chunk_list`

- Time complexity:
- Space complexity:
- My explanation:

### My final explanation for `count_vowels`

- Time complexity:
- Space complexity:
- My explanation:

## Reflection prompts

- Which built-in collection behaviors did you rely on?
- Where does input validation belong?
- How would you explain these solutions in an interview?

## Related files

- [[notes/phase-00-foundations-review|Phase 00 Foundations Review]]
- [[missions/phase-00-foundations|Phase 00 Foundations Mission]]
- [[core/foundation_utils.py]]
- [[tests/core/test_foundation_utils.py]]
- [[systems/mission_tracker.py]]
- [[tests/systems/test_mission_tracker.py]]
