# Interview Checklist — What to Check First

A quick reference distilled from the problems in this repo. The goal: before
writing any code, run through the right questions so you don't get burned by an
edge case or pick the wrong pattern.

> 🇷🇺 Russian version: [interview_checklist_ru.md](interview_checklist_ru.md)

---

## 0. Before you write a single line (any problem)

1. **Clarify the input.** Size of `n`? Value ranges? Negatives? Sorted? Are
   duplicates allowed? Can it be empty?
2. **Nail the edge cases out loud:** empty input, single element, all elements
   equal, min/max values, integer overflow.
3. **Output contract.** In-place vs return new? Index vs value? Order matters?
4. **Pick complexity from the constraints** (see the cheatsheet at the bottom):
   the size of `n` usually tells you what time complexity is expected.
5. **Say the brute force first, then optimize.** Get a correct baseline before
   reaching for the clever trick.

---

## 1. Arrays

**Check first:** sorted or not? duplicates allowed? in-place required? negatives?

**Go-to patterns:**
- Hashing for O(1) lookup → *Two Sum*
- Two pointers on a sorted / in-place array → *Move Zeroes*, *Remove Duplicates*
- Prefix sums / running totals
- Sliding window for subarray problems

**Common pitfalls:** off-by-one on bounds; mutating a list while iterating it;
integer overflow on sums/products.

---

## 2. Strings

**Check first:** ASCII vs Unicode? case-sensitive? leading/trailing whitespace?
empty string?

**Go-to patterns:**
- Frequency counter (`dict` / `collections.Counter`) → *First Unique Character*,
  *Isomorphic Strings*, *Palindrome Permutation*
- Two pointers from both ends → *Valid Palindrome II*
- Stack → *Valid Parentheses*, *Simplify Path*

**Common pitfalls:** *Reverse Integer* overflow (clamp to ±(2³¹−1)); strings are
immutable in Python, so build a `list` and `''.join()` at the end.

---

## 3. Linked lists

**Check first:** empty list? single node? could there be a cycle?

**Go-to patterns:**
- **Dummy head node** to simplify insert/delete at the head
- Fast & slow pointers → *Linked List Cycle*, finding the middle
- Reverse a (half of a) list in place → *Palindrome Linked List*

**Common pitfalls:** losing the reference to `next` before re-linking;
dereferencing `node.next` when `node` is `None`.

---

## 4. Trees

**Check first:** empty tree? single node? BST vs general binary tree? recursion
depth a concern?

**Go-to patterns:**
- DFS recursion → *Maximum Depth*, *Same Tree*
- **Range bounds** for BST validation, not just parent comparison → *Validate BST*
- BFS with `collections.deque` for level-order / mirror checks → *Symmetric Tree*
- Inorder traversal of a BST yields sorted values → *Inorder Traversal*

**Common pitfalls:** validating a BST by only comparing a node to its direct
parent (you need an inherited `(low, high)` range); deep recursion blowing the
stack on skewed trees.

---

## 5. Search & dynamic programming

**Check first:** is the array (or the answer space) monotonic → binary search?
Are there overlapping subproblems / optimal substructure → DP?

**Go-to patterns:**
- Binary search on a sorted array or on the answer → *Search Insert Position*,
  *Sqrt(x)*
- Bottom-up DP / memoization → *Climbing Stairs*, *Triangle*, *Pascal's Triangle*
- Cycle detection via a `set` of seen states → *Happy Number*

**Common pitfalls:** binary-search bound bugs (`lo <= hi` vs `lo < hi`, and how
you move `mid`); forgetting the base cases in DP.

---

## 6. SQL

**Check first:** can columns be NULL? duplicates? what is the **grain** of each
table (one row per what)? which join type keeps the rows you need?

**Go-to patterns:**
- Window functions (`ROW_NUMBER`, `RANK`, `FIRST_VALUE`) are usually **faster and
  cleaner** than a self-join + `GROUP BY` for "top N per group" problems
- CTEs (`WITH`) to break a query into readable steps
- `LEFT JOIN` + `COALESCE` to keep non-matching rows and default their values
- Interval / overlap logic (`a.start < b.end AND a.end > b.start`) → concurrent
  tasks, scheduling

**Common pitfalls:** `NOT IN` with a NULL in the subquery returns no rows (use
`NOT EXISTS`); every non-aggregated column must be in `GROUP BY`; `LEFT JOIN`
filters in the `WHERE` clause silently turn it into an inner join.

---

## 7. Advent of Code (parsing & simulation)

**Check first:** exact input format? grid bounds? 0-based vs 1-based indexing?

**Go-to patterns:**
- **Parse → simulate**: get clean data structures first, then run the rules
- Represent a grid as a `dict` keyed by `(row, col)` for sparse / unbounded grids
- BFS / DFS for shortest paths and reachability

**Repo convention:** every AoC script reads its input from `sys.argv[1]`, falling
back to `input.txt`. Run with `python aoc2024/aoc241.py my_input.txt`.

---

## Complexity cheatsheet (size of `n` → acceptable approach)

| `n` up to | Acceptable complexity | Typical technique |
|---|---|---|
| 10 | O(n!) | permutations / backtracking |
| 20 | O(2ⁿ) | bitmask / subset enumeration |
| 500 | O(n³) | triple loop / DP |
| 5,000 | O(n²) | double loop / DP |
| 1,000,000 | O(n log n) | sort, heap, divide & conquer |
| > 1,000,000 | O(n) / O(log n) | hashing, two pointers, binary search |

When in doubt, read the constraints first: they are a hint about the intended
solution's complexity.
