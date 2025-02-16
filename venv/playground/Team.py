
class Team:
    def __init__(self, name, conference):
        self.name = name
        self.conference = conference
        self.players = []

    def get_name(self):
        return self.name

    def get_conference(self):
        return self.conference

    def get_players(self):
        return self.players

    def add_players(self, player):
        self.players.append(player)

    # Other Member functions

    # Add method to populate teams here
    def populate_teams(team_data):
        teams = []
        for data in team_data:
            name = data[0]
            conference = data[1]
            team = Team(name, conference)
            teams.append(team)
        return teams

    # Method to print individial team
    def print_team(self):
        print(f"Team Name: {self.get_name()}, Conference: {self.get_conference()}")

    def print_data_team(self):
        self.print_team()
        for player in self.players:
            player.print_player()