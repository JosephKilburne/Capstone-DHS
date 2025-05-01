import tkinter as tk
from tkinter import ttk
import time
import threading
import random

def read_sensor():
    # Dummy values – replace with actual sensor reading
    return random.randint(1, 100), random.randint(10,20), random.randint(1,10), random.randint(0,100)

def get_case():
    #this will assign a case id somehow
    return(random.randint(1,5))

def get_data():
    #this is how we'll read data from the other case
    return random.randint(1, 100), random.randint(10,20), random.randint(1,10), random.randint(0,100)

def update_labels():
    while True:
        temp, hum, press, wl = read_sensor()
        case_ID = get_case()
        case_ID_label.config(text=f"Case {case_ID:.1f}")
        temp_label.config(text=f"Temperature: {temp:.1f} °C")
        hum_label.config(text=f"Humidity: {hum:.1f} %")
        press_label.config(text=f"Pressure: {press:.1f} kpa")
        wl_label.config(text=f"Water level: {wl:.1f}")
        time.sleep(2)

# GUI setup
root = tk.Tk()
root.geometry('320x240')
root.title("Microsoft Scalable Drone Deployment Container")

case_ID_label = ttk.Label(root,text="Case --",font=("Arial",10))
case_ID_label.pack(pady=10)

temp_label = ttk.Label(root, text="Temperature: -- °C", font=("Arial", 10))
temp_label.pack(pady=10)

hum_label = ttk.Label(root, text="Humidity: -- %", font=("Arial", 10))
hum_label.pack(pady=10)

press_label = ttk.Label(root, text="Pressure: -- psi", font=("Arial", 10))
press_label.pack(pady=10)

wl_label = ttk.Label(root, text="Water Reading: -- ", font=("Arial", 10))
wl_label.pack(pady=10)

# Start background thread to update sensor values
threading.Thread(target=update_labels, daemon=True).start()

root.mainloop()