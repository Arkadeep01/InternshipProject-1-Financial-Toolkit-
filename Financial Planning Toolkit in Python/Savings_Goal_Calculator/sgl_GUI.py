import tkinter as tk
from tkinter import messagebox
from sgcal import savings_goal_calculator 

def compute_savings():
    try:
        saving_goal = float(entry_goal.get())
        saving_period = float(entry_period.get())
        return_rate = float(entry_return.get())

        if saving_goal <= 0 or saving_period <= 0 or return_rate < 0:
            messagebox.showerror("Input Error", "Please enter positive values for all fields.")
            return

        monthly_saving = savings_goal_calculator(saving_goal, saving_period, return_rate)

        result_label.config(text=f"Monthly Savings Required: ${monthly_saving:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI Setup
root = tk.Tk()
root.title("Savings Goal Calculator")
root.geometry("500x400")
root.minsize(400, 350)

# Responsive Layout
root.grid_columnconfigure(1, weight=1)

# Fonts
title_font = ("Timmana", 16, "bold")
label_font = ("EB Garamond", 12)
entry_font = ("EB Garamond", 12)
button_font = ("Aleo", 12, "bold")

# Title
title_label = tk.Label(root, text="Savings Goal Calculator", font=title_font)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Labels and Entries
tk.Label(root, text="Savings Goal ($):", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_goal = tk.Entry(root, font=entry_font)
entry_goal.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Time Period (Years):", font=label_font).grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_period = tk.Entry(root, font=entry_font)
entry_period.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Annual Rate of Return (%):", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_return = tk.Entry(root, font=entry_font)
entry_return.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Savings", font=button_font, command=compute_savings)
calculate_button.grid(row=4, column=0, columnspan=2, pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Black Ops One", 14, "bold"), fg="blue")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Make layout responsive
for i in range(2):
    root.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":
    root.mainloop()
