# Canvas Drawing Application

```markdown
# Canvas Drawing Application

This project allows users to draw shapes (rectangles and squares) on a customizable canvas using Python. The canvas can be saved as an image (`output_image.png`) once the drawing is complete. The application leverages the `Pillow` library for image manipulation and `NumPy` for data handling.

## Features

- Create a canvas with a specific color and size.
- Draw rectangles and squares by specifying their coordinates, size, and color.
- Save the canvas as an image (`output_image.png`).

## Table of Contents

- [Installation](#installation)
- [Where to Run](#where-to-run)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)

## Installation

Before running the application, ensure you have Python 3.x installed on your system. Follow these steps to install the required dependencies.

1. Clone this repository:

   `git clone https://github.com/your-repo/canvas-drawing-app.git`

   `cd canvas-drawing-app`

2. (Optional) Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   The main dependencies are:

   - `Pillow`: for creating and saving images.
   - `NumPy`: for handling canvas data.
   - `pylint`: for code quality checks.
   - `coverage`: for test coverage.

## Where to Run

This project is intended to run on any system with Python 3.x. You can run the app in a virtual environment to isolate dependencies or run it directly after installation.

## Running the Application

To run the canvas drawing application, execute the `main.py` script:

```bash
python main.py
```

You'll be prompted to enter the width, height, and color of the canvas, followed by options to draw rectangles or squares. After you're done drawing, the canvas will be saved as `output_image.png`.

### Example Interaction

```text
Enter the width of the canvas: 500
Enter the height of the canvas: 400
Enter the color of the canvas (white, black, red, green, blue): white
Enter the shape to draw (rectangle, square) or 'exit' to finish: rectangle
Enter the x-coordinate of the rectangle: 50
Enter the y-coordinate of the rectangle: 100
Enter the height of the rectangle: 200
Enter the width of the rectangle: 150
Enter the red value of the rectangle: 255
Enter the green value of the rectangle: 0
Enter the blue value of the rectangle: 0
```

The above interaction will create a canvas with the specified dimensions and draw a red rectangle. You can continue drawing shapes until you type `exit`, at which point the canvas is saved.

## Running Tests

To ensure code quality and test coverage, you can use `pylint` and `coverage`. The tests are written using Python's `unittest` framework.

### Running Pylint

Check the code quality using `pylint`:

```bash
pylint canvas_app/
```

### Running Tests with Coverage

To run the unit tests and generate a coverage report:

```bash
coverage run -m unittest discover
coverage report -m
```

This will display a detailed report on test coverage. You can also generate an HTML report:

```bash
coverage html
```

The HTML report can be viewed by opening `htmlcov/index.html` in your browser.

### Example Coverage Report

```bash
Name                            Stmts   Miss  Cover   Missing
-------------------------------------------------------------
canvas_app/__init__.py               0      0   100%
canvas_app/canvas.py                10      0   100%
canvas_app/shapes.py                20      1    95%   23
-------------------------------------------------------------
TOTAL                               30      1    97%
```

## Project Structure

The project is organized as follows:

```bash
canvas-drawing-app/
│
├── canvas_app/
│   ├── __init__.py         # Initializes the module
│   ├── canvas.py           # Defines the Canvas class
│   ├── shapes.py           # Defines the Rectangle and Square classes
│
├── tests/
│   ├── __init__.py         # Initializes the test module
│   ├── test_canvas.py      # Unit tests for Canvas class
│   ├── test_shapes.py      # Unit tests for Rectangle and Square classes
│
├── main.py                 # Main script to run the application
├── requirements.txt        # Project dependencies
├── .pylintrc               # Pylint configuration file
├── .gitignore              # Files to ignore in the repository
└── README.md               # This README file
```

## How to Contribute

If you'd like to contribute, please fork the repository and create a new branch for your changes. You can submit a pull request once you've made your changes.

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```

In this version:
- The **"Clone this repository"** point has been moved outside the code block.
- A **"Where to Run"** heading has been added to guide the user about environment requirements.
```
