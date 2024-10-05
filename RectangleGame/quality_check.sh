#!/bin/bash

# Run pylint on the entire project
echo "Running pylint for code quality checks..."
pylint path_to_your_project/

# Check if pylint failed
if [ $? -ne 0 ]; then
    echo "pylint checks failed!"
    exit 1
fi

# Run tests with coverage on the entire project
echo "Running tests with coverage..."
coverage run -m unittest discover
if [ $? -ne 0 ]; then
    echo "Test run failed!"
    exit 1
fi

# Print coverage report
coverage report

# Optionally generate HTML coverage report
coverage html
