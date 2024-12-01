# Simple Chess AI

This is a simple chess AI implemented in Python using the Minimax algorithm with Alpha-Beta pruning. You can play against the AI in the terminal.

## Features

- **Minimax Algorithm**: Implements the basic decision-making algorithm.
- **Alpha-Beta Pruning**: Optimizes the search to improve efficiency.
- **Command-Line Interface**: Play the game directly in the terminal.
- **Adjustable Difficulty**: Change the AI's search depth to adjust difficulty.

## Requirements

- Python 3.6 or higher
- `python-chess` library

## Installation

1. **Clone the Repository:**

   ```bash
   # git clone https://github.com/your-username/chess_ai_project.git

   ```
# chess_ai_project

2. **Navigate to the Project Directory:**
```
# cd chess_ai_project
```

3. **Create a Virtual Environment:**
```
#python3 -m venv venv
#source venv/bin/activate
```

4. **Install Dependencies:**
```
#pip install python-chess
```
# Usage
Run the chess_ai.py script to start the game:
```
#python3 chess_ai.py
```
# Game Instructions
Follow the prompts to enter your moves using UCI format (e.g., e2e4 moves a piece from e2 to e4).
Enter exit at any time to quit the game.


# Example


<img width="275" alt="{181A5A4D-681A-402E-8DFE-8A3171C94D09}" src="https://github.com/user-attachments/assets/fbc022a5-b2a7-4c46-9c5b-61dc6a224a0c">


# Customization
Adjust AI Difficulty: You can modify the search depth in chess_ai.py to change the AI's strength.

ai_move = get_best_move(board, depth=3)  # Increase the number for higher difficulty
