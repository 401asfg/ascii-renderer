class Char(str):        # TODO: should this be called a sprite?
    """
    A single, renderable ascii character
    """

    def __new__(cls, value: str):
        """
        Initializes the class

        :param value: The ascii character that the sprite represents
        :raise ValueError: If the given value has a length that isn't equal to 1
        """
        if len(value) != 1:
            raise ValueError("Tried to create a char with multiple characters")

        return str.__new__(cls, value)
