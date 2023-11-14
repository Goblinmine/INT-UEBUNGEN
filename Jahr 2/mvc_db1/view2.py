import tkinter as tk
from tkinter import ttk     # hat die schöneren Widgets
import model1 as m


def setup():
    global root, output_label, write_button, sachgebiet, autor, titel, ort, jahr, verlag, antwort, mod
    mod = m.Db_Zugriff()
    root = tk.Tk()
    root.title('Master the Database')

    # Eingabe von: sachgebiet, autor, titel, ort, jahr, verlag
    buch_frame = tk.Frame(root)
    buch_frame.grid(row=0, columnspan=3, padx=20, pady=20)
    write_button = ttk.Button(root, text="Eintragen", command=insert_buch)
    write_button.grid(row=1, column=2, sticky=tk.E)
    antwort= tk.StringVar()
    antwort.set("...")
    output_label = ttk.Label(root, textvariable=antwort)
    output_label.grid(row=1, columnspan=2, sticky=tk.W)

    label1 = tk.Label(buch_frame, text='Sachgebiet: ')
    sachgebiet = tk.StringVar()
    sachgebiet_entry = ttk.Entry(buch_frame, textvariable=sachgebiet)
    label1.grid(column=0, row=0, padx=10, sticky=tk.W)
    sachgebiet_entry.grid(row=0, column=1, sticky=tk.W, padx=10)

    label2 = tk.Label(buch_frame, text='Autor: ')
    autor = tk.StringVar()
    autor_entry = ttk.Entry(buch_frame, textvariable=autor)
    label2.grid(column=0, row=1, padx=10, sticky=tk.W)
    autor_entry.grid(row=1, column=1, sticky=tk.W, padx=10)

    label3 = tk.Label(buch_frame, text='Titel: ')
    titel = tk.StringVar()
    titel_entry = ttk.Entry(buch_frame, textvariable=titel)
    label3.grid(column=0, row=2, padx=10, sticky=tk.W)
    titel_entry.grid(row=2, column=1, sticky=tk.W, padx=10)

    label4 = tk.Label(buch_frame, text='Erscheinungsort: ')
    ort = tk.StringVar()
    ort_entry = ttk.Entry(buch_frame, textvariable=ort)
    label4.grid(column=0, row=3, padx=10, sticky=tk.W)
    ort_entry.grid(row=3, column=1, sticky=tk.W, padx=10)

    label5 = tk.Label(buch_frame, text='Erscheinungsjahr: ')
    jahr = tk.StringVar()
    jahr_entry = ttk.Entry(buch_frame, textvariable=jahr)
    label5.grid(column=0, row=4, padx=10, sticky=tk.W)
    jahr_entry.grid(row=4, column=1, sticky=tk.W, padx=10)

    label6 = tk.Label(buch_frame, text='Verlag: ')
    verlag = tk.StringVar()
    verlag_entry = ttk.Entry(buch_frame, textvariable=verlag)
    label6.grid(column=0, row=5, padx=10, sticky=tk.W)
    verlag_entry.grid(row=5, column=1, sticky=tk.W, padx=10)

def insert_buch():
    global sachgebiet, autor, titel, ort, jahr, verlag, antwort, mod
    rows = mod.insertBuch(mod.get_next_buchnr(), sachgebiet.get(), autor.get(), titel.get(), ort.get(), jahr.get(), verlag.get())
    antwortstring = str(rows)+' row(s) effected.'
    antwort.set(antwortstring)



if __name__ == '__main__':
    setup()
    root.mainloop()
