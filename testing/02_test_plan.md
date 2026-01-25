# Test Plan
**LearnHub - Learning Management System**

**Module:** Software Testing & QA - ECS4308  
**Name:** T.R.S. Wickramarathna  
**University Registration No:** 22ug1-0529  
**Version:** 1.0  
**Date Prepared:** January 1 - January 25, 2026

---

## 1. Introduction

### 1.1 Purpose

This Test Plan document outlines the comprehensive testing strategy, scope, resources, and schedule for testing the LearnHub Learning Management System. The plan ensures systematic validation of functional and non-functional requirements to deliver a production-ready LMS application.

### 1.2 Scope

This test plan covers:
- Functional testing of all LearnHub features
- API testing for all backend endpoints
- Database integrity testing
- Performance testing (load and stress)
- Security testing (OWASP Top 10)
- Accessibility testing (WCAG 2.1)
- Automated testing (UI and API)

### 1.3 Objectives

1. Validate all functional requirements are correctly implemented
2. Ensure system performance meets defined standards
3. Identify and document security vulnerabilities
4. Verify WCAG 2.1 accessibility compliance
5. Achieve ≥85% test pass rate
6. Provide production-readiness assessment

---

## 2. Test Items

### 2.1 Application Under Test

**Application Name:** LearnHub LMS  
**Version: 1.0  
**Platform:** Web Application  
**Architecture:** Next.js (Frontend) + Express.js (Backend) + MySQL (Database)

### 2.2 Features to be Tested

| Module | Features | Priority |
|--------|----------|----------|
| **Authentication** | Register, Login, Profile Management, Password Change, Account Deletion | High |
| **Course Management** | Create, Edit, Delete, View, List, Search, Filter Courses | High |
| **Module Management** | Create, Edit, Delete, View Modules | High |
| **Enrollment** | Request, Approve, Reject, View Enrollments | High |
| **Progress Tracking** | Mark Complete, Calculate Progress, Display Badge | High |
| **Dashboard** | User Dashboard, User Dashboard, Real-time Updates | Medium |
| **Notifications** | Enrollment Notifications, View Notifications | Medium |

### 2.3 Features NOT to be Tested

- Third-party integrations (none currently exist)
- Mobile native applications (web-only testing)
- Email delivery infrastructure (out of scope)
- Payment gateway integration (not implemented)

---

## 3. Test Strategy

### 3.1 Testing Types

#### 3.1.1 Functional Testing (Manual + Automated)

**Objective:** Verify all features work as per requirements

**Approach:**
- Create detailed test cases for each feature
- Execute manually first to establish baseline
- Automate repetitive test cases using Selenium
- Test both positive and negative scenarios
- Validate error handling and edge cases

**Techniques:**
- Equivalence Partitioning (EP)
- Boundary Value Analysis (BVA)
- Decision Tables
- State Transition Testing
- Use Case Testing

**Coverage Target:** 100% of functional requirements

#### 3.1.2 API Testing (Automated)

**Objective:** Validate backend API endpoints

**Approach:**
- Create Postman collection for all endpoints
- Test CRUD operations for each resource
- Validate request/response structure  
- Test authentication and authorization
- Validate error responses and status codes

**Tools:** Postman, Newman

**Coverage Target:** All 25+ API endpoints

#### 3.1.3 Database Testing

**Objective:** Ensure data integrity and persistence

**Approach:**
- Validate data insertion, update, deletion
- Test foreign key constraints
- Verify transaction handling
- Test database triggers (if any)
- Validate data persistence across sessions

**Coverage Target:** All 6 database tables

#### 3.1.4 Performance Testing

**Objective:** Validate system performance under load

**Approach:**
- **Load Testing:** Test with 50, 100, 200 concurrent users
- **Stress Testing:** Gradually increase load to find breaking point
- **Endurance Testing:** Sustained load over extended period

**Test Scenarios:**
1. User authentication flow
2. Course browsing and filtering
3. Enrollment request submission
4. Module completion tracking
5. Dashboard loading with multiple enrollments

**Performance Benchmarks:**
- API response time: < 2 seconds
- Page load time: < 3 seconds
- Database query time: < 500ms
- Concurrent users supported: ≥100

**Tools:** Apache JMeter

#### 3.1.5 Security Testing

**Objective:** Identify security vulnerabilities

**Approach:**
- OWASP Top 10 assessment
- SQL injection testing
- XSS (Cross-Site Scripting) testing
- Authentication/Authorization bypass attempts
- Session management testing
- Input validation testing
- HTTPS/TLS verification (production)

