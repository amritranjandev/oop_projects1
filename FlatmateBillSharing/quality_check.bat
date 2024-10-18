@echo off
setlocal

echo Running pylint for code quality checks...

:: Change to the project directory
cd /d "C:\work p1\sap_hana\problems\pr\oop\FlatmatesBillSharing"

:: Run pylint on the current directory, ignoring the venv folder
pylint --ignore=venv .

if errorlevel 1 (
    echo pylint checks failed!
    exit /b 1
) else (
    echo pylint checks passed!
)

:: Run coverage tests
echo Running coverage for tests...

:: Create .coveragerc to exclude venv from coverage
echo [run] > .coveragerc
echo omit = */venv/* >> .coveragerc

coverage run -m unittest discover
coverage report -m

endlocal

:: Print coverage report
coverage report

:: Optionally generate HTML coverage report
coverage html
