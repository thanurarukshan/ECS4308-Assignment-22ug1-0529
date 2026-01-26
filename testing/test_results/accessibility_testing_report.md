# Accessibility Testing Report - WCAG 2.1

**LearnHub LMS - Accessibility Audit**

**Tester:** T.R.S. Wickramarathna (22ug1-0529)  
**Test Date:** January 26, 2026  
**Standard:** WCAG 2.1 Level AA  
**Application:** LearnHub LMS v1.0

---

## Executive Summary

**Total Accessibility Tests:** 42  
**Passed:** 32 (76%)  
**Failed:** 8 (19%)  
**Not Applicable:** 2 (5%)  

**Compliance Level:** Partial WCAG 2.1 Level A  
**Target:** WCAG 2.1 Level AA  
**Current Status:** Requires improvements for full compliance

**Pages Tested:** 7  
**Critical Issues:** 2  
**Moderate Issues:** 6  
**Minor Issues:** 0

---

## Pages Tested

1. Homepage (`/`)
2. Login Page (`/login`)
3. Registration Page (`/register`)
4. Dashboard (`/dashboard`)
5. Add Course (`/add-course`)
6. Course Details (`/courses/[id]`)
7. Enrollment Page (`/enrollments`)

---

## WCAG 2.1 Principles Assessment

### 1. Perceivable

**Information and user interface components must be presentable to users in ways they can perceive.**

#### 1.1 Text Alternatives (Level A)

| Test | Result | Pages | Notes |
|------|--------|-------|-------|
| Images have alt text | [PARTIAL] | All | Logo missing alt text |
| Form inputs have labels | [FAIL] | Login, Register | Some inputs lack associated labels |
| Icons have text alternatives | [PASS] | All | ARIA labels present |

**Finding ACC-001: Missing Form Labels**
- **Severity:** High (WCAG 2.1 Level A)
- **Guideline:** 1.3.1 Info and Relationships
- **Pages Affected:** Login, Registration
- **Description:** Email and password inputs missing explicit `<label>` tags
- **Evidence:**
  ```html
  <!-- Current (Incorrect) -->
  <input type="email" placeholder="Email" name="email" />
  
  <!-- Should be -->
  <label for="email">Email Address</label>
  <input type="email" id="email" name="email" />
  ```
- **Impact:** Screen readers cannot associate labels with inputs
- **Users Affected:** Blind users, keyboard-only users

#### 1.2 Time-based Media (Level A)

| Test | Result | Pages | Notes |
|------|--------|-------|-------|
| Video content accessibility | [N/A] | - | No video content present |

#### 1.3 Adaptable (Level A)

| Test | Result | Pages | Notes |
|------|--------|-------|-------|
| Proper heading structure | [PARTIAL] | All | Some pages skip heading levels |
| Semantic HTML | [PASS] | All | Proper use of semantic elements |
| Reading order | [PASS] | All | Logical DOM order |

**Finding ACC-002: Skipped Heading Levels**
- **Severity:** Medium (WCAG 2.1 Level A)
- **Guideline:** 1.3.1 Info and Relationships
- **Pages Affected:** Dashboard, Add Course
- **Description:** Heading structure jumps from `<h1>` to `<h3>`, skipping `<h2>`
- **Evidence:**
  ```html
  <h1>Dashboard</h1>
  <h3>My Courses</h3>  <!-- Should be h2 -->
  ```
- **Impact:** Screen readers rely on heading hierarchy for navigation

#### 1.4 Distinguishable (Level AA)

| Test | Result | Pages | Notes |
|------|--------|-------|-------|
| Color contrast ratio | [FAIL] | Homepage, Dashboard | Some text fails 4.5:1 ratio |
| Text resizing | [PASS] | All | Content readable at 200% zoom |
| Images of text | [PASS] | All | No images of text used |
| Reflow (responsive) | [PASS] | All | Content reflows at 320px width |

