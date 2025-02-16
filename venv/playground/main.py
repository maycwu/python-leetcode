from Player import Player
from Team import Team


class Main:
    players = []  # This initializes the players list
    @staticmethod
    def main():
        teams = Main.create_teams()

    @staticmethod
    def create_player(teams):
        # Players data
        player_data = [
            ["0", "Allen Iverson", "1"],
            ["0", "Aaron McKie", "2"],
            ["0", "Dikembe Mutombo", "3"],
            ["0", "Tyrone Hill", "4"],
            ["0", "Jumaine Jones", "5"],
            ["1", "Kobe Bryant", "6"],
            ["1", "Shaquille O'Neal", "7"],
            ["1", "Rick Fox", "8"],
            ["1", "Horace Grant", "9"],
            ["1", "Derek Fisher", "10"]
        ]

        team_index = 0

        for team in teams:
            team_players = Player.populate_player(player_data, team_index)
            for player in team_players:
                team.add_players(player)
            team_index += 1

    @staticmethod
    def create_teams():
        team_data = [
            ["Philadelphia 76ers", "Conference 1"],
            ["Los Angeles Lakers", "Conference 2"]
        ]

        teams = Team.populate_teams(team_data)
        player = Main.create_player(teams)
        return teams


    def print_players(players):
        for player in players:
            print(player.get_name() + " " + player.get_number())


# Main execution
if __name__ == "__main__":
    Main.main()
