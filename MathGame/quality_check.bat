@echo off
setlocal

echo Running pylint for code quality checks...

:: Change to the project directory
cd /d "C:\work p1\sap_hana\problems\pr\oop\MathGame"

:: Run pylint and skip the 'venv' directory
pylint --ignore=venv .

if errorlevel 1 (
    echo pylint checks failed!
    exit /b 1
) else (
    echo pylint checks passed!
)

:: Run coverage tests and skip 'venv' directory
echo Running coverage for tests...
coverage run --omit="*/venv/*" -m unittest discover
coverage report -m

:: Check the total coverage percentage
for /f "tokens=4 delims= " %%i in ('coverage report ^| findstr -i "TOTAL"') do set COVERAGE=%%i

:: Inform the user about the coverage percentage
echo Total coverage: %COVERAGE%

if not "%COVERAGE%"=="100%" (
    echo Coverage is less than 100%%! Please improve the tests.
) else (
    echo Coverage is 100%%! Great job!
)

:: Generate the HTML coverage report
echo Generating HTML coverage report...
coverage html

:: Get the path of the generated HTML coverage report and print it
set HTML_REPORT=htmlcov/index.html
if exist %HTML_REPORT% (
    echo HTML coverage report generated at: %CD%\%HTML_REPORT%
) else (
    echo Failed to generate HTML coverage report!
)

endlocal
