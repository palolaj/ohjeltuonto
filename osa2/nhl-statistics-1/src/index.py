from statistics_service import StatisticsService
from player_reader import PlayerReader


def main():
    stats = StatisticsService(PlayerReader("https://raw.githubusercontent.com/ohjelmistotuotanto-jyu/tehtavat/refs/heads/main/osa2/stats/players-23-24.txt"))
    philadelphia_flyers_players = stats.team("PIT")
    top_scorers = stats.top(10)

    print("Pittsburgh Penguins:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)


if __name__ == "__main__":
    main()