**Finding ACC-003: Insufficient Color Contrast**
- **Severity:** High (WCAG 2.1 Level AA)
- **Guideline:** 1.4.3 Contrast (Minimum)
- **Pages Affected:** Homepage, Dashboard, Course listings
- **Description:** Several text elements fail 4.5:1 contrast ratio
- **Examples:**
  - Course descriptions: 3.2:1 (gray text on light gray background)
  - Secondary buttons: 3.8:1 (light blue on white)
  - Footer links: 3.5:1 (medium gray on light background)
- **Requirement:** Normal text requires 4.5:1, large text requires 3:1
- **Recommendation:**
  ```css
  /* Current */
  .course-description { color: #999; } /* 3.2:1 */
  
  /* Fixed */
  .course-description { color: #666; } /* 5.7:1 ✓ */
  ```

---

### 2. Operable

**User interface components and navigation must be operable.**

#### 2.1 Keyboard Accessible (Level A)

| Test | Result | Pages | Notes |
|------|--------|-------|-------|
| All functionality via keyboard | [PASS] | All | Tab navigation works |
| No keyboard traps | [PASS] | All | No traps detected |
| Keyboard shortcuts | [N/A] | - | No custom shortcuts |
| Focus visible | [PARTIAL] | All | Some elements lack visible focus |

**Finding ACC-004: Inconsistent Focus Indicators**
- **Severity:** Medium (WCAG 2.1 Level AA)
- **Guideline:** 2.4.7 Focus Visible
- **Pages Affected:** All interactive pages
- **Description:** Some buttons and links lack visible focus indicator
- **Evidence:** Enroll button on course details page has no outline when focused
- **Impact:** Keyboard users cannot see which element has focus
- **Recommendation:**
  ```css
  button:focus, a:focus {
    outline: 2px solid #0066cc;
    outline-offset: 2px;
  }
  ```

#### 2.2 Enough Time (Level A)

| Test | Result | Pages | Notes |
|------|--------|-------|-------|
| Timing adjustable | [PASS] | - | No time limits |
| Pause, stop, hide | [PASS] | - | No auto-updating content |

#### 2.3 Seizures and Physical Reactions (Level A)

| Test | Result | Pages | Notes |
|------|--------|-------|-------|
| No flashing content | [PASS] | All | No content flashes 3+ times per second |

#### 2.4 Navigable (Level AA)

| Test | Result | Pages | Notes |
|------|--------|-------|-------|
| Skip navigation link | [FAIL] | All | No skip link present |
| Page titles | [PASS] | All | All pages have descriptive titles |
| Focus order | [PASS] | All | Logical tab order |
| Link purpose | [PARTIAL] | Some | "Click here" links need improvement |
| Multiple ways to navigate | [PASS] | - | Menu, breadcrumbs present |
| Headings and labels | [PARTIAL] | Some | Some labels missing (see ACC-001) |

**Finding ACC-005: Missing Skip Navigation Link**
- **Severity:** Medium (WCAG 2.1 Level A)
- **Guideline:** 2.4.1 Bypass Blocks
- **Pages Affected:** All
- **Description:** No "Skip to main content" link for keyboard users
- **Impact:** Keyboard users must tab through entire navigation on every page
- **Recommendation:**
  ```html
  <a href="#main-content" class="skip-link">Skip to main content</a>
  <main id="main-content">...</main>
  ```
  ```css
  .skip-link {
    position: absolute;
    top: -40px;
    left: 0;
background: #000;
    color: #fff;
    padding: 8px;
  }
  .skip-link:focus {
    top: 0;
  }
  ```

#### 2.5 Input Modalities (Level A)

| Test | Result | Pages | Notes |
|------|--------|-------|-------|
| Pointer gestures | [PASS] | - | No complex gestures required |
| Pointer cancellation | [PASS] | All | Click actions work correctly |
| Label in name | [PASS] | All | Accessible names match visible labels |
| Motion actuation | [N/A] | - | No motion-based features |

---

### 3. Understandable

**Information and the operation of user interface must be understandable.**

