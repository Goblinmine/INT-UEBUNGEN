import tkinter as tk
import model1 as m

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.db = m.Db_Zugriff()
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.output_label = tk.Label(self, bg='blue', fg='yellow')
        self.prepare_for_label(self.db.describeLeser(),self.output_label)
        self.quit_button = tk.Button(self, text='Quit', command=self.quit)

        self.output_label.grid()
        self.quit_button.grid()

    def prepare_for_label(self, source_dict, label):
        result_text = "The Result:\n"
        for row in source_dict:
            for part in row:
                result_text += str(part) + " "
            result_text += "\n"
        #label['text'] = result_text                        # oder schöner mit .configure()
        label.configure(text=result_text)

app = Application()
app.mainloop()