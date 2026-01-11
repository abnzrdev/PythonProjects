# python
from tkinter import *

height = 200
width = int(height * 1.75)

# visual settings
bg_color = "#eef6ff"         # window background
widget_bg = "#ffffff"        # widget background (Entry, Labels background)
text_color = "#0b3d91"       # dark blue text for readability
button_bg = "#0b3d91"        # button background
button_fg = "#ffffff"        # button text color
base_font = ("Helvetica", 12, "bold")

window = Tk()
window.geometry(f"{width}x{height}")
window.title("Mile to Km Converter")
window.config(padx=20, pady=20, bg=bg_color)

# first row: Entry in third column with padding then "Miles" label
miles_frame = Frame(window, bg=bg_color)
miles_frame.grid(row=0, column=2)

miles_entry = Entry(
    miles_frame,
    width=10,
    font=base_font,
    bg=widget_bg,
    fg=text_color,
    insertbackground=text_color
)
miles_entry.grid(row=0, column=1, padx=(0, 8))

miles_label = Label(
    miles_frame,
    text="Miles",
    font=base_font,
    bg=bg_color,
    fg=text_color
)
miles_label.grid(row=0, column=2, sticky="w")

# second row: "is equal to" | value (variable) | "Km"
is_label = Label(
    window,
    text="is equal to",
    font=base_font,
    bg=bg_color,
    fg=text_color
)
is_label.grid(row=1, column=0, padx=(0, 12), pady=(10, 0))

km_value = StringVar(value="0")
km_value_label = Label(
    window,
    textvariable=km_value,
    width=6,
    anchor="center",
    font=base_font,
    bg=widget_bg,
    fg=text_color
)
km_value_label.grid(row=1, column=1, pady=(10, 0))

km_unit_label = Label(
    window,
    text="Km",
    font=base_font,
    bg=bg_color,
    fg=text_color
)
km_unit_label.grid(row=1, column=2, padx=(12, 0), pady=(10, 0))

# third row: Calculate button in the second column
def calculate_km():
    try:
        miles = float(miles_entry.get())
    except ValueError:
        km_value.set("0")
        return
    km = round(miles * 1.609, 2)
    km_value.set(str(km))

calculate_button = Button(
    window,
    text="Calculate",
    command=calculate_km,
    font=base_font,
    bg=button_bg,
    fg=button_fg,
    activebackground="#07306b",
    activeforeground=button_fg
)
calculate_button.grid(row=2, column=1, pady=(12, 0))

window.mainloop()
