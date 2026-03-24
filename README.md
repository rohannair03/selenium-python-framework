
# Selenium Python Automation Framework
![Selenium Tests](https://github.com/rohannair03/selenium-python-framework/actions/workflows/tests.yml/badge.svg)

## Overview

This repository contains a scalable UI automation framework built using **Python**, **Selenium WebDriver**, and **PyTest**.  
The framework validates core user workflows on *letskodeit.com* and is designed to reflect real-world automation engineering practices.

The focus of this project is not full site coverage, but the implementation of a maintainable, extensible automation architecture capable of scaling across additional workflows, browsers, and environments.

Key engineering objectives:

- Implement a clean Page Object Model (POM) architecture
- Centralize WebDriver lifecycle management
- Enable CLI-driven runtime configuration
- Integrate structured logging and failure diagnostics
- Support cross-browser and headless execution
- Maintain clear separation between test logic and page behavior


---

## Architecture

```text
selenium-python-framework/
│
├── base/              # Base abstractions (BasePage, WebDriverFactory)
├── pages/             # Page Object classes
├── tests/             # Test classes and workflow validation
├── utilities/         # Logging, data readers, test status helpers
├── configfiles/       # Environment configuration
├── screenshots/       # Auto-captured failure evidence
├── conftest.py        # PyTest fixtures and CLI configuration
```

### Page Object Model (POM)

Each application page is encapsulated within its own class containing:

- Locators
- Page-specific interaction methods
- Reusable workflow abstractions

This enforces separation of concerns, reduces duplication, and improves long-term maintainability.

### WebDriverFactory

The `WebDriverFactory` class abstracts browser initialization and configuration.  
Responsibilities include:

- Browser selection via CLI
- Headless mode configuration
- Driver instantiation and option management

This approach isolates environment concerns from test logic and supports future expansion (e.g., remote execution or Selenium Grid).

### BasePage

Common Selenium interactions (clicking, typing, waiting, scrolling, frame switching) are abstracted into `BasePage`.  
This ensures consistent behavior across page objects and centralizes interaction logic for easier maintenance.


---

## Implemented Capabilities

- Page Object Model architecture
- Explicit waits using `WebDriverWait`
- CLI-configurable browser execution
- Headless mode support
- Screenshot capture on test failure
- Structured logging integration
- Cross-browser support (Chrome, Firefox)
- Data-driven test capability
- Allure reporting with step-level annotations
- Automatic screenshot attachment to Allure report on failure


---

## Automated Workflows

The framework currently validates representative, high-value user flows:

- Valid authentication
- Course search and selection
- Enrollment workflow
- Payment validation (negative scenario)
- Error state verification

These workflows demonstrate end-to-end UI validation, dynamic element handling, frame interaction, and assertion strategy.

The framework is intentionally structured to allow straightforward expansion of coverage.


---

## Installation

Clone the repository:

```bash
git clone https://github.com/rohannair03/selenium-python-framework.git
cd selenium-python-framework
```

---

## Test Execution

Run with default configuration:

```bash
pytest
```

Specify browser:

```bash
pytest --browser=chrome
pytest --browser=firefox
```

Run in headless mode:

```bash
pytest --browser=chrome --headless
```


---

## Failure Diagnostics

On test failure, a screenshot is automatically captured and stored in:
```text
screenshots/
```

Screenshots are also attached directly to the Allure report against the failed test, providing immediate visual context without needing to locate files manually.

To generate and open the Allure report locally:
```bash
pytest --browser=chrome --headless --alluredir=allure-results
allure generate allure-results -o allure-report --clean
allure open allure-report
```

In CI, the Allure report is generated automatically after every run — including failed runs — and uploaded as a downloadable artifact in the GitHub Actions summary.


---

## Locator Strategy

The framework follows a prioritized locator strategy:

1. ID (preferred where available)
2. Name
3. CSS selectors
4. XPath (reserved for dynamic or complex DOM structures)

While some dynamic elements require XPath, the framework is structured to support locator refactoring without impacting test design.


---

## Design Principles

This framework emphasizes:

- Clear separation between environment setup and test logic
- Reusability through abstraction
- Configurability through CLI parameters
- Maintainability through structured architecture
- CI readiness via headless execution and automated failure capture

The implementation reflects production-oriented automation practices rather than tutorial-based scripting.


---

## Potential Enhancements

- ~~CI integration (GitHub Actions)~~
- Parallel execution with pytest-xdist
- ~~Structured reporting (Allure / HTML reports)~~
- Remote execution (Selenium Grid)
- Expanded negative and edge-case coverage


---

## Author

Rohan Nair  
GitHub: https://github.com/rohannair03
