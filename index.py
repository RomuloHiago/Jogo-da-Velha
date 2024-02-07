def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def main():
    board = [[" "]*3 for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    print("Bem-vindo ao Jogo da Velha!")

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Vez do jogador {player}")

        row = int(input("Digite o número da linha (0, 1 ou 2): "))
        col = int(input("Digite o número da coluna (0, 1 ou 2): "))

        if board[row][col] != " ":
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        board[row][col] = player
        if check_winner(board, player):
            print_board(board)
            print(f"O jogador {player} venceu!")
            break
        elif all(cell != " " for row in board for cell in row):
            print_board(board)
            print("Empate!")
            break

        turn += 1

if __name__ == "__main__":
    main()
