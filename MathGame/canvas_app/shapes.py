"""
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE

THIS MODULE CONTAINS CLASSES FOR DRAWING SHAPES ON A CANVAS.
"""


class Rectangle:
    """
    A class to represent a rectangle shape.

    Attributes:
        x (int): X-coordinate of the top-left corner.
        y (int): Y-coordinate of the top-left corner.
        height (int): Height of the rectangle.
        width (int): Width of the rectangle.
        color (tuple): Color of the rectangle in (R, G, B).
    """

    def __init__(
        self, x: int, y: int, height: int, width: int, color: tuple[int, int, int]
    ):
        """
        Initializes the rectangle with position, dimensions, and color.

        Args:
            x (int): X-coordinate of the rectangle.
            y (int): Y-coordinate of the rectangle.
            height (int): Height of the rectangle.
            width (int): Width of the rectangle.
            color (tuple): Color in (R, G, B).
        """
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas) -> None:
        """
        Draws the rectangle on the canvas.

        Args:
            canvas (Canvas): Canvas object where the rectangle is drawn.
        """
        canvas.data[self.x : self.x + self.height, self.y : self.y + self.width] = (
            self.color
        )


class Square:
    """
    A class to represent a square shape.

    Attributes:
        x (int): X-coordinate of the top-left corner.
        y (int): Y-coordinate of the top-left corner.
        side (int): Length of the square's side.
        color (tuple): Color of the square in (R, G, B).
    """

    def __init__(self, x: int, y: int, side: int, color: tuple[int, int, int]):
        """
        Initializes the square with position, side length, and color.

        Args:
            x (int): X-coordinate of the square.
            y (int): Y-coordinate of the square.
            side (int): Length of the square's side.
            color (tuple): Color in (R, G, B).
        """
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas) -> None:
        """
        Draws the square on the canvas.

        Args:
            canvas (Canvas): Canvas object where the square is drawn.
        """
        canvas.data[self.x : self.x + self.side, self.y : self.y + self.side] = (
            self.color
        )
