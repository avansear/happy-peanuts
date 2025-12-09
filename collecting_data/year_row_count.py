import sqlite3

def year_row_count(table, year):
    try:
        conn = sqlite3.connect("peanuts.db")
        c = conn.cursor()
        c.execute(f"SELECT COUNT(*) FROM {table} WHERE year = ?", (year,))
        result = c.fetchone()[0]
        conn.close()
    except (sqlite3.OperationalError, sqlite3.DatabaseError):
        return 0

    return result