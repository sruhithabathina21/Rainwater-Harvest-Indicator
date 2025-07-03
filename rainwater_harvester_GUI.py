import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# ==== Constants ====
THRESHOLD = 10  # mm
LOG_FILE = "rainfall_log.csv"
ICON_PATH = "assets/icons/rainwater.png"
BACKGROUND_PATH = "assets/background.png"

# ==== Function ====
def check_rainfall():
    try:
        rainfall = float(entry.get())
        if rainfall >= THRESHOLD:
            result = "✅ It's worth collecting rainwater today."
        else:
            result = "❌ Rainfall is too low; not worth collecting."

        # Show result
        messagebox.showinfo("Result", result)

        # Log the result
        with open(LOG_FILE, "a") as log:
            log.write(f"{rainfall},{result}\n")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric rainfall value.")

# ==== GUI Setup ====
root = tk.Tk()
root.title("🌧️ Rainwater Harvest Indicator")
root.geometry("500x400")
root.resizable(False, False)

# ==== Load background ====
if os.path.exists(BACKGROUND_PATH):
    bg_img = Image.open(BACKGROUND_PATH)
    bg_img = bg_img.resize((500, 400))
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
else:
    root.configure(bg="#cceeff")  # fallback color

# ==== Header Icon ====
if os.path.exists(ICON_PATH):
    icon_img = Image.open(ICON_PATH)
    icon_img = icon_img.resize((80, 80))
    icon_photo = ImageTk.PhotoImage(icon_img)
    icon_label = tk.Label(root, image=icon_photo, bg="white")
    icon_label.pack(pady=10)

# ==== Label ====
label = tk.Label(root, text="Enter today's Rainfall (in mm):", font=("Helvetica", 14), bg="white")
label.pack(pady=10)

# ==== Entry ====
entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
entry.pack(pady=5)

# ==== Button ====
check_button = tk.Button(root, text="Check", font=("Helvetica", 14, "bold"),
                         command=check_rainfall, bg="#007ACC", fg="white", width=15)
check_button.pack(pady=20)

# ==== Footer ====
footer = tk.Label(root, text="Developed by Bathina Vijaya Sruhitha", font=("Helvetica", 10),
                  bg="white", fg="gray")
footer.pack(side="bottom", pady=10)

root.mainloop()
