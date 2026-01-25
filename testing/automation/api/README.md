# LearnHub API Testing with Postman/Newman

## Overview
This directory contains Postman collections for testing all LearnHub API endpoints.

## Files
- `LearnHub_API.postman_collection.json` - Complete API test collection
- `LearnHub_ENV.postman_environment.json` - Environment variables

## Running Tests

### With Postman GUI
1. Import both JSON files into Postman
2. Select "LearnHub ENV" environment
3. Run the collection

### With Newman (CLI)
```bash
# Basic run
newman run LearnHub_API.postman_collection.json -e LearnHub_ENV.postman_environment.json

# With HTML report
newman run LearnHub_API.postman_collection.json \
  -e LearnHub_ENV.postman_environment.json \
  -r htmlextra \
  --reporter-htmlextra-export api_test_report.html
```

## Test Coverage
- Authentication Endpoints (7 tests)
- Course Endpoints (7 tests)
- Module Endpoints (4 tests)
- Enrollment Endpoints (4 tests)
- Progress Endpoints (2 tests)
- Notification Endpoints (1 test)

**Total:** 25 API tests

## Prerequisites
```bash
npm install -g newman newman-reporter-htmlextra
```
