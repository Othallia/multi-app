from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Ambil data dari form yang dikirimkan
        nama = request.form['nama']
        nim = request.form['nim']
        prodi = request.form['prodi']
        
        return f"Data yang diterima:<br> Nama: {nama}<br> NIM: {nim}<br> Prodi: {prodi}"

if __name__ == '__main__':
    app.run(debug=True)
