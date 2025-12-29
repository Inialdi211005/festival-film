from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import User, Film, get_db
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = 'kunci_rahasia_festival' 

@app.route('/reset-password')
def setup():
    return User.setup_passwords()


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.authenticate(username, password)

        if user:
            session['loggedin'] = True
            session['id'] = user['id']
            session['role'] = user['role']
            session['nama'] = user['nama_lengkap']
            flash(f"Selamat datang, {user['nama_lengkap']}!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Username atau Password salah!", "danger")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Anda berhasil logout.", "info")
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'loggedin' not in session: return redirect(url_for('login'))

    data_films = Film.get_all()
    return render_template('dashboard.html', films=data_films)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if 'loggedin' not in session: return redirect(url_for('login'))

    if request.method == 'POST':
        judul = request.form['judul']
        sutradara = request.form['sutradara']
        genre = request.form['genre']
        tahun = request.form['tahun']
        durasi = request.form['durasi']

        Film.create(judul, sutradara, genre, tahun, durasi, session['id'])
        flash("Film berhasil didaftarkan!", "success")
        return redirect(url_for('dashboard'))

    return render_template('form.html', action="Tambah")

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if 'loggedin' not in session: return redirect(url_for('login'))

    if request.method == 'POST':
        judul = request.form['judul']
        sutradara = request.form['sutradara']
        genre = request.form['genre']
        tahun = request.form['tahun']
        durasi = request.form['durasi']

        Film.update(id, judul, sutradara, genre, tahun, durasi)
        flash("Data film diperbarui!", "success")
        return redirect(url_for('dashboard'))

    data = Film.get_by_id(id)
    return render_template('form.html', action="Edit", film=data)

@app.route('/hapus/<id>')
def hapus(id):
    if 'loggedin' not in session: return redirect(url_for('login'))

    if session['role'] != 'admin':
        flash("Akses Ditolak! Anda bukan Admin.", "warning")
        return redirect(url_for('dashboard'))

    Film.delete(id)
    flash("Film berhasil dihapus!", "success")
    return redirect(url_for('dashboard'))

@app.route('/manage-jury')
def manage_jury():
    if 'loggedin' not in session: return redirect(url_for('login'))
    if session['role'] != 'admin':  
        flash("Akses Ditolak! Hanya Admin yang dapat mengelola juri.", "warning")
        return redirect(url_for('dashboard'))

    users = User.get_all()
    return render_template('manage_jury.html', users=users)

@app.route('/add-jury', methods=['GET', 'POST'])
def add_jury():
    if 'loggedin' not in session: return redirect(url_for('login'))
    if session['role'] != 'admin':  
        flash("Akses Ditolak! Hanya Admin yang dapat menambah juri.", "warning")
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        nama_lengkap = request.form['nama_lengkap']

        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s", (username,))
        existing_user = cur.fetchone()
        conn.close()

        if existing_user:
            flash("Username sudah digunakan. Silakan pilih username lain.", "danger")
            return render_template('add_jury.html')

        User.create(username, password, 'juri', nama_lengkap)
        flash("Juri berhasil ditambahkan!", "success")
        return redirect(url_for('manage_jury'))

    return render_template('add_jury.html')

if __name__ == '__main__':
    app.run(debug=True)