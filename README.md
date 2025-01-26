API Automation Framework

Project Overview

This repository contains the automation framework for the API version of the Money Transfer application. The framework is built using Rest Assured and Java, designed for testing API endpoints efficiently.

Features

Comprehensive API Testing: Covers both functional and negative test scenarios.

Data-Driven Testing: Uses externalized test data with JSON files.

Integration Testing: Validates interdependencies between API endpoints.

Reporting: Integrated with Allure Reports for detailed analysis.

Reusable Utilities: Includes token management and request-response validation utilities.

Prerequisites

Java JDK 11 or later

Maven (Build Tool)

Git: Installed and configured.

Setup Instructions

Clone this repository:

git clone <repository-url>

Navigate to the project directory:

cd api-automation-framework

Install dependencies:

mvn install

Update the config.properties file in the src/test/resources directory with the following details:

Base URL

Token generation endpoint

Authorization credentials

Running Tests

To run all tests:

mvn test

To execute tests for a specific tag:

mvn test -Dcucumber.filter.tags="@regression"


Folder Structure

src/main/java: Core framework code and utilities.

src/test/java: Test cases and data.

src/test/resources: Configuration files and test data.


Troubleshooting

Dependency Issues:

Run mvn clean install to resolve missing dependencies.

Configuration Errors:

Ensure the config.properties file is correctly updated.

Token Generation Issues:

Verify the token endpoint and credentials in the configuration file.


License

This project is licensed under the MIT License.
