---
title: Phase 04 Graphs and Scheduling Guide
date: 2026-04-09
tags:
  - python
  - phase-04
  - graphs
  - learning-guide
aliases:
  - Python Phase 4 Guide
---

# Phase 04 Graphs and Scheduling Guide

## What this phase is really about

Phase 4 is where you move from local structures to relationship systems.

A graph is about connection:

- what depends on what
- what leads to what
- how one node reaches another
- what the cheapest path is

This phase matters because many real engineering systems are not just containers of data. They are networks of relationships.

Examples:

- build systems
- dependency graphs
- route finding
- workflow engines
- job scheduling

---

## Core knowledge you need in this phase

1. graph modeling
2. graph representation
3. traversal strategies
4. dependency ordering
5. shortest-path intuition
6. scheduling applications
7. state tracking during search

---

## 1. What is a graph?

A graph is a set of:

- nodes (things)
- edges (relationships)

That is the simplest mental model.

Examples:

- cities = nodes, roads = edges
- tasks = nodes, dependencies = edges
- users = nodes, follows = edges

### Why graphs matter

Graphs let you represent systems where relationship is the main point.

If the key question is:

- what connects to what?

then a graph is often the right mental model.

---

## 2. Directed vs undirected graphs

### Directed graph

An edge has direction.

Example:

- Task A must happen before Task B

This is not symmetrical.

### Undirected graph

An edge simply means connection.

Example:

- two cities are directly connected

This often goes both ways conceptually.

### Why this matters

The graph type changes what algorithms mean.

Topological sorting only makes sense in directed dependency-like contexts.

---

## 3. Graph representation

The two most common mental models are:

- adjacency list
- adjacency matrix

### Adjacency list

Store neighbors for each node.

This is usually the most natural for sparse graphs and is often the best starting point in learner implementations.

### Adjacency matrix

Store connection presence/cost in a 2D grid.

This is conceptually simple for some problems, but often heavier.

### Why representation matters

The representation affects:

- memory usage
- iteration behavior
- algorithm simplicity

This is a recurring engineering lesson: representation choices shape algorithm cost.

---

## 4. BFS

BFS means Breadth-First Search.

It explores layer by layer.

Mental model:

- start here
- visit all immediate neighbors
- then all neighbors of those
- and so on

### Why BFS matters

BFS is useful when you care about:

- shortest path in an unweighted graph
- minimum number of steps
- layer-based exploration

### Data structure connection

BFS usually relies on a Queue.

That is why your earlier phases matter.

---

## 5. DFS

DFS means Depth-First Search.

It explores one path deeply before backing up.

Mental model:

- go as far as possible
- then backtrack
- then try another branch

### Why DFS matters

DFS is useful for:

- exploring reachability
- recursive graph/tree reasoning
- detecting structure properties
- backtracking-style search

### Data structure connection

DFS can be expressed using:

- recursion
- or an explicit Stack

Again, earlier phases feed into this one.

---

## 6. Visited state

In graphs, unlike simple trees, cycles are common.

That means you cannot always keep revisiting nodes blindly.

So graph traversal usually needs a "visited" concept.

This is where your Hash Set intuition becomes valuable.

### Why it matters

Without visited tracking, traversal can:

- loop forever
- repeat work unnecessarily
- produce wrong results

---

## 7. Topological Sort

Topological Sort is about ordering nodes so dependencies are respected.

Typical meaning:

- if A must come before B, then A appears earlier in the result

### Why this matters

This is directly useful for:

- task scheduling
- build pipelines
- prerequisite planning
- workflow ordering

### Important idea

Topological sorting assumes a dependency graph without cycles.

If a cycle exists, the dependency rules are contradictory for simple linear execution order.

That is an important engineering insight: some systems are invalid, not just incomplete.

---

## 8. Dijkstra

Dijkstra is for shortest-path problems with non-negative edge costs.

Mental question:

- what is the cheapest known path to each node so far?

### Why it matters

This teaches you that traversal is not always enough.
Sometimes you need cost-aware search.

### Data structure connection

Dijkstra usually benefits from a Priority Queue.

That is why Heap/Priority Queue from Phase 3 matters now.

---

## 9. Graphs in scheduling systems

This phase is not only about algorithms for interviews. It is also about real workflow modeling.

### Dependency scheduler

If task B depends on A, you can model that as a directed edge.

Then topological reasoning tells you whether there is a valid execution order.

### Path-finding experiment

If edges carry costs or distances, shortest-path reasoning becomes practical.

This is how algorithmic ideas start feeling like system design tools.

---

## 10. Python concepts connected to this phase

### Generators and `yield`

A traversal can be expressed as a generator.

That means instead of building a whole result list immediately, you can yield nodes one by one.

This matters because traversal is often naturally sequential.

### Callable objects and closures

As workflow/scheduling ideas grow, you may start representing steps as callables or wrapping behavior in closures.

That makes this phase a bridge between algorithmic thinking and runtime abstraction.

---

## 11. Complexity intuition in this phase

When analyzing graph algorithms, ask:

- how many nodes can be visited?
- how many edges can be checked?
- does the structure revisit work?
- does it depend on path cost updates?

Do not reduce everything to one memorized phrase. Explain what the algorithm must inspect and why.

---

## 12. How this phase connects to your experiments

### Dependency scheduler

This teaches:

- directed dependency modeling
- cycle reasoning
- valid execution ordering

### Path finder

This teaches:

- path cost reasoning
- search strategy selection
- how "shortest" depends on the exact problem definition

---

## Common mistakes in this phase

### Mistake 1: Choosing BFS when costs matter

BFS is not the answer to every path question.

### Mistake 2: Forgetting visited tracking

Graphs often cycle.

### Mistake 3: Using the wrong graph representation without thinking

Representation shapes both speed and code complexity.

### Mistake 4: Ignoring cycle behavior in dependency problems

A cyclic dependency is often a design problem, not just a traversal inconvenience.

### Mistake 5: Treating graphs as just another tree

Graphs are more general and more dangerous because repeated connections and cycles exist.

---

## Self-check questions

1. What is the difference between a directed and undirected graph?
2. Why is visited tracking important?
3. When is BFS a good fit?
4. When is DFS a good fit?
5. What problem does Topological Sort solve?
6. Why does a cycle matter in a dependency graph?
7. Why does Dijkstra need cost-aware behavior?
8. How do Queue, Stack, Hash Set, and Priority Queue all reappear in this phase?

## Official references

- Python Tutorial: https://docs.python.org/3/tutorial/index.html
- Built-in Types: https://docs.python.org/3/library/stdtypes.html
- Data Model: https://docs.python.org/3/reference/datamodel.html
- Generators: https://docs.python.org/3/tutorial/classes.html#generators