**Security Checklist:**
1. SQL Injection prevention
2. XSS prevention
3. Password encryption (bcrypt)
4. JWT token security
5. Input sanitization
6. Rate limiting (if implemented)
7. CORS configuration
8. Sensitive data exposure

**Tools:** Manual testing, Browser DevTools, OWASP ZAP (optional)

#### 3.1.6 Accessibility Testing

**Objective:** Ensure WCAG 2.1 compliance

**Approach:**
- Automated accessibility scanning
- Manual keyboard navigation testing
- Screen reader compatibility
- Color contrast verification
- Form label validation
- ARIA attribute verification

**Compliance Levels:**
- **Target:** WCAG 2.1 Level A (minimum)
- **Goal:** WCAG 2.1 Level AA

**Tools:** WAVE, Axe DevTools, Lighthouse, Manual testing

---

## 4. Test Environment

### 4.1 Hardware Requirements

| Component | Specification |
|-----------|---------------|
| Processor | Intel i5 or higher |
| RAM | 8 GB minimum, 16 GB recommended |
| Storage | 20 GB free space |
| Network | Stable internet connection |

### 4.2 Software Requirements

| Software | Version | Purpose |
|----------|---------|---------|
| Operating System | Ubuntu 22.04 LTS | Test environment |
| Docker | 24.0+ | Application deployment |
| Docker Compose | 2.20+ | Multi-container orchestration |
| Web Browsers | Chrome 120+, Firefox 121+ | UI Testing |
| Node.js | 20+ | Backend runtime |
| MySQL | 8.0 | Database |
| Python | 3.12+ | Selenium automation |
| Java | 8+ | JMeter execution |
| Postman | Latest | API testing |

### 4.3 Test Data

#### Test Users

| Role | Email | Password | Purpose |
|------|-------|----------|---------|
| User 1 | instructor1@test.com | Test123! | Course owner |
| User 2 | instructor2@test.com | Test123! | Secondary instructor |
| User 1 | student1@test.com | Test123! | Primary student |
| User 2 | student2@test.com | Test123! | Secondary student |
| User 3 | student3@test.com | Test123! | Enrollment testing |

#### Test Courses

- **Web Development Fundamentals** (Beginner, Free)
- **Advanced React Patterns** (Advanced, Paid)
- **Python for Data Science** (Intermediate, Premium)
- **Mobile App Development** (Intermediate, Paid)
- **Cloud Computing Basics** (Beginner, Free)

### 4.4 Environment URLs

| Environment | Frontend | Backend | Database |
|-------------|----------|---------|----------|
| Local | http://localhost:3001 | http://localhost:5000 | localhost:3307 |
| Docker | http://localhost:3001 | http://localhost:5000 | database:3306 |

---

## 5. Test Deliverables

### 5.1 Test Documentation

1. **Requirement Analysis & RTM** (`01_requirement_analysis.md`)
2. **Test Plan** (`02_test_plan.md`) - This document
3. **Test Cases** (`03_test_cases.md`) - 50-200 test cases
4. **Manual Test Execution Report** (`04_manual_test_execution.md`)
5. **Automation Test Report** (`05_automation_report.md`)
6. **Performance Test Report** (`06_performance_testing.md`)
7. **Security & Accessibility Report** (`07_security_accessibility.md`)
8. **Defect Report** (`08_defect_report.md`)
9. **Test Summary Report** (`09_test_summary_report.md`)

### 5.2 Test Artifacts

- Selenium automation scripts (Python + pytest)
- Postman collection (JSON)
- JMeter test plans (.jmx files)
- Test execution logs
- Screenshots and evidence
- Performance metrics and graphs
- Defect screenshots

### 5.3 Test Code Repository

- GitHub repository with all test scripts
- Automation framework (Selenium + Page Object Model)
- API test collection
- Performance test plans
- README with execution instructions

---

## 6. Entry and Exit Criteria

### 6.1 Entry Criteria

- [PASS] Application is deployed and accessible
- [PASS] Test environment is set up and configured
- [PASS] Test data is prepared and loaded
- [PASS] Test cases are reviewed and approved
- [PASS] Testing tools are installed and configured
- [PASS] Access credentials are available

### 6.2 Exit Criteria

- [PASS] All planned test cases are executed
- [PASS] Test pass rate ≥ 85%
- [PASS] All Critical and High severity defects are resolved or documented
- [PASS] Performance benchmarks are met or documented
- [PASS] Security assessment is complete
- [PASS] Accessibility audit is complete
- [PASS] Test summary report is prepared and approved
- [PASS] Production readiness decision is documented

---

