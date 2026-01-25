# OWASP Security Assessment Report
**LearnHub Learning Management System**

**Assessment Date:** January 23, 2026  
**Assessed By:** T.R.S. Wickramarathna (22ug1-0529)  
**Framework:** OWASP Top 10 (2021)  
**Methodology:** Manual testing + Code review

---

## Executive Summary

LearnHub LMS was assessed against the OWASP Top 10 security risks. The application demonstrates **moderate security** with good protection against injection and XSS attacks, but critical gaps in encryption, rate limiting, and password policies.

**Overall Security Score:** 5.5/10

**Status:** NOT READY **Not Production Ready** - Critical security issues must be addressed

---

## OWASP Top 10 Assessment

### A01:2021 – Broken Access Control

**Status:** [PARTIAL] PARTIAL PASS  
**Severity:** Medium  
**Test Cases:** TC-SEC-005

**Findings:**
[PASS] **Strengths:**
- Role-based access control implemented (student/instructor)
- JWT authentication properly validates user roles
- Students cannot access instructor-only endpoints
- Authorization middleware protects routes

[FAIL] **Weaknesses:**
- No granular permissions (only 2 roles)
- No ownership verification on some endpoints
- Missing RBAC for admin functions

**Evidence:**
```bash
# Test Results:
- Student accessing POST /api/courses → 403 Forbidden [PASS]
- Student editing own profile → 200 OK [PASS]
- Student editing another user's profile → Should fail (not fully tested)
```

**Recommendation:** Implement ownership checks on all user-specific resources

**Risk Level:** Medium

---

### A02:2021 – Cryptographic Failures

**Status:** [FAIL] FAIL  
**Severity:** CRITICAL  
**Defect:** DEF-001

**Findings:**
[FAIL] **Critical Issues:**
- **No HTTPS/TLS encryption** - All data transmitted in plain text
- Credentials sent over HTTP (easily intercepted)
- JWT tokens exposed in network traffic
- Session hijacking possible

[PASS] **Strengths:**
- Passwords hashed with bcrypt (verified)
- JWT secret properly configured (environment variable)
- No sensitive data in client-side storage (except JWT)

**Evidence:**
- Browser shows "Not Secure" warning
- Network traffic inspection reveals plain text credentials
- No SSL certificate configured

**Recommendation:**
1. **IMMEDIATE:** Configure HTTPS with SSL/TLS certificate
2. Set secure cookie flags (`Secure`, `HttpOnly`, `SameSite`)
3. Implement HSTS (HTTP Strict Transport Security)
4. Redirect all HTTP → HTTPS

**Risk Level:** CRITICAL

---

### A03:2021 – Injection

**Status:** [PASS] PASS  
**Severity:** N/A  
**Test Cases:** TC-SEC-004

**Findings:**
[PASS] **Strengths:**
- **Sequelize ORM** prevents SQL injection
- Parametrized queries used throughout
- No raw SQL queries with user input
- Input validation on API layer

**Test Evidence:**
```bash
# SQL Injection Attempts:
Email: admin' OR '1'='1 → Login Failed [PASS]
Search: '; DROP TABLE courses; -- → Sanitized [PASS]
Filter: 1 OR 1=1 → Handled safely [PASS]
```

**Recommendation:** Continue using ORM, avoid raw SQL

**Risk Level:** Low

---

### A04:2021 – Insecure Design

**Status:** [PARTIAL] PARTIAL PASS  
**Severity:** High  
**Defect:** DEF-002

**Findings:**
[FAIL] **Critical Issues:**
- **No rate limiting** on any endpoint
- Brute-force attacks possible on login
- No CAPTCHA on registration
- No account lockout after failed attempts

[PARTIAL] **Weaknesses:**
- No input size limits on some fields
- Missing business logic validation (capacity enforcement)

[PASS] **Strengths:**
- RESTful API design follows best practices
- Proper error handling (no stack traces exposed)
- Logical separation of concerns

**Evidence:**
```bash
# Brute Force Test:
- Sent 500 login attempts in 10 seconds → All processed (No limit) [FAIL]
- No lockout mechanism [FAIL]
- No delay between attempts [FAIL]
```

**Recommendation:**
1. Implement rate limiting (express-rate-limit)
2. Add account lockout (5 failed attempts)
3. Implement CAPTCHA on auth endpoints
4. Add request size limits

**Risk Level:** High

---

### A05:2021 – Security Misconfiguration

**Status:** [FAIL] FAIL  
**Severity:** High  
**Defects:** DEF-001, DEF-003

**Findings:**
[FAIL] **Critical Issues:**
- Default error messages expose system details
- No security headers configured
- Development mode in production
- Weak password policy (allows "123456")

