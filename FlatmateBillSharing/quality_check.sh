#!/bin/bash
set -e  # Exit the script immediately if any command fails

# Run pylint on the entire project
echo "Running pylint for code quality checks..."
pylint --ignore=venv path_to_your_project/

# Check if pylint failed
if [ $? -ne 0 ]; then
    echo "pylint checks failed!"
    exit 1
else
    echo "pylint checks passed!"
fi

# Run tests with coverage on the entire project
echo "Running tests with coverage..."
coverage run -m unittest discover

# Check if tests failed
if [ $? -ne 0 ]; then
    echo "Test run failed!"
    exit 1
fi

# Print coverage report
coverage report

# Optionally generate HTML coverage report
coverage html

# Inform user
echo "Code quality checks and tests completed successfully!"
