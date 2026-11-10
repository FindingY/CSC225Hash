# Instructor setup (remove this file if desired before publishing)

1. Create a new **public** GitHub repository, e.g. `csc225-hash-table-starter`, with **no automatically generated README**, since this folder already contains one.
2. Unzip this starter package locally and open a terminal in the unzipped folder.
3. Run:

   ```bash
   git init
   git add .
   git commit -m "Add CSC 225 hash table assignment starter"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/csc225-hash-table-starter.git
   git push -u origin main
   ```

   Replace `YOUR-USERNAME` (and repository name if different) with your details. If your system needs a Git authentication flow, use your normal GitHub sign-in/credential manager.

4. Copy the new repository URL into Blackboard. Students use **Fork**, not **Use this template**.
5. Keep the original repository available while the assignment is active; students can fork the public repo and work on their own copy.

## Notes on public tests

- The provided tests are educational checks, not a complete hidden grading suite.
- `test_milestone2.py` has one fixed-capacity/full-table test that is **intentionally stage-specific** and should not be part of final grading after resizing is added. Use the final command from README for the terminal check.
- `test_milestone5.py` assumes automatic resizing, which students should not implement until Milestone 5.
- `test_milestone1.py` checks the printed display includes every index, without requiring a particular table aesthetic.
- You can provide a hidden grading suite separately, but do not put hidden answer keys in a public repository.
