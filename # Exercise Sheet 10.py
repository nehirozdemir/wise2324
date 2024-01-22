"""exercise_sheet_10"""


ARMOR = bool(1)

#Aufgabe 1

class Knight:
    """Classifies knights"""
    def __init__(
        self,
        full_name: str,
        special_ability: str,
        skill: int,
        round_table=bool(1),
        health=100,
    ):
        self.full_name = full_name
        self._special_ability = special_ability
        self.skill = skill
        self.round_table = round_table
        self.__health = health
