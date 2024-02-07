# Função para imprimir o tabuleiro
def print_board(board):
    for row in board:
        print(" | ".join(row))  # Junta os elementos da linha com " | " e imprime
        print("-" * 9)  # Imprime uma linha de separação

# Função para verificar se há um vencedor
def check_winner(board, player):
    # Verifica as linhas
    for row in board:
        if all(cell == player for cell in row):  # Verifica se todos os elementos da linha são iguais ao jogador
            return True
    # Verifica as colunas
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):  # Verifica se todos os elementos da coluna são iguais ao jogador
            return True
    # Verifica a diagonal principal
    if all(board[i][i] == player for i in range(3)):
        return True
    # Verifica a diagonal secundária
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Função principal do jogo
def main():
    board = [[" "]*3 for _ in range(3)]  # Cria um tabuleiro vazio
    players = ['X', 'O']  # Define os jogadores
    turn = 0  # Contador de turnos

    print("Bem-vindo ao Jogo da Velha!")

    while True:
        print_board(board)  # Imprime o tabuleiro atual
        player = players[turn % 2]  # Define o jogador atual
        print(f"Vez do jogador {player}")

        row = int(input("Digite o número da linha (0, 1 ou 2): "))  # Solicita a linha ao jogador
        col = int(input("Digite o número da coluna (0, 1 ou 2): "))  # Solicita a coluna ao jogador

        if board[row][col] != " ":  # Verifica se a posição já está ocupada
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        board[row][col] = player  # Coloca a marca do jogador no tabuleiro

        # Verifica se há um vencedor ou se o jogo empatou
        if check_winner(board, player):
            print_board(board)
            print(f"O jogador {player} venceu!")
            break
        elif all(cell != " " for row in board for cell in row):  # Verifica se todas as células estão preenchidas (empate)
            print_board(board)
            print("Empate!")
            break

        turn += 1  # Incrementa o contador de turnos

if __name__ == "__main__":
    main()  # Chama a função principal se o script for executado diretamente
