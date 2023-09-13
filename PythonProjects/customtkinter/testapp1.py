import customtkinter as ctk

ctk.set_default_color_theme("dark-blue")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def login():
    print("test")

def darkLightToggle():
    if switch.get() == "on":
        ctk.set_appearance_mode("light")
    elif switch.get() == "off":
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("dark")

app = ctk.CTk()

button = ctk.CTkButton(app, text="login", command=login)
button.pack(pady=12, padx=10)

switch = ctk.CTkSwitch(app, text="light/dark mode", command=darkLightToggle, onvalue="on", offvalue="off")
switch.pack(pady=12, padx=10)

app.mainloop()