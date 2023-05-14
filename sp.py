import tkinter as tk
import tkinter.messagebox as msg
import PyPDF2

# Fungsi untuk menghitung skor prestasi karyawan berdasarkan penilaian pimpinan


def hitung_skor(penilaian):
    skor = sum(penilaian.values()) / len(penilaian)
    return skor

# Fungsi untuk memberikan rekognisi atau peringatan kepada karyawan berdasarkan skor prestasi mereka


def berikan_rekognisi(karyawan, skor):
    if skor >= 90:
        msg.showinfo(
            "Rekognisi", f"Selamat {karyawan}! Anda mendapatkan insentif sebesar Rp. 10.000.000.")
    elif skor >= 80:
        msg.showinfo(
            "Rekognisi", f"Selamat {karyawan}! Anda mendapatkan sertifikat prestasi.")
    elif skor >= 70:
        msg.showinfo(
            "Peringatan", f"{karyawan}, Anda mendapatkan SP-1 karena tidak mencapai target.")
        with open(f"{karyawan}_SP1.pdf", "wb") as file:
            pdf = PyPDF2.PdfFileWriter()
            pdf.addPage(PyPDF2.PdfFileReader("SP1_template.pdf").getPage(0))
            pdf.encrypt("password")
            pdf.write(file)
    elif skor >= 60:
        msg.showinfo(
            "Peringatan", f"{karyawan}, Anda mendapatkan SP-2 karena sering terlambat.")
        with open(f"{karyawan}_SP2.pdf", "wb") as file:
            pdf = PyPDF2.PdfFileWriter()
            pdf.addPage(PyPDF2.PdfFileReader("SP2_template.pdf").getPage(0))
            pdf.encrypt("password")
            pdf.write(file)
    else:
        msg.showinfo(
            "Peringatan", f"{karyawan}, Anda mendapatkan SP-3 karena sering absen.")
        with open(f"{karyawan}_SP3.pdf", "wb") as file:
            pdf = PyPDF2.PdfFileWriter()
            pdf.addPage(PyPDF2.PdfFileReader("SP3_template.pdf").getPage(0))
            pdf.encrypt("password")
            pdf.write(file)

# Fungsi untuk mengecek validitas input pengguna


def cek_input():
    if karyawan_entry.get() == "":
        msg.showerror("Error", "Nama karyawan harus diisi.")
    elif not all(penilaian_entry[key].get().isdigit() for key in penilaian_entry.keys()):
        msg.showerror("Error", "Penilaian harus berupa angka.")
    else:
        karyawan = karyawan_entry.get()
        penilaian = {key: int(penilaian_entry[key].get())
                     for key in penilaian_entry.keys()}
        skor = hitung_skor(penilaian)
        berikan_rekognisi(karyawan, skor)


# Membuat GUI
root = tk.Tk()
root.title("Program Prestasi Karyawan")

# Frame untuk input data
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Nama Karyawan:").grid(
    row=0, column=0, padx=5, pady=5)
karyawan_entry = tk.Entry(input_frame)
karyawan_entry.grid(row=0, column=1, padx=5, pady=5)

penilaian_entry = {}
for i in range(4):
    tk.Label(
        input_frame, text=f"Penilaian {i+1}:").grid(row=i+1, column=0, padx=5, pady=5)
penilaian_entry[i] = tk.Entry(input_frame)
penilaian_entry[i].grid(row=i+1, column=1, padx=5, pady=5)
submit_button = tk.Button(root, text="Submit", command=cek_input)
submit_button.pack()

root.mainloop()
