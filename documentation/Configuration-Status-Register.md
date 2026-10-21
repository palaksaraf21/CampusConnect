# CampusConnect — Configuration Status Accounting Register

**Project:** College Event Management & Registration System  
**Register version:** 1.0  
**Last updated:** 21 October 2026  
**Configuration baseline:** main  
**Project owner:** Palak Saraf

## 1. Configuration Item Status

| CI ID | Configuration Item | Version / Reference | Status | Owner | Approval |
|---|---|---|---|---|---|
| CI-01 | Project requirements | Review 1 document | Documented | Palak Saraf | Faculty approval to be confirmed |
| CI-02 | System design and architecture | Current design | Documented | Palak Saraf | Faculty approval to be confirmed |
| CI-03 | Frontend interface | main | Implemented | Palak Saraf | Pending final acceptance |
| CI-04 | Frontend JavaScript | main | Implemented | Palak Saraf | Pending final acceptance |
| CI-05 | Frontend stylesheets | main | Implemented | Palak Saraf | Pending final acceptance |
| CI-06 | Flask backend | main | Implemented | Palak Saraf | Pending final acceptance |
| CI-07 | Backend static assets | main | Implemented | Palak Saraf | Pending final acceptance |
| CI-08 | HTML templates | main | Implemented | Palak Saraf | Pending final acceptance |
| CI-09 | SQLite event database | Local database; excluded from Git | Local configuration | Palak Saraf | Local data; not a versioned baseline item |
| CI-10 | Automated test suite | Commit 2acd7e7 | Implemented and merged | Palak Saraf | CI checks passed |
| CI-11 | Test results and evidence | Local pytest and GitHub Actions | Verified | Palak Saraf | Verification recorded |
| CI-12 | SCM change-request records | CR-001 | Documented | Palak Saraf | Formal closure to be confirmed |
| CI-13 | CI workflow configuration | .github/workflows/tests.yml | Implemented and merged | Palak Saraf | CI checks passed |
| CI-14 | Version-control baseline | main; merge 96999d2 | Updated | Palak Saraf | Merged to main |
| CI-15 | SCM documentation | Commit 9910335 | Updated | Palak Saraf | Pending faculty review |

## 2. Version and Baseline History

| Reference | Description | Status |
|---|---|---|
| 27fa58c | Initial clean CampusConnect baseline | Historical baseline |
| 848fba8 | Earlier initial project baseline | Historical commit |
| 7fd1158 | Update platform title | Historical feature commit |
| 1f6375a | Stop tracking local database | Historical commit |
| 2acd7e7 | Add automated tests and GitHub Actions CI | Merged |
| 96999d2 | Merge automated testing pull request #2 | Merged baseline |
| 9910335 | Document CR-001 automated testing and CI | Current documentation commit |

## 3. Change Request Status

| Change Request | Description | Implementation | Verification | Current Status |
|---|---|---|---|---|
| CR-001 | Add automated testing and continuous integration | Merged into main | Seven local tests passed; GitHub Actions checks green | Implemented; formal closure pending acceptance confirmation |

## 4. Status Definitions

- **Planned:** Identified but implementation has not started.
- **In Progress:** Currently being implemented.
- **Implemented:** Work has been completed.
- **Verified:** Required tests or checks have passed.
- **Approved:** Authorized reviewer has approved the item.
- **Released:** Included in the designated release or baseline.
- **Pending:** Awaiting a required action, review, or decision.

## 5. Configuration Accounting Notes

1. The main branch is the authoritative shared code baseline.
2. Feature changes should be implemented on separate branches and submitted through pull requests.
3. GitHub Actions runs the automated test suite for configured pushes and pull requests.
4. The local SQLite database is excluded from version control to avoid committing local data.
5. CI ownership, approval, and release status must be updated when verified evidence or faculty decisions become available.
6. Do not mark an item Approved or Released without the required evidence.

