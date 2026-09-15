from langchain_ollama import OllamaLLM

import helper.InputHandler as InputHandler
import assistant.assistant as assistant

assist = assistant.Assistant()

print("Gemma 4 ready!")
print("To exit write 'Exit'")

while True:
    print("for help type help!")
    user_input = input("You: ")

    if user_input.lower() == 'exit' or user_input.lower() == 'выход':
        print('bye')
        break

    if not user_input.strip():
        continue

    if user_input.strip() == "!" or user_input.strip() == ">":
        user_input = InputHandler.read_multiline()

    if user_input == "help":
        print("""
        Multi Line
            > / ! - write multi line
            ! / end / done / exit - to exit 
        Stop Ai:
            Alt or Ctrl+C
                """)

    else:
        print(assist.ask(user_input))


