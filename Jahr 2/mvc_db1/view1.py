import tkinter as tk
import model1


def setup():
    global root, output_label

    root = tk.Tk()
    root.title('Master the Database')
    db = model1.Db_Zugriff()

    result = db.describeLeser()
    result_text = "The Result:\n"
    for row in result:
        for part in row:
            result_text += str(part) + " "
        result_text += "\n"

    output_label = tk.Label(root, text=result_text, justify=tk.LEFT)
    output_label.grid(row=0, columnspan=3, padx=20, pady=20)


if __name__ == '__main__':
    setup()
    root.mainloop()
