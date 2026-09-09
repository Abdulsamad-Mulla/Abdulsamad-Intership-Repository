import mysql.connector
import bcrypt


# -----------------------------
# MySQL Database Connection
# -----------------------------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="job_skill_extraction"
    )


# -----------------------------
# Hash Password
# -----------------------------
def hash_password(password):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")


# -----------------------------
# Verify Password
# -----------------------------
def verify_password(password, password_hash):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        password_hash.encode("utf-8")
    )


# -----------------------------
# Register User
# -----------------------------
def register_user(name, email, password):

    conn = get_connection()
    cursor = conn.cursor()

    try:
        password_hash = hash_password(password)

        query = """
        INSERT INTO users (name, email, password_hash)
        VALUES (%s, %s, %s)
        """

        cursor.execute(
            query,
            (name, email, password_hash)
        )

        conn.commit()

        return True, "Registration successful!"

    except mysql.connector.IntegrityError:
        return False, "Email already exists."

    except Exception as e:
        return False, str(e)

    finally:
        cursor.close()
        conn.close()


# -----------------------------
# Login User
# -----------------------------
def login_user(email, password):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:

        query = """
        SELECT id, name, email, password_hash
        FROM users
        WHERE email = %s
        """

        cursor.execute(query, (email,))

        user = cursor.fetchone()

        if user is None:
            return None

        if verify_password(
            password,
            user["password_hash"]
        ):
            return user

        return None

    finally:
        cursor.close()
        conn.close()