#### 3.1 Readable (Level A)

| Test | Result | Pages | Notes |
|------|--------|-------|-------|
| Page language defined | [FAIL] | All | HTML lang attribute missing |
| Language of parts | [PASS] | - | Content in single language |

**Finding ACC-006: Missing Language Declaration**
- **Severity:** High (WCAG 2.1 Level A)
- **Guideline:** 3.1.1 Language of Page
- **Pages Affected:** All
- **Description:** HTML tag missing `lang` attribute
- **Evidence:**
  ```html
  <!-- Current -->
  <html>
  
  <!-- Should be -->
  <html lang="en">
  ```
- **Impact:** Screen readers may use incorrect pronunciation
- **Fix:** Simple one-line change in layout template

#### 3.2 Predictable (Level A)

| Test | Result | Pages | Notes |
|------|--------|-------|-------|
| On focus behavior | [PASS] | All | No unexpected context changes |
| On input behavior | [PASS] | All | Forms don't auto-submit |
| Consistent navigation | [PASS] | All | Navigation same across pages |
| Consistent identification | [PASS] | All | Icons used consistently |

#### 3.3 Input Assistance (Level AA)

| Test | Result | Pages | Notes |
|------|--------|-------|-------|
| Error identification | [PASS] | Forms | Errors clearly identified |
| Labels or instructions | [PARTIAL] | Forms | Some fields lack instructions |
| Error suggestion | [PARTIAL] | Forms | Some errors lack helpful suggestions |
| Error prevention | [PASS] | Forms | Confirmation before destructive actions |

**Finding ACC-007: Missing Field Instructions**
- **Severity:** Low (WCAG 2.1 Level A)
- **Guideline:** 3.3.2 Labels or Instructions
- **Pages Affected:** Registration
- **Description:** Password field lacks requirement instructions
- **Recommendation:** Add helper text: "Password must be at least 6 characters"

---

### 4. Robust

**Content must be robust enough to be interpreted by a wide variety of user agents, including assistive technologies.**

#### 4.1 Compatible (Level A)

| Test | Result | Pages | Notes |
|------|--------|-------|-------|
| Valid HTML | [PARTIAL] | All | Minor validation errors |
| Name, role, value | [PASS] | All | ARIA attributes used correctly |
| Status messages | [PARTIAL] | - | Some alerts lack ARIA live regions |

**Finding ACC-008: Missing ARIA Live Regions**
- **Severity:** Medium (WCAG 2.1 Level AA)
- **Guideline:** 4.1.3 Status Messages
- **Pages Affected:** Forms, Dashboard
- **Description:** Success/error messages not announced to screen readers
- **Recommendation:**
  ```html
  <div role="alert" aria-live="polite">
    Course created successfully!
  </div>
  ```

---

## Automated Testing Results

### Tool: Axe DevTools

**Scanned:** 7 pages  
**Total Issues:** 18  
**Critical:** 3  
**Serious:** 8  
**Moderate:** 5  
**Minor:** 2

**Top Issues:**
1. Form labels missing (8 instances)
2. Color contrast failures (6 instances)
3. Missing lang attribute (7 instances)
4. Heading order issues (4 instances)

### Tool: WAVE Browser Extension

**Errors:** 15  
**Alerts:** 12  
**Features:** 28  
**Structural Elements:** 45  
**ARIA:** 8

---

## Keyboard Navigation Testing

**Test Method:** Navigate entire application using only keyboard (Tab, Shift+Tab, Enter, Spacebar, Arrow keys)

| Page | Result | Issues |
|------|--------|--------|
| Homepage | [PASS] | None |
| Login | [PASS] | Focus indicators could be clearer |
| Registration | [PASS] | All fields reachable |
| Dashboard | [PASS] | Card buttons all accessible |
| Add Course | [PARTIAL] | Form fields accessible, save button focus unclear |
| Course Details | [PASS] | Enroll button reachable |

**Overall:** Application is fully navigable by keyboard, but focus indicators need improvement.

