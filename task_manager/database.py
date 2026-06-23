import sqlite3
import os
# from task_manager.models import Task

DB_PATH = "data/tasks.db"

def get_connection():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            priority TEXT DEFAULT 'Medium',
            due_date TEXT,
            done INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def add_task(title,priority="Medium",due_date = None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (title , priority , due_date , done)
        VALUES (? ,?, ?,0)
    """,(title , priority , due_date ))    
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_tasks(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE ID = ?" , (task_id,))
    conn.commit()
    conn.close()

def mark_done(task_id):
    conn = get_connection()
    cursor =conn.cursor()
    cursor.execute("UPDATE tasks SET done = 1 WHERE id =?",(task_id,))
    conn.commit()
    conn.close()