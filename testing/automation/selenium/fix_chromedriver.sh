#!/bin/bash
echo "=== Fixing ChromeDriver Setup ==="

# Remove corrupted ChromeDriver cache
echo "1. Clearing ChromeDriver cache..."
rm -rf ~/.wdm/drivers/chromedriver
rm -rf ~/.cache/selenium

# Activate virtual environment
echo "2. Setting up virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate

# Reinstall dependencies
echo "3. Installing/upgrading dependencies..."
pip install --upgrade pip
pip install --upgrade selenium webdriver-manager pytest pytest-html

# Test ChromeDriver installation
echo "4. Testing ChromeDriver installation..."
python3 << 'PYEOF'
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

print("Downloading/installing ChromeDriver...")
driver_path = ChromeDriverManager().install()
print(f"ChromeDriver installed at: {driver_path}")

# Verify it's executable
import os
if os.path.isfile(driver_path) and os.access(driver_path, os.X_OK):
    print("✓ ChromeDriver is executable")
else:
    print("✗ ChromeDriver is NOT executable")
PYEOF

echo ""
echo "=== Fix Complete ==="
echo "Try running: pytest -v"
