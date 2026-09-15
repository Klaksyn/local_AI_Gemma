# [RU](InputHandler_ru.md) | EN

## Location
`helper/InputHandler.py`

## Functions

### `read_multiline() -> str`
Allows the user to enter multi-line text in the console line by line.

* **How it works:**
  * Continues reading input lines until the user types one of the termination commands: `done`, `exit`, `!`, or `end`.
* **Returns:**
  * `str`: The collected text with all lines joined by a newline character (`\n`).