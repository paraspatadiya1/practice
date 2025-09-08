# RepairMate - Simple TechFix App
# Beginner Developer Version :)

import tkinter as tk
from tkinter import messagebox
import re

# ------------------------------
# Simple Classes for Customer & Device
# ------------------------------
class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

class Device:
    def __init__(self, model, issue):
        self.model = model
        self.issue = issue
        self.status = "Pending"

# ------------------------------
# Main App Logic
# ------------------------------
customers = []   # list to store all customers

# Save data to file (very simple way)
def save_to_file():
    with open("customers.txt", "w") as f:
        for c in customers:
            f.write(f"{c.name},{c.phone}\n")
            for d in c.devices:
                f.write(f"   Device:{d.model}, Issue:{d.issue}, Status:{d.status}\n")
    messagebox.showinfo("Saved", "Data saved to customers.txt")

# Add customer function
def add_customer():
    name = entry_name.get()
    phone = entry_phone.get()
    if name == "" or phone == "":
        messagebox.showerror("Error", "Enter all fields")
        return
    cust = Customer(name, phone)
    customers.append(cust)
    messagebox.showinfo("Added", "Customer Added!")

# Add device to last customer
def add_device():
    if len(customers) == 0:
        messagebox.showerror("Error", "No customer found!")
        return
    model = entry_model.get()
    issue = entry_issue.get()
    if model == "" or issue == "":
        messagebox.showerror("Error", "Enter all fields")
        return
    dev = Device(model, issue)
    customers[-1].add_device(dev)
    messagebox.showinfo("Added", "Device Added!")

# Show all customers
def show_customers():
    text_area.delete("1.0", tk.END)
    for c in customers:
        text_area.insert(tk.END, f"Customer: {c.name}, Phone: {c.phone}\n")
        for d in c.devices:
            text_area.insert(tk.END, f"   Device: {d.model}, Issue: {d.issue}, Status: {d.status}\n")

# Simple regex search
def search_device():
    pattern = entry_search.get()
    text_area.delete("1.0", tk.END)
    for c in customers:
        for d in c.devices:
            if re.search(pattern, d.status, re.IGNORECASE) or re.search(pattern, d.model, re.IGNORECASE):
                text_area.insert(tk.END, f"{c.name} - {d.model} - {d.status}\n")

# ------------------------------
# Tkinter GUI
# ------------------------------
root = tk.Tk()
root.title("RepairMate - Beginner Version")

# Customer frame
frame1 = tk.Frame(root)
frame1.pack(pady=5)
tk.Label(frame1, text="Name").grid(row=0, column=0)
tk.Label(frame1, text="Phone").grid(row=1, column=0)
entry_name = tk.Entry(frame1)
entry_phone = tk.Entry(frame1)
entry_name.grid(row=0, column=1)
entry_phone.grid(row=1, column=1)
tk.Button(frame1, text="Add Customer", command=add_customer).grid(row=2, column=0, columnspan=2)

# Device frame
frame2 = tk.Frame(root)
frame2.pack(pady=5)
tk.Label(frame2, text="Device Model").grid(row=0, column=0)
tk.Label(frame2, text="Issue").grid(row=1, column=0)
entry_model = tk.Entry(frame2)
entry_issue = tk.Entry(frame2)
entry_model.grid(row=0, column=1)
entry_issue.grid(row=1, column=1)
tk.Button(frame2, text="Add Device", command=add_device).grid(row=2, column=0, columnspan=2)

# Action buttons
frame3 = tk.Frame(root)
frame3.pack(pady=5)
tk.Button(frame3, text="Show Customers", command=show_customers).pack(side=tk.LEFT, padx=5)
tk.Button(frame3, text="Save Data", command=save_to_file).pack(side=tk.LEFT, padx=5)

# Search
frame4 = tk.Frame(root)
frame4.pack(pady=5)
tk.Label(frame4, text="Search (model/status)").pack(side=tk.LEFT)
entry_search = tk.Entry(frame4)
entry_search.pack(side=tk.LEFT)
tk.Button(frame4, text="Search", command=search_device).pack(side=tk.LEFT)

# Text area
text_area = tk.Text(root, height=15, width=50)
text_area.pack(pady=10)

root.mainloop()
