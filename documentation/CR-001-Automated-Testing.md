# Change Request Record — CR-001

## 1. Change Request Details

| Field | Details |
|---|---|
| Change Request ID | CR-001 |
| Project | CampusConnect — College Event Management & Registration System |
| Change Title | Add Automated Testing and Continuous Integration |
| Change Type | Software enhancement / process improvement |
| Priority | Medium |
| Implementation Status | Implemented and merged |
| Target Baseline | main |
| Feature Branch | feature/automated-testing |
| Implementation Commit | 2acd7e7 |
| Merge Commit | 96999d2 |

## 2. Reason for Change

Manual testing alone does not provide repeatable verification whenever application code changes. Automated tests and continuous integration were introduced to identify regressions earlier and provide repeatable evidence of software quality.

## 3. Configuration Items Affected

| CI ID | Configuration Item | Change |
|---|---|---|
| CI-06 | Backend application | Tested existing Flask routes |
| CI-10 | Automated test suite | Added tests/test_app.py |
| CI-11 | Test results and verification evidence | Local and CI results recorded |
| CI-18 | Version and change records | Feature branch, commit, and merge recorded |
| CI-19 | CI workflow configuration | Added .github/workflows/tests.yml |

Note: CI IDs should be reconciled with the project's master configuration-item register.

## 4. Implementation Summary

- Created a separate feature branch for the change.
- Added seven pytest tests.
- Tested homepage loading, admin access control, admin authentication, login API responses, and student registration.
- Used a temporary SQLite database for test isolation.
- Added a GitHub Actions workflow for feature-branch pushes and pull requests targeting main.
- Submitted the implementation through a pull request and merged it into main.

## 5. Verification Results

| Test / Verification | Result |
|---|---|
| Homepage loads | PASS |
| Admin dashboard requires authentication | PASS |
| Invalid admin credentials rejected | PASS |
| Valid admin credentials accepted | PASS |
| Login API accepts valid credentials | PASS |
| Login API rejects invalid credentials | PASS |
| Student registration saved successfully | PASS |
| Total automated tests | 7 passed, 0 failed |
| GitHub Actions checks | Both reported green |
| Pull request | Merged |
| Main baseline synchronized | Verified by Git status |

## 6. Risk and Impact Assessment

Risk level: Low.

The automated tests use a temporary SQLite database and do not intentionally modify the project's local event database. The workflow installs its dependencies in GitHub's hosted runner and runs the test suite there.

## 7. SCM Process Followed

1. Change request identified and documented.
2. Feature branch created.
3. Implementation and automated tests committed.
4. Feature branch pushed to the remote repository.
5. Automated checks executed by GitHub Actions.
6. Pull request reviewed and merged.
7. Local main synchronized with origin/main.

## 8. Evidence to Retain

- GitHub issue for CR-001.
- Pull request #2 and its merge record.
- GitHub Actions runs showing successful checks.
- Local pytest output showing seven passing tests.
- Git commit and merge history.

## 9. Closure

Implementation status: Implemented and merged.

Acceptance/closure status: Confirm against the faculty's acceptance checklist before marking the change request formally closed.

Prepared for: SCM project review
Project: CampusConnect
