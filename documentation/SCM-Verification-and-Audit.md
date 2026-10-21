# CampusConnect — SCM Verification and Audit Checklist

**Project:** College Event Management & Registration System  
**Prepared by:** Palak Saraf  
**Audit type:** Software Configuration Verification and Audit  
**Reference baseline:** main  
**Date:** 21 October 2026

## 1. Change Request Verification

| No. | Verification Item | Status | Evidence / Remarks |
|---|---|---|---|
| 1 | Change request documented | YES | CR-001 record created |
| 2 | Change implemented | YES | Automated tests and workflow added |
| 3 | Change committed to version control | YES | Commit 2acd7e7 |
| 4 | Change submitted through pull request | YES | Pull request #2 |
| 5 | Automated checks passed | YES | Both GitHub Actions checks green |
| 6 | Change merged into main | YES | Merge commit 96999d2 |
| 7 | Formal acceptance and closure recorded | PENDING | Confirm faculty acceptance criteria |

## 2. Requirements and Testing Verification

| No. | Verification Item | Status | Evidence / Remarks |
|---|---|---|---|
| 1 | Requirements mapped to test cases | PARTIAL | Mapping for CR-001 tests can be added |
| 2 | Homepage functional test completed | YES | test_homepage_loads |
| 3 | Admin dashboard access control tested | YES | test_admin_dashboard_requires_login |
| 4 | Invalid admin credentials tested | YES | test_admin_login_rejects_invalid_credentials |
| 5 | Valid admin credentials tested | YES | test_admin_login_accepts_valid_credentials |
| 6 | Login API success response tested | YES | test_login_api_accepts_valid_credentials |
| 7 | Login API failure response tested | YES | test_login_api_rejects_invalid_credentials |
| 8 | Registration API tested | YES | test_registration_api_saves_registration |
| 9 | All automated tests passed locally | YES | 7 passed |
| 10 | Continuous integration checked | YES | GitHub Actions checks green |
| 11 | Full end-to-end browser acceptance testing completed | PENDING | Perform and record separately |
| 12 | Critical defect review completed | PENDING | Review issues and test evidence |

## 3. Physical Configuration Audit

| No. | Audit Item | Status | Evidence / Remarks |
|---|---|---|---|
| 1 | Approved baseline identified | YES | main branch |
| 2 | Source code available in repository | YES | backend and frontend folders |
| 3 | Git history available | YES | Git commits and merge history |
| 4 | Automated test source available | YES | tests/test_app.py |
| 5 | CI workflow configuration available | YES | .github/workflows/tests.yml |
| 6 | Configuration status register maintained | YES | Configuration-Status-Register.md |
| 7 | Change request record maintained | YES | CR-001-Automated-Testing.md |
| 8 | Database schema and seed/recovery scripts documented | PENDING | Verify database setup and recovery documentation |
| 9 | User documentation available and current | PENDING | Verify the user guide |
| 10 | Release/build identifier recorded | PARTIAL | Git baseline exists; formal release identifier not assigned |
| 11 | Backup and restoration procedure tested | PENDING | Perform a controlled restoration test |
| 12 | Local database excluded from version control | YES | database/events.db listed in .gitignore |

## 4. Configuration Audit Findings

### Passed
- A clean shared baseline is maintained on main.
- Automated tests are version controlled.
- A GitHub Actions workflow executes the tests.
- CR-001 has a pull request and merge record.
- The configuration status register and change record are version controlled.
- Local SQLite data is excluded from Git.

### Outstanding Actions
1. Reconcile CI IDs with the faculty-approved master configuration-item list.
2. Add a requirement-to-test traceability matrix.
3. Complete end-to-end browser testing of the main user journeys.
4. Review and record known defects and unresolved issues.
5. Verify database initialization, schema setup, and recovery documentation.
6. Verify the user guide and assign a formal release/build identifier.
7. Confirm faculty acceptance before formally closing CR-001.

## 5. Audit Conclusion

The automated testing and continuous integration change has been implemented, tested, merged into the main baseline, and documented. The recorded local tests and GitHub Actions checks passed.

The audit is not a claim that every application feature has been fully acceptance-tested. Outstanding items above must be completed or explicitly accepted before the overall project can be declared fully audited and released.

