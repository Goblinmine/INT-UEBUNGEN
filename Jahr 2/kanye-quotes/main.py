from tkinter import *
import requests


def get_quote():
    global quote_text
    result = requests.put('https://api.kanye.rest/')
    if result.status_code == 200:
        canvas.itemconfig('text', text=result.json()['quote'])

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="Jahr 2/kanye-quotes/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text='Kanye Quote Goes HERE', width=250, font=("Arial", 30, "bold"), fill="white", tags='text')
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="Jahr 2/kanye-quotes/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()