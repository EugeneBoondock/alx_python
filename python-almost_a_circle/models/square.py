from models.rectangle import Rectangle

class Square(Rectangle):
    """
    A class representing a square, inheriting from the Rectangle class.
    true
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): one size of the square.
            x (int, optional): X-coordinate of the top-left corner. Defaults to 0.
            y (int, optional): Y-coordinate of the top-left corner. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Property for the size of the square (same as width).
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square.

        Args:
            value (int): Value to set the size of the square to.
        """
        self.width = value
        self.height = value

    def area(self):
        """
        Calculate the area of the square.
        """
        return self.width * self.width

    def display(self):
        """
        Display the square using the '#' character.
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)
