# Manual Test Execution Log
**LearnHub LMS - Manual Testing Results**

**Tester:** T.R.S. Wickramarathna  
**Student ID:** 22ug1-0529  
**Test Period:** January 15 - January 23, 2026  
**Test Environment:** Local Docker (http://localhost:3001)  
**Browser:** Chrome 120.0.6099.109

---

## Test Execution Summary

| Module | Total Cases | Passed | Failed | Blocked | Pass Rate |
|--------|-------------|--------|--------|---------|-----------|
| Authentication | 15 | 14 | 1 | 0 | 93% |
| Course Management | 12 | 11 | 1 | 0 | 92% |
| Module Management | 8 | 8 | 0 | 0 | 100% |
| Enrollment | 10 | 9 | 0 | 1 | 90% |
| Progress Tracking | 8 | 8 | 0 | 0 | 100% |
| Dashboard | 6 | 6 | 0 | 0 | 100% |
| Notifications | 4 | 3 | 1 | 0 | 75% |
| **TOTAL** | **63** | **59** | **3** | **1** | **94%** |

---

## Detailed Test Execution Results

### 1. Authentication Module (January 15-16, 2026)

| TC ID | Test Case | Date | Status | Notes |
|-------|-----------|------|--------|-------|
| TC-AUTH-001 | User Registration - Valid Data | Jan 15, 10:30 | PASS | User created successfully, redirected to dashboard |
| TC-AUTH-002 | User Registration - Duplicate Email | Jan 15, 10:35 | PASS | Error displayed: "Email already exists" |
| TC-AUTH-003 | User Registration - Invalid Email | Jan 15, 10:40 | PASS | Form validation prevented submission |
| TC-AUTH-004 | User Login - Valid Credentials | Jan 15, 11:00 | PASS | Logged in successfully, JWT token stored |
| TC-AUTH-005 | User Login - Invalid Credentials | Jan 15, 11:05 | PASS | Error message shown, login denied |
| TC-AUTH-006 | Session Persistence | Jan 15, 14:20 | PASS | Session maintained after browser restart |
| TC-AUTH-007 | View User Profile | Jan 15, 14:30 | PASS | Profile data displayed correctly, email field disabled |
| TC-AUTH-008 | Update Profile - Change Username | Jan 15, 14:45 | PASS | Username updated, reflected across app |
| TC-AUTH-009 | Change Password - Valid | Jan 15, 15:00 | PASS | Password changed, can login with new password |
| TC-AUTH-010 | Delete Account | Jan 15, 15:20 | PASS | Account deleted after password confirmation |
| TC-AUTH-011 | Password Strength Validation | Jan 15, 15:30 | PASS | Weak passwords rejected with proper message |
| TC-AUTH-012 | Logout Functionality | Jan 16, 09:00 | PASS | Logged out, token cleared, redirected to home |
| TC-AUTH-013 | Session Persistence | Jan 16, 09:15 | PASS | Session persists across browser sessions |
| TC-AUTH-014 | Concurrent Login Sessions | Jan 16, 09:30 | PASS | Multiple sessions work independently |
| TC-AUTH-015 | Password Mismatch on Change | Jan 16, 09:45 | FAIL | Validation error message unclear - see DEF-011 |

**Module Notes:**
- Most authentication features work well
- Password change validation needs improvement (error message could be clearer)
- No issues with session management or JWT handling

---

### 2. Course Management Module (January 16-17, 2026)

| TC ID | Test Case | Date | Status | Notes |
|-------|-----------|------|--------|-------|
| TC-COURSE-001 | Create Course - Valid Data | Jan 16, 10:30 | PASS | Course created successfully with all fields |
| TC-COURSE-002 | Create Course - Missing Required | Jan 16, 10:45 | PASS | Validation error for missing title |
| TC-COURSE-003 | Edit Course - Update Details | Jan 16, 11:00 | PASS | Course updated, changes reflected immediately |
| TC-COURSE-004 | Edit Course - Unauthorized Access | Jan 16, 11:20 | PASS | Access denied when trying to edit another user's course |
| TC-COURSE-005 | Delete Course | Jan 16, 11:35 | PASS | Course deleted, modules also removed |
| TC-COURSE-006 | View Course Details - Public | Jan 16, 14:00 | PASS | Course details visible without login |
| TC-COURSE-007 | List All Courses - Homepage | Jan 16, 14:15 | PASS | All courses displayed as cards, responsive layout |
| TC-COURSE-008 | Filter Courses by Category | Jan 16, 14:30 | PASS | Filtering works correctly |
| TC-COURSE-009 | Filter Courses by Level | Jan 16, 14:45 | PASS | Level filter applied correctly |
| TC-COURSE-010 | Filter Courses by Type | Jan 16, 15:00 | PASS | Type filter working properly |
| TC-COURSE-011 | Search Courses by Keyword | Jan 16, 15:15 | PASS | Search returns relevant results |
| TC-COURSE-012 | Course Capacity Validation | Jan 17, 09:00 | FAIL | Negative capacity accepted - see DEF-002 |

**Module Notes:**
- Course CRUD operations working perfectly
- Search and filter functionality solid
- Capacity validation needs improvement (should reject negative values)
- Course deletion properly cascades to modules

---

### 3. Module Management (January 17, 2026)

| TC ID | Test Case | Date | Status | Notes |
|-------|-----------|------|--------|-------|
| TC-MODULE-001 | Add Module to Course | Jan 17, 10:00 | PASS | Module created and linked correctly |
| TC-MODULE-002 | Edit Module Details | Jan 17, 10:15 | PASS | Module title updated successfully |
| TC-MODULE-003 | Delete Module | Jan 17, 10:30 | PASS | Module deleted, progress records handled |
| TC-MODULE-004 | Add Multiple Modules | Jan 17, 10:45 | PASS | All 5 modules created in correct order |
| TC-MODULE-005 | View Modules - User Perspective | Jan 17, 11:00 | PASS | Modules displayed in sequential order |
| TC-MODULE-006 | Module Ordering | Jan 17, 11:15 | PASS | Modules sorted by order field correctly |
| TC-MODULE-007 | Module without Description | Jan 17, 11:30 | PASS | Description is optional, module created |
| TC-MODULE-008 | Duplicate Module Order | Jan 17, 11:45 | PASS | System handles duplicate orders gracefully |

**Module Notes:**
- Module management working flawlessly
- Order field properly enforced
- No issues encountered in this module

---

### 4. Enrollment Management (January 18-19, 2026)

| TC ID | Test Case | Date | Status | Notes |
|-------|-----------|------|--------|-------|
| TC-ENROLL-001 | Request Enrollment - User | Jan 18, 10:00 | PASS | Enrollment request created with pending status |
| TC-ENROLL-002 | Prevent Duplicate Enrollment | Jan 18, 10:15 | PASS | Duplicate enrollment blocked with error message |
| TC-ENROLL-003 | View Enrollment Requests | Jan 18, 10:30 | PASS | All pending requests displayed for course creator |
| TC-ENROLL-004 | Approve Enrollment Request | Jan 18, 10:45 | PASS | Status changed to approved, notification sent |
| TC-ENROLL-005 | Reject Enrollment Request | Jan 18, 11:00 | PASS | Status changed to rejected, notification sent |
| TC-ENROLL-006 | View My Enrollments - User | Jan 18, 11:15 | PASS | All enrollments shown with progress bars |
| TC-ENROLL-007 | Enrollment Status Visibility | Jan 18, 11:30 | PASS | Status badges display correctly (Pending/Approved) |
| TC-ENROLL-008 | Capacity Enforcement | Jan 18, 14:00 | BLOCKED | Cannot test - capacity check not fully implemented |
| TC-ENROLL-009 | Payment Amount Tracking | Jan 18, 14:15 | PASS | Payment amount stored in enrollment record |
| TC-ENROLL-010 | User Cannot Approve Own Enrollment | Jan 19, 09:00 | PASS | Authorization check works, access denied |

**Module Notes:**
- Enrollment workflow functioning well
- Notifications working properly on approve/reject
- Capacity enforcement placeholder identified (TC-ENROLL-008)
- Security checks in place for authorization

---

### 5. Progress Tracking (January 19, 2026)

| TC ID | Test Case | Date | Status | Notes |
|-------|-----------|------|--------|-------|
| TC-PROGRESS-001 | Mark Module as Complete | Jan 19, 10:00 | PASS | Module marked complete, checkbox persists |
| TC-PROGRESS-002 | Calculate Completion Percentage | Jan 19, 10:20 | PASS | Percentages calculated correctly (0%, 25%, 50%, 75%, 100%) |
| TC-PROGRESS-003 | Progress Bar Display | Jan 19, 10:35 | PASS | Progress bars fill proportionally, colors applied |
| TC-PROGRESS-004 | Course Completion Badge | Jan 19, 10:50 | PASS | Badge appears only at 100% completion |
| TC-PROGRESS-005 | Progress Persistence | Jan 19, 11:05 | PASS | Progress saved and restored across sessions |
| TC-PROGRESS-006 | View Detailed Progress | Jan 19, 11:20 | PASS | API returns accurate module progress data |
| TC-PROGRESS-007 | Unmark Module as Complete | Jan 19, 11:35 | PASS | Can uncheck modules, progress updates accordingly |
| TC-PROGRESS-008 | Progress for Multiple Enrollments | Jan 19, 11:50 | PASS | Each enrollment tracks progress independently |

**Module Notes:**
- Progress tracking rock solid
- All calculations accurate
- No issues with data persistence
- Badge system working perfectly

---

### 6. Dashboard (January 20, 2026)

| TC ID | Test Case | Date | Status | Notes |
|-------|-----------|------|--------|-------|
| TC-DASH-001 | User Dashboard - Enrolled Courses | Jan 20, 10:00 | PASS | All enrolled courses displayed as cards |
| TC-DASH-002 | Real-time Progress Display | Jan 20, 10:15 | PASS | Progress updates reflected after page refresh |
| TC-DASH-003 | User Dashboard - My Courses | Jan 20, 10:30 | PASS | Created courses shown with enrollment counts |
| TC-DASH-004 | Pending Enrollment Requests Display | Jan 20, 10:45 | PASS | Pending requests listed with student info |
| TC-DASH-005 | Dashboard Auto-refresh on Focus | Jan 20, 11:00 | PASS | Data refreshes when returning to tab |
| TC-DASH-006 | Empty State - No Enrollments | Jan 20, 11:15 | PASS | Helpful empty state message with browse link |

**Module Notes:**
- Dashboard very intuitive and functional
- Real-time updates working
- Empty states handled gracefully
- No performance issues with 10+ enrollments

---

### 7. Notifications (January 20, 2026)

| TC ID | Test Case | Date | Status | Notes |
|-------|-----------|------|--------|-------|
| TC-NOTIF-001 | Enrollment Approval Notification | Jan 20, 14:00 | PASS | Notification created and visible |
| TC-NOTIF-002 | Enrollment Rejection Notification | Jan 20, 14:15 | PASS | Rejection notification appears correctly |
| TC-NOTIF-003 | View All Notifications | Jan 20, 14:30 | PASS | All notifications listed, sorted by date |
| TC-NOTIF-004 | Unread Notification Count | Jan 20, 14:45 | FAIL | Unread count not visible - see DEF-012 |

**Module Notes:**
- Notifications being created properly
- Missing unread count badge feature
- Otherwise functional

---

## Defects Identified During Testing

### DEF-011: Password Mismatch Error Message Unclear
- **Severity:** Low
- **Module:** Authentication
- **Test Case:** TC-AUTH-015
- **Description:** When new password and confirmation don't match, error message just says "Error" instead of "Passwords do not match"
- **Date Found:** January 16, 2026
- **Status:** Logged

### DEF-002: Negative Course Capacity Accepted
- **Severity:** Medium  
- **Module:** Course Management
- **Test Case:** TC-COURSE-012
- **Description:** System accepts negative values for course capacity (e.g., -5). Should validate capacity >= 0
- **Date Found:** January 17, 2026
- **Status:** Logged

### DEF-012: Notification Unread Count Not Displayed
- **Severity:** Low
- **Module:** Notifications
- **Test Case:** TC-NOTIF-004
- **Description:** No visual indicator (badge/count) showing number of unread notifications
- **Date Found:** January 20, 2026
- **Status:** Logged

---

## Test Environment Details

**Setup:**
- Docker containers: learnhub-frontend, learnhub-api, learnhub-mysql
- Frontend: http://localhost:3001
- Backend API: http://localhost:5000
- Database: MySQL 8.0 on port 3307

**Test Data Used:**
- Users: user1@test.com, user2@test.com, user3@test.com, creator1@test.com
- Courses: 8 test courses across different categories
- Test password: Test123! (for all test users)

**Tools:**
- Chrome DevTools for network inspection
- Manual form interaction
- Database queries via MySQL Workbench for verification

---

## Issues/Observations

1. **Performance:** Application is responsive even with 50+ courses loaded. No noticeable lag.

2. **Browser Compatibility:** Tested primarily on Chrome. Should test on Firefox later.

3. **Data Persistence:** All data properly persists across sessions and browser restarts.

4. **Error Handling:** Most error messages are clear and actionable. A few could be improved (see defects).

5. **User Experience:** Overall UX is smooth. Dashboard is intuitive. Navigation is logical.

6. **Edge Cases:** System handles most edge cases well (empty states, missing data, etc.).

---

## Test Completion Checklist

- [DONE] All high priority test cases executed (64/64)
- [DONE] Medium and low priority cases executed (59/63 - 94%)
- [DONE] Defects logged with reproduction steps
- [DONE] Screenshots captured for failed tests (stored in test_results/screenshots/)
- [DONE] Test environment stable throughout testing period
- [DONE] All test data scenarios covered
- [PENDING] Browser compatibility testing (Firefox, Safari)
- [PENDING] Mobile responsiveness testing

---

## Recommendations

1. **Fix Identified Defects:** Address DEF-002 (capacity validation) and DEF-011 (error messages) before production

2. **Capacity Enforcement:** Implement full capacity checking logic (TC-ENROLL-008 currently blocked)

3. **Unread Count Feature:** Add notification badge to improve UX

4. **Cross-browser Testing:** Extend testing to Firefox and Safari

5. **Performance Testing:** Current manual testing shows good performance, but run JMeter load tests to confirm

6. **Accessibility:** Run WCAG compliance scan (not part of manual functional testing)

---

## Test Execution Metrics

- **Total Test Cases:** 63
- **Executed:** 63 (100%)
- **Passed:** 59 (94%)
- **Failed:** 3 (5%)
- **Blocked:** 1 (1%)
- **Test Duration:** 6 days (15-20 Jan)
- **Defects Found:** 3 (1 medium, 2 low)
- **Average Execution Time:** ~3-5 minutes per test case

---

## Sign-off

**Tested By:** T.R.S. Wickramarathna  
**Date:** January 23, 2026  
**Result:** 94% Pass Rate - Application is functional with minor issues  
**Recommendation:** Address medium severity defects before production deployment

**Next Steps:**
- Execute automation tests (Selenium + Postman)
- Perform performance testing (JMeter)
- Conduct security and accessibility audits
- Retest defects after fixes

---

**File:** test_results/manual_test_log.md  
**Last Updated:** January 23, 2026, 17:30  
**Version:** 1.0
