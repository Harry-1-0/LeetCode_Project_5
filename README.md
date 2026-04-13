# Maximum Subarray Problem

> **Midterm Group Project** — C++ implementations by Hariharan · Python implementation by Vu Hai Nam

---

## Table of Contents

1. [Problem Statement](#problem-statement)
2. [Solutions Overview](#solutions-overview)
3. [C++ Implementations](#c-implementations)
   - [Brute Force](#1-brute-force)
   - [Dynamic Programming](#2-dynamic-programming)
   - [Kadane's Algorithm](#3-kadanes-algorithm)
4. [Python vs C++ Comparison](#python-vs-c-comparison)
5. [Complexity Summary](#complexity-summary)
6. [Example Walkthrough](#example-walkthrough)
7. [How to Run](#how-to-run)

---

## Problem Statement

Given an integer array `nums`, find the **contiguous subarray** (containing at least one number) which has the **largest sum**, and return that sum.

**Example:**

```
Input:  [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Reason: Subarray [4, -1, 2, 1] has the largest sum = 6
```

**Constraints:**
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

---

## Solutions Overview

| Approach | Time Complexity | Space Complexity | Notes |
|---|---|---|---|
| Brute Force | O(n²) | O(1) | Try every subarray |
| Dynamic Programming | O(n) | O(n) | Build dp array |
| Kadane's Algorithm | O(n) | O(1) | **Optimal solution** |

```
Operations growth (n = 1000):
  Brute Force  ████████████████████████████████████████  1,000,000
  DP / Kadane  █                                              1,000
```

---

## C++ Implementations

### 1. Brute Force

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size(), res = nums[0];
        for (int i = 0; i < n; i++) {
            int cur = 0;
            for (int j = i; j < n; j++) {
                cur += nums[j];
                res = max(res, cur);
            }
        }
        return res;
    }
};
```

**How it works:**

For every starting index `i`, iterate through all possible ending indices `j`, accumulating the sum and tracking the maximum seen so far. Although simple and correct, the nested loop means each pair `(i, j)` is evaluated — giving quadratic growth.

**Step-by-step on `[-2, 1, -3, 4]`:**

```
i=0: [-2], [-2,1], [-2,1,-3], [-2,1,-3,4]  → max = 2
i=1: [1],  [1,-3], [1,-3,4]                → max = 2
i=2: [-3], [-3,4]                           → max = 2
i=3: [4]                                    → max = 4  ✓
```

**Pros:** Easy to understand, no extra space needed.  
**Cons:** Too slow for large inputs (`n = 10^5` → 10 billion operations).

---

### 2. Dynamic Programming

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> dp(nums);
        for (int i = 1; i < nums.size(); i++) {
            dp[i] = max(nums[i], nums[i] + dp[i - 1]);
        }
        return *max_element(dp.begin(), dp.end());
    }
};
```

**How it works:**

Define `dp[i]` as the **maximum subarray sum ending at index `i``. At each step, decide: is it better to start a new subarray at `i`, or extend the best subarray that ended at `i-1`?

```
dp[i] = max(nums[i],  nums[i] + dp[i-1])
          ↑ start     ↑ extend
          fresh       previous best
```

**Step-by-step on `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`:**

```
Index:  0   1   2   3   4   5   6   7   8
nums:  -2   1  -3   4  -1   2   1  -5   4
dp:    -2   1  -2   4   3   5   6   1   5
                                    ↑
                              max_element = 6
```

**Pros:** Linear time, very clear recurrence relation.  
**Cons:** Uses O(n) extra space for the `dp` array (can be optimized — see Kadane's).

---

### 3. Kadane's Algorithm

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSub = nums[0], curSum = 0;
        for (int num : nums) {
            if (curSum < 0) {
                curSum = 0;
            }
            curSum += num;
            maxSub = max(maxSub, curSum);
        }
        return maxSub;
    }
};
```

**How it works:**

Kadane's Algorithm is essentially the DP solution with O(1) space — instead of storing all `dp[i]` values, we only track the **current running sum** and reset it to 0 whenever it goes negative (because a negative running sum can never help extend a future subarray).

**The key insight:**
> If the sum of everything seen so far is negative, it's always better to discard it and start fresh from the current element.

**Step-by-step on `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`:**

```
num=-2: curSum=0→reset→0+-2=-2,  maxSub=-2
num= 1: curSum=-2→reset→0, 0+1=1, maxSub=1
num=-3: curSum=1,  1+-3=-2,       maxSub=1
num= 4: curSum=-2→reset→0, 0+4=4, maxSub=4
num=-1: curSum=4,  4+-1=3,        maxSub=4
num= 2: curSum=3,  3+2=5,         maxSub=5
num= 1: curSum=5,  5+1=6,         maxSub=6  ✓
num=-5: curSum=6,  6+-5=1,        maxSub=6
num= 4: curSum=1,  1+4=5,         maxSub=6
```

**Final answer: 6**

**Pros:** Optimal — linear time *and* constant space. Industry standard.  
**Cons:** Slightly less intuitive than DP at first glance.

---

## Python vs C++ Comparison

This section compares the C++ implementations above with equivalent Python implementations of the same three approaches.

### Code Style & Syntax

| Aspect | C++ | Python |
|---|---|---|
| Type declaration | `vector<int>& nums` | `nums: list[int]` or duck-typed |
| Loop syntax | `for (int i = 0; i < n; i++)` | `for i in range(n)` |
| Max utility | `max(a, b)` / `*max_element(...)` | `max(a, b)` / `max(...)` |
| Array init | `vector<int> dp(nums)` | `dp = nums[:]` |
| Return | `return maxSub` | `return max_sub` |

### Equivalent Python (for reference)

**Brute Force:**
```python
def maxSubArray(nums: list[int]) -> int:
    res = nums[0]
    for i in range(len(nums)):
        cur = 0
        for j in range(i, len(nums)):
            cur += nums[j]
            res = max(res, cur)
    return res
```

**Dynamic Programming:**
```python
def maxSubArray(nums: list[int]) -> int:
    dp = nums[:]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i - 1])
    return max(dp)
```

**Kadane's Algorithm:**
```python
def maxSubArray(nums: list[int]) -> int:
    max_sub = nums[0]
    cur_sum = 0
    for num in nums:
        if cur_sum < 0:
            cur_sum = 0
        cur_sum += num
        max_sub = max(max_sub, cur_sum)
    return max_sub
```

### Performance Comparison

Both languages implement the same algorithms with the same asymptotic complexity. However, raw execution speed differs significantly due to how each language is executed.

```
Relative execution speed (Kadane's, n = 10^6, approximate):

  C++     ██  ~10 ms    (compiled to native machine code)
  Python  ██████████████████████████████  ~300–500 ms  (interpreted)
```

| Factor | C++ | Python |
|---|---|---|
| Execution model | Compiled to native binary | Interpreted (CPython) |
| Speed (rough) | ~20–50× faster for tight loops | Slower; can use NumPy to close gap |
| Memory | Manual/RAII-managed, very lean | GC-managed, higher overhead per object |
| Verbosity | More boilerplate | More concise |
| Error detection | Compile-time type errors caught early | Runtime errors only |
| Best for | Performance-critical / embedded systems | Rapid prototyping, data science |

> **Note:** Python's `numpy.max(numpy.cumsum(nums) - ...)` approaches can be very fast in practice due to vectorized C extensions, but for a pure loop implementation, C++ wins by a wide margin.

### When to choose which

- **C++** — when performance is critical (game engines, embedded systems, competitive programming with tight time limits)
- **Python** — when readability, development speed, or ecosystem (pandas, numpy, sklearn) matters more than raw speed

---

## Complexity Summary

```
╔══════════════════════╦════════════════╦═════════════════╗
║ Algorithm            ║ Time           ║ Space           ║
╠══════════════════════╬════════════════╬═════════════════╣
║ Brute Force          ║ O(n²)          ║ O(1)            ║
║ Dynamic Programming  ║ O(n)           ║ O(n)            ║
║ Kadane's Algorithm   ║ O(n)     ★     ║ O(1)      ★     ║
╚══════════════════════╩════════════════╩═════════════════╝
```

★ Kadane's Algorithm is the **optimal solution** — it achieves the best possible time complexity while using constant extra space.

**Why can't we do better than O(n)?**  
We must examine every element at least once to determine whether it contributes to the maximum subarray. This gives a provable lower bound of Ω(n), so Kadane's Algorithm is asymptotically optimal.

---

## Example Walkthrough

Full trace on `nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]` using Kadane's:

```
Step | num | curSum before | reset? | curSum after | maxSub
-----|-----|---------------|--------|--------------|-------
  1  |  -2 |       0       |   no   |     -2       |   -2
  2  |   1 |      -2       |  YES   |      1       |    1
  3  |  -3 |       1       |   no   |     -2       |    1
  4  |   4 |      -2       |  YES   |      4       |    4
  5  |  -1 |       4       |   no   |      3       |    4
  6  |   2 |       3       |   no   |      5       |    5
  7  |   1 |       5       |   no   |      6       |    6  ← answer
  8  |  -5 |       6       |   no   |      1       |    6
  9  |   4 |       1       |   no   |      5       |    6
```

The maximum subarray is **[4, -1, 2, 1]** with sum **6**.

---

## How to Run

### C++

```bash
# Compile
g++ -std=c++17 -O2 -o solution solution.cpp

# Run
./solution
```

### Python

```bash
python3 solution.py
```

### LeetCode

All three C++ solutions can be submitted directly to [LeetCode #53 — Maximum Subarray](https://leetcode.com/problems/maximum-subarray/).

---

*Maximum Subarray Problem · Midterm Group Project*
