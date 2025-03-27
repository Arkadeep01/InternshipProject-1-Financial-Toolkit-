import tkinter as tk
import subprocess  # To launch calculator scripts
import os  # To manage file paths

# Get the base directory (update as needed)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Function to open Bulk Tax Calculator
def open_bulk_calculator():
    bulk_gui_path = os.path.join(BASE_DIR, "Bulk_Calculator", "Bulk_GUI.py")
    subprocess.Popen(["python", bulk_gui_path])  

def open_Income_Tax_Calculator():
    income_tax_gui_path = os.path.join(BASE_DIR, "Income_Tax_Calculator", "ITcal_GUI.py")
    subprocess.Popen(["python", income_tax_gui_path])  
def open_Investment_calculator():
    investment_gui_path = os.path.join(BASE_DIR, "Investment_Calculator", "invest_GUI.py")
    subprocess.Popen(["python", investment_gui_path])  
def open_Mortgage_Calculator():
    Mortgage_gui_path = os.path.join(BASE_DIR, "Mortgage_Calculator", "mort_GUI.py")
    subprocess.Popen(["python", Mortgage_gui_path])  
def open_Saving_Calculator():
    Saving_gui_path = os.path.join(BASE_DIR, "Savings_Goal_Calculator", "sgl_GUI.py")
    subprocess.Popen(["python", Saving_gui_path])  

# Main GUI Window
root = tk.Tk()
root.title("Financial Toolkit - Main")
root.geometry("400x300")

# Fonts
title_font = ("Timmana", 16, "bold")
button_font = ("Aleo", 12, "bold")

# Title Label
tk.Label(root, text="Financial Toolkit", font=title_font).pack(pady=15)

# Buttons for Calculators
tk.Button(root, text="Bulk Tax Calculator", font=button_font, command=open_bulk_calculator).pack(pady=5)
tk.Button(root, text="Income Tax Calculator", font=button_font, command=open_Income_Tax_Calculator).pack(pady=5)
tk.Button(root, text="Investment Calculator", font=button_font, command=open_Investment_calculator).pack(pady=5)
tk.Button(root, text="Mortgage Calculator", font=button_font, command=open_Mortgage_Calculator).pack(pady=5)
tk.Button(root, text="Savings Goal Calculator", font=button_font, command=open_Saving_Calculator).pack(pady=5)

# Add more buttons for other calculators here...

root.mainloop()
