"""
rectangle_game.py
A module for creating a rectangle and checking if points fall within it.
"""

# MIT License
#
# Copyright (c) 2024 Amrit
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software...


from random import randint


class Point:
    """
    Represents a point in 2D space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Initializes a new point with given x and y coordinates.

        Args:
            x (float): The x-coordinate.
            y (float): The y-coordinate.
        """
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle: "Rectangle") -> bool:
        """
        Determines whether the point falls within a given rectangle.

        Args:
            rectangle (Rectangle): The rectangle to check against.

        Returns:
            bool: True if the point is within the rectangle, False otherwise.
        """
        return (
            rectangle.point1.x < self.x < rectangle.point2.x
            and rectangle.point1.y < self.y < rectangle.point2.y
        )


class Rectangle:
    """
    Represents a rectangle in 2D space, defined by two diagonal points.

    Attributes:
        point1 (Point): The bottom-left corner of the rectangle.
        point2 (Point): The top-right corner of the rectangle.
    """

    def __init__(self, point1: Point, point2: Point) -> None:
        """
        Initializes a rectangle with two points.

        Args:
            point1 (Point): The first diagonal corner point of the rectangle.
            point2 (Point): The opposite diagonal corner point of the rectangle.
        """
        self.point1 = point1
        self.point2 = point2

    def area(self) -> float:
        """
        Computes the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)


if __name__ == "__main__":

    # Main game logic to guess whether a user-supplied point is inside a randomly
    # generated rectangle and whether their guess for the area is accurate.

    # Create a rectangle with random points
    rect = Rectangle(
        Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19))
    )  # pragma: no cover

    # Print rectangle coordinates
    print(
        "Rectangle Coordinates: ",
        rect.point1.x,
        ",",
        rect.point1.y,
        "and",
        rect.point2.x,
        ",",
        rect.point2.y,
    )  # pragma: no cover

    # Get point and area from user
    user_point = Point(
        float(input("Guess x: ")), float(input("Guess y: "))
    )  # pragma: no cover
    user_area = float(input("Guess rectangle area: "))  # pragma: no cover

    # Print the results of the game
    print(
        "Your point was inside rectangle: ", user_point.falls_in_rectangle(rect)
    )  # pragma: no cover
    print("Your area was off by: ", rect.area() - user_area)  # pragma: no cover
