import bcrypt
from db_config import get_db_connection

def fetch_context(user_id):
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT question, answer FROM interactions WHERE user_id = %s ORDER BY timestamp DESC LIMIT 10"
            cursor.execute(sql, (user_id,))
            interactions = cursor.fetchall()
        context = " ".join([f"Q: {i['question']} A: {i['answer']}" for i in interactions])
        return context
    finally:
        connection.close()

def register_user(username, password):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(sql, (username, hashed_password))
    connection.commit()
    connection.close()

def authenticate_user(username, password):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "SELECT id, password FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        user = cursor.fetchone()
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return user['id']
    connection.close()
    return None

def save_message(user_id, role, message):
    connection = get_db_connection()
    with connection.cursor() as cursor:
        sql = "INSERT INTO chats (user_id, role, message) VALUES (%s, %s, %s)"
        cursor.execute(sql, (user_id, role, message))
    connection.commit()
    connection.close()