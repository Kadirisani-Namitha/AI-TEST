import sqlite3

# Initialize SQLite DB
conn = sqlite3.connect("memory.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS memory (id INTEGER PRIMARY KEY, prompt TEXT)")
conn.commit()
