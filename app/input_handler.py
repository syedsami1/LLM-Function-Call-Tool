def needs_more_info(response_text):
    """Checks if the LLM response is uncertain and needs more user input."""
    uncertain_phrases = [
        "I am not sure", "Could you clarify", "I don't have enough information",
        "Please provide more details", "I'm uncertain", "Can you specify"
    ]
    
    return any(phrase.lower() in response_text.lower() for phrase in uncertain_phrases)
