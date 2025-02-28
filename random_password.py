import random
import customtkinter as ctk
import pyperclip, string

""" 
## 👉 To-Do List
- Light- Dark Theme options.    ------------> DONE
- Implement a password strength indicator.  ------------> DONE
- Save password history.
"""


copied = None

def copy():
    global copied
    pyperclip.copy(password_entry.get())

    if copied:
        copied.destroy()

    copied = ctk.CTkLabel(result_frame, text = "Copied!", fg_color="transparent")
    copied.pack()

def error():
    error_window = ctk.CTkToplevel(app)
    error_window.geometry("300x150")
    error_window.title("Error")

    # to interact directly with this window
    error_window.grab_set()
    error_window.focus_set()

    label = ctk.CTkLabel(error_window, text="Please select at least one character type!")
    label.pack(pady=20)

    close_button = ctk.CTkButton(error_window, text="OK", command=error_window.destroy,
                                 corner_radius = 15, width = 30)
    close_button.pack(pady=10)

def generate():
    global copied
    if copied:
        copied.destroy()
        copied = None

    digits = string.digits
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    symbols = string.punctuation

    chars = ""

    if uppercase_var.get():
        chars += uppercase
    if lowercase_var.get():
        chars += lowercase
    if digits_var.get():
        chars += digits
    if symbols_var.get():
        chars += symbols

    # create password
    password_length = int(slider.get())

    if chars:
        password = ""
        for i in range(password_length):
            password += random.choice(chars)
        password_entry.delete(0, ctk.END)
        password_entry.insert(0, password)

        check_password_strength()   # Added here to check strength after generating the password
    else:
        error()

def update_slider(value):
    slider_label.configure(text=f"Length of Password: {int(value)}")

def switch_theme():
    if switch_var.get() == "Dark":
        ctk.set_appearance_mode("dark")
        password_entry.configure(text_color="white")
    else:
        ctk.set_appearance_mode("light")
        password_entry.configure(text_color="black")

def check_password_strength():
    strength = 0
    value = None

    password = password_entry.get()

    if len(password) < 12:
        strength += 0
    elif len(password) < 16:
        strength += 1
    else:
        strength += 2

    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    if strength <= 2:
        value =  "Weak"
        strength_label.configure(text=value, text_color = "red")
    elif strength <= 4:
        value =  "Medium"
        strength_label.configure(text=value, text_color = "yellow")
    else:
        value =  "Strong"
        strength_label.configure(text=value, text_color = "green")



# system
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# app frame
app = ctk.CTk()
app.geometry("800x600")
app.title("Random Password Generator")

# title
title = ctk.CTkLabel(app, text = "Random Password Generator", font = ("Arial", 32))
title.pack(pady = 50)

# password
result_frame = ctk.CTkFrame(app)
result_frame.pack(pady=10)

password_entry = ctk.CTkEntry(result_frame, width=250, font=("Arial", 14), placeholder_text="Generated Password",
                              state="normal", text_color="white", corner_radius=15)
password_entry.pack(side=ctk.LEFT, padx = 5)

# switch theme
switch_var = ctk.StringVar(value = "Dark Mode")
switch = ctk.CTkSwitch(app, text = "Dark Mode", command = switch_theme, variable = switch_var,
                       corner_radius=15, onvalue = "Dark", offvalue = "Light")
switch.select() # switch on
switch.place(x = 670, y = 24 )

# copy button
copy_button = ctk.CTkButton(result_frame, text="Copy", corner_radius=15, width=80, command=copy)
copy_button.pack(side=ctk.LEFT, padx = 5)

# password strength label
strength_label = ctk.CTkLabel(app, text="", font=("Arial", 16))
strength_label.pack(pady=10)

# bind password entry to check password strength
password_entry.bind("<KeyRelease>", check_password_strength)

# length of password
slider_frame = ctk.CTkFrame(app)
slider_frame.pack(pady=20)

default_char = 14
slider_label = ctk.CTkLabel(slider_frame, text = f"Length of Password: {default_char}")
slider_label.pack()

slider = ctk.CTkSlider(slider_frame, from_ = 8, to = 24, width = 300, command = update_slider)
slider.set(default_char)  # default value
slider.pack(pady = 10)

# checkboxes
checkbox_frame = ctk.CTkFrame(app)
checkbox_frame.pack(pady=10)

uppercase_var = ctk.BooleanVar(value = True)
uppercase = ctk.CTkCheckBox(checkbox_frame, text = "UPPERCASE", variable = uppercase_var)
uppercase.grid(row = 0, column = 0, padx = 5, pady = 10)

lowercase_var = ctk.BooleanVar(value = True)
lowercase = ctk.CTkCheckBox(checkbox_frame, text = "lowercase", variable = lowercase_var)
lowercase.grid(row = 1, column = 0, padx = 5, pady = 10)

digits_var = ctk.BooleanVar(value = True)
digits = ctk.CTkCheckBox(checkbox_frame, text = "123", variable = digits_var)
digits.grid(row = 0, column = 1, padx = 15, pady = 10)

symbols_var = ctk.BooleanVar(value = False)
symbols = ctk.CTkCheckBox(checkbox_frame, text = "#$?", variable = symbols_var)
symbols.grid(row = 1, column = 1, padx = 15, pady = 10)


# generate button
generate_button = ctk.CTkButton(app, text = "Generate", command = generate, corner_radius = 15)
generate_button.pack(pady = 10)

# run
app.mainloop()