from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'rahasia_super_penting'  # Dibutuhkan untuk session

@app.route('/', methods=['GET', 'POST'])
def input_nilai():
    if request.method == 'POST':
        # Simpan data di session
        session['nama'] = request.form['nama']
        session['nim'] = request.form['nim']
        session['jurusan'] = request.form['jurusan']
        session['email'] = request.form['email']
        session['kode'] = request.form['kode']
        session['matkul'] = request.form['matkul']
        session['sks'] = request.form['sks']
        session['nilai'] = request.form['nilai']
        return redirect(url_for('dashboard'))
    return render_template('input.html')

@app.route('/dashboard')
def dashboard():
    if 'nama' not in session:
        return redirect(url_for('input_nilai'))
    return render_template('dashboard.html')

@app.route('/data_diri')
def data_diri():
    if 'nama' not in session:
        return redirect(url_for('input_nilai'))
    return render_template(
        'data_diri.html', 
        nama=session['nama'], 
        nim=session['nim'], 
        jurusan=session['jurusan'], 
        email=session['email']
    )
    
@app.route('/krs')
def krs():
    if 'matkul' not in session:
        return redirect(url_for('input_nilai'))
    return render_template(
        'krs.html', 
        kode=session['kode'], 
        matkul=session['matkul'], 
        sks=session['sks']
    )

@app.route('/ipk')
def ipk():
    if 'nilai' not in session:
        return redirect(url_for('input_nilai'))
    return render_template('ipk.html', nilai=session['nilai'])

@app.route('/logout')
def logout():
    session.clear()  # Hapus semua data di session
    return redirect(url_for('input_nilai'))

if __name__ == '__main__':
    app.run(debug=True)
