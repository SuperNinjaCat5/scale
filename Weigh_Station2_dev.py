import tkinter as tk
import random
import datetime
import customtkinter
from CTkMessagebox import CTkMessagebox

BAUDRATE = 9600

root = customtkinter.CTk()
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue", "green", "dark-blue"
root.geometry('1000x500')
root.resizable(True, True)
root.title('Troop 30 Food Drive Weigh Station')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)

scout = tk.StringVar(root)
weight_to_display = tk.StringVar(root)
ScoutType = tk.StringVar(root)
ScoutType.set("Scout")
Bigtotal = tk.StringVar(root)
Bigtotal.set("0")

# Simulated scale data for testing
def get_serial(StringToSend):  # Dummy scale
    weight = random.randint(0, 200)
    return weight


# Write donation data to a file
def write_to_file():
    ScoutName = scout.get().strip().title()
    ScoutTypeDisplay = ScoutType.get().strip()
    weight_to_file = weight_to_display.get().rstrip(" lbs.")

    if ScoutName != "":
        with open("C:/Users/nicos/Documents/Food_Pantry_Donations.csv", "a") as hs:
            ct = datetime.datetime.now()
            bt = float(Bigtotal.get())
            bt = round(bt + float(weight_to_file), 2)
            Bigtotal.set(str(bt))

            hs.write(f"{ScoutName},{ScoutTypeDisplay},{weight_to_file},lbs,{bt},lbs,{ct}\n")

        CTkMessagebox(
            title="Saved", message=f"{ScoutName}, thank you for your {weight_to_file} lbs. donation!"
        )
    else:
        CTkMessagebox(
            title="Error, Not saved",
            message=f"Please Name The {ScoutTypeDisplay}",
            icon="cancel",
        )


# Tare function placeholder
def Tare_The_Scale():
    pass  # No tare functionality needed for dummy scale


# Buttons and labels
btnSaveToFile = customtkinter.CTkButton(
    root, text="Save To File", font=("Helvetica", 60), command=write_to_file
)
btnSaveToFile.grid(row=4, column=2, columnspan=1, rowspan=3)

btnTare = customtkinter.CTkButton(
    root, text="Tare", font=("Helvetica", 20), command=Tare_The_Scale
)
btnTare.grid(row=3, column=2, columnspan=1, rowspan=3)

label1 = customtkinter.CTkLabel(
    root, textvariable=weight_to_display, font=("Helvetica", 200), width=100
)
label1.grid(row=0, column=0, columnspan=3, rowspan=3)

label2 = customtkinter.CTkLabel(root, textvariable=Bigtotal, font=("Helvetica", 60))
label2.grid(row=3, column=2, columnspan=1, rowspan=1)

label3 = customtkinter.CTkLabel(
    root, text=("200 lbs. maximum on scale."), font=("Helvetica", 40)
)
label3.grid(row=5, column=1, columnspan=1, rowspan=1)

NameEntry = customtkinter.CTkEntry(
    root, textvariable=scout, font=("Helvetica", 60), width=300, height=60
)
NameEntry.grid(row=4, column=1, columnspan=1, rowspan=3)

r1 = customtkinter.CTkRadioButton(
    root, text="Scout", font=("Helvetica", 20), value="Scout", variable=ScoutType
)
r1.grid(row=3, column=0, rowspan=1)

r2 = customtkinter.CTkRadioButton(
    root, text="Webelo", font=("Helvetica", 20), value="Webelo", variable=ScoutType
)
r2.grid(row=4, column=0, rowspan=1)

r3 = customtkinter.CTkRadioButton(
    root, text="Other", font=("Helvetica", 20), value="Other", variable=ScoutType
)
r3.grid(row=5, column=0, rowspan=1)


# Adjust font size dynamically without flickering
current_font_size = 0  # Store the current font size

def adjust_font_size(event=None):
    global current_font_size
    new_font_size = int((root.winfo_width() + root.winfo_height()) // 50)

    if new_font_size != current_font_size:
        current_font_size = new_font_size
        btnSaveToFile.configure(font=("Helvetica", int(new_font_size // 1.5)))
        btnTare.configure(font=("Helvetica", new_font_size // 1.5))
        label1.configure(font=("Helvetica", new_font_size))
        label2.configure(font=("Helvetica", new_font_size))
        label3.configure(font=("Helvetica", int(new_font_size // 1.3)))
        NameEntry.configure(font=("Helvetica", new_font_size))
        r1.configure(font=("Helvetica", new_font_size // 2))
        r2.configure(font=("Helvetica", new_font_size // 2))
        r3.configure(font=("Helvetica", new_font_size // 2))


# Update weight dynamically only if it changes
last_weight = None  # Store the last weight

def my_mainloop():
    global last_weight
    weight = get_serial("0")  # Simulated or real weight
    if weight != last_weight:
        last_weight = weight
        weight_to_display.set(f"{weight} lbs.")
    root.after(1000, my_mainloop)


root.after(1000, my_mainloop)
adjust_font_size(0)
root.bind("<Configure>", adjust_font_size)

root.mainloop()
