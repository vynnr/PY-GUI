import tkinter as tk
import tkinter.messagebox as msg

# Fungsi untuk menghitung uang kehadiran berdasarkan jumlah jam hadir


def hitung_uang_kehadiran(jam_hadir):
    if jam_hadir >= 8:
        return 35000
    elif jam_hadir >= 4 and jam_hadir <= 7:
        return (jam_hadir * 5000) - 5000
    else:
        return 0

# Fungsi untuk mengecek validitas input pengguna


def cek_input():
    if jam_hadir_entry.get() == "":
        msg.showerror("Error", "Jam hadir harus diisi.")
    elif not jam_hadir_entry.get().isdigit():
        msg.showerror("Error", "Jam hadir harus berupa angka.")
    else:
        jam_hadir = int(jam_hadir_entry.get())
        uang_kehadiran = hitung_uang_kehadiran(jam_hadir)
        msg.showinfo(
            "Uang Kehadiran", f"Karyawan berhak mendapatkan uang sebesar Rp. {uang_kehadiran}")


# Membuat GUI
root = tk.Tk()
root.title("Program Presensi Karyawan")

# Frame untuk input data
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Jam Hadir:").grid(row=0, column=0, padx=5, pady=5)
jam_hadir_entry = tk.Entry(input_frame)
jam_hadir_entry.grid(row=0, column=1, padx=5, pady=5)

# Tombol untuk submit data
submit_button = tk.Button(root, text="Submit", command=cek_input)
submit_button.pack()

root.mainloop()
