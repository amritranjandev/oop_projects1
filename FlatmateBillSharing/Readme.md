# Flatmates Bill Sharing Application

The **Flatmates Bill Sharing** application calculates how much each flatmate needs to pay based on the number of days they stayed in the house during a billing period. The app generates a PDF report containing the billing details and includes a simple test suite with linting and coverage checks.

## Project Structure

```
flatmates-bill-sharing/
│
├── flatmate_bill/
│   ├── __init__.py
│   ├── bill.py                 # Bill class for representing the bill amount and period
│   ├── flatmate.py             # Flatmate class to calculate each tenant's contribution
│   └── pdf_report.py           # PdfReport class to generate a PDF report
│
├── tests/
│   ├── __init__.py
│   └── test_flatmate_bill.py    # Unit tests for the project
│
├── venv/                        # Virtual environment (excluded from linting)
├── .pylintrc                    # Pylint configuration file
├── .gitignore                   # Files and directories to be ignored by Git
├── quality_check.sh             # Script to run pylint, tests, and coverage on Unix-like systems
├── quality_check.bat            # Script to run pylint, tests, and coverage on Windows
├── requirements.txt             # Project dependencies
├── main.py                      # The entry point to run the app
└── README.md                    # Project documentation
```

---

## Features

- Calculates the share of the bill for each flatmate based on the number of days they stayed.
- Generates a PDF report with the details of the bill, the names of the flatmates, and their individual amounts.
- Includes a small logo at the top-left corner of the PDF.
- Can run unit tests with coverage, as well as linting for code quality checks.

---

## Logic Breakdown

### Classes

1. **Bill**

   - Represents the bill with attributes:
     - `amount`: The total bill amount.
     - `period`: The billing period (e.g., "March 2024").
2. **Flatmate**

   - Represents a flatmate and calculates their share of the bill.
   - Attributes:
     - `name`: The flatmate's name.
     - `days_in_house`: The number of days the flatmate stayed during the billing period.
   - **Method**:
     - `pays(bill, flatmate2)`: Calculates the portion of the bill based on how long they stayed compared to the other flatmate.
3. **PdfReport**

   - Generates a PDF with the bill details and payments.
   - **Method**:
     - `generate(flatmate1, flatmate2, bill, logo_path)`: Generates the PDF file, centered title, and bill breakdown for each flatmate.

---

## How to Run the Application

### Step 1: Set Up the Environment

1. Clone the repository and navigate to the project directory.
2. Create a virtual environment and activate it:

   - **Unix/MacOS**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Run the Application

1. Open a terminal or command prompt in the project directory.
2. Run the `main.py` file:

   ```bash
   python main.py
   ```
3. The app will prompt you for input:

   - Total bill amount.
   - Bill period.
   - Names and days in the house for two flatmates.
4. After entering the information, the application will calculate the payment shares for each flatmate and generate a PDF report named `Report1.pdf` in the project directory.

---

## Running Tests

### Step 1: Running Unit Tests

To run the unit tests and ensure everything works as expected:

```bash
python -m unittest discover
```

This will run all the tests located in the `tests/` directory.

### Step 2: Checking Test Coverage

To run the tests with coverage and generate a coverage report:

```bash
coverage run -m unittest discover
coverage report -m
```

You can also generate an HTML report using:

```bash
coverage html
```

The HTML report will be created in the `htmlcov/` directory.

---

## Linting the Code

The project uses `pylint` for code linting.

### Step 1: Running `pylint`

You can run the lint checks using one of the provided scripts.

- **On Unix/Linux systems**:

  ```bash
  ./quality_check.sh
  ```
- **On Windows**:

  ```bash
  .\quality_check.bat
  ```

This will run `pylint` on the project while excluding the `venv` directory.

### Step 2: Ignoring the Virtual Environment in `pylint`

In case you manually run `pylint` and want to avoid scanning the `venv` folder:

```bash
pylint --ignore=venv .
```

This will skip linting for files inside the `venv` directory.

---

## How to Run Quality Checks and Coverage

You can run the complete quality checks including linting, unit tests, and coverage using the scripts:

- **On Unix/Linux systems**:

  ```bash
  ./quality_check.sh
  ```
- **On Windows**:

  ```bash
  .\quality_check.bat
  ```

These scripts will run `pylint`, unit tests, and generate coverage reports in one go. If any of these checks fail, the script will exit and notify you of the failure.

---

## How the Application Works

1. **Bill Calculation**:

   - The app takes the total bill and divides it based on how long each flatmate stayed.
   - It uses the `Flatmate.pays()` method to calculate each flatmate's contribution relative to the other.
2. **PDF Generation**:

   - The `PdfReport.generate()` method creates a PDF report, adds a header, and lists each flatmate's payment share.
   - A logo is included at the top-left of the PDF.

---

## Example Output

```
Enter the total bill amount: 1200
Enter the bill period in format -> Month Year (e.g. March 2024): March 2024
Enter the name of tenant1: Tony
Enter the number of days tenant1 stayed in the house: 20
Enter the name of tenant2: Bob
Enter the number of days tenant2 stayed in the house: 10

Tony pays: 800.0
Bob pays: 400.0
```

The application will generate a PDF (`Report1.pdf`) with the following details:

```
Flatmate Bill
Bill Period: March 2024

Tony: $800.0
Bob: $400.0
```

The report will also include a small logo in the top-left corner.

---

## License

This project is licensed under the MIT License.
