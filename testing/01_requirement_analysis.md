# Requirement Analysis & Traceability Matrix
**LearnHub - Learning Management System**

**Module:** Software Testing & QA - ECS4308  
**Name:** T.R.S. Wickramarathna  
**University Registration No:** 22ug1-0529  
**Version:** 1.0  
**Date Prepared:** January 1 - January 25, 2026

---

## 1. System Overview

### 1.1 Application Description

**LearnHub** is a comprehensive Learning Management System (LMS) built with modern web technologies. It enables instructors to create courses with structured modules and allows students to enroll, track progress, and complete courses through an intuitive interface.

**Architecture:**
- **Frontend:** Next.js 16 with React 19, TypeScript, Tailwind CSS
- **Backend:** Node.js with Express.js, TypeScript, Sequelize ORM
- **Database:** MySQL 8.0
- **Authentication:** JWT-based security
- **Deployment:** Docker containerization

### 1.2 Application Purpose

LearnHub is a community-based learning platform where all users have equal capabilities:

**All Users Can:**
- Create and manage courses with structured modules
- Enroll in any available course
- Track learning progress and earn completion badges
- Approve/reject enrollment requests for their own courses
- Share knowledge and learn from peers

This peer-to-peer model encourages knowledge sharing without rigid role hierarchies.

---

## 2. Identified Requirements

### 2.1 Functional Requirements

#### FR-AUTH: Authentication & User Management

| Req ID | Requirement Description | Priority | Status |
|--------|------------------------|----------|--------|
| FR-AUTH-01 | Users must be able to register with username, email, and password | High | [PASS] Implemented |
| FR-AUTH-02 | Users must be able to login with email and password | High | [PASS] Implemented |
| FR-AUTH-03 | Users must be able to view their profile information | Medium | [PASS] Implemented |
| FR-AUTH-04 | Users must be able to update their username | Medium | [PASS] Implemented |
| FR-AUTH-05 | Users must be able to change their password | High | [PASS] Implemented |
| FR-AUTH-06 | Users must be able to delete their account with password confirmation | Low | [PASS] Implemented |
| FR-AUTH-07 | System must use JWT tokens for session management | High | [PASS] Implemented |
| FR-AUTH-08 | Passwords must be hashed using bcrypt | High | [PASS] Implemented |

#### FR-COURSE: Course Management

| Req ID | Requirement Description | Priority | Status |
|--------|------------------------|----------|--------|
| FR-COURSE-01 | Users must be able to create new courses | High | [PASS] Implemented |
| FR-COURSE-02 | Course must have title, description, category, level, type, fee, duration, capacity | High | [PASS] Implemented |
| FR-COURSE-03 | Users must be able to edit their own courses | High | [PASS] Implemented |
| FR-COURSE-04 | Users must be able to delete their own courses | Medium | [PASS] Implemented |
| FR-COURSE-05 | All users must be able to view course details | High | [PASS] Implemented |
| FR-COURSE-06 | All users must be able to list all available courses | High | [PASS] Implemented |
| FR-COURSE-07 | Users must be able to filter courses by category | Medium | [PASS] Implemented |
| FR-COURSE-08 | Users must be able to filter courses by level (beginner/intermediate/advanced) | Medium | [PASS] Implemented |
| FR-COURSE-09 | Users must be able to filter courses by type (free/paid/premium) | Medium | [PASS] Implemented |
| FR-COURSE-10 | Users must be able to search courses by keyword | Medium | [PASS] Implemented |

#### FR-MODULE: Module Management

| Req ID | Requirement Description | Priority | Status |
|--------|------------------------|----------|--------|
| FR-MODULE-01 | Course creators must be able to add modules to their courses | High | [PASS] Implemented |
| FR-MODULE-02 | Each module must have title, description, and order | High | [PASS] Implemented |
| FR-MODULE-03 | Course creators must be able to edit module details | High | [PASS] Implemented |
| FR-MODULE-04 | Course creators must be able to delete modules | Medium | [PASS] Implemented |
| FR-MODULE-05 | All users must be able to view modules in a course | High | [PASS] Implemented |
| FR-MODULE-06 | Modules must be displayed in sequential order | Medium | [PASS] Implemented |

#### FR-ENROLL: Enrollment Management

