import tkinter as tk
from tkinter import ttk, Toplevel, Label, filedialog
import webbrowser
import os
import requests

def open_github():
    webbrowser.open("https://github.com/corv1njano/Display-Entities-Scripts")
def open_patreon():
    webbrowser.open("https://www.patreon.com/corv1njano/membership")
def update_checker(msg, type):
    dialogUpdate = Toplevel(root)
    dialogUpdate.title("Check for Updates...")
    dialogUpdate.resizable(False, False)
    dialogUpdate.config(bg='#101010')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    icon_file = 'icon.png'
    icon_path = os.path.join(script_dir, icon_file)
    icon = tk.PhotoImage(file=icon_path)
    dialogUpdate.iconphoto(False, icon)
    center_window(dialogUpdate, offset=100)
    if type == 0 or type == 1:
        dialogUpdate.geometry("400x100")
        Label(dialogUpdate, text=f"{msg}", bg="#101010", fg='#D6D6D6', font=("Verdana", 11)).place(relx=0.5, rely=0.5, anchor='center')
    elif type == 2:
        dialogUpdate.geometry("400x120")
        label = tk.Label(dialogUpdate, text=f"{msg}", anchor="n", bg="#101010", fg='#D6D6D6', font=("Verdana", 11), padx=0, pady=15)
        label.pack(fill="x")
        gridDialog = tk.Frame(dialogUpdate, bg="#101010")
        gridDialog.pack(fill="both", expand=True)
        button_yes = ttk.Button(gridDialog, text="Yes", command=download_update, style='TButton')
        button_no = ttk.Button(gridDialog, text="No", command=dialogUpdate.destroy, style='TButton')
        button_yes.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        button_no.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        gridDialog.grid_columnconfigure(0, weight=1)
        gridDialog.grid_columnconfigure(1, weight=1)
    dialogUpdate.focus_set()

def download_update():
    webbrowser.open("https://github.com/corv1njano/Display-Entities-Scripts/releases")

def update_request():
    CURRENTVER = 140
    updateUrl = "https://raw.githubusercontent.com/corv1njano/Display-Entities-Scripts/refs/heads/main/.appversion"
    res = requests.get(updateUrl)
    if res.status_code == 200:
        ver = int(res.text.strip())
        if ver > CURRENTVER:
            update_checker("There is a new update available!\nDownload now?", 2)
        elif ver == CURRENTVER:
            update_checker("You are up to date!", 0)
    elif res.status_code != 200:
        update_checker("Could not connect to server.\nPlease try again.", 1)

def save_directory(*args):
    currentDir = os.getcwd()
    dir = filedialog.askdirectory(title="Select a Folder for your .mcfunction-Files...", initialdir=currentDir)
    if dir:
        clicked6.set(dir)

def generate_files():
    selectedMode =      clicked1.get()
    command =           entry0.get().replace("/summon","summon")
    blockTarget =       clicked2.get()
    blockReplacement =  clicked3.get()
    filename =          entry4.get()
    replaceValue =      clicked5.get()
    saveLocation =      clicked6.get()
    if selectedMode == "Change Color":
        colors = ["white","yellow","orange","red","pink","magenta","purple","blue","cyan","light_blue","lime","green","brown","gray","light_gray","black"]
        for color in colors:
            outputText = command.replace(f"{replaceValue}_{blockTarget}", f"{color}_{blockReplacement}")
            if saveLocation == "Same as .exe-File":
                with open(f"{color}_{filename}.mcfunction", "w") as file:
                    file.write(outputText)
            else:
                with open(f"{saveLocation}/{color}_{filename}.mcfunction", "w") as file:
                    file.write(outputText)
        open_dialog("16")
    elif selectedMode == "Change Wood":
        woodtypes = ["oak","birch","spruce","dark_oak","jungle","acacia","mangrove","cherry","warped","crimson"]
        for wood in woodtypes:
            if replaceValue == "crimson" or replaceValue == "warped":
                if wood == "crimson" or wood == "warped":
                    outputText = command.replace(replaceValue, wood)
                else:
                    outputText = command.replace(f"{replaceValue}_hyphae",f"{wood}_wood").replace(f"{replaceValue}_stem", f"{wood}_log").replace(f"{replaceValue}_planks",f"{wood}_planks")
            else:
                if wood == "crimson" or wood == "warped":
                    outputText = command.replace(f"{replaceValue}_wood", f"{wood}_hyphae").replace(f"{replaceValue}_log", f"{wood}_stem").replace(f"{replaceValue}_planks",f"{wood}_planks")
                else:
                    outputText = command.replace(replaceValue, wood)
            if saveLocation == "Same as .exe-File":
                with open(f"{wood}_{filename}.mcfunction", "w") as file:
                    file.write(outputText)
            else:
                with open(f"{saveLocation}/{wood}_{filename}.mcfunction", "w") as file:
                    file.write(outputText)
        open_dialog("10")

