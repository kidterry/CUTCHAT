import sqlite3

# Connect to the database
conn = sqlite3.connect('cutbot_database.db')
c = conn.cursor()

# Create the conversations table
c.execute('''CREATE TABLE IF NOT EXISTS conversations
             (id INTEGER PRIMARY KEY, user_input TEXT, bot_response TEXT)''')

# Commit the changes and close the connection
conn.commit()
conn.close()