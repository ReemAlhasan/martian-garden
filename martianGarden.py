import random
import time
import tkinter as tk

# ----- Logik för bevattning -----
THRESHOLD = 40  # 0–100, lägre = torrare

moisture = 80   # startfukt (procent)
pump_on = False

# ----- Tkinter-setup -----
root = tk.Tk()
root.title("Martian Garden")

canvas_width = 400
canvas_height = 200
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Rita en horisontell "jord-linje"
line_y = canvas_height // 2
line = canvas.create_line(50, line_y, 350, line_y, width=10, fill="green")  # startar som grön

status_label = tk.Label(root, text="Startar...", font=("Arial", 12))
status_label.pack(pady=10)

def update_visual(moisture, pump_on):
    """Uppdatera färg på linjen och texten."""
    if pump_on:
        color = "green"   # jorden är blöt
        text = f"Fukt: {moisture}% – Vattnar 🌧 (grön linje)"
    else:
        color = "brown"   # jorden är torr
        text = f"Fukt: {moisture}% – Torr (brun linje)"

    canvas.itemconfig(line, fill=color)
    status_label.config(text=text)

def simulate_day(day):
    global moisture, pump_on

    # Jorden torkar lite slumpmässigt
    moisture -= random.randint(5, 15)
    if moisture < 0:
        moisture = 0

    # Kolla om vi behöver vattna
    if moisture < THRESHOLD:
        pump_on = True
        moisture += 30  # pumpen höjer fukten
        if moisture > 100:
            moisture = 100
    else:
        pump_on = False

    print(f"Dag {day}")
    print(f"Fukt i jorden: {moisture}%")
    print("Pump:", "PÅ (vattnar 🌧)" if pump_on else "AV")
    print("-" * 20)

    update_visual(moisture, pump_on)

    if day < 10:
        # anropa nästa dag efter 1 sekund (1000 ms)
        root.after(1000, simulate_day, day + 1)
    else:
        status_label.config(text=status_label.cget("text") + " – Simulering klar!")

# Starta simulering dag 1 när fönstret kommit igång
root.after(500, simulate_day, 1)

root.mainloop()
