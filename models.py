import pymysql.cursors
from werkzeug.security import generate_password_hash, check_password_hash

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'siff_db',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_db():
    return pymysql.connect(**DB_CONFIG)

class User:
    @staticmethod
    def authenticate(username, password):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cur.fetchone()
        conn.close()

        if user and check_password_hash(user['password'], password):
            return user
        return None

    @staticmethod
    def get_by_id(user_id):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id=%s", (user_id,))
        user = cur.fetchone()
        conn.close()
        return user

    @staticmethod
    def get_all():
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users ORDER BY id DESC")
        users = cur.fetchall()
        conn.close()
        return users

    @staticmethod
    def create(username, password, role, nama_lengkap):
        conn = get_db()
        cur = conn.cursor()
        hashed_password = generate_password_hash(password)
        cur.execute("INSERT INTO users (username, password, role, nama_lengkap) VALUES (%s, %s, %s, %s)",
                    (username, hashed_password, role, nama_lengkap))
        user_id = cur.lastrowid
        conn.commit()
        conn.close()
        return user_id

    @staticmethod
    def setup_passwords():
        conn = get_db()
        cur = conn.cursor()
        p_admin = generate_password_hash('admin123')
        p_juri = generate_password_hash('juri123')

        cur.execute("UPDATE users SET password=%s WHERE username='admin'", (p_admin,))
        cur.execute("UPDATE users SET password=%s WHERE username='juri'", (p_juri,))
        conn.commit()
        conn.close()
        return "Password berhasil di-hash! Silakan login."

class Film:
    @staticmethod
    def get_all():
        conn = get_db()
        cur = conn.cursor()
        query = """
            SELECT films.*, users.nama_lengkap as penginput
            FROM films
            LEFT JOIN users ON films.diinput_oleh = users.id
            ORDER BY films.id DESC
        """
        cur.execute(query)
        films = cur.fetchall()
        conn.close()
        return films
    
    @staticmethod
    def get_by_id(film_id):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM films WHERE id=%s", (film_id,))
        film = cur.fetchone()
        conn.close()
        return film
    
    @staticmethod
    def create(judul, sutradara, genre, tahun, durasi, user_id):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO films VALUES (NULL, %s, %s, %s, %s, %s, %s)",
                    (judul, sutradara, genre, tahun, durasi, user_id))
        conn.commit()
        film_id = cur.lastrowid
        conn.close()
        return film_id
    
    @staticmethod
    def update(film_id, judul, sutradara, genre, tahun, durasi):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""UPDATE films SET judul=%s, sutradara=%s, genre=%s,
                       tahun=%s, durasi_menit=%s WHERE id=%s""",
                    (judul, sutradara, genre, tahun, durasi, film_id))
        conn.commit()
        conn.close()
    
    @staticmethod
    def delete(film_id):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM films WHERE id=%s", (film_id,))
        conn.commit()
        conn.close()