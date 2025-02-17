# LLM Function Call Tool

This task implements a chatbot powered by an LLM (Language Learning Model) that can trigger function calls when additional user input is needed. The chatbot is capable of handling specific tasks like booking a flight by asking for further details when needed.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Requirements](#requirements)
3. [Setup Instructions](#setup-instructions)
4. [How It Works](#how-it-works)
5. [Interactive Example](#interactive-example)
6. [Usage](#usage)

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
git clone https://github.com/syedsami1/LLM-Function-Call-Tool.git
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

## Interactive Example

Here’s an interactive example demonstrating how the chatbot interacts with the user, requests additional details, and provides a response:

**Example Interaction**:

```
Welcome to the LLM Chatbot! Type 'exit' or 'quit' to end the chat.

You: What is AI?
LLM: AI stands for Artificial Intelligence. It is a branch of computer science that focuses on the development of intelligent machines that can perform tasks that typically require human intelligence, such as visual perception, speech recognition, decision-making, and language translation. AI systems use algorithms, machine learning, and other techniques to learn from data and improve their performance over time. They can be used in a wide range of applications, from virtual assistants and self-driving cars to medical diagnosis and financial analysis.

You: Book a flight
LLM: Sure, I can help you book a flight. Can you please provide me with the following information:

1. Departure city and airport
2. Arrival city and airport
3. Departure date and time
4. Return date and time (if applicable)
5. Number of passengers
6. Class of seating (economy, business, first class)
7. Preferred airline (if any)
8. Any specific requirements or preferences
```

In this example, after the user asks to "book a flight", the LLM triggers a function call to collect additional details before proceeding.

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

