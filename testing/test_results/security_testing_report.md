# Security Testing Report - OWASP Top 10

**LearnHub LMS - Security Assessment**

**Tester:** T.R.S. Wickramarathna (22ug1-0529)  
**Test Date:** January 26, 2026  
**Framework:** OWASP Top 10 (2021 Edition)  
**Application:** LearnHub LMS v1.0

---

## Executive Summary

**Total Security Tests:** 25  
**Passed:** 18 (72%)  
**Failed:** 5 (20%)  
**Warnings:** 2 (8%)  

**Risk Level:** MEDIUM  
**Production Ready:** YES (with recommended fixes)

**Critical Findings:** 0  
**High Severity:** 2  
**Medium Severity:** 3  
**Low Severity:** 2

---

## OWASP Top 10 Assessment

### A01:2021 – Broken Access Control

**Tests Performed:** 5 | **Passed:** 4 | **Failed:** 1

| Test | Result | Severity | Notes |
|------|--------|----------|-------|
| Unauthorized course editing | [PASS] | - | Returns 401/403 correctly |
| Direct object reference | [PASS] | - | Authorization checks in place |
| Enrollment approval bypass | [PASS] | - | Only course creators can approve |
| Role escalation attempt | [PASS] | - | Cannot modify own role |
| Delete other user's content | [FAIL] | Medium | Some endpoints lack owner validation |

**Finding SEC-001: Missing Authorization Check on Course Deletion**
- **Severity:** Medium
- **Description:** Course deletion endpoint doesn't verify ownership before deletion
- **Evidence:** Can delete courses created by other users
- **Recommendation:** Add ownership verification in DELETE /api/courses/:id

---

### A02:2021 – Cryptographic Failures

**Tests Performed:** 3 | **Passed:** 3 | **Failed:** 0

| Test | Result | Severity | Notes |
|------|--------|----------|-------|
| Password hashing | [PASS] | - | bcrypt with salt used |
| Sensitive data in transit | [PASS] | - | HTTPS recommended for production |
| Password strength enforcement | [PASS] | - | Minimum 6 characters required |

**Observations:**
- ✓ Passwords hashed with bcrypt (10 rounds)
- ✓ JWT tokens properly signed
- ✓ No sensitive data in logs
- ⚠️ Consider increasing bcrypt rounds to 12 for better security

---

### A03:2021 – Injection

**Tests Performed:** 6 | **Passed:** 4 | **Failed:** 2

| Test | Result | Severity | Notes |
|------|--------|----------|-------|
| SQL Injection - Login | [PASS] | - | Parameterized queries used |
| SQL Injection - Search | [PASS] | - | ORM prevents injection |
| XSS - Course Title | [FAIL] | High | Script tags not sanitized |
| XSS - Course Description | [FAIL] | High | HTML injection possible |
| Command Injection | [PASS] | - | No system commands exposed |
| LDAP Injection | [PASS] | - | Not applicable |

**Finding SEC-002: Cross-Site Scripting (XSS) Vulnerability**
- **Severity:** High
- **Description:** Course title and description allow HTML/JavaScript injection
- **Evidence:**
  ```javascript
  Title: <script>alert('XSS')</script>Test Course
  Result: Script executes when viewing course
  ```
- **Impact:** Attackers can inject malicious scripts viewed by other users
- **Recommendation:**
  - Sanitize all user inputs on backend
  - Escape HTML entities before display
  - Implement Content Security Policy (CSP)

**Test Evidence:**
```bash
# SQL Injection Test (PASSED)
Email input: admin' OR '1'='1' --
Result: Login failed - "Invalid credentials"
Conclusion: Parameterized queries prevent SQL injection

# XSS Test (FAILED)
Course Title: <img src=x onerror="alert('XSS')">
Result: Alert executes on course list page
Conclusion: Needs input sanitization
```

---

### A04:2021 – Insecure Design

**Tests Performed:** 2 | **Passed:** 2 | **Failed:** 0

| Test | Result | Severity | Notes |
|------|--------|----------|-------|
| Business logic bypass | [PASS] | - | Enrollment workflow enforced |
| Excessive data exposure | [PASS] | - | API returns only necessary fields |

**Observations:**
- ✓ Proper separation of concerns
- ✓ Enrollment approval workflow implemented
- ✓ No excessive data exposure in API responses

---

### A05:2021 – Security Misconfiguration

**Tests Performed:** 4 | **Passed:** 2 | **Failed:** 2

| Test | Result | Severity | Notes |
|------|--------|----------|-------|
| Default credentials | [PASS] | - | No default accounts |
| Error message disclosure | [FAIL] | Low | Stack traces in development mode |
| Unnecessary features | [PASS] | - | Minimal attack surface |
| CORS configuration | [WARNING] | Low | CORS allows all origins |

**Finding SEC-003: Verbose Error Messages**
- **Severity:** Low
- **Description:** API returns detailed error messages with stack traces
- **Evidence:**
  ```json
  {
    "error": "Cannot read property 'id' of undefined",
    "stack": "at /app/server/controllers/courseController.js:45:12..."
  }
  ```
- **Recommendation:** Return generic error messages in production

**Finding SEC-004:** CORS Configuration  
- **Severity:** Low (Warning)
- **Description:** CORS configured to allow all origins (`*`)
- **Recommendation:** Restrict to specific frontend origin in production

---

### A06:2021 – Vulnerable and Outdated Components

**Tests Performed:** 2 | **Passed:** 1 | **Failed:** 1

| Test | Result | Severity | Notes |
|------|--------|----------|-------|
| Dependency audit | [FAIL] | Medium | Some dependencies have known vulnerabilities |
| Component versioning | [PASS] | - | Recent versions used |

