class PointWithoutSlots:
    """A simple class to represent a point in 2D space without using __slots__.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """

    def __init__(self, x, y):
        """Initialize a Point instance.

        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def distance_to_origin(self):
        """Calculate the distance from the point to the origin (0, 0).

        Returns:
            float: The Euclidean distance to the origin.
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5


class PointWithSlots:
    """A simple class to represent a point in 2D space using __slots__ to optimize memory usage.

    The use of __slots__ will tell Python explicitly what attributes this class will have,
    leading to memory savings and potentially faster attribute access.

    __slots__:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        """Initialize a Point instance with __slots__.

        Args:
            x (float): The x-coordinate of the point.
            y (float): The y-coordinate of the point.
        """
        self.x = x  # Assigns value to the slot 'x'
        self.y = y  # Assigns value to the slot 'y'

    def distance_to_origin(self):
        """Calculate the distance from the point to the origin (0, 0) using __slots__.

        Returns:
            float: The Euclidean distance to the origin.
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5