root = tk.Tk()

def center_window(window, offset=0):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2) - offset
    window.geometry(f'{width}x{height}+{x}+{y}')

style = ttk.Style()
style.configure('TButton', 
                font=('Verdana', 10), 
                foreground='#101010', 
                background='#101010',
                padding=(15, 0))

def open_dialog(msg):
    dialog = Toplevel(root)
    dialog.geometry("500x100")
    dialog.title("Files created!")
    dialog.resizable(False, False)
    dialog.config(bg='#101010')
    script_dir = os.path.dirname(os.path.abspath(__file__))
    icon_file = 'icon.png'
    icon_path = os.path.join(script_dir, icon_file)
    icon = tk.PhotoImage(file=icon_path)
    dialog.iconphoto(False, icon)
    center_window(dialog, offset=100)
    Label(dialog, text=f"{msg} Files have been placed in the selected Directory.\n\nThis Window will close in 5 Seconds...", bg="#101010", fg='#D6D6D6', font=("Verdana", 11)).place(relx=0.5, rely=0.5, anchor='center')
    dialog.focus_set()
    dialog.after(5000, dialog.destroy)

root.title("Display Entities Varient Editor")
root.geometry("520x320") # prev 520x350
root.resizable(False, False)
root.config(bg='#101010')
border = tk.Frame(root, bg='#101010')
border.pack(fill=tk.BOTH, expand=True)
center_window(root, offset=100)

script_dir = os.path.dirname(os.path.abspath(__file__))
icon_file = 'icon.png'
icon_path = os.path.join(script_dir, icon_file)
icon = tk.PhotoImage(file=icon_path)
root.iconphoto(False, icon)

border.grid_columnconfigure(0, weight=1)
border.grid_columnconfigure(1, minsize=180)
for i in range(9):
    border.grid_rowconfigure(i, weight=1)

style.configure('TEntry', foreground='#101010', background='#101010', padding=6)

label0 = tk.Label(border, text="Command (only one per Run):", bg="#101010", fg='#D6D6D6', font=("Verdana", 12))
label0.grid(row=1, column=0, sticky="e")
entry0 = ttk.Entry(border, style='TEntry')
entry0.grid(row=1, column=1, sticky="ew", padx=(0, 6))

label5 = tk.Label(border, text="Value Replacement (Color/Wood Type):", bg="#101010", fg='#D6D6D6', font=("Verdana", 12))
label5.grid(row=3, column=0, sticky="e")
options5a = ["white","yellow","orange","red","pink","magenta","purple","blue","cyan","light_blue","lime","green","brown","gray","light_gray","black"]
options5b = ["oak","birch","spruce","dark_oak","jungle","acacia","mangrove","cherry","warped","crimson"]
clicked5 = tk.StringVar()
clicked5.set(options5a[0])
entry5 = tk.OptionMenu(border, clicked5, *options5a)
entry5.grid(row=3, column=1, sticky="ew", padx=(0, 6))

