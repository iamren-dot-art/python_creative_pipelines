# Python for Creative Pipelines - Progress Tracker

**Student:** Arian
**Started:** February 2026
**Curriculum:** v1.1

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
|----|----------|-----------|----------------|--------|
| 1 | samples[-2:] | 40, 50 | [40, 50] | ✓ |
| 2 | enumerate print(i) only | 1 null, 2 cube... | 1, 2, 3 | ✗ |
| 3 | zip() mismatched lengths | Trims to shortest | Stops at shortest | ✓ |
| 4 | Reverse a list | frames[::-1] | frames[::-1] | ✓ |
| 5 | list(zip(a,b))[1] | 1, 10 | (2, 20) | ✗ |

**Score:** 3/5

### Key Corrections
- Q2: Read exactly what print() outputs — only `i` was printed, not `name`
- Q5: zip() produces tuples, indexing the result list returns a whole tuple