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


This module runs the main execution of the Flatmate Bill Sharing project.
It interacts with the user, takes inputs, and generates the bill report.
"""

from flatmate_bill.bill import Bill
from flatmate_bill.flatmate import Flatmate
from flatmate_bill.pdf_report import PdfReport


if __name__ == "__main__":

    amt = float(input("Enter the total bill amount: "))
    prd = input("Enter the bill period in format -> Month Year (e.g. March 2024): ")
    tenant1 = input("Enter the name of tenant1: ")
    days1 = int(input("Enter the number of days tenant1 stayed in the house: "))
    tenant2 = input("Enter the name of tenant2: ")
    days2 = int(input("Enter the number of days tenant2 stayed in the house: "))
    the_bill = Bill(amount=amt, period=prd)
    first_tenant = Flatmate(name=tenant1, days_in_house=days1)
    second_tenant = Flatmate(name=tenant2, days_in_house=days2)

    print(
        f"{first_tenant.name} pays: {first_tenant.pays(bill=the_bill, flatmate2=second_tenant)}"
    )
    print(
        f"{second_tenant.name} pays: {second_tenant.pays(bill=the_bill,flatmate2=first_tenant)}"
    )

    pdf_report = PdfReport("Report1.pdf")
    pdf_report.generate(flatmate1=first_tenant, flatmate2=second_tenant, bill=the_bill)
