import sqlite3

def return_row_count(table):
    """
    Desc: Checks table mentioned and returns rows collected so far.
    """
    try:
        conn = sqlite3.connect('peanuts.db')
        c = conn.cursor()

        c.execute(f"SELECT COUNT(*) FROM {table}")
        row_count = c.fetchone()[0]
        conn.close()
    except (sqlite3.OperationalError, sqlite3.DatabaseError):
        return 0

    return row_count