import tkinter as tk
from tkinter import ttk, Toplevel, Label, Button, PhotoImage
import webbrowser
import os

def open_github():
    webbrowser.open("https://github.com/corv1njano/Display-Entities-Scripts")

def open_patreon():
    webbrowser.open("https://www.patreon.com/corv1njano/membership")

def generate_files():
    selectedMode = clicked1.get()
    command = entry0.get()
    blockTarget = clicked2.get()
    blockReplacement = clicked3.get()
    filename = entry4.get()
    replaceValue = clicked5.get()
    if selectedMode == "Change Color":
        colors = ["white","yellow","orange","red","pink","magenta","purple","blue","cyan","light_blue","lime","green","brown","gray","light_gray","black"]
        for color in colors:
            outputText = command.replace(f"{replaceValue}_{blockTarget}", f"{color}_{blockReplacement}")
            with open(f"{color}_{filename}.mcfunction", "w") as file:
                file.write(outputText)
        open_dialog("16 Files have been placed in the current Directory.")
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
            with open(f"{wood}_{filename}.mcfunction", "w") as file:
                file.write(outputText)
        open_dialog("10 Files have been placed in the current Directory.")

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
                background='#101010')

def open_dialog(msg):
    dialog = Toplevel(root)
    dialog.geometry("450x75")
    dialog.title("Files created!")
    dialog.resizable(False, False)
    dialog.config(bg='#101010')
    dialog.focus_set()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    icon_file = 'icon.png'
    icon_path = os.path.join(script_dir, icon_file)
    icon = tk.PhotoImage(file=icon_path)
    dialog.iconphoto(False, icon)
    center_window(dialog, offset=100)
    Label(dialog, text=f"{msg}\n\nThis Window will close in 5 Seconds...", bg="#101010", fg='#D6D6D6', font=("Verdana", 12)).pack(padx=6, pady=6)
    dialog.focus_set()
    dialog.after(5000, dialog.destroy)

root.title("Display Entities Varient Editor")
root.geometry("520x350")
root.resizable(False, False)
root.config(bg='#101010')
border = tk.Frame(root, bg='#101010')
border.pack(fill=tk.BOTH, expand=True)

script_dir = os.path.dirname(os.path.abspath(__file__))
icon_file = 'icon.png'
icon_path = os.path.join(script_dir, icon_file)
icon = tk.PhotoImage(file=icon_path)
root.iconphoto(False, icon)

border.grid_columnconfigure(0, weight=1)
border.grid_columnconfigure(1, minsize=180)
for i in range(8):
    border.grid_rowconfigure(i, weight=1)

button0 = ttk.Button(border, text="Open Help/Tutorial", command=open_github, style='TButton')
button0.grid(row=0, column=0, sticky="w", padx=(6, 0))
button1 = ttk.Button(border, text="Donate!", command=open_patreon, style='TButton')
button1.grid(row=0, column=1, sticky="e", padx=(0, 6))

style.configure('TEntry', foreground='#101010', background='#101010', padding=6)

label0 = tk.Label(border, text="Command (without \"/\" at Beginning):", bg="#101010", fg='#D6D6D6', font=("Verdana", 12))
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
options2 = ["wool", "terracotta", "glazed_terracotta", "concrete", "concrete_powder", "stained_glass"]
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

versionLabel = tk.Label(border, text="Version 1.1 by corv1njano", bg="#101010", fg='#666666', font=("Verdana", 9))
versionLabel.grid(row=7, column=0, sticky="w", padx=(6, 0))
button2 = ttk.Button(border, text="Generate Files...", command=generate_files, style='TButton')
button2.grid(row=7, column=1, sticky="e", padx=(0, 6))

center_window(root, offset=100)

root.mainloop()
