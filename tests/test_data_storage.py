from backend.data_storage import store_email
import sqlite3
import os

def test_data_storage():
    # Setup a test database
    db_path = 'test_sdr.db'
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS emails (prospect TEXT, email TEXT)''')

    # Test storing an email
    store_email("John Doe", "This is a test email.")
    
    # Verify that the email is stored
    c.execute("SELECT * FROM emails WHERE prospect='John Doe'")
    result = c.fetchone()
    
    assert result is not None, "Email was not stored in the database"
    assert result[1] == "This is a test email.", "Email content does not match"
    
    # Clean up
    conn.close()
    os.remove(db_path)
