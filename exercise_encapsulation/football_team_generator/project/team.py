class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player):
        for plr in self.__players:
            if plr.name == player.name:
                return f"Player {player.name} has already joined"

        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        for plr in self.__players:
            if plr.name == player_name:
                self.__players.remove(plr)
                return plr

        return f"Player {player_name} not found"
