import tkinter as tk
from tkinter import ttk
import webbrowser
import os

def open_link():
    webbrowser.open("https://github.com/corv1njano/Display-Entities-Scripts")

def center_window(window, offset=0):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2) - offset
    window.geometry(f'{width}x{height}+{x}+{y}')

def generate_files():
    selectedMode = clicked1.get()
    command = entry0.get()
    blockTarget = clicked2.get()
    blockReplacement = clicked3.get()
    filename = entry4.get()
    if selectedMode == "Change Color":
        colors = ["red","magenta","pink","purple","blue","light_blue","green","lime","gray","light_gray","black","brown","orange","yellow","cyan"]
        for color in colors:
            outputText = command.replace(f"white_{blockTarget}", f"{color}_{blockReplacement}")
            with open(f"{color}_{filename}.mcfunction", "w") as file:
                file.write(outputText)
    elif selectedMode == "Change Wood":
        woodtypes = ["spruce","mangrove","birch","jungle","cherry","warped","acacia","dark_oak","crimson"]
        for wood in woodtypes:
            outputText = command.replace("oak", wood)
            if wood == "crimson" or wood == "warped":
                outputText = command.replace("oak_wood", f"{wood}_hyphae").replace("oak_log", f"{wood}_stem")
            with open(f"{wood}_{filename}.mcfunction", "w") as file:
                file.write(outputText)

def selected_mode(*args):
    selectedMode = clicked1.get()
    if selectedMode == "Change Color":
        entry2.config(state=tk.ACTIVE)
        entry3.config(state=tk.ACTIVE)
    else:
        entry2.config(state=tk.DISABLED)
        entry3.config(state=tk.DISABLED)

root = tk.Tk()

style = ttk.Style()
style.configure('TButton', 
                font=('Verdana', 10), 
                foreground='#101010', 
                background='#101010')

root.title("Display Entities Varient Editor")
root.geometry("550x300")
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
border.grid_columnconfigure(1, weight=1)
for i in range(7):
    border.grid_rowconfigure(i, weight=1)

button0 = ttk.Button(border, text="Open up Help / Tutorial", command=open_link, style='TButton')
button0.grid(row=0, column=0, sticky="w", padx=10)

label0 = tk.Label(border, text="Command (without \"/\" at beginning):", bg="#101010", fg='#D6D6D6', font=("Verdana", 12))
label0.grid(row=1, column=0, sticky="e")
entry0 = tk.Entry(border)
entry0.grid(row=1, column=1, sticky="w")

label1 = tk.Label(border, text="Block Type:", bg="#101010", fg='#D6D6D6', font=("Verdana", 12))
label1.grid(row=2, column=0, sticky="e")
options1 = ["Change Color", "Change Wood"]
clicked1 = tk.StringVar()
clicked1.set(options1[0])
clicked1.trace_add("write", selected_mode)
entry1 = tk.OptionMenu(border, clicked1, *options1)
entry1.grid(row=2, column=1, sticky="w")

label2 = tk.Label(border, text="Block varient to target:", bg="#101010", fg='#D6D6D6', font=("Verdana", 12))
label2.grid(row=3, column=0, sticky="e")
options2 = ["wool", "terracotta", "glazed_terracotta", "concrete", "concrete_powder", "stained_glass"]
clicked2 = tk.StringVar()
clicked2.set(options2[0])
entry2 = tk.OptionMenu(border, clicked2, *options2)
entry2.grid(row=3, column=1, sticky="w")

label3 = tk.Label(border, text="Replacement for target:", bg="#101010", fg='#D6D6D6', font=("Verdana", 12))
label3.grid(row=4, column=0, sticky="e")
clicked3 = tk.StringVar()
clicked3.set(options2[0])
entry3 = tk.OptionMenu(border, clicked3, *options2)
entry3.grid(row=4, column=1, sticky="w")

label4 = tk.Label(border, text="Filename (no extension needed):", bg="#101010", fg='#D6D6D6', font=("Verdana", 12))
label4.grid(row=5, column=0, sticky="e")
entry4 = tk.Entry(border)
entry4.grid(row=5, column=1, sticky="w")

versionLabel = tk.Label(border, text="Version 1.0, by corv1njano", bg="#101010", fg='#666666', font=("Verdana", 9))
versionLabel.grid(row=6, column=0, sticky="w", padx=10)
button1 = ttk.Button(border, text="Generate Files...", command=generate_files, style='TButton')
button1.grid(row=6, column=1, sticky="e", padx=10)

center_window(root, offset=100)

root.mainloop()
