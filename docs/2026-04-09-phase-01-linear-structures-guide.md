---
title: Phase 01 Linear Structures Guide
date: 2026-04-09
tags:
  - python
  - phase-01
  - data-structures
  - learning-guide
aliases:
  - Python Phase 1 Guide
---

# Phase 01 Linear Structures Guide

## What this phase is really about

Phase 1 is where you stop thinking of Python as only a scripting language and start thinking like a data structure engineer.

The structures in this phase look simple:

- Dynamic Array
- Singly Linked List
- Doubly Linked List
- Stack
- Queue
- Deque

But they teach very deep ideas:

- how data is organized
- how access patterns affect performance
- how interfaces hide implementation details
- how one structure can be built on top of another

This phase is also where object-oriented design starts becoming more concrete.

---

## Core knowledge you need in this phase

1. sequential data organization
2. indexing vs traversal
3. mutation operations and their cost
4. basic class design
5. iteration protocol awareness
6. representation and debugging helpers

---

## 1. Sequential data organization

A linear structure stores elements in a sequence.

That means every element has some notion of:

- previous / next
- position
- insertion order

### Two major models

#### Array-style model

Data is conceptually stored by position.

You usually get:

- fast indexing
- easy append at the end
- harder insertion/removal in the middle

#### Linked model

Data is connected node by node.

You usually get:

- easy local insertion/removal when you already have the node position
- no cheap direct indexing
- more pointer/reference management

This distinction is one of the most important mental models in data structures.

---

## 2. Dynamic Array

### What it is

A Dynamic Array behaves like a resizable array.

Python's built-in `list` already acts like this at a high level, but here you implement the idea manually to understand the tradeoffs.

### Core operations

- append
- indexing
- length
- resizing when capacity is full

### Why it matters

A Dynamic Array teaches you:

- amortized thinking
- contiguous-style storage mental model
- why appending is usually cheap but not always free

### The key idea: capacity vs size

These are not the same.

- size = how many elements are actually stored
- capacity = how many elements can be stored before resize is needed

### Why append is often called amortized O(1)

Most appends do not resize.
Only occasional appends trigger a resize and copy existing elements.

So one operation can be expensive, but many appends together average out well.

### Example intuition

If capacity is 4 and size is 4, appending one more element may require:

1. allocate bigger storage
2. copy 4 existing elements
3. store the new element

That append is expensive.
But if the next several appends do not resize, their average cost stays low.

---

## 3. Linked Lists

### Singly Linked List

Each node points to the next node.

Conceptually:

```text
A -> B -> C -> None
```

Each node usually stores:

- a value
- a reference to the next node

### Doubly Linked List

Each node points both ways.

Conceptually:

```text
None <- A <-> B <-> C -> None
```

Each node usually stores:

- a value
- previous reference
- next reference

### Why linked lists matter

They teach you to reason about:

- local rewiring of references
- head/tail edge cases
- traversal cost
- node-based design

### Common edge cases

- empty list
- one-element list
- removing the head
- removing the tail
- removing a middle node

If you do not think clearly about edge cases, linked list implementations become buggy quickly.

---

## 4. Stack

A Stack follows:

- last in, first out
n
Examples of stack-like behavior:

- undo systems
- function call stacks
- expression parsing

### Core operations

- push
- pop
- peek/top

### Why Stack is important

It teaches restricted interfaces.

Even if a Stack is built using another structure underneath, the public contract is intentionally narrow.

That is a valuable engineering idea: expose only the operations that fit the abstraction.

---

## 5. Queue

A Queue follows:

- first in, first out

Examples:

- task scheduling
- print jobs
- request processing

### Core operations

- enqueue
- dequeue
- peek/front

### Why Queue matters

It teaches ordered processing and why data structure choice should reflect workflow semantics.

If the system means "who came first gets handled first", Queue is a strong fit.

---

## 6. Deque

Deque means double-ended queue.

It supports operations at both ends.

### Typical operations

- push left
- push right
- pop left
- pop right

### Why it matters

It is a flexible abstraction between Stack and Queue.

It teaches you that sometimes a structure is valuable not because it is totally different, but because it gives you a more expressive interface.

---

## 7. Class design in this phase

Phase 1 is where class design becomes real.

You should start thinking about each structure in terms of:

- constructor
- internal storage
- public methods
- error behavior
- readable representation

### Example mindset

For a stack, ask:

- what should users be allowed to do?
- what internal details should stay private?
- what happens when pop is called on an empty stack?

That is already software design, not just coding.

---

## 8. `__repr__` and debugging friendliness

When building data structures, debugging gets easier if objects print clearly.

Example idea:

```python
def __repr__(self) -> str:
    return f"Stack(size={self._size})"
```

You do not need fancy formatting at first. The point is to make debugging less painful.

---

## 9. Iterable awareness

Some of your structures may become iterable later.

That means Python can loop over them:

```python
for item in structure:
    ...
```

You do not need to master the full iterator protocol yet, but you should start noticing that user-defined structures can feel more Pythonic when they support familiar operations.

This becomes much more important in Phase 5.

---

## 10. Complexity thinking in this phase

You should start building operation-by-operation complexity intuition.

### Dynamic Array

Typical reasoning:

- indexing: fast
- append: usually cheap, occasionally resize-heavy
- insert in middle: expensive because later elements must shift

### Linked List

Typical reasoning:

- indexing by position: slow because traversal is needed
- insert at known node/head: can be cheap
- traversal: linear

### Stack and Queue

Typical reasoning:

- operations at the chosen end(s) should be cheap if implementation fits the abstraction

The point is not memorizing symbols. The point is being able to explain the cause of the cost.

---

## How this phase connects to your future mini-systems

### Expression evaluator

This typically makes Stack feel real.

Because parentheses and operator handling often require "most recent unfinished thing first" behavior.

### Task queue simulator

This makes Queue feel real.

Because it models "first submitted, first processed" naturally.

That connection matters: data structures are not just interview toys. They encode workflow rules.

---

## Common mistakes in this phase

### Mistake 1: Mixing abstraction and implementation

Do not expose internal node details unless users truly need them.

### Mistake 2: Forgetting empty-structure cases

Most data structure bugs hide there.

### Mistake 3: Confusing position-based access with traversal-based access

Arrays and linked lists do not behave the same way.

### Mistake 4: Treating all appends/inserts/removes as equally expensive

The cost depends on the underlying structure.

### Mistake 5: Writing the structure without thinking about its public contract

Ask what the API should feel like, not just how to store values.

---

## Self-check questions

1. Why is a Dynamic Array different from a Linked List?
2. Why can append be amortized O(1) in an array-like structure?
3. Why is indexing easy in arrays but not in linked lists?
4. Why is a Stack not just "a list with different method names" conceptually?
5. When is Queue a better abstraction than Stack?
6. What extra power does a Deque provide?
7. What edge cases make linked list code hard?
8. How would you explain to an interviewer when to prefer a linked list over an array-backed structure?

## Official references

- Python Data Model: https://docs.python.org/3/reference/datamodel.html
- Built-in Types: https://docs.python.org/3/library/stdtypes.html
- Python Tutorial, Classes: https://docs.python.org/3/tutorial/classes.html
