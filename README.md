# CSC 225 — Hash Table Simulator

A guided Python programming assignment. **Fork this repository, complete one milestone at a time, test your work, and push your code to your fork.**

**Do not implement everything at once.** The starter code deliberately raises `NotImplementedError` in methods you must write.

## Learning goals

Build a hash table from a Python list using **linear probing**, **quadratic probing**, and **separate chaining**. Use two supplied hash functions, add a terminal menu, and grow the table by **rehashing** when its load factor gets too high.

Do **not** use `dict`, `set`, or Python's built-in `hash()` to implement the data structure. You may use ordinary Python lists, loops, and helper methods. No third-party packages are needed.

## Files

| File | Purpose |
| --- | --- |
| `hash_functions.py` | Two complete, provided hash functions; do not edit. |
| `hash_table.py` | Student skeleton: implement the table and collision strategies. |
| `main.py` | Student skeleton: menu-driven application. |
| `tests/test_milestone1.py` | Public checks for initialization and hashing. |
| `tests/test_milestone2.py` | Linear probing tests for the **fixed-capacity** stage. |
| `tests/test_milestone3.py` | Quadratic probing, chaining, digit-sum tests. |
| `tests/test_milestone5.py` | Resizing and rehashing checks, run after Milestone 5. |

## How to fork and work on the assignment

1. Sign in to GitHub and open the **instructor's original repository link**.
2. Select **Fork** (top-right) → choose your account as the owner → **Create fork**. You now have your own copy under `github.com/YOUR-USERNAME/csc225-hash-table-starter` (the name may differ if you change it).
3. In **your fork**, select the green **Code** button and copy the HTTPS URL.
4. Open VS Code and choose **Terminal → New Terminal**. Run:

   ```bash
   git clone https://github.com/YOUR-USERNAME/csc225-hash-table-starter.git
   cd csc225-hash-table-starter
   code .
   ```

   Replace `YOUR-USERNAME` with your GitHub username. If `code .` is unavailable, open the cloned folder manually in VS Code.

5. Work through the milestones below. After each milestone, **commit and push**:

   ```bash
   git status
   git add .
   git commit -m "Complete milestone 1"
   git push
   ```

   Update the commit message for each milestone. GitHub may ask you to authenticate when pushing.

6. Open **your fork** on GitHub to verify that your latest changes appear. **Submit the URL to your fork** in Blackboard (or as otherwise directed by your instructor). You do *not* need to open a pull request to the instructor's repository.

> If GitHub shows a **Sync fork** option, do not use it during the assignment unless your instructor explicitly directs you to; it may bring in changes you did not intend.

## Testing: short feedback loops

Run tests from the **repository root** (the folder containing `hash_table.py`):

```bash
python -m unittest tests.test_milestone1 -v
```

If your operating system uses `python3`, substitute it for `python`.

- A **failure** shows what behavior did not match the expected result.
- An **error** involving `NotImplementedError` means that milestone has not been implemented yet.
- Never use the number of passing tests alone as evidence that your algorithm is correct: also inspect the printed table and try your own values.
- Add temporary `print()` statements to track hash indices, probe attempts, and resizing; remove debugging output before submission.

**Important milestone boundary:** `tests.test_milestone2` includes a *full fixed-capacity table* test. This is meant for Milestone 2 **before automatic resizing exists**. Once you add Milestone 5's resizing, that one early test no longer applies. For final grading, run Milestones 1, 3, and 5; test the menu manually. The expected final behavior is to resize rather than reject an insertion solely because the old table is full.

## Required interface

Keep these method names, so the provided tests can call your code:

