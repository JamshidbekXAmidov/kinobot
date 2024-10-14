import sqlite3
from db import connect

cur = connect.cur
conn = connect.conn


class Base:
    def __init__(self, table):
        self.table = table
    def create_data(self, telegram_id: str):
        query = f"INSERT INTO {self.table} (telegram_id) VALUES (?)"
        cur.execute(query, (telegram_id,))
        conn.commit()

    def get_data(self, telegram_id: str):
        query = f"SELECT * FROM {self.table} WHERE telegram_id = ?"
        cur.execute(query, (telegram_id,))
        return cur.fetchone()

    def delete_data(self, telegram_id: str):
        query = f"DELETE FROM {self.table} WHERE telegram_id = ?"
        cur.execute(query, (telegram_id,))
        conn.commit()

    def get_datas(self):
        query = f"SELECT * FROM {self.table}"
        cur.execute(query)
        return cur.fetchall()

    def statistika(self):
        query_month = f"SELECT * FROM {self.table} WHERE created_at >= datetime('now', 'start of month', '-1 month')"
        cur.execute(query_month)
        month = cur.fetchall()

        query_week = f"SELECT * FROM {self.table} WHERE created_at >= datetime('now', 'weekday 0', '-7 days')"
        cur.execute(query_week)
        week = cur.fetchall()

        query_day = f"SELECT * FROM {self.table} WHERE created_at >= datetime('now', 'start of day', '-1 day')"
        cur.execute(query_day)
        day = cur.fetchall()

        return {'month': month, 'week': week, 'day': day}


class MediaClass(Base):

    def create_data(self, post_id: int, file_id: str, caption: str):
        query = f"INSERT INTO {self.table} (post_id, file_id, caption) VALUES (?, ?, ?)"
        cur.execute(query, (post_id, file_id, caption))
        conn.commit()

    def get_data(self, post_id: int):
        query = f"SELECT * FROM {self.table} WHERE post_id = ?"
        cur.execute(query, (post_id,))
        return cur.fetchone()

    def get_movie(self, file_id: str):
        query = f"SELECT * FROM {self.table} WHERE file_id = ?"
        cur.execute(query, (file_id,))
        return cur.fetchone()

    def delete_movie(self, post_id: int):
        query = f"DELETE FROM {self.table} WHERE post_id = ?"
        cur.execute(query, (post_id,))
        conn.commit()


class ChannelClass(Base):

    def create_data(self, username: str, channel_id: str):
        query = f"INSERT INTO {self.table} (username, channel_id) VALUES (?, ?)"
        cur.execute(query, (username, channel_id))
        conn.commit()

    def get_data(self, channel_id: str):
        query = f"SELECT * FROM {self.table} WHERE channel_id = ?"
        cur.execute(query, (channel_id,))
        return cur.fetchone()

    def delete_data(self, channel_id: str):
        query = f"DELETE FROM {self.table} WHERE channel_id = ?"
        cur.execute(query, (channel_id,))
        conn.commit()
