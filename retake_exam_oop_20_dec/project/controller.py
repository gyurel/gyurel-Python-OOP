class Controller:
    def __init__(self):
        self.players: list = []
        self.supplies: list = []

    def add_player(self, *args):
        successfully_added = []
        for player in args:
            if self.object_name_not_in_list(player, self.players):
                self.players.append(player)
                successfully_added.append(player.name)
        return f"Successfully added: {', '.join(x for x in successfully_added)}"

    def add_supply(self, *args):
        for supll in args:
            self.supplies.append(supll)

    def sustain(self, player_name: str, sustenance_type: str):
        types_list = ["Food", "Drink"]
        if sustenance_type not in types_list:
            return None

        current_player = self.find_player(player_name, self.players)
        if not current_player.need_sustenance:
            return f"{player_name} have enough stamina."

        current_supply = self.find_supply(sustenance_type, self.supplies)

        if 100 - current_player.stamina <= current_supply.energy:
            current_player.stamina += current_supply.energy
            return f"{player_name} sustained successfully with {current_supply.name}."
        else:
            current_player.stamina += 100 - current_player.stamina
            return f"{player_name} sustained successfully with {current_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.find_player(first_player_name, self.players)
        second_player = self.find_player(second_player_name, self.players)

        if first_player.stamina == 0 and second_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\n" \
                   f"Player {second_player_name} does not have enough stamina."
        elif first_player.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif second_player.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        first_stamina = first_player.stamina
        second_stamina = second_player.stamina

        if first_player.stamina < second_player.stamina:
            second_stamina -= first_stamina * 0.5
            if self.has_lost(second_stamina, second_player):
                return f"Winner: {first_player.name}"
            first_stamina -= second_stamina * 0.5
            if self.has_lost(first_stamina, first_player):
                return f"Winner: {second_player.name}"

        if second_player.stamina < first_player.stamina:
            first_stamina -= second_stamina * 0.5
            if self.has_lost(first_stamina, first_player):
                return f"Winner: {second_player.name}"
            second_stamina -= first_stamina * 0.5
            if self.has_lost(second_stamina, second_player):
                return f"Winner: {first_player.name}"

        if first_player.stamina > second_player.stamina:
            return f"Winner: {first_player.name}"

        if second_player.stamina > first_player.stamina:
            return f"Winner: {second_player.name}"

    def next_day(self):
        for player in self.players:
            current_stamina = player.stamina
            to_reduce = player.age * 2
            current_stamina -= to_reduce
            if current_stamina < 0:
                player.stamina = 0
            else:
                player.stamina = current_stamina

            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    @staticmethod
    def object_name_not_in_list(obj, list_obj):
        if obj in list_obj:
            return False
        return True

    def find_player(self, name, list_players):
        for player in list_players:
            if player.name == name:
                return player
        return None

    def find_supply(self, sustainance_type, sustainance_list):
        for sust in sustainance_list[::-1]:
            if sust.__class__.__name__ == sustainance_type:
                self.supplies.remove(sust)
                return sust
        raise Exception(f"There are no {sustainance_type.lower()} supplies left!")

    def has_lost(self, stamina, player):
        if stamina <= 0:
            player.stamina = 0
            return True
        player.stamina = stamina
        return False