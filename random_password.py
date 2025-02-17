import random
import customtkinter as ctk
import pyperclip

def copy():
    pass

def generate():
    pass




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

password_entry = ctk.CTkEntry(result_frame, width=250, font=("Arial", 24), placeholder_text="Generated Password",
                              state="readonly", text_color="white", corner_radius=15)
password_entry.pack(side=ctk.LEFT, padx = 5)

# copy button
copy_button = ctk.CTkButton(result_frame, text="Copy", corner_radius=15, width=80, command=copy)
copy_button.pack(side=ctk.LEFT, padx = 5)

# length of password
slider = ctk.CTkSlider(app, from_ = 8, to = 32, width = 300)
slider.set(12)  # default value
slider.pack(pady = 30)

# checkboxes
checkbox_frame = ctk.CTkFrame(app)
checkbox_frame.pack(pady=10)

uppercase = ctk.CTkCheckBox(checkbox_frame, text = "UPPERCASE")
uppercase.grid(row = 0, column = 0, padx = 5, pady = 10)

lowercase = ctk.CTkCheckBox(checkbox_frame, text = "lowercase")
lowercase.grid(row = 1, column = 0, padx = 5, pady = 10)

digits = ctk.CTkCheckBox(checkbox_frame, text = "123")
digits.grid(row = 0, column = 1, padx = 15, pady = 10)

symbols = ctk.CTkCheckBox(checkbox_frame, text = "#$?")
symbols.grid(row = 1, column = 1, padx = 15, pady = 10)

generate_button = ctk.CTkButton(app, text = "Generate", command = generate, corner_radius = 15)
generate_button.pack(pady = 10)


# run
app.mainloop()