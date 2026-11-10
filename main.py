"""CSC 225 interactive menu — Milestone 4.

Run: python main.py
"""

from hash_table import HashTable


def show_menu(table: HashTable) -> None:
    """Print the menu and basic information about the active table."""
    # TODO (Milestone 4): display strategy, hash method, capacity, count,
    # load factor, and all eight menu options from the README.
    print("\n========== HASH TABLE SIMULATOR ==========")
    print("TODO: implement the menu in Milestone 4")


def main() -> None:
    # Milestone 4: initialize a table, then build an input loop.
    # Menu items: insert, search, display, bulk insert, statistics,
    # change strategy, change hash function, and exit.
    # When changing a strategy or hash method, confirm before creating
    # a NEW empty HashTable(capacity=11, ...).
    # Validate integer and menu input instead of crashing.
    print("Starter project: complete Milestones 1–3 before the menu.")
    # TODO: replace this stub with your program.


if __name__ == "__main__":
    main()
