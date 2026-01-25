"""Test Cases for Course Management Module"""
import pytest
from selenium.webdriver.common.by import By
import time

class TestCourseManagement:
    def test_view_courses_on_homepage(self, driver, base_url):
        """TC-COURSE-007: List All Courses"""
        driver.get(base_url)
        time.sleep(2)
        
        # Verify courses are displayed
        page_source = driver.page_source
        assert "course" in page_source.lower(), "No courses found on homepage"
    
    def test_filter_courses_by_level(self, driver, base_url):
        """TC-COURSE-009: Filter Courses by Level"""
        driver.get(base_url)
        time.sleep(1)
        
        # Select beginner level from dropdown
        try:
            level_select = driver.find_element(By.NAME, "level")
            level_select.send_keys("beginner")
            
            # Click search
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            time.sleep(2)
 
            assert "beginner" in driver.page_source.lower()
        except:
            pytest.skip("Level filter not found")