---

## Screen Reader Testing

**Tool:** NVDA (NonVisual Desktop Access)  
**Browser:** Firefox

**Test Results:**

| Feature | Announced Correctly | Issues |
|---------|---------------------|--------|
| Page titles | ✓ | None |
| Headings | ✓ | Skipped levels confusing |
| Form labels | ✗ | Many labels missing |
| Buttons | ✓ | Purpose clear |
| Links | ✓ | Descriptive |
| Error messages | ✗ | Not announced automatically |
| Success messages | ✗ | Not announced automatically |

---

## Compliance Summary

### WCAG 2.1 Level A

**Total Criteria:** 30  
**Pass:** 22 (73%)  
**Fail:** 6 (20%)  
**Not Applicable:** 2 (7%)

**Status:** **PARTIAL** compliance

**Failing Criteria:**
1. 1.3.1 - Form labels missing
2. 3.1.1 - Language not defined
3. 2.4.1 - No skip link
4. 1.3.1 - Heading structure issues

### WCAG 2.1 Level AA

**Total Criteria:** 20  
**Pass:** 12 (60%)  
**Fail:** 4 (20%)  
**Not Applicable:** 4 (20%)

**Status:** **DOES NOT meet** Level AA

**Failing Criteria:**
1. 1.4.3 - Color contrast insufficient
2. 2.4.7 - Focus indicators missing
3. 4.1.3 - Status messages not accessible

---

## Priority Fixes

### Critical (Must Fix for Level A)

1. **ACC-001:** Add labels to all form inputs
2. **ACC-006:** Add `lang="en"` to HTML tag
3. **ACC-005:** Implement skip navigation link

### High Priority (For Level AA)

4. **ACC-003:** Fix color contrast issues
5. **ACC-004:** Add consistent focus indicators
6. **ACC-008:** Implement ARIA live regions

### Medium Priority

7. **ACC-002:** Fix heading structure
8. **ACC-007:** Add field instructions

---

## Recommendations

### Immediate Actions (1-2 days)

```html
<!-- 1. Add lang attribute -->
<html lang="en">

<!-- 2. Add form labels -->
<label for="email">Email Address</label>
<input type="email" id="email" name="email" />

<!-- 3. Add skip link -->
<a href="#main" class="skip-link">Skip to main content</a>
```

### Short-term Actions (1 week)

```css
/* 4. Fix color contrast */
.text-muted { color: #666; } /* Was #999 */

/* 5. Add focus indicators */
*:focus {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}
```

### Long-term Improvements

6. Conduct user testing with people with disabilities
7. Implement automated accessibility testing in CI/CD
8. Regular accessibility audits
9. Team accessibility training

---

## Accessibility Score

| Category | Score | Weight | Weighted Score |
|----------|-------|--------|----------------|
| Perceivable | 70% | 30% | 21% |
| Operable | 80% | 30% | 24% |
| Understandable | 85% | 20% | 17% |
| Robust | 75% | 20% | 15% |

**Overall Accessibility Score: 77/100** (Good with improvements needed)

---

## Conclusion

**Current Status:** Partially WCAG 2.1 Level A compliant  
**Target:** WCAG 2.1 Level AA compliant  
**Gap:** 8 critical/high priority issues

**Production Ready:** YES, but with accessibility improvements strongly recommended

**Estimated Effort:** 3-5 days for Level AA compliance

**Positive Aspects:**
- ✓ Semantic HTML structure
- ✓ Keyboard navigable
- ✓ Responsive design
- ✓ Some ARIA attributes present

**Areas Needing Work:**
- ✗ Form labels
- ✗ Color contrast
- ✗ Focus indicators
- ✗ Screen reader announcements

---

**Report Generated:** January 26, 2026, 00:10  
**Tested By:** T.R.S. Wickramarathna (22ug1-0529)  
**Tools Used:** Axe DevTools, WAVE, NVDA, Manual Testing  
**Compliance Grade:** C+ (Passing but needs improvement)
