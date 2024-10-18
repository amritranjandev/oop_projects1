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

This module defines the PdfReport class, which generates a PDF file
containing the details of the bill and how much each flatmate owes.
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class PdfReport:
    """Generates a PDF report of the flatmates' bill sharing."""

    def __init__(self, filename: str):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill, logo_path: str = "assets/bill.png"):
        """Generates a PDF showing each flatmate's contribution to the bill."""
        flatmate1_pay = round(flatmate1.pays(bill, flatmate2), 2)
        flatmate2_pay = round(flatmate2.pays(bill, flatmate1), 2)
        c = canvas.Canvas(self.filename, pagesize=letter)
        width, height = letter

        # Add logo image
        logo_width, logo_height = 25, 25
        c.drawImage(
            logo_path,
            20,
            height - logo_height - 20,
            width=logo_width,
            height=logo_height,
        )

        # Add header
        header_text = "Flatmate Bill"
        c.setFont("Helvetica-Bold", 16)
        text_width = c.stringWidth(header_text, "Helvetica-Bold", 16)
        c.drawString((width - text_width) / 2, height - 50, header_text)

        # Add bill period
        c.setFont("Helvetica", 12)
        c.drawString(100, height - 80, f"Bill Period: {bill.period}")

        # Add names and amounts
        c.setFont("Helvetica", 12)
        c.drawString(100, height - 120, f"{flatmate1.name}: ${flatmate1_pay}")
        c.drawString(100, height - 140, f"{flatmate2.name}: ${flatmate2_pay}")

        # Save the PDF
        c.save()