| Req ID | Requirement Description | Priority | Status |
|--------|------------------------|----------|--------|
| FR-ENROLL-01 | Users must be able to request enrollment in courses | High | [PASS] Implemented |
| FR-ENROLL-02 | Enrollment request must include payment amount | Medium | [PASS] Implemented |
| FR-ENROLL-03 | Course creators must be able to view enrollment requests for their courses | High | [PASS] Implemented |
| FR-ENROLL-04 | Course creators must be able to approve enrollment requests | High | [PASS] Implemented |
| FR-ENROLL-05 | Course creators must be able to reject enrollment requests | High | [PASS] Implemented |
| FR-ENROLL-06 | Users must be able to view their enrollment status | High | [PASS] Implemented |
| FR-ENROLL-07 | System must prevent enrollment if course capacity is full | Medium | [PARTIAL] Partial |
| FR-ENROLL-08 | System must prevent duplicate enrollments | High | [PASS] Implemented |

#### FR-PROGRESS: Progress Tracking

| Req ID | Requirement Description | Priority | Status |
|--------|------------------------|----------|--------|
| FR-PROGRESS-01 | Enrolled users must be able to mark modules as complete | High | [PASS] Implemented |
| FR-PROGRESS-02 | System must calculate completion percentage automatically | High | [PASS] Implemented |
| FR-PROGRESS-03 | System must display progress bar on dashboard | High | [PASS] Implemented |
| FR-PROGRESS-04 | System must award "Course Completed" badge when all modules are done | Medium | [PASS] Implemented |
| FR-PROGRESS-05 | Progress must persist across sessions | High | [PASS] Implemented |
| FR-PROGRESS-06 | Users must be able to view detailed progress for each enrollment | Medium | [PASS] Implemented |

#### FR-DASHBOARD: Dashboard

| Req ID | Requirement Description | Priority | Status |
|--------|------------------------|----------|--------|
| FR-DASH-01 | Users must see all their enrolled courses on dashboard | High | [PASS] Implemented |
| FR-DASH-02 | Dashboard must display real-time progress for each course | High | [PASS] Implemented |
| FR-DASH-03 | Users must see their created courses on dashboard | High | [PASS] Implemented |
| FR-DASH-04 | Course creators must see pending enrollment requests for their courses | High | [PASS] Implemented |
| FR-DASH-05 | Dashboard must refresh on window focus | Low | [PASS] Implemented |

#### FR-NOTIF: Notifications

| Req ID | Requirement Description | Priority | Status |
|--------|------------------------|----------|--------|
| FR-NOTIF-01 | Users must receive notifications when enrollment is approved | Medium | [PASS] Implemented |
| FR-NOTIF-02 | Users must receive notifications when enrollment is rejected | Medium | [PASS] Implemented |
| FR-NOTIF-03 | Users must be able to view all their notifications | Medium | [PASS] Implemented |
| FR-NOTIF-04 | Notifications must show unread count | Low | [PARTIAL] Partial |

### 2.2 Non-Functional Requirements

#### NFR-PERF: Performance

| Req ID | Requirement Description | Priority | Status |
|--------|------------------------|----------|--------|
| NFR-PERF-01 | API response time should be < 2 seconds for all endpoints | High | [TEST] To Test |
| NFR-PERF-02 | System should handle 100 concurrent users | Medium | [TEST] To Test |
| NFR-PERF-03 | Database queries should complete in < 500ms | Medium | [TEST] To Test |
| NFR-PERF-04 | Page load time should be < 3 seconds | Medium | [TEST] To Test |

#### NFR-SEC: Security

| Req ID | Requirement Description | Priority | Status |
|--------|------------------------|----------|--------|
| NFR-SEC-01 | System must protect against SQL injection | High | [PASS] Implemented (ORM) |
| NFR-SEC-02 | System must protect against XSS attacks | High | [TEST] To Test |
| NFR-SEC-03 | Passwords must never be stored in plain text | High | [PASS] Implemented (bcrypt) |
| NFR-SEC-04 | API must validate JWT tokens on protected routes | High | [PASS] Implemented |
| NFR-SEC-05 | System should implement rate limiting on API endpoints | Medium | [FAIL] Missing |
| NFR-SEC-06 | System should use HTTPS in production | High | [FAIL] Missing |

#### NFR-ACCESS: Accessibility

| Req ID | Requirement Description | Priority | Status |
|--------|------------------------|----------|--------|
| NFR-ACCESS-01 | Application must be keyboard navigable | Medium | [TEST] To Test |
| NFR-ACCESS-02 | Application must have proper ARIA labels | Medium | [TEST] To Test |
| NFR-ACCESS-03 | Application must meet WCAG 2.1 Level A | Medium | [TEST] To Test |
| NFR-ACCESS-04 | Color contrast must meet WCAG guidelines | Low | [TEST] To Test |

