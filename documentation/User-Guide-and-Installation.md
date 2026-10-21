# CampusConnect User Guide and Installation Instructions

Project: College Event Management & Registration System
Document ID: CC-UG-001
Version: 1.0
Status: Draft - Pending practical verification

## 1. Introduction

CampusConnect is a web-based college event management and registration system. Students can view events and register, while authorized administrators can manage event information.

## 2. System Requirements

- Python 3.10 or a compatible version
- Git
- A modern web browser
- Internet access for cloning the repository and installing dependencies
- Terminal or command-line access

## 3. Obtain the Project

Clone the repository:

    git clone https://github.com/palaksaraf21/CampusConnect.git
    cd CampusConnect

If the project already exists on your computer, navigate to its existing folder instead.

## 4. Set Up the Environment

From the project root, run:

    python3 -m venv venv
    source venv/bin/activate
    python -m pip install Flask pytest

## 5. Database Setup

CampusConnect uses SQLite. The database file is excluded from Git. A fresh checkout may require database initialization. Verify the initialization procedure in the application code before running the project on a new computer.

## 6. Start the Application

From the project root, run:

    python backend/app.py

Open the local URL printed in Terminal. If Flask uses its default address, open:

    http://127.0.0.1:5000/

Keep Terminal open while using the application. Press Control+C to stop the server.

## 7. Student Usage

1. Open the homepage.
2. Browse the available events.
3. Open the relevant registration interface.
4. Enter the requested details.
5. Submit the registration.
6. Verify the response.

The exact steps depend on the implemented interface.

## 8. Administrator Usage

1. Open the administrator login page.
2. Enter the configured administrator credentials.
3. Open the admin dashboard.
4. Use the available controls to add, edit, or delete events.
5. Verify that the changes are reflected.

Do not assume default administrator credentials. Use verified credentials configured for the project.

## 9. Run Automated Tests

From the project root, with the virtual environment activated, run:

    python -m pytest -v

Review the output. The existing test suite previously reported seven passing tests; rerun it to confirm the current result.

## 10. Troubleshooting

- Python not found: check with python3 --version.
- Flask module missing: activate the virtual environment and install Flask.
- Database error: check the database path and initialization procedure.
- Port already in use: stop the other server or configure another port.
- Login fails: verify the credentials and database records.
- Tests fail: review the error output, dependencies, and database setup.

## 11. Security and Data Notes

- Never commit passwords or access tokens to Git.
- Use test data for demonstrations.
- Do not expose the development server publicly without suitable security measures.
- Back up any database data you need because the local SQLite database file is excluded from Git.

## 12. Limitations and Verification

This guide is a draft until its setup and usage steps have been tested from a clean checkout. Database initialization, administrator credentials, and student and administrator workflows still require verification.

## 13. Approval

Prepared by: Student project developer
Technical verification: Pending
Faculty review: Pending
