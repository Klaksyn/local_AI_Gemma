# [RU](assistant_ru.md) | EN

# Class assistant

## Location
`assistant/assistant.py`

## Methods
### `ask(text: str)` -> str 
Sends a prompt to the local Gemma model and streams the response directly to the console.
* **Parameters:**
  * `text` (`str`): The prompt or question you want to send to the AI.
* **Returns:**
  * `str`: The full concatenated response text, or a `"stopped by user"` message if interrupted.
* **Features:**
  * Real-time chunk printing (`flush=True`).
  * Instant abort if the **`Alt`** key is pressed during generation.
  * Exception handling for keyboard interrupts (`Ctrl+C`) and runtime errors.