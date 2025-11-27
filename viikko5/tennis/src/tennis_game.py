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
                return "P1ADV"
            case -1:
                return "P2ADV"
            case _ if score_diff >= 2:
                return "P1WIN"
            case _ if score_diff <= -2:
                return "P2WIN"

    def score_to_string(self, score):
        match score:
            case 0:
                string = "Love"
            case 1:
                string = "Fifteen"
            case 2:
                string = "Thirty"
            case 3:
                string = "Forty"
        return string

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
            output += self.score_to_string(self.scores[self.p1])
            output += "-"
            output += self.score_to_string(self.scores[self.p2])
        return output
