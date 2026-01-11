from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json

# Constants
BACKGROUND = "#120321"
FONT_NAME = "Courier"
WINDOW_PADDING = 50
PASSWORD_LENGTH = 12
MIN_PASSWORD_LENGTH = 4
ENTRY_WIDTH = 35
SHORT_ENTRY_WIDTH = 32
BUTTON_WIDTH_SMALL = 21
BUTTON_WIDTH_LARGE = 36
LABEL_FONT_SIZE = 12
BUTTON_FONT_SIZE = 10
DEFAULT_EMAIL = "abnzr@gmail.com"
DATA_FILE = "data.json"
LOGO_FILE = "logo.png"
PASSWORD_SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?/|"

# Creating the window
window = Tk()
window.title("Password Manager")
window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=BACKGROUND)
window.resizable(False,False)

# ======================== Password Generator ================

def generate_password(length: int = PASSWORD_LENGTH):
    """
    Generate a random password using random
    Ensures at least one lowercase, one uppercase, one digit and one symbol.
    """
    try:
        if length < MIN_PASSWORD_LENGTH:
            raise ValueError("length must be at least 4 to include all character types")

        lowers = string.ascii_lowercase
        uppers = string.ascii_uppercase
        digits = string.digits
        symbols = PASSWORD_SYMBOLS

        # Guarantee one of each required type
        password_chars = [
            random.choice(lowers),
            random.choice(uppers),
            random.choice(digits),
            random.choice(symbols),
        ]

        all_chars = lowers + uppers + digits + symbols
        password_chars += [random.choice(all_chars) for _ in range(length - 4)]

        random.shuffle(password_chars)
        password="".join(password_chars)
        try:
            pyperclip.copy(password)
        except (pyperclip.PyperclipException, PermissionError, OSError) as e:
            print(f"Could not copy to clipboard: {e}")
        except Exception as e:
            print(f"Unexpected clipboard error: {e}")
            messagebox.showwarning(title="Clipboard Access", message="Could not copy to clipboard")
        password_entry.delete(0, END)
        password_entry.insert(0, password)
    except Exception as e:
        messagebox.showerror(title="Error", message=f"Could not generate password: {e}")

# ========================= Finding the Password ====================
def search_password():
    website = website_entry.get()

    if len(website) == 0:
        messagebox.showerror(title="Error", message="Please enter a website name")
        return

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        try:
            with open(DATA_FILE, "w") as file:
                json.dump({}, file, indent=4)
            messagebox.showinfo(title="Info", message=f"No data file found. Created `{DATA_FILE}` for future storage.")
        except Exception as e:
            messagebox.showerror(title="Error", message=f"Could not create data file: {e}")
        return
    except json.JSONDecodeError:
        try:
            with open(DATA_FILE, "w") as file:
                json.dump({}, file, indent=4)
            messagebox.showinfo(title="Info",
                                message=f"Data file was corrupted. Recreated `{DATA_FILE}` for future storage.")
        except Exception as e:
            messagebox.showerror(title="Error", message=f"Could not recreate data file: {e}")
        return

    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website,
                message=f"Username: {username}\nPassword: {password}"
            )
            try:
                pyperclip.copy(password)
            except Exception as e:
                print(f"Could not copy to clipboard: {e}")
        else:
            messagebox.showinfo(title="Not Found", message=f"No details for {website} found")
    finally:
        password_entry.delete(0,END)


# ========================= Taking the file ====================
def save_password():
    """
        Validate and save website credentials to DATA_FILE after user confirmation.

        Validates all fields are filled, shows confirmation dialog, appends data
        in pipe-separated format (website | username | password), and clears
        website/password fields on success. Displays error/success messages.
    """
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(website) != 0 and len(username) != 0 and len(password) != 0:
        response = messagebox.askokcancel(
            title="Save",
            message=(
                "These are the details you entered:\n"
                f"Website: {website}\n"
                f"Email: {username}\n"
                f"Password: {password}\n"
                "Save to file?"
            )
        )
        if response:
            try:
                # Read existing data
                try:
                    with open(DATA_FILE, "r") as file:
                        data = json.load(file)
                except FileNotFoundError:
                    data = {}
                except json.JSONDecodeError:
                    data = {}

                # Update with new entry
                data.update(new_data)

                # Write back all data
                with open(DATA_FILE, "w") as file:
                    json.dump(data, file, indent=4)

            except IOError as e:
                messagebox.showerror(title="Error", message=f"Could not save to file: {e}")
            else:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo(title="Success", message="Password saved successfully!")
    else:
        messagebox.showerror(title="Error", message="Don't leave any place empty")


# ========================= UI SETUP =========================

# Canvas with logo
try:
    logo = PhotoImage(file=LOGO_FILE)
    canvas = Canvas(width=logo.width(), height=logo.height(), bg=BACKGROUND, highlightthickness=0)
    canvas.create_image(logo.width() // 2, logo.height() // 2, image=logo)
    canvas.grid(row=0, column=1)
except Exception as e:
    # If logo fails to load, create a simple canvas without image
    canvas = Canvas(width=200, height=200, bg=BACKGROUND, highlightthickness=0)
    canvas.create_text(100, 100, text="Password\nManager", fill="white", font=(FONT_NAME, 16))
    canvas.grid(row=0, column=1)
    print(f"Warning: Could not load logo: {e}")

# Website
website_label = Label(text="Website:", bg=BACKGROUND, fg="white", font=(FONT_NAME, LABEL_FONT_SIZE))
website_label.grid(row=1, column=0, sticky="e")
website_entry = Entry(width=SHORT_ENTRY_WIDTH)
website_entry.grid(row=1, column=1, sticky="w")
search_button = Button(
    text="Search Password",
    width=BUTTON_WIDTH_SMALL,
    bg=BACKGROUND,
    fg="white",
    font=(FONT_NAME, BUTTON_FONT_SIZE),
    command=search_password
)
search_button.grid(row=1, column=2, sticky="ew")
website_entry.focus()

# Email/Username
username_label = Label(text="Email/Username:", bg=BACKGROUND, fg="white", font=(FONT_NAME, LABEL_FONT_SIZE))
username_label.grid(row=2, column=0, sticky="e")
username_entry = Entry(width=ENTRY_WIDTH)
username_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
username_entry.insert(0, DEFAULT_EMAIL)

# Password
password_label = Label(text="Password:", bg=BACKGROUND, fg="white", font=(FONT_NAME, LABEL_FONT_SIZE))
password_label.grid(row=3, column=0, sticky="e")
password_entry = Entry(width=SHORT_ENTRY_WIDTH)
password_entry.grid(row=3, column=1, sticky="w")
gen_pwd = Button(
    text="Generate Password",
    width=BUTTON_WIDTH_SMALL,
    bg=BACKGROUND,
    fg="white",
    font=(FONT_NAME, BUTTON_FONT_SIZE),
    command=generate_password
)
gen_pwd.grid(row=3, column=2, sticky="ew")

# Add Button
add_button = Button(
    text="Add",
    width=BUTTON_WIDTH_LARGE,
    bg=BACKGROUND,
    fg="white",
    font=(FONT_NAME, BUTTON_FONT_SIZE),
    command=save_password
)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")



window.mainloop()