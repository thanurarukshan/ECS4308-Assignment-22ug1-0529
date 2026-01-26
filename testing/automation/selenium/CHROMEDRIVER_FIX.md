# Quick Fix for ChromeDriver Exec Format Error

## Problem
ChromeDriver download is corrupted or pointing to wrong file (THIRD_PARTY_NOTICES instead of actual executable).

## Solution

Run these commands in your terminal:

```bash
cd /home/thanura/softwareTestingAndQA/testing/automation/selenium

# 1. Clear the corrupted cache
rm -rf ~/.wdm/drivers/chromedriver

# 2. Activate virtual environment
source venv/bin/activate

# 3. Upgrade dependencies
pip install --upgrade pip webdriver-manager selenium

# 4. Test ChromeDriver installation
python3 << 'EOF'
from webdriver_manager.chrome import ChromeDriverManager
path = ChromeDriverManager().install()
print(f"ChromeDriver installed at: {path}")
EOF

# 5. Run tests
pytest -v --html=report.html --self-contained-html
```

## Alternative: Use system ChromeDriver

If the above doesn't work, install ChromeDriver system-wide:

```bash
# Install ChromeDriver for your system
sudo dnf install chromium-chromedriver  # For Fedora/RHEL
# OR
sudo apt install chromium-chromedriver  # For Ubuntu/Debian

# Then update conftest.py to use system driver:
# Comment out: service = Service(ChromeDriverManager().install())
# Add: service = Service('/usr/bin/chromedriver')
```

## Test Execution After Fix

```bash
cd /home/thanura/softwareTestingAndQA/testing/automation/selenium
source venv/bin/activate
pytest -v --html=report.html --self-contained-html
```

Expected output: 11 tests should run (some may pass, some may fail due to timing/UI issues).