#### NFR-USABILITY: Usability

| Req ID | Requirement Description | Priority | Status |
|--------|------------------------|----------|--------|
| NFR-USAB-01 | UI must be responsive (mobile, tablet, desktop) | High | [PASS] Implemented |
| NFR-USAB-02 | Error messages must be clear and actionable | Medium | [PASS] Implemented |
| NFR-USAB-03 | Success feedback must be provided for user actions | Medium | [PASS] Implemented |

---

## 3. Missing or Unclear Requirements

### 3.1 Critical Missing Requirements

1. **Email Verification**
   - Current Status: Users can register without email verification
   - Risk: Fake accounts, invalid emails
   - Recommendation: Implement email verification flow

2. **Password Reset/Recovery**
   - Current Status: No "Forgot Password" functionality
   - Risk: Users locked out if they forget password
   - Recommendation: Implement password reset via email

3. **Role-Based Access Control (RBAC)**
   - Current Status: Basic role assignment exists but not fully enforced
   - Risk: Students might access instructor-only features
   - Recommendation: Implement comprehensive RBAC middleware

4. **File Upload for Course Content**
   - Current Status: Modules only have text description
   - Risk: Limited course content types
   - Recommendation: Add support for PDFs, videos, images

5. **Search Functionality Enhancement**
   - Current Status: Basic keyword search only
   - Risk: Poor discoverability
   - Recommendation: Implement full-text search with filters

### 3.2 Unclear Requirements

1. **Enrollment Approval Process**
   - Unclear: Can students access course content while enrollment is pending?
   - Needs Clarification: Automatic approval for free courses vs manual for paid?

2. **Module Completion Logic**
   - Unclear: Can students un-mark a module as complete?
   - Unclear: Are there any prerequisites between modules?

3. **Course Capacity Management**
   - Unclear: What happens after capacity is reached?
   - Unclear: Is there a waitlist feature?

4. **Payment Integration**
   - Unclear: Is there actual payment processing or just payment amount tracking?
   - Missing: Payment gateway integration

5. **Instructor Verification**
   - Unclear: Can anyone become an instructor?
   - Missing: Instructor verification/approval process

---

## 4. Requirement Traceability Matrix (RTM)

### 4.1 Authentication & User Management

| Req ID | Requirement | Test Case IDs | Test Type | Priority |
|--------|-------------|---------------|-----------|----------|
| FR-AUTH-01 | User registration | TC-AUTH-001, TC-AUTH-002, TC-AUTH-003, TC-API-001 | Functional, API | High |
| FR-AUTH-02 | User login | TC-AUTH-004, TC-AUTH-005, TC-API-002 | Functional, API | High |
| FR-AUTH-03 | View profile | TC-AUTH-007, TC-API-003 | Functional, API | Medium |
| FR-AUTH-04 | Update profile | TC-AUTH-008, TC-API-004 | Functional, API | Medium |
| FR-AUTH-05 | Change password | TC-AUTH-009, TC-API-005 | Functional, API | High |
| FR-AUTH-06 | Delete account | TC-AUTH-010, TC-API-006 | Functional, API | Low |
| FR-AUTH-07 | JWT authentication | TC-SEC-001, TC-SEC-002 | Security | High |
| FR-AUTH-08 | Password hashing | TC-DB-001 | Security, Database | High |

### 4.2 Course Management

| Req ID | Requirement | Test Case IDs | Test Type | Priority |
|--------|-------------|---------------|-----------|----------|
| FR-COURSE-01 | Create course | TC-COURSE-001, TC-COURSE-002, TC-API-007 | Functional, API | High |
| FR-COURSE-02 | Course attributes | TC-COURSE-003, TC-DB-002 | Functional, Database | High |
| FR-COURSE-03 | Edit course | TC-COURSE-004, TC-API-008 | Functional, API | High |
| FR-COURSE-04 | Delete course | TC-COURSE-005, TC-API-009 | Functional, API | Medium |
| FR-COURSE-05 | View course details | TC-COURSE-006, TC-API-010 | Functional, API | High |
| FR-COURSE-06 | List courses | TC-COURSE-007, TC-API-011 | Functional, API | High |
| FR-COURSE-07 | Filter by category | TC-COURSE-008, TC-API-012 | Functional, API | Medium |
| FR-COURSE-08 | Filter by level | TC-COURSE-009, TC-API-013 | Functional, API | Medium |
| FR-COURSE-09 | Filter by type | TC-COURSE-010, TC-API-014 | Functional, API | Medium |
| FR-COURSE-10 | Search courses | TC-COURSE-011 | Functional | Medium |

