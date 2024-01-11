import pygame
import sys

def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def tic_tac_toe():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption('Tic Tac Toe')

    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    def draw_board():
        screen.fill((0, 0, 0))
        for row in range(3):
            for col in range(3):
                x = 100 * col + 50
                y = 100 * row + 50
                if board[row][col] == 'X':
                    pygame.draw.line(screen, (255, 255, 255), (x - 50, y - 50), (x + 50, y + 50), 5)
                    pygame.draw.line(screen, (255, 255, 255), (x - 50, y + 50), (x + 50, y - 50), 5)
                elif board[row][col] == 'O':
                    pygame.draw.circle(screen, (255, 255, 255), (x, y), 40, 5)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // 100
                row = y // 100

                if board[row][col] == ' ':
                    board[row][col] = player
                    if check_win(board):
                        print(f"Player {player} wins!")
                        running = False
                    else:
                        player = 'O' if player == 'X' else 'X'

        screen.fill((255, 255, 255))

        draw_board()

        pygame.display.flip()

if __name__ == "__main__":
    tic_tac_toe()