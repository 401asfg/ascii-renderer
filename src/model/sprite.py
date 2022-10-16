class Sprite:
    """
    A renderable ascii character
    """

    _character: str

    def __init__(self, character: str):
        """
        Initializes the class

        :param character: The ascii character that this sprite represents
        :raise ValueError: If the given character has a length that is not equal to 1
        """
        if len(character) != 1:
            raise ValueError("Attempted to create a sprite with a character that doesn't have a length of 1")

        self._character = character

    def __str__(self) -> str:
        """
        :return: The ascii character this sprite represents
        """
        return self._character

    def __eq__(self, other) -> bool:
        """
        :param other: The other sprite
        :return: True if both sprites have the same values; otherwise false
        """
        return self.__dict__ == other.__dict__
