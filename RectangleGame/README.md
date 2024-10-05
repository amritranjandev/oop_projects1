# Rectangle Game

## Overview

The Rectangle Game is a Python-based interactive application that allows users to determine if a point falls inside a randomly generated rectangle and estimate the rectangle's area. It utilizes object-oriented programming principles, making it a great example of OOP concepts in Python.

## Features

- Generates a random rectangle defined by two points.
- Prompts the user to input a point's coordinates.
- Allows the user to guess the area of the rectangle.
- Determines if the guessed point is inside the rectangle.
- Provides feedback on the area guess.

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/RectangleGame.git
   cd RectangleGame
   ```
2. (Optional) Create a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install required packages (if any):

   ```
   pip install -r requirements.txt
   ```

## Usage

Run the game using the following command:

```
python rectangle_game.py
```

## Example

When you run the program, it will generate a rectangle and ask for your input:

```
Rectangle Coordinates:  3 , 4 and 12 , 15
Guess x: 5
Guess y: 10
Guess rectangle area: 45
Your point was inside rectangle:  True
Your area was off by:  15
```

## Testing

The project includes unit tests to verify functionality. To run the tests, execute the following command:

```
python -m unittest tests.py
```

## Coverage

To check the code coverage of the tests, run:

```
coverage run -m unittest tests.py
coverage report
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find a bug or have a feature request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
