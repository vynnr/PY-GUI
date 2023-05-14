import PySimpleGUI as sg
import pymysql

# Koneksi ke database
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="seminar"
)

# Membuat kursor
cur = conn.cursor()

# Membuat layout interface
layout = [
    [sg.Text("Nama:"), sg.InputText(key="nama")],
    [sg.Text("Email:"), sg.InputText(key="email")],
    [sg.Text("Telepon:"), sg.InputText(key="telepon")],
    [sg.Text("Alamat:"), sg.InputText(key="alamat")],
    [sg.Button("Tambah"), sg.Button("Baca"), sg.Button(
        "Perbarui"), sg.Button("Hapus"), sg.Button("Keluar")]
]

# Membuat window interface
window = sg.Window("Pendataan Peserta Seminar", layout)

# Fungsi untuk menambahkan data peserta


def tambah_peserta(nama, email, telepon, alamat):
    sql = "INSERT INTO peserta (nama, email, telepon, alamat) VALUES (%s, %s, %s, %s)"
    val = (nama, email, telepon, alamat)
    cur.execute(sql, val)
    conn.commit()
    sg.Popup("Peserta berhasil ditambahkan")

# Fungsi untuk membaca data peserta


def baca_peserta():
    cur.execute("SELECT * FROM peserta")
    rows = cur.fetchall()
    peserta = ""
    for row in rows:
        peserta += f"ID: {row[0]} | Nama: {row[1]} | Email: {row[2]} | Telepon: {row[3]} | Alamat: {row[4]}\n"
    sg.PopupScrolled(peserta, title="Data Peserta")

# Fungsi untuk memperbarui data peserta


def update_peserta(id, nama, email, telepon, alamat):
    sql = "UPDATE peserta SET nama=%s, email=%s, telepon=%s, alamat=%s WHERE id=%s"
    val = (nama, email, telepon, alamat, id)
    cur.execute(sql, val)
    conn.commit()
    sg.Popup("Peserta berhasil diperbarui")

# Fungsi untuk menghapus data peserta


def hapus_peserta(id):
    sql = "DELETE FROM peserta WHERE id=%s"
    val = (id,)
    cur.execute(sql, val)
    conn.commit()
    sg.Popup("Peserta berhasil dihapus")


# Looping interface
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Keluar":
        break
    elif event == "Tambah":
        tambah_peserta(values["nama"], values["email"],
                       values["telepon"], values["alamat"])
    elif event == "Baca":
        baca_peserta()
    elif event == "Perbarui":
        update_peserta(values["_id_"], values["nama"],
                       values["email"], values["telepon"], values["alamat"])
    elif event == "Hapus":
        hapus_peserta(values["_id_"])

# Menutup koneksi ke database dan window interface
cur.close()
conn.close()
window.close()