## 7. Suspension and Resumption Criteria

### 7.1 Suspension Criteria

Testing will be suspended if:
1. Critical application defects prevent test execution
2. Test environment is unavailable for >4 hours
3. Database corruption or data loss occurs
4. Major security vulnerability is discovered
5. Test data integrity is compromised

### 7.2 Resumption Criteria

Testing will resume when:
1. Blocking defects are fixed and verified
2. Test environment is restored and stable
3. Fresh database is deployed
4. Security patches are applied
5. Test data is restored

---

## 8. Test Tools

| Tool | Purpose | Category | License |
|------|---------|----------|---------|
| **Selenium WebDriver** | UI automation | Automation | Open Source |
| **pytest** | Test framework | Automation | Open Source |
| **Postman** | API testing | API | Free/Commercial |
| **Newman** | CLI API testing | Automation | Open Source |
| **Apache JMeter** | Performance testing | Performance | Open Source |
| **WAVE** | Accessibility scanning | Accessibility | Free |
| **Axe DevTools** | Accessibility testing | Accessibility | Free |
| **Chrome DevTools** | Debugging, inspection | Development | Free |
| **MySQL Workbench** | Database validation | Database | Free |
| **Docker** | Application deployment | Infrastructure | Free |

---

## 9. Roles and Responsibilities

| Role | Name | Responsibilities |
|------|------|------------------|
| **QA Engineer** | T.R.S. Wickramarathna | Test planning, test case design, test execution, defect reporting, automation, final reporting |
| **Test Manager** | T.R.S. Wickramarathna | Test strategy, resource planning, reporting, approval |
| **Developer** | (Self) | Defect fixing, code review, deployment |

---

## 10. Risk Assessment

### 10.1 Project Risks

| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|---------------------|
| **Incomplete test coverage** | Medium | High | Prioritize critical features, use RTM to track coverage |
| **Environment instability** | Low | High | Use Docker for consistent environment, maintain backups |
| **Time constraints** | Medium | Medium | Focus on high-priority tests first, automate regression |
| **Tool license limitations** | Low | Low | Use open-source tools, plan for commercial tool needs |
| **Data corruption** | Low | High | Regular database backups, use fresh schema for each test cycle |
| **Defect backlog** | Medium | Medium | Categorize by severity, focus on Critical/High first |

### 10.2 Technical Risks

| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|---------------------|
| **Browser compatibility issues** | Medium | Medium | Test on multiple browsers (Chrome, Firefox) |
| **Performance degradation** | Medium | High | Regular performance testing, optimize queries |
| **Security vulnerabilities** | High | Critical | Comprehensive security testing, follow OWASP guidelines |
| **Database connection pool exhaustion** | Low | High | Load testing to identify limits, configure pool size |
| **Third-party dependency failures** | Low | Medium | Document dependencies, have fallback plans |

---

## 11. Test Schedule

### 11.1 Timeline

| Phase | Duration | Start Date | End Date | Deliverable |
|-------|----------|------------|----------|-------------|
| **Test Planning** | 1 day | Jan 23, 2026 | Jan 23, 2026 | Test Plan, RTM |
| **Test Design** | 2 days | Jan 24, 2026 | Jan 25, 2026 | Test Cases (50-200) |
| **Test Environment Setup** | 0.5 days | Jan 24, 2026 | Jan 24, 2026 | Environment ready |
| **Manual Test Execution** | 1.5 days | Jan 26, 2026 | Jan 27, 2026 | Execution logs, defects |
| **Automation Development** | 2 days | Jan 26, 2026 | Jan 27, 2026 | Selenium + Postman scripts |
| **Automation Execution** | 0.5 days | Jan 28, 2026 | Jan 28, 2026 | Automation results |
| **Performance Testing** | 1 day | Jan 28, 2026 | Jan 28, 2026 | JMeter results |
| **Security Testing** | 1 day | Jan 29, 2026 | Jan 29, 2026 | OWASP assessment |
| **Accessibility Testing** | 0.5 days | Jan 29, 2026 | Jan 29, 2026 | WCAG audit |
| **Defect Verification** | 1 day | Jan 30, 2026 | Jan 30, 2026 | Verified defects |
| **Final Reporting** | 1 day | Jan 31, 2026 | Jan 31, 2026 | Test Summary Report |

**Total Duration:** 9 working days

---

## 12. Test Metrics

### 12.1 Metrics to be Collected

