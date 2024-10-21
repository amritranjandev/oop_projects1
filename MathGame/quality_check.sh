#!/bin/bash

# Run pylint on the entire project, ignoring 'venv' directory
echo "Running pylint for code quality checks..."
pylint path_to_your_project/ --ignore=venv

# Check if pylint failed
if [ $? -ne 0 ]; then
    echo "pylint checks failed!"
    exit 1
else
    echo "pylint checks passed!"
fi

# Run tests with coverage on the entire project, skipping 'venv' directory
echo "Running tests with coverage..."
coverage run --omit="*/venv/*" -m unittest discover
if [ $? -ne 0 ]; then
    echo "Test run failed!"
    exit 1
fi

# Print the coverage report
coverage report -m

# Extract the total coverage percentage
COVERAGE=$(coverage report | grep TOTAL | awk '{print $4}' | tr -d '%')

# Notify user if coverage is less than 100%
if [ "$COVERAGE" -lt 100 ]; then
    echo "Coverage is less than 100%! Current coverage: $COVERAGE%"
else
    echo "Coverage is 100%! Great job!"
fi

# Optionally generate HTML coverage report
echo "Generating HTML coverage report..."
coverage html

# Get the path of the generated HTML coverage report and print it
HTML_REPORT="htmlcov/index.html"
if [ -f "$HTML_REPORT" ]; then
    echo "HTML coverage report generated at: $(pwd)/$HTML_REPORT"
else
    echo "Failed to generate HTML coverage report!"
fi
