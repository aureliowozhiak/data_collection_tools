-- SQLite
CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(1024), 
        message VARCHAR(1024), 
        created VARCHAR(1024)
)