import random

class Card:
    def __init__(self, name):
        self.name = name
        self.rows = self.generate_card()

    def generate_card(self):
        numbers = random.sample(range(1, 91), 15)  # 15 уникальных чисел
        rows = []
        for i in range(3):
            row_numbers = sorted(numbers[i*5:(i+1)*5])
            row = [''] * 9
            positions = random.sample(range(9), 5)
            for pos, num in zip(sorted(positions), row_numbers):
                row[pos] = num
            rows.append(row)
        return rows

    def has_number(self, number):
        for row in self.rows:
            if number in row:
                return True
        return False

    def cross_number(self, number):
        for row in self.rows:
            for i in range(len(row)):
                if row[i] == number:
                    row[i] = '-'
                    return True
        return False

    def is_complete(self):
        for row in self.rows:
            for item in row:
                if isinstance(item, int):
                    return False
        return True

    def display(self):
        print("-----Карточка", self.name + "-----")
        for row in self.rows:
            print(' '.join(f'{str(num):>2}' if num != '' else '  ' for num in row))
        print("-" * 26)


class Barrel:
    def __init__(self):
        self.barrels = list(range(1, 91))
        random.shuffle(self.barrels)

    def draw(self):
        if self.barrels:
            return self.barrels.pop()
        return None

    def remaining(self):
        return len(self.barrels)


class Player:
    def __init__(self, name):
        self.card = Card(name)

    def make_turn(self, number, auto=False):
        if self.card.has_number(number):
            if auto:
                self.card.cross_number(number)
                return True
            else:
                answer = input("Зачеркнуть цифру? (y/n): ").strip().lower()
                if answer == 'y':
                    if self.card.cross_number(number):
                        return True
                    else:
                        print("Числа нет на карточке. Вы проиграли!")
                        return False
                elif answer == 'n':
                    print("Число было на карточке. Вы проиграли!")
                    return False
        else:
            if not auto:
                answer = input("Зачеркнуть цифру? (y/n): ").strip().lower()
                if answer == 'y':
                    print("Числа нет на карточке. Вы проиграли!")
                    return False
            return True


class Game:
    def __init__(self):
        self.user = Player("Вы")
        self.computer = Player("Компьютер")
        self.barrel = Barrel()

    def start(self):
        while True:
            number = self.barrel.draw()
            if number is None:
                print("Бочонки закончились. Ничья!")
                break

            print("\nНовый бочонок:", number, "(осталось", str(self.barrel.remaining()) + ")")
            self.user.card.display()
            self.computer.card.display()

            if not self.user.make_turn(number, auto=False):
                print("Победа компьютера!")
                break

            self.computer.make_turn(number, auto=True)

            if self.user.card.is_complete():
                print("Вы победили!")
                break
            if self.computer.card.is_complete():
                print("Победа компьютера!")
                break


if __name__ == "__main__":
    game = Game()
    game.start()
