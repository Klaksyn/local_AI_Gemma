from langchain_ollama import OllamaLLM

model = OllamaLLM(model="gemma4:e4b")

print("Gemma 4 ready!")
print("To exit write 'Exit'")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit' or user_input.lower() == 'выход':
        print('bye')
        break

    if not user_input.strip():
        continue

    print('\nGemma thinking....')

    try:
        response = model.invoke(user_input)
    except Exception as e:
        print(e)

    print(f"\nAi:\n{response}\n")
    print("-" * 40)