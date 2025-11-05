import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    players = sorted(list(filter(lambda p: p.nationality == "FIN", list(map(lambda p: Player(p), response)))), key=lambda p: p.goals + p.assists, reverse=True)

    print("Players from FIN:\n")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
