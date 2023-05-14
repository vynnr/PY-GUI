from tkinter import *

root = Tk()
root.title("Konversi Suhu")

def konversi_celcius():
    fahrenheit = float(input_entry.get()) * 9/5 + 32
    reamur = float(input_entry.get()) * 4/5
    kelvin = float(input_entry.get()) + 273
    fahrenheit_label.config(text=f"{fahrenheit:.2f} F")
    reamur_label.config(text=f"{reamur:.2f} R")
    kelvin_label.config(text=f"{kelvin:.2f} K")

input_label = Label(root, text="Masukkan suhu dalam Celcius:")
input_label.pack()

input_entry = Entry(root)
input_entry.pack()

konversi_button = Button(root, text="Konversi", command=konversi_celcius)
konversi_button.pack()

fahrenheit_label = Label(root, text="")
fahrenheit_label.pack()

reamur_label = Label(root, text="")
reamur_label.pack()

kelvin_label = Label(root, text="")
kelvin_label.pack()

root.mainloop()