### 4.3 Module Management

| Req ID | Requirement | Test Case IDs | Test Type | Priority |
|--------|-------------|---------------|-----------|----------|
| FR-MODULE-01 | Add modules | TC-MODULE-001, TC-API-015 | Functional, API | High |
| FR-MODULE-02 | Module attributes | TC-MODULE-002, TC-DB-003 | Functional, Database | High |
| FR-MODULE-03 | Edit modules | TC-MODULE-003, TC-API-016 | Functional, API | High |
| FR-MODULE-04 | Delete modules | TC-MODULE-004, TC-API-017 | Functional, API | Medium |
| FR-MODULE-05 | View modules | TC-MODULE-005, TC-API-018 | Functional, API | High |
| FR-MODULE-06 | Module ordering | TC-MODULE-006 | Functional | Medium |

### 4.4 Enrollment Management

| Req ID | Requirement | Test Case IDs | Test Type | Priority |
|--------|-------------|---------------|-----------|----------|
| FR-ENROLL-01 | Request enrollment | TC-ENROLL-001, TC-API-019 | Functional, API | High |
| FR-ENROLL-02 | Payment amount | TC-ENROLL-002, TC-DB-004 | Functional, Database | Medium |
| FR-ENROLL-03 | View enrollment requests | TC-ENROLL-003 | Functional | High |
| FR-ENROLL-04 | Approve enrollment | TC-ENROLL-004, TC-API-020 | Functional, API | High |
| FR-ENROLL-05 | Reject enrollment | TC-ENROLL-006, TC-API-021 | Functional, API | High |
| FR-ENROLL-06 | View enrollment status | TC-ENROLL-007 | Functional | High |
| FR-ENROLL-07 | Capacity enforcement | TC-ENROLL-008 | Functional | Medium |
| FR-ENROLL-08 | Prevent duplicates | TC-ENROLL-009, TC-DB-005 | Functional, Database | High |

### 4.5 Progress Tracking

| Req ID | Requirement | Test Case IDs | Test Type | Priority |
|--------|-------------|---------------|-----------|----------|
| FR-PROGRESS-01 | Mark complete | TC-PROGRESS-001, TC-API-022 | Functional, API | High |
| FR-PROGRESS-02 | Calculate percentage | TC-PROGRESS-002 | Functional | High |
| FR-PROGRESS-03 | Display progress bar | TC-PROGRESS-003 | Functional | High |
| FR-PROGRESS-04 | Completion badge | TC-PROGRESS-004 | Functional | Medium |
| FR-PROGRESS-05 | Persist progress | TC-PROGRESS-005, TC-DB-006 | Functional, Database | High |
| FR-PROGRESS-06 | View detailed progress | TC-PROGRESS-006, TC-API-023 | Functional, API | Medium |

### 4.6 Dashboard

| Req ID | Requirement | Test Case IDs | Test Type | Priority |
|--------|-------------|---------------|-----------|----------|
| FR-DASH-01 | Student enrolled courses | TC-DASH-001 | Functional | High |
| FR-DASH-02 | Real-time progress | TC-DASH-002 | Functional | High |
| FR-DASH-03 | Instructor courses | TC-DASH-003 | Functional | High |
| FR-DASH-04 | Pending enrollments | TC-DASH-004 | Functional | High |
| FR-DASH-05 | Auto-refresh | TC-DASH-005 | Functional | Low |

### 4.7 Notifications

| Req ID | Requirement | Test Case IDs | Test Type | Priority |
|--------|-------------|---------------|-----------|----------|
| FR-NOTIF-01 | Approval notification | TC-NOTIF-001, TC-API-024 | Functional, API | Medium |
| FR-NOTIF-02 | Rejection notification | TC-NOTIF-002, TC-API-025 | Functional, API | Medium |
| FR-NOTIF-03 | View notifications | TC-NOTIF-003 | Functional | Medium |
| FR-NOTIF-04 | Unread count | TC-NOTIF-004 | Functional | Low |

### 4.8 Non-Functional Requirements

