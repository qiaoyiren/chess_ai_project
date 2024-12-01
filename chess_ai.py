import chess

def evaluate_board(board):
    """
    Evaluates the board and returns a score.
    Positive values favor White, negative values favor Black.
    """
    # Define the material value of each piece type
    piece_values = {
        chess.PAWN: 1,     # Pawn
        chess.KNIGHT: 3,   # Knight
        chess.BISHOP: 3,   # Bishop
        chess.ROOK: 5,     # Rook
        chess.QUEEN: 9,    # Queen
        chess.KING: 0      # King (value is 0 because the game's goal is to checkmate)
    }

    # Initialize total evaluation
    value = 0

    # Evaluate material on the board
    for piece_type in piece_values:
        # Count White pieces
        value += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        # Count Black pieces
        value -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]
    
    return value

def minimax(board, depth, alpha, beta, maximizing_player):
    """
    Implements the Minimax algorithm with Alpha-Beta pruning.
    - board: current board state
    - depth: search depth
    - alpha: best score for maximizing player (lower bound)
    - beta: best score for minimizing player (upper bound)
    - maximizing_player: True if maximizing player's turn, False otherwise
    """
    # Base case: maximum depth reached or game over
    if depth == 0 or board.is_game_over():
        return evaluate_board(board)
    
    if maximizing_player:
        max_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)  # Make the move
            eval = minimax(board, depth - 1, alpha, beta, False)  # Recursion
            board.pop()  # Undo the move
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

def get_best_move(board, depth):
    """
    Determines the best move for the AI.
    - board: current board state
    - depth: search depth
    """
    best_move = None
    max_eval = -float('inf')
    alpha = -float('inf')
    beta = float('inf')

    for move in board.legal_moves:
        board.push(move)
        eval = minimax(board, depth - 1, alpha, beta, False)
        board.pop()
        if eval > max_eval:
            max_eval = eval
            best_move = move
            alpha = max(alpha, eval)
    return best_move

def main():
    board = chess.Board()  # Initialize the board
    while not board.is_game_over():
        print(board)  # Display the board
        if board.turn == chess.WHITE:
            # Player's turn
            move_input = input("Enter your move (e.g., e2e4, or 'exit' to quit): ")
            if move_input.lower() == 'exit':
                print("You have chosen to exit the game.")
                break
            try:
                move = chess.Move.from_uci(move_input)
                if move in board.legal_moves:
                    board.push(move)
                else:
                    print("Illegal move. Please try again.")
            except ValueError:
                print("Invalid input format. Please try again.")
        else:
            # AI's turn
            print("AI is thinking...")
            ai_move = get_best_move(board, depth=3)  # Adjust depth for difficulty
            if ai_move is None:
                print("AI could not find a valid move. Game over.")
                break
            board.push(ai_move)
            print(f"AI played: {ai_move.uci()}")
    print(board)
    print("Game over. Result:", board.result())

if __name__ == "__main__":
    main()
