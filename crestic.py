class TicTacToe:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display_board(self):
        print("\nТекущее поле:")
        for row in self.board:
            print(" | ".join(cell if cell else " " for cell in row))
            print("-" * 9)

    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == "":
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self):
        col_mark, mark2 = "null", False
        for i in range(3):
            for j in range(3):
                if (self.board[j][i] == "" or self.board[j][i] != col_mark) and col_mark != "null":
                    mark2 = True
                    break
                else:
                    col_mark = self.board[j][i]
            if not mark2:
                return self.board[i][0]

            row_mark, mark2 = "null", False
            for j in self.board[i]:
                if (j == "" or j != row_mark) and row_mark != "null":
                    mark2 = True
                    break
                else:
                    row_mark = i
            if not mark2:
                return self.board[i][0]

            if (self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] or
            self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]):
                return self.board[1][1]

        return ""

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def is_full(self) -> bool:
        return all(cell != "" for row in self.board for cell in row)



class Game:
    def __init__(self):
        self.game = TicTacToe()

    def play(self):
        print("Игра 'Крестики-Нолики' началась!")
        self.game.display_board()

        while True:
            try:
                row = int(input("строка:"))
                col = int(input("столбец"))
            except ValueError:
                print("не корректный ход.")
                continue

            if not self.game.make_move(row, col):
                print("Ошибка пользователя!")
                continue

            self.game.display_board()

            winner = self.game.check_winner()
            if winner:
                print(f"Игрок {winner} победил!")
                break
            elif self.game.is_full():
                print("Ничья! Поле заполнено.")
                break
            else:
                self.game.switch_player()



if __name__ == "__main__":
    game = Game()
    game.play()
