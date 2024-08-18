import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('cutbot_database.db')
        self.c = self.conn.cursor()

    def insert_conversation(self, user_input, bot_response):
        self.c.execute("INSERT INTO conversations VALUES (NULL, ?, ?)", (user_input, bot_response))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()