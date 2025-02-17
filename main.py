from app.model_loader import llm

def chat():
    print("Welcome to the LLM Chatbot! Type 'exit' or 'quit' to end the chat.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye! 👋")
            break

        response = llm(user_input)
        print(f"LLM: {response}")

if __name__ == "__main__":
    chat()