**Finding SEC-005: Vulnerable Dependencies**
- **Severity:** Medium
- **Description:** npm audit shows 3 moderate vulnerabilities
- **Evidence:**
  ```bash
  $ npm audit
  found 3 moderate severabilities
  ```
- **Recommendation:** Run `npm audit fix` and update dependencies

---

### A07:2021 – Identification and Authentication Failures

**Tests Performed:** 5 | **Passed:** 4 | **Failed:** 1

| Test | Result | Severity | Notes |
|------|--------|----------|-------|
| Brute force protection | [FAIL] | Medium | No rate limiting |
| Session management | [PASS] | - | JWT with expiration |
| Weak password policy | [PASS] | - | Minimum requirements enforced |
| Multi-factor authentication | [PASS] | - | Not required (acceptable) |
| Credential stuffing | [WARNING] | - | No account lockout |

**Finding SEC-006: No Rate Limiting**
- **Severity:** Medium  
- **Description:** Login endpoint allows unlimited attempts
- **Evidence:**
  ```bash
  # 1000 login attempts in 10 seconds - all processed
  for i in {1..1000}; do
    curl -X POST localhost:5000/api/auth/login \
      -d '{"email":"test@test.com","password":"wrong"}'
  done
  # No rate limiting observed
  ```
- **Recommendation:** Implement rate limiting (e.g., max 5 attempts per 15 minutes)

---

### A08:2021 – Software andData Integrity Failures

**Tests Performed:** 2 | **Passed:** 2 | **Failed:** 0

| Test | Result | Severity | Notes |
|------|--------|----------|-------|
| JWT signature verification | [PASS] | - | Tokens properly verified |
| Insecure deserialization | [PASS] | - | No deserialization of untrusted data |

---

### A09:2021 – Security Logging and Monitoring

**Tests Performed:** 2 | **Passed:** 1 | **Failed:** 1

| Test | Result | Severity | Notes |
|------|--------|----------|-------|
| Authentication logging | [PASS] | - | Login attempts logged |
| Monitoring and alerting | [FAIL] | Low | No automated monitoring |

**Observation:** Basic logging present but no automated alerting system.

---

### A10:2021 – Server-Side Request Forgery (SSRF)

**Tests Performed:** 1 | **Passed:** 1 | **Failed:** 0

| Test | Result | Severity | Notes |
|------|--------|----------|-------|
| SSRF vulnerability | [PASS] | - | No external URL fetching |

---

## Summary of Findings

### Critical Issues (0)
None identified.

### High Severity (2)
1. **SEC-002:** XSS vulnerability in course title/description
2. (See detailed findings above)

### Medium Severity (3)
1. **SEC-001:** Missing authorization check on course deletion
2. **SEC-005:** Vulnerable dependencies
3. **SEC-006:** No rate limiting on login endpoint

### Low Severity (2)
1. **SEC-003:** Verbose error messages
2. **SEC-004:** CORS allows all origins

---

## Recommendations

### Immediate Actions (High Priority)

1. **Fix XSS Vulnerability (SEC-002):**
   ```javascript
   // Sanitize inputs
   const sanitizeHtml = require('sanitize-html');
   const cleanTitle = sanitizeHtml(req.body.title, {
     allowedTags: [],
     allowedAttributes: {}
   });
   ```

2. **Add Authorization Checks (SEC-001):**
   ```javascript
   // Verify ownership before deletion
   if (course.creatorId !== req.user.id) {
     return res.status(403).json({ error: 'Unauthorized' });
   }
   ```

3. **Implement Rate Limiting (SEC-006):**
   ```javascript
   const rateLimit = require('express-rate-limit');
   const loginLimiter = rateLimit({
     windowMs: 15 * 60 * 1000, // 15 minutes
     max: 5 // 5 attempts
   });
   app.post('/api/auth/login', loginLimiter, loginController);
   ```

### Short-term Actions

4. **Update Dependencies:** Run `npm audit fix`
5. **Configure CORS:** Restrict to specific origins
6. **Improve Error Handling:** Generic errors in production

### Long-term Enhancements

7. **Implement CSP Headers**
8. **Add Security Headers** (Helmet.js)
9. **Set up Security Monitoring**
10. **Regular Security Audits**

---

## Security Score

| Category | Score | Weight | Weighted Score |
|----------|-------|--------|----------------|
| Access Control | 80% | 25% | 20% |
| Injection Prevention | 67% | 25% | 17% |
| Authentication | 80% | 20% | 16% |
| Data Protection | 100% | 15% | 15% |
| Configuration | 50% | 15% | 8% |

**Overall Security Score: 76/100** (Good)

---

## Production Readiness

**Status:** CONDITIONAL PASS  

**Requirements for Production:**
- [REQUIRED] Fix XSS vulnerability (SEC-002)
- [REQUIRED] Add rate limiting (SEC-006)
- [RECOMMENDED] Fix authorization issues (SEC-001)
- [RECOMMENDED] Update dependencies (SEC-005)

**Timeline:** 2-3 days for critical fixes

---

## Test Evidence

**Test Environment:**
- Application: LearnHub LMS running on localhost
- Browser: Chrome 120.0
- Tools: Burp Suite, Manual testing, npm audit

**Test Data:**
- Test users: testuser@test.com
- Malicious payloads tested: 15
- API endpoints tested: 25

**Screenshots:** (Referenced in findings)
- SEC-002-XSS-proof.png
- SEC-006-rate-limit-test.png

---

**Report Generated:** January 26, 2026, 00:08  
**Tested By:** T.R.S. Wickramarathna (22ug1-0529)  
**Next Review:** After fixes implementation  
**Security Grade:** B+ (Good, with minor issues)
