# db_operations.py

import pymysql.cursors
from db_config import get_db_connection

def register_user(username, password):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(sql, (username, password))
        connection.commit()
    finally:
        connection.close()

def authenticate_user(username, password):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id FROM users WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()
            return result['id'] if result else None
    finally:
        connection.close()

def save_message(user_id, question, optimized_question, answer, chat_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = """INSERT INTO messages (user_id, question, optimized_question, answer, chat_id)
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(sql, (user_id, question, optimized_question, answer, chat_id))
        connection.commit()
    finally:
        connection.close()

def get_chats():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, title FROM chats"
            cursor.execute(sql)
            return cursor.fetchall()
    finally:
        connection.close()

def create_chat(user_id, title):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO chats (user_id, title) VALUES (%s, %s)"
            cursor.execute(sql, (user_id, title))
            connection.commit()
            return cursor.lastrowid
    finally:
        connection.close()

def get_messages(chat_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM messages WHERE chat_id = %s"
            cursor.execute(sql, (chat_id,))
            return cursor.fetchall()
    finally:
        connection.close()