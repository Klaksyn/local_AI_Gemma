from langchain_ollama import OllamaLLM

import keyboard

class Assistant:
    _model = OllamaLLM(model="gemma4:e4b")

    def ask(self, text: str) -> str:
        print('\nGemma thinking....')
        print("\nAi: ", end="", flush=True)

        full_response = ""

        try:
            for chunk in self._model.stream(text):

                if keyboard.is_pressed('Alt'):
                    return "\nstopped by user"

                print(chunk, end="", flush=True)
                full_response += chunk

        except KeyboardInterrupt:
            return "\nstopped by user"

        except Exception as e:
            print(f"\nERROR: {e}")
            return ""

        print("-" * 40)
        return full_response
