from app.model_loader import llm

def chat_with_llm(user_input):
    """Handles chatbot conversation."""
    if user_input.lower() in ["exit", "quit"]:
        return "Goodbye! 👋"
    
    response = llm(user_input)  # Get response from LLM
    return f"LLM: {response}"