| Method | Expected behavior |
| --- | --- |
| `HashTable(capacity=11, collision_method="linear", hash_method="mod")` | Initializes the table. Valid collision methods: `linear`, `quadratic`, `chaining`. Hash methods: `mod`, `digit_sum`. |
| `table._hash(key)` | Returns the current hash index using the selected provided function. |
| `table.insert(key)` | Returns `True` for a new insertion; `False` for a duplicate (or, prior to resizing, no available placement). |
| `table.search(key)` | Returns **`True` or `False`**, not an index. |
| `table.display()` | Prints *every index* and the value/bucket at it. |
| `table.load_factor()` | Returns `count / capacity`. |
| `table.statistics()` | Prints method, hash function, capacity, count, load factor. |
| `table.get_values()` | Returns a flat list containing all values. |
| `table.resize()` | Grows to the next required prime capacity and rehashes all values. |

Store `capacity`, `count`, `collision_method`, `hash_method`, and `table` as instance attributes. Store only **integer** keys. Do not insert duplicates. Use `None` as an empty open-addressing slot. For chaining, use **independent** inner lists (`[[] for _ in range(capacity)]`). You do not need deletion in this assignment.

---

## Milestone 1 — Initialization, hash functions, display (10 pts)

In `hash_table.py`:

1. Implement `__init__` to store configuration, set `count = 0`, and create an empty table. For probing, use `[None] * capacity`; for chaining use one separate empty list per index.
2. Implement `_hash` to call either `hash_mod` or `hash_digit_sum` from `hash_functions.py`, always using the **current** capacity.
3. Implement `display()` to print every index, including empty ones.
4. Try these examples: under `mod` and capacity 11, `21` and `32` both map to 10; under `digit_sum`, `10000` maps to 1.

Test:

```bash
python -m unittest tests.test_milestone1 -v
```

**Checkpoint:** A table starts empty, has the correct capacity, prints all 11 positions, and chooses the correct hash function. Commit and push your progress.

## Milestone 2 — Linear probing (15 pts)

Implement `insert()` and `search()` for `collision_method="linear"`.

1. Probe `(h(key) + i) % capacity` for `i = 0, 1, ...`.
2. When inserting, find an empty slot; **reject duplicates** without changing `count`.
3. When searching, follow the same probe order; stop at an empty slot or after at most `capacity` probes.
4. For now, **do not resize**. If you inspect all slots and find none available, return `False` rather than looping forever.

Insert `[10, 21, 32, 43, 54]` into an empty 11-slot modulo table. Expected positions:

```text
index 10: 10
index  0: 21
index  1: 32
index  2: 43
index  3: 54
```

Test:

```bash
python -m unittest tests.test_milestone2 -v
```

Also try searching for `32` (found), `999` (not found), and inserting `21` twice (count must not increase). **Checkpoint:** Collision placement, wraparound, search, and duplicate handling work. Commit and push.

## Milestone 3 — Quadratic probing and chaining (25 pts)

Extend both `insert()` and `search()`.

**Quadratic probing** uses `(h(key) + i*i) % capacity`. For capacity 11, modulo hashing and `[10, 21, 32, 43, 54]`, the expected indices are respectively `[10, 0, 3, 8, 4]`. Keep prime capacities and do not add a sixth element before you implement resizing. While the table is fixed-size, reject an insertion that would put quadratic probing above a 0.50 load factor. Limit probes to avoid infinite loops.

**Separate chaining** stores a list at each index. For the same five values, bucket 10 should be `[10, 21, 32, 43, 54]`. Insertion checks that the key is not already in its chain; searching examines the appropriate chain.

Try the second hash function with `[10, 100, 1000, 10000]`. All four keys hash to index 1 for capacity 11.

Test:

```bash
python -m unittest tests.test_milestone3 -v
```

**Checkpoint:** All three strategies insert/search correctly with either hash function. Commit and push.

## Milestone 4 — Menu-driven program (10 pts)

Replace the `main.py` stub with a menu loop that stays active until Exit:

```text
========== HASH TABLE SIMULATOR ==========
Collision strategy: Linear Probing
Hash function: Modulo
Table capacity: 11
Elements stored: 0
Load factor: 0.00

1. Insert a value
2. Search for a value
3. Display hash table
4. Insert multiple values
5. Display table statistics
6. Change collision strategy
7. Change hash function
8. Exit
```

