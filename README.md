# IRP2 Programming Problems

**Name:** Eshita Chauhan  
**Roll No.:** 2481123

This repository contains four Python programs that read input from standard input.

## How to run

Run a script from the repository root with Python 3:

```bash
python problems/p1_reverse_words.py
python problems/p2_binary_search.py
python problems/p3_digit_sum.py
python problems/p4_pair_count.py
```

Type or pipe the problem input into the program. Example:

```bash
printf 'I love coding\n' | python problems/p1_reverse_words.py
```

## Problems

1. **Reverse word order** — prints the input words in reverse order.
2. **Binary search** — searches a sorted integer list without built-in search and prints the 0-based index, or `-1`.
3. **Recursive digit sum** — computes the sum of the digits using recursion.
4. **Pair count** — counts index pairs `i < j` whose absolute difference is `k`. The original problem statement available for this repository was cut off after “count pairs i”; this explicit interpretation is used here. The implementation treats pairs as distinct index pairs.

Each problem has a sample input and expected output in `tests/`.