def selected_mode(*args):
    selectedMode = clicked1.get()
    if selectedMode == "Change Color":
        entry2.config(state=tk.ACTIVE)
        entry3.config(state=tk.ACTIVE)
        entry5 = tk.OptionMenu(border, clicked5, *options5a)
        entry5.grid(row=3, column=1, sticky="ew", padx=(0, 6))
        clicked5.set(options5a[0])
    else:
        entry2.config(state=tk.DISABLED)
        entry3.config(state=tk.DISABLED)
        entry5 = tk.OptionMenu(border, clicked5, *options5b)
        entry5.grid(row=3, column=1, sticky="ew", padx=(0, 6))
        clicked5.set(options5b[0])

label1 = tk.Label(border, text="Block Type:", bg="#101010", fg='#D6D6D6', font=("Verdana", 12))
label1.grid(row=2, column=0, sticky="e")
options1 = ["Change Color", "Change Wood"]
clicked1 = tk.StringVar()
clicked1.set(options1[0])
clicked1.trace_add("write", selected_mode)
entry1 = tk.OptionMenu(border, clicked1, *options1)
entry1.grid(row=2, column=1, sticky="ew", padx=(0, 6))

label2 = tk.Label(border, text="Block Varient to Target:", bg="#101010", fg='#D6D6D6', font=("Verdana", 12))
label2.grid(row=4, column=0, sticky="e")
options2 = ["terracotta", "glazed_terracotta", "concrete", "concrete_powder", "stained_glass", "stained_glass_pane", "banner", "wall_banner", "candle", "candle_cake", "bed", "shulker_box", "wool", "carpet"]
clicked2 = tk.StringVar()
clicked2.set(options2[0])
entry2 = tk.OptionMenu(border, clicked2, *options2)
entry2.grid(row=4, column=1, sticky="ew", padx=(0, 6))

label3 = tk.Label(border, text="Replacement for Target:", bg="#101010", fg='#D6D6D6', font=("Verdana", 12))
label3.grid(row=5, column=0, sticky="e")
clicked3 = tk.StringVar()
clicked3.set(options2[0])
entry3 = tk.OptionMenu(border, clicked3, *options2)
entry3.grid(row=5, column=1, sticky="ew", padx=(0, 6))

label4 = tk.Label(border, text="Filename (no Extension needed):", bg="#101010", fg='#D6D6D6', font=("Verdana", 12))
label4.grid(row=6, column=0, sticky="e")
entry4 = ttk.Entry(border, style='TEntry')
entry4.grid(row=6, column=1, sticky="ew", padx=(0, 6))

label6 = tk.Label(border, text="Save Location:", bg="#101010", fg='#D6D6D6', font=("Verdana", 12))
label6.grid(row=7, column=0, sticky="e")
clicked6 = tk.StringVar()
entry6 = ttk.Entry(border, style='TEntry', textvariable=clicked6)
clicked6.set("Same as .exe-File")
entry6.grid(row=7, column=1, sticky="ew", padx=(0, 6))
entry6.bind("<Button-1>", save_directory)

versionLabel = tk.Label(border, text="Version 1.4.0 by corv1njano", bg="#101010", fg='#666666', font=("Verdana", 9))
versionLabel.grid(row=8, column=0, sticky="w", padx=(6, 0))
button2 = ttk.Button(border, text="Generate Files...", command=generate_files, style='TButton')
button2.grid(row=8, column=1, sticky="e", padx=(0, 6))

menu_bar = tk.Menu(root, bg='#202020', fg='#d6d6d6', activebackground='blue', activeforeground='white')
menu_bar.add_command(label="GitHub", command=open_github)
menu_bar.add_command(label="Update", command=update_request)
menu_bar.add_command(label="Donate", command=open_patreon)
root.config(menu=menu_bar)

root.mainloop()
