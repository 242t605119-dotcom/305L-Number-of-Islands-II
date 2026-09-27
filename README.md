# LeetCode 305 - Number of Islands II

## Problem Statement

You are given an empty `m × n` grid where all cells initially contain water.

Land is added one position at a time. After each addition, return the current number of islands.

## Example

### Input

```text
m = 3
n = 3
positions = [[0,0], [0,1], [1,2], [2,1]]
```

### Output

```text
[1, 1, 2, 3]
```

## Approach

Use the **Union-Find (Disjoint Set Union)** technique.

When a new land cell is added, check its four neighboring cells. If a neighboring cell is already land, merge the two islands.

## Algorithm

1. Start with zero islands.
2. Add each position as land.
3. Increase the island count by `1`.
4. Check the four adjacent cells.
5. Merge connected land cells using Union-Find.
6. Decrease the count whenever two separate islands are merged.
7. Store the island count after each addition.

## Time Complexity

`O(k × α(m × n))`

where `k` is the number of positions and `α` is the inverse Ackermann function.

## Space Complexity

`O(m × n)`

## Key Concepts

* Union-Find
* Disjoint Set Union
* Path Compression
* Union by Rank
* Grid Traversal

## Language

Python

## LeetCode Details

* **Problem:** 305
* **Title:** Number of Islands II
* **Difficulty:** Hard

## Author

**T. Nandhini Reddy**

GitHub: `242t605119-dotcom`
