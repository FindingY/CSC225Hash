# CSC 225 — Hash Table Starter

Complete the `TODO` sections of **`hash_table.py`**. The menu in `main.py`, hash functions, display method, and table sizes are already provided. You do **not** need to build your own menu, prime-number checker, or linked list.

## Fork and run

1. Open the instructor's GitHub repository.
2. Click **Fork** (top right), then **Create fork**.
3. On **your fork**, click **Code** and copy the HTTPS address.
4. In a terminal, run:

   ```bash
   git clone YOUR-FORK-URL
   cd CSC225_Hash_Table_SIMPLE
   python main.py
   ```

   The folder name may differ if you renamed your fork. Use `python3 main.py` if your computer requires it.
5. Open the folder in VS Code. Work only in the `TODO` sections of `hash_table.py` unless you have a good reason to change another file.

## Milestone 1 — Linear probing

In `insert()`, find the starting index with `hash_key(key)`. If that position is occupied, try the next index, wrapping around the table. In `search()`, follow the same sequence. Do not insert the same number twice. For now, **ignore resizing** and stop with a message if the table is full.

**Test:** Choose `linear` and `mod`. Insert `10, 21, 32, 43, 54` individually. Display the table. Expect `10` at index 10 and `21, 32, 43, 54` at indices `0, 1, 2, 3`. Search for `32` (found) and `999` (not found). Try inserting `21` again (count must stay 5).

## Milestone 2 — Quadratic probing

Add the `quadratic` case to `insert()` and `search()`. Instead of trying consecutive indices, try `(start + i*i) % capacity` for `i = 0, 1, 2, ...`. Do not exceed a load factor of 0.50 before resizing is implemented.

**Test:** Start a fresh `quadratic` / `mod` table. Insert `10, 21, 32, 43, 54`. Expected indices: `10, 0, 3, 8, 4`. Search for each key.

## Milestone 3 — Separate chaining

For `chaining`, each table position is already initialized as its own empty list. In `insert()`, append to the list at the hash index. In `search()`, look for the key in that list.

**Test:** Start a fresh `chaining` / `mod` table. Insert `10, 21, 32, 43, 54`. All should appear in the list at index 10. Switch to `digit` hashing and try `10, 100, 1000, 10000`; they should all appear in the list at index 1.

## Milestone 4 — Grow and rehash

Now complete `resize()` and add the load-factor check near the start of `insert()`. Resize **before** a new insertion would exceed these limits: linear 0.70, quadratic 0.50, chaining 0.75. The next table capacity must come from the provided `SIZES` list. Reinsert every old value into the new table (the index may change).

**Test:** With a fresh 11-position table, insert 8 different numbers in linear mode, 6 in quadratic mode, or 9 in chaining mode. Each should grow from 11 to 23. After the resize, search for every number. Try more values to check another resize.

## Finish and submit

Test each of the three methods with both hash functions. Also test an absent value, a duplicate, and a resize. In this README or a separate `NOTES.md`, write 2–3 sentences answering: **Why can't you copy values into the same positions when the table grows?**

After each milestone:

```bash
git add .
git commit -m "Finish milestone 1"
git push
```

Change the milestone number in each commit message. Submit the URL of **your fork** to Blackboard.
