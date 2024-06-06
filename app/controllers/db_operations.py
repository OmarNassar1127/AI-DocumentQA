import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
from db_config import get_db_connection

def register_user(username, password):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        hashed_password = generate_password_hash(password)
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(sql, (username, hashed_password))
    connection.commit()
    connection.close()

def authenticate_user(username, password):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "SELECT id, password FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()
    connection.close()
    if result and check_password_hash(result['password'], password):
        return result['id']
    return None

def create_chat(user_id, title):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO chats (user_id, title) VALUES (%s, %s)"
        cursor.execute(sql, (user_id, title))
    connection.commit()
    connection.close()

def get_chats(user_id):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "SELECT id, title, created_at FROM chats WHERE user_id = %s ORDER BY created_at DESC"
        cursor.execute(sql, (user_id,))
        result = cursor.fetchall()
    connection.close()
    return result

def save_message(chat_id, role, question, optimized_question, answer):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO messages (chat_id, role, question, optimized_question, answer) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (chat_id, role, question, optimized_question, answer))
    connection.commit()
    connection.close()

def get_messages(chat_id):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "SELECT role, question, optimized_question, answer, created_at FROM messages WHERE chat_id = %s ORDER BY created_at ASC"
        cursor.execute(sql, (chat_id,))
        result = cursor.fetchall()
    connection.close()
    return result