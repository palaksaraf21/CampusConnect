# Requirements-to-Test Traceability Matrix

**Project:** CampusConnect – College Event Management & Registration System  
**Document ID:** SCM-RTM-001  
**Version:** 1.0  
**Status:** Draft – Pending review against the approved requirements

## 1. Purpose

This matrix connects selected system requirements and change-request requirements to their verification methods and available test evidence. Requirement IDs in this draft are provisional and must be reconciled with the faculty-approved requirements list.

## 2. Traceability Matrix

| Requirement ID | Requirement / Expected Behaviour | Verification Method | Test Case ID | Current Status |
|---|---|---|---|---|
| REQ-T01 | The home page should load successfully. | Automated functional test | TC-01: test_homepage_loads | Passed |
| REQ-T02 | The admin dashboard should require authentication. | Automated access-control test | TC-02: test_admin_dashboard_requires_login | Passed |
| REQ-T03 | Invalid admin credentials should be rejected. | Automated negative test | TC-03: test_admin_login_rejects_invalid_credentials | Passed |
| REQ-T04 | Valid admin credentials should be accepted. | Automated positive test | TC-04: test_admin_login_accepts_valid_credentials | Passed |
| REQ-T05 | The login API should accept valid credentials. | Automated API test | TC-05: test_login_api_accepts_valid_credentials | Passed |
| REQ-T06 | The login API should reject invalid credentials. | Automated negative API test | TC-06: test_login_api_rejects_invalid_credentials | Passed |
| REQ-T07 | Event registration data should be saved successfully. | Automated registration API test | TC-07: test_registration_api_saves_registration | Passed |
| CR-001 | Automated tests should run through GitHub Actions on configured pushes and pull requests. | Workflow configuration review and GitHub Actions run inspection | CI-01: GitHub Actions workflow | Passed; successful run observed |
| REQ-T08 | Event creation, editing, deletion, database integrity, and complete user workflows should be verified. | Additional functional and integration testing required | Not yet assigned | Pending |

## 3. Verification Summary

- Automated test cases documented in this matrix: 7 application tests.
- Application tests reported passing locally: 7 of 7.
- Continuous integration: GitHub Actions run reported successful.
- Additional coverage: Event administration, broader database integrity, security, and end-to-end acceptance testing remain to be verified.

## 4. Evidence to Retain

1. Automated test source file: `tests/test_app.py`
2. CI workflow: `.github/workflows/tests.yml`
3. GitHub Actions run showing the successful test result.
4. Change-request record: `documentation/CR-001-Automated-Testing.md`
5. Related commits and pull request history.

## 5. Review and Approval

**Prepared by:** Student project developer  
**Reviewed by:** Pending faculty review  
**Approval status:** Pending

This matrix is a working traceability record, not proof that every project requirement has been tested. Final requirement IDs and acceptance criteria must be checked against the approved project specification.
