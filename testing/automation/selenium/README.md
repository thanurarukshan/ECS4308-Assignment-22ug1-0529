# Selenium UI Automation for LearnHub

## Overview
Automated UI testing using Selenium WebDriver with Python and pytest.

## Test Coverage
- **Authentication** (5 tests): Register, Login, Logout, Profile, Invalid credentials
- **Course Management** (2 tests): View courses, Filter courses
- **Enrollment** (2 tests): Request enrollment, View enrollment status
- **Progress Tracking** (2 tests): Mark complete, Dashboard progress

**Total:** 11+ automated UI tests

## Prerequisites
```bash
Python 3.12+
pip
Chrome browser
```

## Installation
```bash
cd testing/automation/selenium

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Running Tests

### Run All Tests
```bash
pytest -v
```

### Run Specific Test File
```bash
pytest test_authentication.py -v
pytest test_course_management.py -v
pytest test_enrollment.py -v
pytest test_progress_tracking.py -v
```

### Run with HTML Report
```bash
pytest -v --html=report.html --self-contained-html
```

### Run in Headless Mode (Default)
Headless mode is configured in `conftest.py`. To run with browser visible:
```python
# Edit conftest.py and comment out:
# chrome_options.add_argument("--headless")
```

## Test Structure

### conftest.py
Contains pytest fixtures:
- `driver`: WebDriver instance with Chrome
- `base_url`: Application frontend URL (http://localhost:3001)
- `api_url`: Backend API URL (http://localhost:5000)

### Test Files
Each test file follows naming convention: `test_<module>.py`

Test methods must start with `test_` for pytest discovery.

## Adding New Tests

Example test structure:
```python
def test_example(self, driver, base_url):
    """Test description"""
    driver.get(f"{base_url}/page")
    element = driver.find_element(By.ID, "element-id")
    element.click()
    assert "expected" in driver.page_source
```

## Troubleshooting

### ChromeDriver Issues
The `webdriver-manager` package automatically downloads and manages ChromeDriver.
If issues persist:
```bash
pip install --upgrade webdriver-manager
```

### Element Not Found
Increase implicit wait in `conftest.py`:
```python
driver.implicitly_wait(15)  # Increase from 10 to 15 seconds
```

### Tests Fail in Headless Mode
Some UI elements behave differently in headless mode. Run with visible browser for debugging.

## CI/CD Integration
These tests can be integrated into CI/CD pipelines:
```yaml
# Example GitHub Actions
- name: Run Selenium Tests
  run: |
    cd testing/automation/selenium
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    pytest -v --html=report.html
```

## Best Practices
1. Use explicit waits for dynamic content
2. Use data-testid attributes for stable selectors
3. Keep tests independent (no dependencies between tests)
4. Clean up test data after execution
5. Use Page Object Model for complex applications

## Reports
HTML reports are generated in the same directory:
- `report.html` - Test execution results
- `assets/` - Screenshots (if configured)
