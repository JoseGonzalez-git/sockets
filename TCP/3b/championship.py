import math
import random
from operator import attrgetter
from typing import TypeVar
import copy

T = TypeVar("T")


def split_list(l: list[T]) -> tuple[list[T], list[T]]:
    middle_index = math.ceil(len(l) / 2)
    return l[:middle_index], l[middle_index:]


class Team:
    def __init__(self, name: str) -> None:
        self.name = name
        self.points = int(0)

    def __str__(self):
        return f"Team {self.name}, points: {self.points}"


class Match:
    def __init__(self, pair: tuple[Team, Team]) -> None:
        self.team1, self.team2 = pair
        self.points_team1, self.points_team2 = int(0), int(0)
        self.__play()

    def __play(self) -> None:
        self.points_team1 = random.randint(0, 20)
        self.points_team2 = random.randint(0, 20)

    def __result(self) -> tuple[Team, Team]:
        self.team1.points += self.points_team1
        self.team2.points += self.points_team2
        return self.team1, self.team2

    def winner(self) -> Team:
        return max(self.__result(), key=attrgetter("points"))

    def loser(self) -> Team:
        return min(self.__result(), key=attrgetter("points"))


class Group:
    def __init__(self, teams: list[Team]) -> None:
        self.teams = teams
        self.eliminated: list[Team] = []

    def pairs(self):
        splitted = split_list(self.teams)
        return zip(splitted[0], splitted[1])

    def winner(self) -> Team:
        return max(self.teams, key=attrgetter("points"))

    def winners(self, matches: list[Match]):
        winners: list[Team] = []
        for _match in matches:
            winners.append(_match.winner())
        return winners

    def losers(self, matches: list[Match]):
        losers: list[Team] = []
        for _match in matches:
            losers.append(_match.loser())
        return losers

    def remove_losers(self, matches: list[Match]):
        self.eliminated.extend(self.losers(matches))
        self.teams = self.winners(matches)

    def has_pending_matches(self):
        return len(self.teams) > 1

    def __str__(self):
        result = ""
        for team in self.teams:
            result += str(team) + "\n"

        if len(self.eliminated) > 0:
            result += "\nEliminated\n"
            for team in self.eliminated:
                result += str(team) + "\n"

        return result


class Phase:
    def __init__(self, groups: tuple[Group, Group]) -> None:
        self.group1, self.group2 = groups

    def execute(self):
        return self.__play(self.group1), self.__play(self.group2)

    def __play(self, group: Group):
        matches: list[Match] = []
        pairs = group.pairs()
        for pair in pairs:
            matches.append(Match(pair))
        return matches

    def __str__(self) -> str:
        result = ""
        groups = self.group1, self.group2
        for i, group in enumerate(groups):
            result += f"Group {i+1}:\n"
            result += str(group) + "\n"

        return result


class Championship:
    def __init__(self, teams: list[Team]) -> None:
        if len(teams) > 20 or len(teams) < 10:
            raise Exception("The champion only allows 20 teams, or at least 10.")

        group1, group2 = split_list(teams)

        self.groups = Group(group1), Group(group2)
        self.phases: list[Phase] = []
        self.winner: Team
        self.loser: Team

        self.__start()
        self.__final()

    def __start(self):
        while (
            self.groups[0].has_pending_matches()
            and self.groups[1].has_pending_matches()
        ):
            current_phase = Phase((self.groups[0], self.groups[1]))
            self.phases.append(copy.deepcopy(current_phase))
            result = current_phase.execute()
            self.groups[0].remove_losers(result[0])
            self.groups[1].remove_losers(result[1])

    def __final(self):
        pair = self.groups[0].winner(), self.groups[1].winner()
        match = Match(pair)
        self.winner = match.winner()
        self.loser = match.loser()

    def result(self):
        return f"Winner {self.winner.name} with {self.winner.points} points.\nSecond {self.loser.name} with {self.loser.points} points."

    def number_of_phases(self):
        return len(self.phases)

    def __str__(self):
        result = ""
        for i, phase in enumerate(self.phases):
            result += f"\nPhase {i+1}:\n"
            result += str(phase)

        result += "\nFinal:\n" + self.result()
        return result.strip()
