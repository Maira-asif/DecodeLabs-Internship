# Project 1: Rule-Based AI Chatbot 🤖

## Description
A simple rule-based chatbot that responds to predefined user inputs using
dictionary-based intent matching (instead of long if-elif chains). It handles
greetings, common questions, and exit commands through a continuous input loop.

## Features
- Continuous input loop (`while True`) that keeps the conversation running
- Input sanitization (`.lower().strip()`) to handle case and whitespace differences
- Dictionary-based knowledge base for instant (O(1)) response lookup
- Fallback response for unrecognized inputs
- Clean exit on commands like "bye", "exit", or "quit"

## How to Run
```
python Project1_chatbot.py
```
Then type messages like `hello`, `how are you`, `thank you`, or `bye` to exit.

## Key Skills Demonstrated
Control flow, decision-making logic, basic AI concepts.

---
Part of the DecodeLabs AI Internship — Batch 2026
