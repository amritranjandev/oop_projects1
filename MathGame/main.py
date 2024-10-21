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

main.py: Main script to draw shapes on a canvas.
"""

from canvas_app.canvas import Canvas
from canvas_app.shapes import Rectangle, Square

if __name__ == "__main__":
    canvas_width = int(input("Enter the width of the canvas: "))
    canvas_height = int(input("Enter the height of the canvas: "))

    colors = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
    }
    canvas_color = input(
        "Enter the color of the canvas (white, black, red, green, blue): "
    )

    canvas = Canvas(canvas_height, canvas_width, colors[canvas_color])

    while True:
        shape = input(
            "Enter the shape to draw (rectangle, square) or 'exit' to finish: "
        )

        if shape == "exit":
            break

        if shape.lower() == "rectangle":
            x = int(input("Enter the x-coordinate of the rectangle: "))
            y = int(input("Enter the y-coordinate of the rectangle: "))
            height = int(input("Enter the height of the rectangle: "))
            width = int(input("Enter the width of the rectangle: "))
            red = int(input("Enter the red value of the rectangle: "))
            green = int(input("Enter the green value of the rectangle: "))
            blue = int(input("Enter the blue value of the rectangle: "))
            rectangle = Rectangle(x, y, height, width, (red, green, blue))
            rectangle.draw(canvas)

        elif shape.lower() == "square":
            x = int(input("Enter the x-coordinate of the square: "))
            y = int(input("Enter the y-coordinate of the square: "))
            side = int(input("Enter the side length of the square: "))
            red = int(input("Enter the red value of the square: "))
            green = int(input("Enter the green value of the square: "))
            blue = int(input("Enter the blue value of the square: "))
            square = Square(x, y, side, (red, green, blue))
            square.draw(canvas)

    # Save the canvas as an image
    canvas.make("output_image.png")
