class Player:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return str("Имя: " + str(self.name) + " Возраст: " + str(self.age) + " Позиция: " + str(self.position))


class Team:
    def __init__(self, name, coach):
        self.name = name
        self.coach = coach
        self.players = []

    def add_player(self, player):
        if player not in self.players:
            self.players.append(player)

    def remove_player(self, player):
        if player in self.players:
            self.players.remove(player)

    def list_players(self):
        if not self.players:
            print("игроков нет")
        else:
            for player in self.players:
                print(player)


if __name__ == "__main__":
    # Создаем игроков
    player1 = Player("Иванов", 25, "Нападающий")
    player2 = Player("Петров", 30, "Полузащитник")
    player3 = Player("Сидоров", 28, "Защитник")

    team1 = Team("Красные", "Краснов")
    team2 = Team("Синие", "Синёв")

    team1.add_player(player1)
    team1.add_player(player2)
    team2.add_player(player3)

    team1.list_players()
    team2.list_players()

    team1.remove_player(player2)

    team1.list_players()
