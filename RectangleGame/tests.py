"""run this file to test all modules"""

import unittest
from unittest.mock import MagicMock
from rectangle_game import (
    Point,
    Rectangle,
    GuiRecctangle,
    GuiPoint
)  # Adjust the import based on your file structure


class TestRectangleGame(unittest.TestCase):
    """test class for checking all scenarios"""

    def setUp(self):
        """Set up test cases with some default rectangles and points."""
        self.rect1 = Rectangle(
            Point(0, 0), Point(10, 10)
        )  # Bottom-left (0,0) to top-right (10,10)
        self.rect2 = Rectangle(
            Point(5, 5), Point(15, 15)
        )  # Bottom-left (5,5) to top-right (15,15)
        self.rect3 = Rectangle(Point(0, 0), Point(5, 10))  # Area = 5 * 10 = 50
        self.point_inside = Point(6, 6)  # This point is inside rect2
        self.point_on_edge = Point(
            5, 5
        )  # This point is on the edge of rect2 (should be considered outside)
        self.point_on_corner = Point(10, 10)  # This point is on the corner of rect1
        self.point_outside = Point(16, 16)  # This point is outside rect2

    def test_point_falls_in_rectangle(self):
        """Test points that are inside the rectangle."""
        self.assertTrue(
            self.point_inside.falls_in_rectangle(self.rect2),
            "Point should be inside the rectangle.",
        )

    def test_point_on_edge(self):
        """Test points that are on the edge of the rectangle."""
        self.assertFalse(
            self.point_on_edge.falls_in_rectangle(self.rect2),
            "Point on edge should be outside the rectangle.",
        )

    def test_point_on_corner(self):
        """Test points that are on the corners of the rectangle."""
        self.assertFalse(
            self.point_on_corner.falls_in_rectangle(self.rect1),
            "Point on corner should be outside the rectangle.",
        )

    def test_point_falls_outside_rectangle(self):
        """Test points that are outside the rectangle."""
        self.assertFalse(
            self.point_outside.falls_in_rectangle(self.rect2),
            "Point should be outside the rectangle.",
        )

    def test_rectangle_area(self):
        """Test the area calculation of the rectangle."""
        self.assertEqual(self.rect1.area(), 100, "Area of rect1 should be 100.")
        self.assertEqual(self.rect2.area(), 100, "Area of rect2 should be 100.")
        self.assertEqual(self.rect3.area(), 50, "Area of rect3 should be 50.")

    def test_gui_rectangle_draw(self):
        """Test the drawing of the GuiRecctangle."""
        canvas_mock = MagicMock()
        gui_rect = GuiRecctangle(Point(0, 0), Point(10, 10))
        gui_rect.draw(canvas_mock)
        self.assertTrue(canvas_mock.goto.called)
        self.assertTrue(canvas_mock.pendown.called)

    def test_gui_point_draw(self):
        """Test the drawing of the GuiPoint."""
        canvas_mock = MagicMock()
        gui_point = GuiPoint(5, 5)
        gui_point.draw(canvas_mock)
        self.assertTrue(canvas_mock.goto.called)
        self.assertTrue(canvas_mock.dot.called)

if __name__ == "__main__":
    unittest.main()  # pragma: no cover