- Implement `load_factor()` and `statistics()` in `hash_table.py`.
- Bulk insert accepts space-separated integers.
- When a user changes either strategy or hash method, **ask for confirmation** and then create a **new empty table of capacity 11**.
- Handle invalid menu choices and non-integer input without crashing.

Test interactively:

```bash
python main.py
```

Try insert → display → search → bulk insert → statistics → switch strategy → confirm reset → invalid menu choice → exit. **Checkpoint:** All options work across repeated interactions. Commit and push.

## Milestone 5 — Automatic growth and rehashing (20 pts)

Before inserting a *new, nonduplicate* key, calculate the **projected** load factor `(count + 1) / capacity`. If it exceeds the chosen threshold, **resize before inserting**:

| Method | Resize when projected load factor exceeds |
| --- | ---: |
| Linear probing | 0.70 |
| Quadratic probing | 0.50 |
| Chaining | 0.75 |

To resize:

1. Collect **all values** from the old table, including every value within chains. Your `get_values()` method should return a flat list.
2. Choose the smallest prime number `>= 2 * old_capacity + 1` (11 → **23**).
3. Allocate a new, empty table of the correct storage type.
4. Reinsert **each old value using the new capacity and the selected collision method**; do **not** copy old indices.
5. Complete the new insertion and ensure `count` remains accurate. Avoid recursively triggering another resize during the rehash process.
6. Display a brief message showing the capacity change.

Test:

```bash
python -m unittest tests.test_milestone5 -v
```

Expected first resizes from capacity 11:

- Linear: insert `0` through `7`; insertion #8 triggers resize to 23.
- Quadratic: insert `10, 21, 32, 43, 54, 65`; insertion #6 triggers resize to 23.
- Chaining: insert `0` through `8`; insertion #9 triggers resize to 23.

Then insert 50 distinct values using **each strategy** and search for every one. **Checkpoint:** Rehashing preserves every key and the table can grow more than once. Commit and push.

## Milestone 6 — Final tests and reflection (10 pts)

Test all **six combinations** of 2 hash functions × 3 collision strategies. For each combination try collisions, existing/missing searches, duplicates, and enough values to trigger resizing. Also try negative integers, zero, and invalid user input.

Final automated test command (run from repository root):

```bash
python -m unittest tests.test_milestone1 tests.test_milestone3 tests.test_milestone5 -v
```

Then launch and manually test the menu:

```bash
python main.py
```

In your `README.md`, add a section titled **My Testing and Reflection**. Include:

- The command you used to run your program and test suites.
- Which tests you ran, whether they passed, and any remaining known issues.
- Answers to the following questions:
  1. How do open addressing and separate chaining differ?
  2. Why does quadratic probing require special care with capacity and load factor?
  3. Why must keys be rehashed when capacity changes?
  4. How does load factor affect performance?
  5. Which strategy would you select for a general-purpose hash table, and why?

**Do not erase the assignment directions** when adding your reflection; append your section below.

---

## Grading (100 pts)

| Component | Points |
| --- | ---: |
| Milestone 1: structure and hashing | 10 |
| Milestone 2: linear probing | 15 |
| Milestone 3: quadratic probing and chaining | 25 |
| Milestone 4: terminal menu | 10 |
| Milestone 5: resize and rehash | 20 |
| Milestone 6: testing and written reflection | 10 |
| Individual code demonstration | 10 |
| **Total** | **100** |

You may be asked to run the program, demonstrate a collision, and explain where resizing and rehashing happen in your code. Your work should reflect your own understanding.

## Submission checklist

- [ ] All milestone code is complete (no required `NotImplementedError` remains).
- [ ] Three collision-resolution methods work.
- [ ] Both provided hash functions work.
- [ ] Menu is interactive and handles invalid input.
- [ ] Duplicate insertion leaves `count` unchanged.
- [ ] Every key remains searchable after resizing.
- [ ] Tests and README reflection are completed.
- [ ] At least one commit has been pushed after each milestone.
- [ ] Submit the URL to **your fork** (not the instructor's original repository).
