from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, Or

class Query:
    def __init__(self):
        self.matchers = []

    def add_matcher(self, matcher):
        self.matchers.append(matcher)

    def get_query(self):
        if self.matchers:
            return And(*self.matchers)
        return All()

class QueryOneOf:
    def __init__(self, query, matchers):
        self.query = query
        if matchers:
            self.built = map(lambda m: m.build(), matchers)
        else:
            self.built = Not(All())

    def add_matcher(self, matcher):
        return self.query.add_matcher(matcher)

    def get_query(self):
        return Or(self.built)

class QueryPlaysIn:
    def __init__(self, query, team):
        self.query = query
        self.query.add_matcher(PlaysIn(team))

    def add_matcher(self, matcher):
        return self.query.add_matcher(matcher)

    def get_query(self):
        return self.query.get_query()

class QueryHasAtLeast:
    def __init__(self, query, val, attr):
        self.query = query
        self.query.add_matcher(HasAtLeast(val, attr))

    def add_matcher(self, matcher):
        return self.query.add_matcher(matcher)

    def get_query(self):
        return self.query.get_query()

class QueryHasFewerThan:
    def __init__(self, query, val, attr):
        self.query = query
        self.query.add_matcher(HasFewerThan(val, attr))

    def add_matcher(self, matcher):
        return self.query.add_matcher(matcher)

    def get_query(self):
        return self.query.get_query()

class QueryBuilder:
    def __init__(self, query=Query()):
        self.query_object = query

    def plays_in(self, team):
        return QueryBuilder(QueryPlaysIn(self.query_object, team))

    def has_at_least(self, val, attr):
        return QueryBuilder(QueryHasAtLeast(self.query_object, val, attr))

    def has_fewer_than(self, val, attr):
        return QueryBuilder(QueryHasFewerThan(self.query_object, val, attr))

    def one_of(self, *matchers):
        return QueryBuilder(QueryOneOf(self.query_object, matchers))

    def build(self):
        return self.query_object.get_query()

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = (
      query
        .one_of(
          query.plays_in("PHI")
              .has_at_least(10, "assists")
              .has_fewer_than(10, "goals"),
          query.plays_in("EDM")
              .has_at_least(50, "points")
        )
        .build()
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
