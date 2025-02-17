import requests
import os
import json

API_URL = "https://api.together.xyz/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
    "Content-Type": "application/json"
}

def llm(prompt):
    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 100
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        result = response.json()

        # Extract the assistant's message
        assistant_message = result["choices"][0]["message"]

        # Check if the response includes function calling
        if "tool_calls" in assistant_message and assistant_message["tool_calls"]:
            print("🔹 LLM needs more information. Please provide input: ", end="")
            user_input = input()
            return llm(user_input)  # Retry with new user input

        # Normal response
        return assistant_message["content"].strip()

    except requests.exceptions.RequestException as e:
        return f"API Error: {str(e)}"
