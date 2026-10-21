import sys
import sqlite3
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "backend"))

import app as campus_app


@pytest.fixture
def client(tmp_path, monkeypatch):
    test_db = tmp_path / "test_events.db"
    monkeypatch.setattr(campus_app, "DATABASE", str(test_db))

    conn = sqlite3.connect(test_db)
    conn.execute("""
        CREATE TABLE events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            date TEXT,
            description TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT NOT NULL,
            student_name TEXT,
            email TEXT,
            student_id TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.execute(
        "INSERT INTO events (name, category, date, description) VALUES (?, ?, ?, ?)",
        ("Test Workshop", "TECHNOLOGY", "2026-10-25", "Test event description"),
    )
    conn.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        ("testadmin", "testpassword"),
    )
    conn.commit()
    conn.close()

    campus_app.app.config.update(TESTING=True, SECRET_KEY="test-secret")
    with campus_app.app.test_client() as test_client:
        yield test_client


def test_homepage_loads(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Test Workshop" in response.data


def test_admin_dashboard_requires_login(client):
    response = client.get("/admin/dashboard")
    assert response.status_code == 302


def test_admin_login_rejects_invalid_credentials(client):
    response = client.post(
        "/admin",
        data={"username": "wronguser", "password": "wrongpassword"},
    )
    assert response.status_code == 200
    assert b"Invalid username or password" in response.data


def test_admin_login_accepts_valid_credentials(client):
    response = client.post(
        "/admin",
        data={"username": "testadmin", "password": "testpassword"},
    )
    assert response.status_code == 302
    assert "/admin/dashboard" in response.headers["Location"]


def test_login_api_accepts_valid_credentials(client):
    response = client.post(
        "/login",
        json={"username": "testadmin", "password": "testpassword"},
    )
    assert response.status_code == 200
    assert response.get_json()["success"] is True


def test_login_api_rejects_invalid_credentials(client):
    response = client.post(
        "/login",
        json={"username": "wronguser", "password": "wrongpassword"},
    )
    assert response.status_code == 200
    assert response.get_json()["success"] is False


def test_registration_api_saves_registration(client):
    response = client.post(
        "/register",
        json={
            "event": "Test Workshop",
            "name": "Test Student",
            "email": "student@example.com",
            "student_id": "TEST001",
        },
    )
    assert response.status_code == 200
    assert response.get_json()["success"] is True

    conn = sqlite3.connect(campus_app.DATABASE)
    row = conn.execute(
        "SELECT event_name, student_name, email, student_id FROM registrations"
    ).fetchone()
    conn.close()

    assert row == (
        "Test Workshop",
        "Test Student",
        "student@example.com",
        "TEST001",
    )
