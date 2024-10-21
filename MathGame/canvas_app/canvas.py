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

script to create a canvas on which shapes can be drawn.
"""

import numpy as np
from PIL import Image


class Canvas:
    """
    A class to represent a canvas on which shapes can be drawn.

    Attributes:
        height (int): Height of the canvas.
        width (int): Width of the canvas.
        color (tuple): Background color of the canvas (R, G, B).
        data (np.ndarray): Numpy array to represent the canvas.
    """

    def __init__(self, height: int, width: int, color: tuple[int, int, int]):
        """
        Initializes the canvas with the given height, width, and color.

        Args:
            height (int): Height of the canvas.
            width (int): Width of the canvas.
            color (tuple): Background color in (R, G, B).
        """
        self.height = height
        self.width = width
        self.color = color
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath: str) -> None:
        """
        Saves the current state of the canvas as an image.

        Args:
            imagepath (str): Path to save the image file.
        """
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)