| Metric | Formula | Target |
|--------|---------|--------|
| **Test Case Pass Rate** | (Passed / Total) × 100 | ≥85% |
| **Defect Density** | Total Defects / Total Test Cases | <0.2 |
| **Defect Detection Rate** | New Defects / Testing Day | N/A |
| **Automation Coverage** | Automated TCs / Total TCs × 100 | ≥40% |
| **Requirement Coverage** | Requirements Tested / Total Requirements × 100 | 100% |
| **API Coverage** | APIs Tested / Total APIs × 100 | 100% |
| **Test Execution Progress** | Executed / Total × 100 | 100% |
| **Defect Resolution Rate** | Resolved / Total Defects × 100 | ≥70% |

### 12.2 Reporting Frequency

- **Daily:** Test execution status update
- **Weekly:** Progress report with metrics (if applicable)
- **Final:** Comprehensive test summary report

---

## 13. Defect Management

### 13.1 Defect Lifecycle

1. **New** → Defect identified and logged
2. **Assigned** → Assigned to developer for fixing
3. **In Progress** → Developer is working on fix
4. **Fixed** → Developer claims fix is complete
5. **Retest** → QA retests the defect
6. **Verified** → Defect fix confirmed by QA
7. **Closed** → Defect officially closed
8. **Reopened** → Defect fix failed retest

### 13.2 Severity and Priority

**Severity Levels:**
- **Critical:** System crash, data loss, security breach
- **High:** Major feature not working, incorrect functionality
- **Medium:** Minor feature issue, workaround available
- **Low:** Cosmetic issues, minor UI problems

**Priority Levels:**
- **P1:** Fix immediately
- **P2:** Fix in current sprint
- **P3:** Fix in next sprint
- **P4:** Fix when time permits

### 13.3 Defect Reporting

Each defect report will include:
- Defect ID
- Title and description
- Steps to reproduce
- Expected vs actual results
- Severity and priority
- Screenshots/evidence
- Environment details
- Test case reference

---

## 14. Communication Plan

### 14.1 Stakeholder Communication

| Stakeholder | Method | Frequency | Content |
|-------------|--------|-----------|---------|
| Project Supervisor | Email/Document | Weekly | Progress updates, blocking issues |
| Documentation Review | GitHub | On-demand | Test artifacts, reports |

### 14.2 Reporting Structure

- **Test Progress:** Daily status updates in test execution log
- **Defect Reports:** Logged immediately upon discovery
- **Test Summary:** Final comprehensive report at end of testing

---

## 15. Assumptions and Dependencies

### 15.1 Assumptions

1. Application is stable enough for testing
2. All features mentioned in requirements are implemented
3. Test environment will be available throughout testing period
4. No major architectural changes during testing
5. Reasonable defect fix turnaround time

### 15.2 Dependencies

1. Docker and Docker Compose installed and configured
2. MySQL database accessible
3. Network connectivity for API testing
4. Browser drivers for Selenium automation
5. JMeter installation for performance testing
6. Access to all application features (no restricted areas)

---

| **Prepared By** | T.R.S. Wickramarathna | __________ | Jan 23, 2026 |
| **Reviewed By** | (Self-review) | __________ | Jan 23, 2026 |
| **Approved By** | (Course Instructor) | __________ | __________ |

---

## 17. Appendix

### 17.1 Test Case Template

```
Test Case ID: TC-XXX-###
Title: [Brief description]
Module: [Authentication/Course/Enrollment/etc.]
Priority: [High/Medium/Low]
Preconditions: [Setup required]
Test Steps:
  1. [Step 1]
  2. [Step 2]
  3. [Step 3]
Expected Result: [What should happen]
Actual Result: [What actually happened]
Status: [Pass/Fail/Blocked]
Test Data: [Data used]
```

### 17.2 Defect Report Template

```
Defect ID: DEF-###
Title: [Brief description]
Severity: [Critical/High/Medium/Low]
Priority: [P1/P2/P3/P4]
Module: [Affected module]
Steps to Reproduce:
  1. [Step 1]
  2. [Step 2]
Expected: [Expected behavior]
Actual: [Actual behavior]
Environment: [Browser, OS, etc.]
Attachments: [Screenshots]
```

### 17.3 References

1. LearnHub GitHub Repository
2. OWASP Top 10: https://owasp.org/www-project-top-ten/
3. WCAG 2.1 Guidelines: https://www.w3.org/WAI/WCAG21/quickref/
4. Selenium Documentation: https://www.selenium.dev/documentation/
5. JMeter User Manual: https://jmeter.apache.org/usermanual/

---

**Document Status:** [PASS] Complete  
**Version:** 1.0  
**Next Step:** Test Case Design  
**Prepared by:** T.R.S. Wickramarathna (22ug1-0529)
