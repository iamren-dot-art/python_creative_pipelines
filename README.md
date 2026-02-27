# Python for Creative Pipelines - Progress Tracker

**Student:** Arian
**Started:** February 2026
**Curriculum:** v1.1

## Week 1, Day 3
**Date:** February 24, 2026
**Topic:** Dict Comprehensions

### Summary
- Dict comprehension syntax: {key: value for item in iterable}
- Filtering with conditions: {k: v for k, v in data if condition}
- Set comprehension for unique values: {item for item in list}
- .items() for iterating dict key-value pairs
- zip() + dict comprehension for building lookups from parallel lists
- Nested comprehension inside dict comprehension for counting

### Exercises Completed
1. `exercise_01_basic_dict_comp.py` — Scene object lookups, type counting, filtering
2. `exercise_02_parameter_maps.py` — Object-to-position mapping, filtering, normalization

### Quiz

| Q# | Question | My Answer | Correct Answer | Result |
|----|----------|-----------|----------------|--------|
| 1 | Dict key access via print | sphere: 20 | 20 | ✗ |
| 2 | Filtered dict | {b: 2, c: 3} | {'b': 2, 'c': 3} | ✓ |
| 3 | len() dict comprehension | {5, 5} | {"hello": 5, "world": 5} | ✗ |
| 4 | len() of filtered enumerate dict | 3 | 3 | ✓ |

**Score:** 2/4

### Key Corrections
- Q1: Dict key access returns the value only, not key: value
- Q3: Dict keys are the words, values are the lengths — two entries, not one

### Key Insight
- Comprehension variables are defined by the `for` clause — write that first, then build expression and filter around it
- Variable names are arbitrary — position in unpacking determines what data they hold

---

## Week 1, Day 2
**Date:** February 23, 2026
**Topic:** List Comprehensions

### Summary
- Basic list comprehensions: [expression for item in list]
- Filtered comprehensions: [expression for item in list if condition]
- Nested comprehensions: [expression for x in list1 for y in list2]
- Generator expressions inside sum()
- Comprehensions vs for loops — same result, one line

### Exercises Completed
1. `exercise_01_basic_comprehensions.py` — Frame timing, even frames, labels
2. `exercise_02_scene_filtering.py` — C4D scene object filtering
3. `exercise_03_transform_pipeline.py` — Render path generation

### Quiz

| Q# | Question | My Answer | Correct Answer | Result |
|----|----------|-----------|----------------|--------|
| 1 | Filter even numbers | [2, 4, 6] | [2, 4, 6] | ✓ |
| 2 | Rewrite loop as comprehension | upper([for...]) | [name.upper() for name in list] | ✗ |
| 3 | scaled[0] value | 0 | 0.333... | ✗ |
| 4 | Nested comprehension count | 2 | 6 (every combination) | ½ |
| 5 | Filtered list output | Light | ["Light"] | ✗ |

**Score:** 1.5/5

### Key Corrections
- Comprehension syntax: [expression for item in list] — expression comes first
- Trace math instead of guessing: 10/30 = 0.333, not 0
- Nested comprehension = every combination (2×3=6), not zip pairing
- Comprehensions always produce lists, even with one result

---

## Week 1, Day 1

**Date:** February 22, 2026
**Topic:** List Slicing, enumerate(), zip()

### Summary

- List slicing with [start:stop:step]
- Negative indexing for counting from the end
- enumerate() for index + value pairs
- zip() for pairing parallel lists
- Nesting enumerate(zip()) for indexed pairs

### Exercises Completed

1. `exercise_01_slicing.py` — Audio sample slicing
2. `exercise_02_enumerate_zip.py` — Render layer pairing
3. `exercise_03_creative_data.py` — Keyframe data manipulation

### Quiz

| Q# | Question | My Answer | Correct Answer | Result |
| ---- | ---------- | ----------- | ---------------- | -------- |
| 1 | samples[-2:] | 40, 50 | [40, 50] | ✓ |
| 2 | enumerate print(i) only | 1 null, 2 cube... | 1, 2, 3 | ✗ |
| 3 | zip() mismatched lengths | Trims to shortest | Stops at shortest | ✓ |
| 4 | Reverse a list | frames[::-1] | frames[::-1] | ✓ |
| 5 | list(zip(a,b))[1] | 1, 10 | (2, 20) | ✗ |

**Score:** 3/5

### Key Corrections

- Q2: Read exactly what print() outputs — only `i` was printed, not `name`
- Q5: zip() produces tuples, indexing the result list returns a whole tuple