| Req ID | Requirement | Test Case IDs | Test Type | Priority |
|--------|-------------|---------------|-----------|----------|
| NFR-PERF-01 | API response time | TC-PERF-001, TC-PERF-002 | Performance | High |
| NFR-PERF-02 | Concurrent users | TC-PERF-003, TC-PERF-004 | Performance | Medium |
| NFR-PERF-03 | Database performance | TC-PERF-005 | Performance | Medium |
| NFR-PERF-04 | Page load time | TC-PERF-006 | Performance | Medium |
| NFR-SEC-01 | SQL injection | TC-SEC-004 | Security | High |
| NFR-SEC-02 | XSS protection | TC-SEC-005 | Security | High |
| NFR-SEC-03 | Password security | TC-SEC-003 | Security | High |
| NFR-SEC-04 | JWT validation | TC-SEC-001, TC-SEC-002 | Security | High |
| NFR-ACCESS-01 | Keyboard navigation | TC-ACCESS-001 | Accessibility | Medium |
| NFR-ACCESS-02 | ARIA labels | TC-ACCESS-002 | Accessibility | Medium |
| NFR-ACCESS-03 | WCAG 2.1 Level A | TC-ACCESS-003 | Accessibility | Medium |
| NFR-ACCESS-04 | Color contrast | TC-ACCESS-004 | Accessibility | Low |
| NFR-USAB-01 | Responsive design | TC-USAB-001 | Usability | High |
| NFR-USAB-02 | Error messages | TC-USAB-002 | Usability | Medium |
| NFR-USAB-03 | Success feedback | TC-USAB-003 | Usability | Medium |

---

## 5. Requirements Coverage Summary

### 5.1 Coverage Statistics

| Category | Total Requirements | Implemented | Partial | Missing | To Test |
|----------|-------------------|-------------|---------|---------|---------|
| Authentication | 8 | 8 | 0 | 0 | 0 |
| Course Management | 10 | 10 | 0 | 0 | 0 |
| Module Management | 6 | 6 | 0 | 0 | 0 |
| Enrollment | 8 | 7 | 1 | 0 | 0 |
| Progress Tracking | 6 | 6 | 0 | 0 | 0 |
| Dashboard | 5 | 5 | 0 | 0 | 0 |
| Notifications | 4 | 3 | 1 | 0 | 0 |
| Performance | 4 | 0 | 0 | 0 | 4 |
| Security | 6 | 3 | 0 | 2 | 1 |
| Accessibility | 4 | 0 | 0 | 0 | 4 |
| Usability | 3 | 3 | 0 | 0 | 0 |
| **TOTAL** | **64** | **51** | **2** | **2** | **9** |

### 5.2 Implementation Status

- [PASS] Implemented: 51 (80%)
- [PARTIAL] Partial: 2 (3%)
- [FAIL] Missing: 2 (3%)
- [TEST] To Test: 9 (14%)

**Overall Implementation:** 80% complete

---

## 6. Test Scope Based on RTM

Based on the RTM, the following test scopes are defined:

### 6.1 Functional Testing Scope
- **75+ functional test cases** covering all implemented features
- Focus on: Authentication, Course Management, Enrollment, Progress Tracking

### 6.2 API Testing Scope
- **25+ API test cases** for all endpoints
- Includes positive and negative scenarios
- Authentication, CRUD operations, business logic validation

### 6.3 Database Testing Scope
- **6+ database test cases**
- Data integrity, constraints, transactions

### 6.4 Performance Testing Scope
- **6 performance test cases**
- Load testing (50, 100 users)
- Stress testing
- Response time validation

### 6.5 Security Testing Scope
- **5 security test cases**
- OWASP Top 10 assessment
- Authentication vulnerabilities
- Input validation testing

### 6.6 Accessibility Testing Scope
- **4 accessibility test cases**
- WCAG 2.1 Level A/AA compliance
- Keyboard navigation, screen readers

---

## 7. Conclusion

The LearnHub LMS has a solid foundation with 80% of identified requirements fully implemented. The system demonstrates good coverage of core LMS functionality including authentication, course management, enrollment workflows, and progress tracking.

**Key Strengths:**
- Comprehensive authentication system
- Well-designed course and module management
- Effective progress tracking mechanism
- Clean, modern UI with responsive design

**Areas for Improvement:**
- Implement missing security features (rate limiting, HTTPS)
- Add email verification and password reset
- Enhance RBAC implementation
- Improve accessibility compliance
- Add file upload capabilities for course content

**Testing Priority:**
1. **High:** Functional testing of core workflows
2. **High:** Security testing (OWASP)
3. **Medium:** Performance testing under load
4. **Medium:** Accessibility compliance (WCAG 2.1)
5. **Low:** UI/UX enhancements

This requirement analysis provides a solid foundation for comprehensive testing of the LearnHub system.

---

**Document Status:** Complete  
**Next Step:** Test Plan Creation  
**Prepared by:** T.R.S. Wickramarathna (22ug1-0529)
