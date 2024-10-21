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

all test cases for the canvas_app module.
"""

import unittest
import numpy as np
from canvas_app.canvas import Canvas
from canvas_app.shapes import Rectangle, Square


class TestCanvas(unittest.TestCase):
    """
    Test cases for the Canvas class.
    """

    def test_canvas_initialization(self):
        """
        Test the initialization of the Canvas class.

        This method verifies that the Canvas object is initialized correctly
        with the given height, width, and background color.
        """
        canvas = Canvas(100, 100, (255, 255, 255))
        self.assertEqual(canvas.height, 100)
        self.assertEqual(canvas.width, 100)
        self.assertTrue(np.array_equal(canvas.color, (255, 255, 255)))
        self.assertEqual(canvas.data.shape, (100, 100, 3))

    def test_canvas_make(self):
        """
        Test the 'make' method of the Canvas class.

        This method tests if the Canvas object correctly saves the canvas
        as an image to the specified file path.
        """
        canvas = Canvas(100, 100, (255, 255, 255))
        canvas.make("test_output.png")
        with open("test_output.png", "rb") as f:
            self.assertIsNotNone(f.read())


class TestShapes(unittest.TestCase):
    """
    Test cases for the Rectangle and Square shape classes.
    """

    def test_rectangle_draw(self):
        """
        Test the 'draw' method of the Rectangle class.

        This method verifies that the Rectangle is drawn correctly
        on the Canvas object at the specified position and size.
        """
        canvas = Canvas(100, 100, (255, 255, 255))
        rect = Rectangle(10, 10, 20, 30, (255, 0, 0))
        rect.draw(canvas)
        expected_color = [255, 0, 0]
        self.assertTrue(np.array_equal(canvas.data[10, 10], expected_color))
        self.assertTrue(np.array_equal(canvas.data[29, 39], expected_color))

    def test_square_draw(self):
        """
        Test the 'draw' method of the Square class.

        This method verifies that the Square is drawn correctly
        on the Canvas object at the specified position and size.
        """
        canvas = Canvas(100, 100, (255, 255, 255))
        square = Square(20, 20, 15, (0, 255, 0))
        square.draw(canvas)
        expected_color = [0, 255, 0]
        self.assertTrue(np.array_equal(canvas.data[20, 20], expected_color))
        self.assertTrue(np.array_equal(canvas.data[34, 34], expected_color))


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
