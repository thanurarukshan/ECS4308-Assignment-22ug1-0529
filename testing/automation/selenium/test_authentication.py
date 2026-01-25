"""
Selenium Test Cases for LearnHub Authentication Module
Test Cases: TC-AUTH-001 through TC-AUTH-015
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestAuthentication:
    """Test suite for authentication functionality"""
    
    def test_user_registration_valid_data(self, driver, base_url):
        """TC-AUTH-001: User Registration with Valid Data"""
        driver.get(f"{base_url}/register")
        
        # Generate unique email for testing
        timestamp = int(time.time())
        email = f"testuser{timestamp}@test.com"
        
        # Fill registration form
        driver.find_element(By.NAME, "username").send_keys(f"testuser{timestamp}")
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys("Test123!")
        
        # Select role (if dropdown exists)
        try:
            role_select = driver.find_element(By.NAME, "role")
            role_select.send_keys("student")
        except:
            pass
        
        # Submit form
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Wait for redirect or success message
        time.sleep(2)
        
        # Verify registration succeeded (redirected to login or dashboard)
        current_url = driver.current_url
        assert "/login" in current_url or "/dashboard" in current_url, "Registration failed"
    
    def test_user_login_valid_credentials(self, driver, base_url):
        """TC-AUTH-004: User Login with Valid Credentials"""
        driver.get(f"{base_url}/login")
        
        # Use existing test credentials
        driver.find_element(By.NAME, "email").send_keys("student1@test.com")
        driver.find_element(By.NAME, "password").send_keys("Test123!")
        
        # Submit login
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        # Wait for dashboard
        WebDriverWait(driver, 10).until(
            lambda d: "/dashboard" in d.current_url
        )
        
        # Verify successful login
        assert "/dashboard" in driver.current_url, "Login failed"
    
    def test_user_login_invalid_credentials(self, driver, base_url):
        """TC-AUTH-005: User Login with Invalid Credentials"""
        driver.get(f"{base_url}/login")
        
        driver.find_element(By.NAME, "email").send_keys("student1@test.com")
        driver.find_element(By.NAME, "password").send_keys("WrongPassword123!")
        
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        time.sleep(2)
        
        # Should remain on login page
        assert "/login" in driver.current_url, "Should stay on login page after failed login"
        
        # Check for error message
        page_source = driver.page_source.lower()
        assert "invalid" in page_source or "error" in page_source, "Error message not displayed"
    
    def test_view_profile(self, driver, base_url):
        """TC-AUTH-007: View User Profile"""
        # First login
        driver.get(f"{base_url}/login")
        driver.find_element(By.NAME, "email").send_keys("student1@test.com")
        driver.find_element(By.NAME, "password").send_keys("Test123!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        WebDriverWait(driver, 10).until(
            lambda d: "/dashboard" in d.current_url
        )
        
        # Navigate to profile
        driver.get(f"{base_url}/profile")
        
        time.sleep(2)
        
        # Verify profile page loaded
        assert "/profile" in driver.current_url, "Profile page didn't load"
        
        # Check that email field exists and is disabled
        email_field = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        assert email_field.get_attribute("disabled") == "true", "Email field should be disabled"
    
    def test_logout_functionality(self, driver, base_url):
        """TC-AUTH-012: Logout Functionality"""
        # Login first
        driver.get(f"{base_url}/login")
        driver.find_element(By.NAME, "email").send_keys("student1@test.com")
        driver.find_element(By.NAME, "password").send_keys("Test123!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        WebDriverWait(driver, 10).until(
            lambda d: "/dashboard" in d.current_url
        )
        
        # Find and click logout button
        try:
            logout_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Logout')]")
            logout_button.click()
        except:
            # Try finding by link text
            logout_link = driver.find_element(By.LINK_TEXT, "Logout")
            logout_link.click()
        
        time.sleep(2)
        
        # Verify redirected to public page
        current_url = driver.current_url
        assert "/" == current_url or "/login" in current_url, "Logout didn't redirect properly"
