# Build and Release Management Record

**Project:** CampusConnect – College Event Management & Registration System
**Document ID:** SCM-BRM-001
**Version:** 1.0
**Status:** Draft – Pending release verification

## 1. Purpose

This document records the procedure for building, verifying, versioning, and preparing CampusConnect for release.

## 2. Build Identification

| Field | Record |
|---|---|
| Project | CampusConnect |
| Repository | https://github.com/palaksaraf21/CampusConnect.git |
| Main branch | main |
| Build ID | CC-BUILD-001 |
| Application | Python Flask web application |
| Database | SQLite |
| Test framework | pytest |
| CI platform | GitHub Actions |
| Release status | Pending final verification |

## 3. Build Inputs

| Configuration Item | Purpose |
|---|---|
| backend/app.py | Backend application and routes |
| backend/templates/ | HTML templates |
| backend/static/ | Backend static assets |
| frontend/ | Frontend files |
| database/ | Database location |
| tests/test_app.py | Automated tests |
| .github/workflows/tests.yml | Continuous integration workflow |
| config/ | Project configuration |
| documentation/ | SCM records and project documentation |

## 4. Build Procedure

1. Obtain the required source version from Git.
2. Record the selected branch and commit ID.
3. Set up the Python environment.
4. Install the required application dependencies.
5. Run `python -m pytest -v`.
6. Review the test results and investigate failures.
7. Start the Flask application and manually verify key workflows.
8. Record the build identifier, commit ID, verification results, and date.
9. Obtain the required approval before declaring a release.

## 5. Release Readiness Checklist

| Verification Item | Status |
|---|---|
| Source code tracked in Git | YES |
| Main branch synchronized with remote | Verify before release |
| Automated test suite available | YES |
| Latest automated test results reviewed | Pending |
| Homepage manually tested | Pending |
| Login and registration workflows tested | Pending |
| Admin event-management workflows tested | Pending |
| Database setup documented | Pending |
| Dependencies documented | Pending |
| User guide prepared | Pending |
| Faculty acceptance | Pending |

## 6. Release Contents

The release should contain the application source code, templates, static assets, automated tests, CI workflow, dependency instructions, database setup instructions, user guide, release notes, and relevant SCM documentation.

The SQLite database file is excluded from Git. Document how to initialize the database so that a fresh setup does not depend on a local database file.

## 7. Version Control and Release Identification

Identify each build using its Git commit ID. After verification and approval, assign an appropriate Git release tag, such as `v1.0.0`, to the approved commit.

Do not create a final release tag until the required verification and approval are complete.

## 8. Known Limitations

- Current automated tests cover selected application behaviours, not every feature.
- Event creation, editing, deletion, database integrity, and end-to-end workflows require additional verification.
- Database initialization and dependency setup must be documented for reproducible builds.
- Final release approval is pending.

## 9. Approval Record

| Role | Name / Signature | Date | Status |
|---|---|---|---|
| Developer | Student project developer | Pending | Prepared |
| Reviewer | Faculty / authorized reviewer | Pending | Not reviewed |
| Release approver | Authorized approver | Pending | Not approved |
