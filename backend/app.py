from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "campusconnect-secret-key"

DATABASE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "database",
    "events.db"
)


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_name TEXT NOT NULL,
            student_name TEXT,
            email TEXT,
            student_id TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT,
            date TEXT,
            description TEXT
        )
    """)

    existing_events = conn.execute(
        "SELECT COUNT(*) FROM events"
    ).fetchone()[0]

    if existing_events == 0:
        conn.executemany(
            """
            INSERT INTO events (name, category, date, description)
            VALUES (?, ?, ?, ?)
            """,
            [
                (
                    "AI & Innovation Workshop",
                    "TECHNOLOGY",
                    "15 OCT",
                    "Learn about artificial intelligence and emerging technologies."
                ),
                (
                    "Campus Cultural Fest",
                    "CULTURAL",
                    "20 OCT",
                    "Experience music, dance, art and performances from students."
                ),
                (
                    "Inter-College Hackathon",
                    "COMPETITION",
                    "25 OCT",
                    "Build innovative solutions and compete with students from different colleges."
                ),
                (
                    "Web Development Workshop 2026",
                    "TECHNOLOGY",
                    "30 OCT",
                    "Learn modern web development technologies and build practical projects."
                )
            ]
        )
    conn.commit()
    conn.close()


@app.route("/")
def home():

    conn = get_db_connection()

    events = conn.execute(
        "SELECT * FROM events ORDER BY id"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        events=events
    )

@app.route("/admin", methods=["GET", "POST"])
def admin():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        conn = get_db_connection()

        user = conn.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()

        conn.close()

        if user:

            session["admin_logged_in"] = True

            return redirect(url_for("admin_dashboard"))

        return render_template(
            "admin_login.html",
            error="Invalid username or password"
        )

    if not session.get("admin_logged_in"):

        return render_template("admin_login.html")

    return redirect(url_for("admin_dashboard"))


@app.route("/admin/dashboard")
def admin_dashboard():

    if not session.get("admin_logged_in"):
        return redirect(url_for("admin"))

    conn = get_db_connection()

    registrations = conn.execute(
        "SELECT * FROM registrations ORDER BY id DESC"
    ).fetchall()

    events = conn.execute(
        "SELECT * FROM events ORDER BY id"
    ).fetchall()

    conn.close()

    return render_template(
        "admin.html",
        registrations=registrations,
        events=events
    )

@app.route("/admin/add-event", methods=["POST"])
def add_event():

    if not session.get("admin_logged_in"):
        return redirect(url_for("admin"))

    name = request.form.get("name")
    category = request.form.get("category")
    date = request.form.get("date")
    description = request.form.get("description")

    conn = get_db_connection()

    conn.execute(
        """
        INSERT INTO events (name, category, date, description)
        VALUES (?, ?, ?, ?)
        """,
        (name, category, date, description)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("admin_dashboard"))

@app.route("/admin/delete-event/<int:event_id>", methods=["POST"])
def delete_event(event_id):

    if not session.get("admin_logged_in"):
        return redirect(url_for("admin"))

    conn = get_db_connection()

    conn.execute(
        "DELETE FROM events WHERE id = ?",
        (event_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("admin_dashboard"))

@app.route("/admin/edit-event/<int:event_id>", methods=["GET", "POST"])
def edit_event(event_id):

    if not session.get("admin_logged_in"):
        return redirect(url_for("admin"))

    conn = get_db_connection()

    if request.method == "POST":

        name = request.form.get("name")
        category = request.form.get("category")
        date = request.form.get("date")
        description = request.form.get("description")

        conn.execute(
            """
            UPDATE events
            SET name = ?, category = ?, date = ?, description = ?
            WHERE id = ?
            """,
            (name, category, date, description, event_id)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("admin_dashboard"))

    event = conn.execute(
        "SELECT * FROM events WHERE id = ?",
        (event_id,)
    ).fetchone()

    conn.close()

    return render_template(
        "edit_event.html",
        event=event
    )

@app.route("/admin/logout")
def admin_logout():

    session.pop("admin_logged_in", None)

    return redirect(url_for("admin"))

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    conn = get_db_connection()

    user = conn.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    ).fetchone()

    conn.close()

    if user:
        return jsonify({
            "success": True,
            "message": "Login successful"
        })

    return jsonify({
        "success": False,
        "message": "Invalid username or password"
    })


@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    event = data.get("event")
    name = data.get("name")
    email = data.get("email")
    student_id = data.get("student_id")

    conn = get_db_connection()

    conn.execute(
        """
        INSERT INTO registrations
        (event_name, student_name, email, student_id)
        VALUES (?, ?, ?, ?)
        """,
        (event, name, email, student_id)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": f"Successfully registered for {event}"
    })


if __name__ == "__main__":
    create_table()
    app.run(debug=True)