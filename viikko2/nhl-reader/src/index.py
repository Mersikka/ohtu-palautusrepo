from tarfile import SUPPORTED_TYPES
import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url).json()

class PlayerStats:
    def __init__(self, reader):
        self.response = reader.response

    def top_scorers_by_nationality(self, nat):
        filtered_ps = list(filter(lambda p: p["nationality"]==nat, self.response))
        sorted_ps = sorted(filtered_ps, key=lambda p: p["goals"]+p["assists"], reverse=True)
        sorted_ps = list(map(lambda p: Player(p), sorted_ps))
        return sorted_ps
    
def main():
    # url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    # response = requests.get(url).json()

    # players = sorted(list(filter(lambda p: p.nationality == "FIN", list(map(lambda p: Player(p), response)))), key=lambda p: p.goals + p.assists, reverse=True)

    # print("Players from FIN:\n")

    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
