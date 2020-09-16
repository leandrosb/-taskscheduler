from typing import Dict


class person():
    """Class of person"""

    def __init__(self) -> None:
        self._persons = []
        self.name = None
        self.age = None
        self.genre = None
        self.person = {}

    def insert(self, name: str, age: int, genre: str) -> Dict:
        """insert person
        Args:
            name (str): [name of person]
            age (int): [age of person]
            genre (str): [genre (M or F)]

        Returns:
            Dict: [Person simple]
        """
        self.name = name
        self.age = age
        self.genre = genre
        self.person = {'name': self.name, 'age': self.age, 'genre': self.genre}
        return self.person

    def addperson(self) -> None:
        """add person to the global object"""

        self._persons.append(self.person)