[FAIL] **Missing Security Headers:**
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `X-XSS-Protection: 1; mode=block`
- `Content-Security-Policy`
- `Strict-Transport-Security`

**Evidence:**
```bash
curl -I http://localhost:5000/api/courses
# Missing all security headers [FAIL]
```

**Recommendation:**
1. Use helmet.js middleware for security headers
2. Implement strong password policy
3. Remove stack traces from error responses
4. Configure CSP policy
5. Set `NODE_ENV=production` in deployment

**Risk Level:** High

---

### A06:2021 – Vulnerable and Outdated Components

**Status:** [SKIP] NOT TESTED  
**Severity:** N/A

**Notes:**
- Dependencies not audited  in this assessment
- Run `npm audit` to check for vulnerabilities
- Keep dependencies up to date

**Recommendation:** Regular dependency audits

---

### A07:2021 – Identification and Authentication Failures

**Status:** [PARTIAL] PARTIAL PASS  
**Severity:** High  
**Defect:** DEF-003

**Findings:**
[FAIL] **Critical Issues:**
- **Weak password policy** - Minimum 6 characters only
- No password complexity requirements
- No email verification
- No password reset mechanism
- Passwords like "123456" accepted

[PASS] **Strengths:**
- JWT tokens expire (proper expiration handling)
- bcrypt hashing with salt
- No password stored in plain text
- Session management working correctly

**Evidence:**
```bash
# Password Tests:
Password: "123456" → Accepted [FAIL]
Password: "password" → Accepted [FAIL]
Password: "aaaaaa" → Accepted [FAIL]
```

**Recommendation:**
1. Require minimum 8 characters
2. Enforce password complexity (uppercase, lowercase, numbers, symbols)
3. Implement email verification
4. Add "Forgot Password" feature
5. Use password strength meter

**Risk Level:** High

---

### A08:2021 – Software and Data Integrity Failures

**Status:** [PASS] PASS  
**Severity:** N/A

**Findings:**
[PASS] **Strengths:**
- JWT tokens properly signed and verified
- No unsigned data accepted
- Integrity checks on authentication

**Recommendation:** Continue current practices

**Risk Level:** Low

---

### A09:2021 – Security Logging and Monitoring Failures

**Status:** [SKIP] NOT TESTED  
**Severity:** N/A

**Notes:**
- Logging not comprehensively assessed
- No centralized logging observed
- No security monitoring configured

**Recommendation:**
1. Implement comprehensive logging (Winston/Bunyan)
2. Log authentication failures
3. Log authorization violations
4. Set up monitoring alerts

---

### A10:2021 – Server-Side Request Forgery (SSRF)

**Status:** [SKIP] NOT APPLICABLE  
**Severity:** N/A

**Notes:**
- Application doesn't make server-side requests to user-provided URLs
- No apparent SSRF vectors

---

## Security Summary

| OWASP Risk | Status | Severity | Defects |
|------------|--------|----------|---------|
| A01: Broken Access Control | [PARTIAL] Partial | Medium | Minor gaps |
| A02: Cryptographic Failures | [FAIL] Fail | CRITICAL | DEF-001 |
| A03: Injection | [PASS] Pass | Low | None |
| A04: Insecure Design | [PARTIAL] Partial | High | DEF-002 |
| A05: Security Misconfiguration | [FAIL] Fail | High | DEF-001, DEF-003 |
| A06: Vulnerable Components | [SKIP] Not Tested | - | - |
| A07: Authentication Failures | [PARTIAL] Partial | High | DEF-003 |
| A08: Data Integrity | [PASS] Pass | Low | None |
| A09: Logging Failures | [SKIP] Not Tested | - | - |
| A10: SSRF | N/A | - | None |

**Score: 5.5/10**

---

## Critical Recommendations (P1)

1. [PASS] **Implement HTTPS/TLS** (DEF-001) - MUST FIX before production
2. [PASS] **Add API Rate Limiting** (DEF-002) - Prevent brute-force
3. [PASS] **Strengthen Password Policy** (DEF-003) - Require complexity
4. Add security headers (helmet.js)
5. Implement email verification

---

## Conclusion

LearnHub has **good foundational security** (ORM, password hashing, JWT) but **critical production gaps** (HTTPS, rate limiting, weak passwords). These issues must be resolved before production deployment.

**Status:** NOT READY NOT PRODUCTION READY  
**Estimated Remediation Time:** 3-5 days

---

**Assessed By:** T.R.S. Wickramarathna (22ug1-0529)  
**Date:** January 23, 2026
