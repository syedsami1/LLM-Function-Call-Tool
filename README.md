
# LLM Function Call Tool

This Task implements a chatbot powered by an LLM (Language Learning Model) that can trigger function calls when additional user input is needed. The chatbot is able to handle specific tasks like booking a flight by asking for further details when needed.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Requirements](#requirements)
3. [Setup Instructions](#setup-instructions)
4. [How It Works](#how-it-works)
5. [Code Files Overview](#code-files-overview)
6. [Usage](#usage)
7. [License](#license)

---

## Project Overview
This project is designed to create a chatbot using an API for LLMs like **Mistral-7B-Instruct**. It listens for requests, triggers a function call to request more details when needed, and provides dynamic responses based on the user's input.

The primary goal of this project is to create a system where, upon receiving a specific request (like booking a flight), the LLM asks for additional user input, thus allowing seamless interactions with a tool that can perform real-world tasks.

---

## Requirements
- Python 3.x+
- `requests` library for API interactions
- `flask` for API management
- Environment variables for secure API keys
- `python-dotenv` for loading environment variables from `.env` file

### Python Libraries:
- `flask`
- `requests`
- `python-dotenv`

You can install the dependencies by running the following command:

```bash
pip install -r requirements.txt
```

---

## Setup Instructions
### 1. Clone the repository
First, clone this repository to your local machine.

```bash
git clone <repository_url>
cd llm_function_call_tool
```

### 2. Set up a virtual environment
It is recommended to use a virtual environment for this project to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
Install the required libraries by running:

```bash
pip install -r requirements.txt
```

### 4. Set up the `.env` file
Create a `.env` file in the root directory of the project to securely store your API keys and other environment variables. Here's an example `.env` file:

```env
TOGETHER_API_KEY=your_api_key_here
```

---

## How It Works
### 1. **API Interaction**: 
The chatbot interacts with an external LLM API (such as Together API or another service). It sends requests to the API to get responses based on user input.

### 2. **Function Call Triggering**:
Whenever the LLM detects that more information is needed (for example, to book a flight), the system triggers a function call that asks for further details. These details are then passed to the LLM to generate a complete response.

### 3. **Flask API**:
A Flask server is used to handle incoming requests and manage the interactions between the user and the LLM.

---

## Code Files Overview

### 1. **main.py**
This file is the entry point for the chatbot. It runs the Flask application and handles incoming requests.

```python
from app.chat import chat_with_llm
from app.input_handler import handle_user_input
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def main():
    print("Welcome to the LLM Chatbot! Type 'exit' or 'quit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye! 👋")
            break
        
        # Process user input
        response = chat_with_llm(user_input)
        
        # Handle response
        if "LLM needs more information" in response:
            print(f"🔹 LLM needs more information. Please provide input:")
            additional_input = input()
            response = chat_with_llm(additional_input)
        
        print(f"LLM: {response}")
        
if __name__ == "__main__":
    main()
```

### 2. **app/chat.py**
This file contains the core logic for interacting with the LLM. It sends user input to the API and processes the response.

```python
import requests
import os

API_URL = "https://api.together.xyz/v1/chat/completions"
API_KEY = os.getenv("TOGETHER_API_KEY")

def chat_with_llm(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": [{"role": "user", "content": user_input}]
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        return response_json['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"API Error: {e}"

```

### 3. **app/input_handler.py**
This file is responsible for handling and validating the user's input.

```python
def handle_user_input(user_input):
    # Check if the input requires more information
    if "book a flight" in user_input.lower():
        return "🔹 LLM needs more information. Please provide input:"
    return user_input
```

### 4. **app/model_loader.py**
This file is used to load and interact with the model and API.

```python
import os
import requests

API_KEY = os.getenv("TOGETHER_API_KEY")
API_URL = "https://api.together.xyz/v1/chat/completions"

def generate_response(prompt):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"API Error: {e}"

```

### 5. **requirements.txt**
Contains all the dependencies for the project:

```
flask
requests
python-dotenv
```

---

## Usage
1. **Run the chatbot**:
   To start the chatbot, simply run the following command:

   ```bash
   python main.py
   ```

2. **Interacting with the chatbot**:
   Once the program starts, you can type questions or requests. The bot will either respond or ask for additional input when necessary.

3. **Example Flow**:

   ```
   You: What is AI?
   LLM: AI stands for Artificial Intelligence. It is a branch of computer science...
   You: Book a flight
   LLM: Sure, I can help you book a flight. Can you provide the details?
   ```

---



