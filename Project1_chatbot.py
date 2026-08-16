"""
DecodeLabs Internship - Project 1
Rule-Based AI Chatbot

A simple chatbot that uses dictionary-based intent matching
(instead of a long if-elif ladder) to respond to predefined
user inputs, with sanitization, a fallback response, and a
clean exit command.
"""

# ---------------------------------------------------------
# 1. KNOWLEDGE BASE
# Dictionary of intents -> responses (O(1) lookup, not O(n) if-elif)
# ---------------------------------------------------------
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a bunch of if-else logic, but I'm doing great!",
    "what is your name": "I'm ChatBot, your friendly rule-based assistant.",
    "what can you do": "I can chat with you using simple predefined rules. Try saying 'hello' or 'bye'!",
    "help": "You can talk to me using greetings like 'hello', or ask 'what is your name'. Type 'bye' to exit.",
    "thank you": "You're welcome!",
    "thanks": "Anytime!",
}

# Words that trigger the exit / kill command
exit_commands = {"bye", "exit", "quit"}

# Fallback message when no rule matches
fallback_response = "I do not understand. Could you rephrase that?"


def get_response(user_input: str) -> str:
    """Look up the sanitized input in the knowledge base, with a fallback."""
    return responses.get(user_input, fallback_response)


def chatbot():
    print("ChatBot: Hello! I'm your rule-based assistant. Type 'bye' to exit.")

    # ---------------------------------------------------------
    # 2. THE INFINITE LOOP (The Heartbeat)
    # Keeps running until the user issues the kill command
    # ---------------------------------------------------------
    while True:
        raw_input_text = input("You: ")

        # ---------------------------------------------------------
        # 3. SANITIZATION / NORMALIZATION
        # Handles case sensitivity and stray whitespace
        # ---------------------------------------------------------
        clean_input = raw_input_text.lower().strip()

        # ---------------------------------------------------------
        # 4. EXIT STRATEGY
        # ---------------------------------------------------------
        if clean_input in exit_commands:
            print("ChatBot: Goodbye! Have a great day.")
            break

        # ---------------------------------------------------------
        # 5. RESPONSE GENERATION (with fallback)
        # ---------------------------------------------------------
        reply = get_response(clean_input)
        print(f"ChatBot: {reply}")


if __name__ == "__main__":
    chatbot()
