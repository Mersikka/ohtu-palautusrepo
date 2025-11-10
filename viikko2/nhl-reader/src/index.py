import re

import requests
from rich.console import Console
from rich.table import Table
from rich.text import Text

from player import Player

console = Console(color_system="auto")


class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url, timeout=10).json()


class PlayerStats:
    def __init__(self, reader):
        self.response = reader.response

    def top_scorers_by_nationality(self, nat):
        filtered_ps = list(filter(lambda p: p["nationality"] == nat, self.response))
        sorted_ps = sorted(
            filtered_ps, key=lambda p: p["goals"] + p["assists"], reverse=True
        )
        sorted_ps = list(map(lambda p: Player(p), sorted_ps))
        return sorted_ps


def get_season():
    header = Text()
    header.append("Season ", style="bold white")
    header.append(
        "[2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26] ",
        style="cyan",
    )
    header.append("(2024-25)", style="bold green")
    header.append(": ", style="bold white")

    season = console.input(header)
    return season


def is_valid_season(season):
    pattern = r"^(2018-19|2019-20|2020-21|2021-22|2022-23|2023-24|2024-25|2025-26|)$"
    return bool(re.match(pattern, season))


def get_nationality():
    nationality = Text()
    nationality.append("Nationality ", style="bold white")
    nationality.append(
        "[USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS]",
        style="magenta",
    )
    nationality.append(": ", style="strong white")

    nat = console.input(nationality)
    return nat.upper()


def is_valid_nat(nat):
    pattern = r"^(USA|FIN|CAN|SWE|CZE|RUS|SLO|FRA|GBR|SVK|DEN|NED|AUT|BLR|GER|SUI|NOR|UZB|LAT|AUS)$"
    return bool(re.match(pattern, nat))


def make_player_table(players):
    p_table = Table(show_header=True, header_style="bold white")
    p_table.add_column("Player", style="cyan")
    p_table.add_column("teams", style="magenta")
    p_table.add_column("goals", style="green")
    p_table.add_column("assists", style="green")
    p_table.add_column("points", style="green")

    for p in players:
        p_table.add_row(
            p.name,
            p.team,
            f"{p.goals}",
            f"{p.assists}",
            f"{p.goals + p.assists}",
        )
    return p_table


def main():
    url = ""
    season = ""
    while True:
        season = get_season()
        if is_valid_season(season):
            if season == "":
                url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
                season = "2024-25"
            else:
                url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
            break
    console.print('\n')
    
    nat = ""
    while True:
        nat = get_nationality()
        if nat == "":
            break
        if is_valid_nat(nat):
            reader = PlayerReader(url)
            stats = PlayerStats(reader)
            players = stats.top_scorers_by_nationality(nat)

            console.print(
                Text(f"Season {season} players from {nat}", style="italic dim")
            )

            player_table = make_player_table(players)
            console.print(player_table)

if __name__ == "__main__":
    main()
