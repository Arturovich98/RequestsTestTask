# API Automation Tests (FavQs)
This repository contains API automation tests for the FavQs API using Python.

## Tech Stack
- Python
- pytest
- requests

### Positive Test Cases
1. *Create a user and verify creation*
2. *Update an existing user*

### Negative Test Cases
*Invalid user creation scenarios (parameterized tests)*

## Parameterization
Negative test scenarios are implemented using *pytest parametrization* to efficiently validate multiple invalid input combinations with minimal code duplication.

## Fixtures & Helpers
To improve code reusability and reduce duplication:
- *Fixtures (conftest.py)* were implemented to manage test data and user creation logic
- *Helper methods (api_helpers.py)* were introduced to centralize API request logic (create user, update user, get user)

This approach improves:
- maintainability
- readability
- scalability of the test framework

## Authentication
API authentication is performed using a token-based mechanism.
- The API token is stored in a `.env` file for simplicity in this project
- Requests include the token for authorization

###  Best Practice Note
A more secure and production-ready approach would be to store sensitive credentials in **GitHub Secrets**, but for the purpose of this task, the `.env` approach was implemented as required.

## CI Integration (GitHub Actions)
A CI pipeline is configured using GitHub Actions.
It provides:
- automatic test execution on push / pull request
- remote test execution in CI environment
- consistent test validation process

## Allure Reporting
The project uses *Allure Framework* for test reporting.
Features include:
- detailed test execution reports
- step-by-step test visualization
- request/response attachments
- structured test results (features, stories, severity, etc.)

## Allure Report Deployment
Allure reports are automatically deployed to [*GitHub Pages*](https://Arturovich98.github.io/RequestsTestTask/).
This allows:
- viewing test results as a static website
- easy sharing of test execution results
- always-updated latest report after each CI run

## Test Report
Click the badge above to open the latest Allure report.
[![Allure Report](https://img.shields.io/badge/Allure-Report-green)](https://Arturovich98.github.io/RequestsTestTask/)

## Bugs Found
During test implementation, several issues were identified in the API behavior.
These are documented directly in the test code as inline comments next to the affected test cases.

## All dependencies are listed in:
requirements.txt

## How to Run Tests locally
`bash`
pip install -r requirements.txt
pytest

