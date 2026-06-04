# leetcode_droch

A personal practice repository for coding-interview preparation: LeetCode,
HackerRank, SQL drills, and Advent of Code. Solutions are mostly in **Python**
with a sizeable chunk of **SQL** (Presto / MySQL dialects).

The repo is organized by *practice track* rather than by difficulty, so each
folder maps to a kind of prep I was doing for a given interview loop.

### Conventions
- Files are named `NNN_snake_case.py` where `NNN` is the LeetCode/HackerRank
  problem number.
- Advent of Code files read their puzzle input from a path passed on the command
  line, falling back to `input.txt` in the current directory:
  ```bash
  python aoc2024/aoc241.py path/to/input.txt
  ```

---

## Repository layout

| Folder | What's inside | Languages |
|---|---|---|
| [`top_interview_question/`](#top_interview_question) | Classic interview problems grouped by data structure, plus SQL collections | Python, SQL |
| [`lc25/`](#lc25) | LeetCode easy/medium set + HackerRank SQL | Python, SQL |
| [`aoc2022/`](#advent-of-code) | Advent of Code 2022, days 1-16 | Python |
| [`aoc2024/`](#advent-of-code) | Advent of Code 2024, days 1-19 | Python |

---

## top_interview_question

Problems grouped by the data structure / pattern they exercise.

### Arrays — [`arrayez/`](top_interview_question/arrayez)
| Problem | Pattern |
|---|---|
| [Two Sum](top_interview_question/arrayez/two_sum.py) | hashing |
| [Remove Duplicates from Sorted Array](top_interview_question/arrayez/remove_duplicates_from_array.py) | two pointers |
| [Move Zeroes](top_interview_question/arrayez/move_zeroes.py) | two pointers, in-place |
| [Plus One](top_interview_question/arrayez/plus_one.py) | array arithmetic / carry |
| [Rotate Matrix](top_interview_question/arrayez/matrixrotate.py) | in-place rotation |
| [Intersection of Two Arrays](top_interview_question/arrayez/intersection_of_2_arrays.py) | sets / counting |
| [Valid Sudoku](top_interview_question/arrayez/validsudoku.py) | hashing, board validation |

### Linked lists — [`listsez/`](top_interview_question/listsez)
| Problem | Pattern |
|---|---|
| [Linked list fundamentals](top_interview_question/listsez/linkedlistez.py) | traversal, insert/delete |
| [Linked List Cycle](top_interview_question/listsez/linked_list_cycle.py) | fast & slow pointers |
| [Palindrome Linked List](top_interview_question/listsez/palindrome_linked_list.py) | reverse half / two pointers |

### Strings — [`stringsez.py`](top_interview_question/stringsez.py)
Reverse String, Reverse Integer (overflow handling), First Unique Character
(frequency counting), and other string-manipulation drills.

### Trees — [`treesez.py`](top_interview_question/treesez.py)
Maximum Depth (DFS recursion), Validate BST (range-bounded recursion),
Symmetric Tree (BFS with `deque`), and other binary-tree traversals.

### Algorithmic puzzles
| File | What it does |
|---|---|
| [`bus_correct.py`](top_interview_question/bus_correct.py) / [`bus_incorrect.py`](top_interview_question/bus_incorrect.py) | divisor / prefix-sum puzzle (`accumulate`, `filterfalse`); a buggy and a fixed version kept side by side |
| [`count_user_events.py`](top_interview_question/count_user_events.py) | sessionization: collapse user events into sessions with a 30-minute inactivity gap |

### SQL
| File | Topics |
|---|---|
| [`sql_leetcode.sql`](top_interview_question/sql_leetcode.sql) | ~35 LeetCode SQL problems: joins, aggregation, `GROUP BY`, `COALESCE`, self-joins |
| [`sql_leetcode_advanced.sql`](top_interview_question/sql_leetcode_advanced.sql) | ~35 harder problems: window functions (`ROW_NUMBER`, `RANK`, `FIRST_VALUE`), CTEs, with notes on the more efficient approach |
| [`leetcode_hard_sql_problems/`](top_interview_question/leetcode_hard_sql_problems) | [3156 Employee Task Duration & Concurrent Tasks](top_interview_question/leetcode_hard_sql_problems/3156_employee_task_duration_and_concurrent_tasks.sql) (interval overlap), [3103 Find Trending Hashtags II](top_interview_question/leetcode_hard_sql_problems/3103_find_trending_hashtags_ii.sql) |
| [`contesthacker.sql`](top_interview_question/contesthacker.sql) | contest SQL |

---

## lc25

A run through a LeetCode set (problem number in each filename).

| # | Problem | Topic |
|---|---|---|
| 13 | [Roman to Integer](lc25/13_roman_to_integer.py) | strings |
| 14 | [Longest Common Prefix](lc25/14_longest_common_prefix.py) | strings |
| 20 | [Valid Parentheses](lc25/20_valid_parentheses.py) | stack |
| 25 | [Simplify Path](lc25/25_simplify_path.py) ([test](lc25/test_25_simplify_path.py)) | stack |
| 35 | [Search Insert Position](lc25/35_search_inside_position.py) | binary search |
| 38 | [Count and Say](lc25/38_count_and_say.py) | strings |
| 58 | [Length of Last Word](lc25/58_length_of_last_word.py) | strings |
| 67 | [Add Binary](lc25/67_add_binary.py) | math / binary |
| 69 | [Sqrt(x)](lc25/69_sqrt_x.py) | binary search / math |
| 70 | [Climbing Stairs](lc25/70_climbing_stairs.py) | dynamic programming |
| 83 | [Remove Duplicates from Sorted List](lc25/83_remove_duplicates_from_sorted_list.py) | linked list |
| 94 | [Binary Tree Inorder Traversal](lc25/94_binary_tree_inorder_traversal.py) | trees |
| 100 | [Same Tree](lc25/100_same_tree.py) | trees |
| 118 | [Pascal's Triangle I](lc25/118_pascals_triangle_i.py) | arrays / DP |
| 119 | [Pascal's Triangle II](lc25/119_pascals_triangle_ii.py) | arrays / DP |
| 120 | [Triangle](lc25/120_triangle.py) | dynamic programming |
| 157 | [Read N Characters Given Read4](lc25/157_read_n_characters_given_read4.py) | strings / simulation |
| 202 | [Happy Number](lc25/202_happy_number.py) | math / cycle detection |
| 205 | [Isomorphic Strings](lc25/205_isomorphic_strings.py) | hashing |
| 266 | [Palindrome Permutation](lc25/266_palindrome_permutation.py) | hashing |
| 680 | [Valid Palindrome II](lc25/680_valid_palindrome_ii.py) | two pointers |

### [`lc25/hackerrank_sql/`](lc25/hackerrank_sql)
| File | Topic |
|---|---|
| [670 Maximum Swap](lc25/hackerrank_sql/670_maximum_swap.py) ([test](lc25/hackerrank_sql/test_maximum_swap.py)) | greedy / digits |
| [Weather Observation Station 20](lc25/hackerrank_sql/weather_observation_station_20.sql) | SQL (median) |
| [`challenges.sql`](lc25/hackerrank_sql/challenges.sql) / [`challenges_optimized.sql`](lc25/hackerrank_sql/challenges_optimized.sql) | a query and its tuned version |

---

## Advent of Code

Pure-Python solutions, one file per day (parts split into `_p1` / `_p2` where
they diverge). Good practice for parsing, simulation, and grid/graph problems.

- [`aoc2022/`](aoc2022) — days 1-16
- [`aoc2024/`](aoc2024) — days 1-19

Run any day by passing its input file:
```bash
python aoc2022/aoc221.py my_input.txt   # or drop an input.txt next to the script
```

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
