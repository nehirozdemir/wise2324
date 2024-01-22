"""Aufgabe 1:"""


class Knight:
    """Classifies knights"""

    armor = bool(1)

    def __init__(
        self,
        full_name: str,
        special_ability: str,
        skill: int,
        round_table: bool = True,
        health: int = 100,
    ):
        self.full_name = full_name
        self._special_ability = special_ability
        self.skill = skill
        self.round_table = round_table
        self.__health = health

    # 9: refactor (R0913, too-many-arguments, Knight.__init__) Too many arguments (6/5)
    # Ich bekomme immer den gleichen Pylint-Fehler. Da dies (self, full_name, usw.) die
    # vorgegebenen Spezifikationen waren, wusste ich nicht, wie ich es mit "weniger Argumenten"
    # machen sollte.

    # Aufgabe 2:
    def gethealth(self):
        """Gets health"""
        return self.__health

    def sethealth(self, health):
        """Sets the value of health and raises errors"""
        if health <= 0:
            raise ValueError("Death is not an option.")

    health = property(gethealth, sethealth)

    # Aufgabe 3:
    def __repr__(self):
        return f"{self.full_name} is at {self.health}% health."

    # Aufgabe 4:
    def h(self):
        """Health x 0.8"""
        self.__health = int(self.__health - 20)

    def duel(self, knight):
        """Makes the knights don't fight each other"""
        if self.round_table is True and knight.round_table is True:
            print("Knights of the Round Table don't fight each other.")
        else:
            if self.skill > knight.skill:
                print(self.full_name + " wins, " + knight.full_name + " loses.")
                knight.h()
            else:
                print(knight.full_name + " wins, " + self.full_name + " loses.")
                self.__health = int(self.__health - 20)

    # Aufgabe 5

    # References
    # https://chat.openai.com/share/199c92a8-81d5-40f4-9db9-238b9bdafc44


class King(Knight):
    """ "Class inheritance / child class"""

    def __init__(self, full_name: str):
        super().__init__(
            full_name,
            special_ability="aristocracy",
            skill=float("inf"),
            round_table=True,
            health=100,
        )

    def __repr__(self):
        return f"The health of {self.full_name} is none of your business."


if __name__ == "__main__":
    bedevere = Knight("Sir Bedevere the Wise", "wisdom", 55)
    lancelot = Knight("Sir Lancelot the Brave", "bravery", 60)
    black_knight = Knight("Black Knight", "confidence", 100, False)
    knight_of_ni = Knight("Knight Who Says Ni", "ni", 55, False)
    bedevere.duel(lancelot)
    # Knights of the Round Table don't fight each other.
    print(bedevere)
    # Sir Bedevere the Wise is at 100% health.
    bedevere.duel(black_knight)
    # Black Knight wins, Sir Bedevere the Wise loses.
    print(bedevere)
    # Sir Bedevere the Wise is at 80% health.
    bedevere.duel(knight_of_ni)
    # Knight Who Says Ni wins, Sir Bedevere the Wise loses.
    print(bedevere)
    # Sir Bedevere the Wise is at 60% health.
    arthur = King("King Arthur")
    print(arthur)
