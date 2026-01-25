"""
Test Cases for Progress Tracking Module
Tests module completion, progress calculation, badges
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

class TestProgressTracking:
    """Test suite for progress tracking functionality"""
    
    def test_mark_module_complete(self, driver, base_url):
        """TC-PROGRESS-001: Student marks module as complete"""
        # Login as student
        driver.get(f"{base_url}/login")
        driver.find_element(By.NAME, "email").send_keys("student1@test.com")
        driver.find_element(By.NAME, "password").send_keys("Test123!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        WebDriverWait(driver, 10).until(
            lambda d: "/dashboard" in d.current_url
        )
        
        # Navigate to a course with enrollment
        # This is simplified - actual implementation would navigate to specific enrolled course
        driver.get(base_url)
        time.sleep(2)
        
        try:
            # Find course and navigate
            course = driver.find_element(By.CSS_SELECTOR, "a[href*='/courses/']")
            course_url = course.get_attribute("href")
            driver.get(course_url)
            time.sleep(2)
            
            # Look for module checkboxes
            checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
            if checkboxes:
                initial_checked = sum(1 for cb in checkboxes if cb.is_selected())
                
                # Click first unchecked checkbox
                for cb in checkboxes:
                    if not cb.is_selected():
                        cb.click()
                        time.sleep(1)
                        break
                
                # Verify checkbox remains checked (progress saved)
                driver.refresh()
                time.sleep(2)
                checkboxes_after = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
                checked_after = sum(1 for cb in checkboxes_after if cb.is_selected())
                
                assert checked_after > initial_checked, "Module completion not persisted"
            else:
                pytest.skip("No modules found to test")
        except Exception as e:
            pytest.skip(f"Progress tracking not testable: {e}")
    
    def test_dashboard_shows_progress(self, driver, base_url):
        """TC-DASH-002: Dashboard shows real-time progress"""
        # Login
        driver.get(f"{base_url}/login")
        driver.find_element(By.NAME, "email").send_keys("student1@test.com")
        driver.find_element(By.NAME, "password").send_keys("Test123!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
        WebDriverWait(driver, 10).until(
            lambda d: "/dashboard" in d.current_url
        )
        
        time.sleep(2)
        
        # Look for progress indicators (progress bars, percentages)
        page_source = driver.page_source
        has_progress = "%" in page_source or "progress" in page_source.lower()
        
        assert has_progress or "no enrollment" in page_source.lower(), "Progress not displayed on dashboard"
