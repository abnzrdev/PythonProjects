from tkinter import *
import requests

# helper to load images: try Pillow (for JPG), then fall back to PhotoImage, else placeholder
def load_image(path):
    try:
        from PIL import Image, ImageTk
        img = Image.open(path)
        return ImageTk.PhotoImage(img)
    except Exception:
        try:
            return PhotoImage(file=path)
        except Exception:
            # placeholder 1x1 image to avoid crashes if file missing or unsupported
            return PhotoImage(width=1, height=1)

def get_quote():
    try:
        res = requests.get("https://api.kanye.res", timeout=5)
        res.raise_for_status()
        quote = res.json().get("quote", "No quote found.")
    except Exception:
        quote = "አለማዊ ነገር ብዙ አያሳስበኝም"
    return quote

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg='black')
window.resizable(False, False)

canvas = Canvas(width=300, height=414, bg='black', bd=0, highlightthickness=0)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote = get_quote()
quote_text = canvas.create_text(150, 207, text=quote, width=250, font=("Arial", 30, "bold"), fill="black")
canvas.grid(row=0, column=0)

# changed: load button image from kidus.jpg (uses load_image helper)
kanye_img = load_image("kidus.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, bd=0, relief='flat', bg='black', activebackground='black', command=lambda: canvas.itemconfig(quote_text, text=get_quote()))
kanye_button.grid(row=1, column=0)

window['bg'] = 'black'


window.mainloop()