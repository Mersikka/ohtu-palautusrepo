from enum import Enum, auto

class Advantage(Enum):
    P1ADV = auto()
    P2ADV = auto()
    P1WIN = auto()
    P2WIN = auto()

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.p1 = player1_name
        self.p2 = player2_name
        self.scores = {
            self.p1: 0,
            self.p2: 0
        }

    def won_point(self, player_name):
        self.scores[player_name] += 1

    def is_tied(self):
        return self.scores[self.p1] == self.scores[self.p2]

    def is_advantage_state(self):
        return self.scores[self.p1] >= 4 or self.scores[self.p2] >= 4

    def get_player_advantage(self):
        score_diff = self.scores[self.p1] - self.scores[self.p2]
        match score_diff:
            case 1:
                return Advantage.P1ADV.name
            case -1:
                return Advantage.P2ADV.name
            case _ if score_diff >= 2:
                return Advantage.P1WIN.name
            case _ if score_diff <= -2:
                return Advantage.P2WIN.name

    def get_score(self):
        output = ""

        if self.is_tied():
            if self.scores[self.p1] == 0:
                output = "Love-All"
            elif self.scores[self.p1] == 1:
                output = "Fifteen-All"
            elif self.scores[self.p1] == 2:
                output = "Thirty-All"
            else:
                output = "Deuce"
        elif self.is_advantage_state():
            adv = self.get_player_advantage()
            match adv:
                case "P1ADV":
                    output = "Advantage player1"
                case "P2ADV":
                    output = "Advantage player2"
                case "P1WIN":
                    output = "Win for player1"
                case "P2WIN":
                    output = "Win for player2"
        else:
            for player, score in self.scores.items():
                if player == self.p2:
                    output += "-"
                match score:
                    case 0:
                        output += "Love"
                    case 1:
                        output += "Fifteen"
                    case 2:
                        output += "Thirty"
                    case 3:
                        output += "Forty"

        return output
