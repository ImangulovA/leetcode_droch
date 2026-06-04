# leetcode_droch

A personal practice repository for coding-interview preparation: LeetCode,
HackerRank, SQL drills, and Advent of Code. Solutions are mostly in **Python**
with a sizeable chunk of **SQL** (Presto / MySQL dialects).

The repo is organized by *practice track* rather than by difficulty, so each
folder maps to a kind of prep I was doing for a given interview loop.

---

## Repository layout

| Folder | What's inside | Main languages |
|---|---|---|
| [`top_interview_question/`](#top_interview_question) | Classic interview problems grouped by data structure, plus SQL collections | Python, SQL |
| [`lc25/`](#lc25) | LeetCode easy/medium set + HackerRank SQL | Python, SQL |
| [`aoc2022/`](#advent-of-code) | Advent of Code 2022, days 1-16 | Python |
| [`aoc2024/`](#advent-of-code) | Advent of Code 2024, days 1-19 | Python |

---

## top_interview_question

Problems grouped by the data structure / pattern they exercise.

### Arrays — [`arrayez/`](top_interview_question/arrayez)
- Two Sum (hashing)
- Remove Duplicates from Sorted Array (two pointers)
- Move Zeroes (two pointers, in-place)
- Plus One (array arithmetic / carry)
- Rotate Matrix (in-place rotation)
- Intersection of Two Arrays (sets / counting)
- Valid Sudoku (hashing, board validation)

### Linked lists — [`listsez/`](top_interview_question/listsez)
- Linked list fundamentals (`linkedlistez.py`)
- Linked List Cycle (Floyd's tortoise & hare)
- Palindrome Linked List (reverse half / two pointers)

### Strings — [`stringsez.py`](top_interview_question/stringsez.py)
- Reverse String / Reverse Integer (with overflow handling)
- First Unique Character (frequency counting)
- and other string-manipulation drills

### Trees — [`treesez.py`](top_interview_question/treesez.py)
- Maximum Depth (DFS recursion)
- Validate BST (range-bounded recursion)
- Symmetric Tree (BFS with `deque`)
- and other binary-tree traversals

### Algorithmic puzzles
- [`bus_correct.py`](top_interview_question/bus_correct.py) / `bus_incorrect.py` — divisor / prefix-sum puzzle (`accumulate`, `filterfalse`); the two files keep a buggy and a fixed version side by side
- [`count_user_events.py`](top_interview_question/count_user_events.py) — sessionization: collapse user events into sessions with a 30-minute inactivity gap

### SQL
- [`sql_leetcode.sql`](top_interview_question/sql_leetcode.sql) — ~35 LeetCode SQL problems (joins, aggregation, `GROUP BY`, `COALESCE`, self-joins). e.g. Rising Temperature, Average Time of Process per Machine, Students and Examinations, Managers with 5+ Direct Reports
- [`sql_leetcode_advanced.sql`](top_interview_question/sql_leetcode_advanced.sql) — ~35 harder problems with window functions (`ROW_NUMBER`, `RANK`, `FIRST_VALUE`), CTEs, and notes on the *more efficient* approach for each
- [`leetcode_hard_sql_problems/`](top_interview_question/leetcode_hard_sql_problems) — hard SQL (e.g. 3156 Employee Task Duration & Concurrent Tasks — interval overlap; 3103 Find Trending Hashtags II)
- [`contesthacker.sql`](top_interview_question/contesthacker.sql) — contest SQL

---

## lc25

A run through a LeetCode set (problem number in each filename). Topics covered:

- **Strings:** Roman to Integer (13), Longest Common Prefix (14), Valid
  Parentheses (20), Simplify Path (25, with `test_25_simplify_path.py`),
  Count and Say (38), Length of Last Word (58), Isomorphic Strings (205),
  Palindrome Permutation (266), Valid Palindrome II (680), Read N Characters
  Given Read4 (157)
- **Math / binary:** Add Binary (67), Sqrt(x) (69), Happy Number,
  Pascal's Triangle I/II (118/119)
- **Search / DP:** Search Insert Position (35), Climbing Stairs (70),
  Triangle (120)
- **Trees:** Same Tree (100), Binary Tree Inorder Traversal (94)
- **Linked lists:** Remove Duplicates from Sorted List (83)

### `lc25/hackerrank sql/`
- Maximum Swap (670) with `test_maximum_swap.py`
- Weather Observation Station (HackerRank SQL)
- `challenges.sql` / `challenges_optimized.sql` — a query and its tuned version

---

## Advent of Code

Pure-Python solutions, one file per day (parts split into `_p1` / `_p2` where
they diverge). Good practice for parsing, simulation, and grid/graph problems.

- [`aoc2022/`](aoc2022) — days 1-16
- [`aoc2024/`](aoc2024) — days 1-19

> Note: AoC files read their puzzle input from a local `input.txt` path that
> was hard-coded on the machine where they ran, so they won't execute as-is
> without pointing them at your own input.

---

## Topics & patterns at a glance

- **Patterns:** two pointers, hashing / frequency counting, sliding window,
  fast & slow pointers (cycle detection), prefix sums, recursion / DFS / BFS,
  dynamic programming, in-place array manipulation
- **Data structures:** arrays, strings, linked lists, binary trees, hash maps,
  sets, stacks, queues (`deque`)
- **SQL:** joins & self-joins, aggregation, window functions, CTEs, interval /
  overlap logic, query optimization
- **Languages:** Python 3, SQL (Presto / MySQL)
