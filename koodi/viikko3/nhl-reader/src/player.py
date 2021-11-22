import requests

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
    
    def __str__(self):
        return self.response

class PlayerStats:
    def __init__(self, response):
        self.players = []
        self.response = response

    def top_scorers_by_nationality(self, nationality):

        for player_dict in self.response:
            if player_dict['nationality'] == nationality:
                player = Player(
                    player_dict['name'], player_dict['team'], player_dict['goals'], player_dict['assists']
                )
                self.players.append(player)

    def __str__(self):
        return self.players