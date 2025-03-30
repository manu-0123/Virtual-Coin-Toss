import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def coin_toss():
    return random.choice(["Heads", "Tails"])

def update_results():
    total = heads_count.get() + tails_count.get()
    if total > 0:
        heads_percentage = (heads_count.get() / total) * 100
        tails_percentage = (tails_count.get() / total) * 100
    else:
        heads_percentage = tails_percentage = 0

    result_label.config(text=f"Heads: {heads_count.get()} ({heads_percentage:.2f}%)\n"
                             f"Tails: {tails_count.get()} ({tails_percentage:.2f}%)")

def flip_coin():
    try:
        num_flips = int(entry.get())
        if num_flips <= 0:
            messagebox.showerror("Error", "Please enter a positive integer.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter a number.")
        return

    for _ in range(num_flips):
        result = coin_toss()
        if result == "Heads":
            heads_count.set(heads_count.get() + 1)
            coin_image_label.config(image=heads_image)
        else:
            tails_count.set(tails_count.get() + 1)
            coin_image_label.config(image=tails_image)

    history.append(f"Session {len(history) + 1}: Heads - {heads_count.get()}, Tails - {tails_count.get()}")
    update_results()

def show_history():
    history_text = "\n".join(history)
    messagebox.showinfo("Historical Results", history_text if history_text else "No history available.")

def reset():
    heads_count.set(0)
    tails_count.set(0)
    update_results()
    coin_image_label.config(image=default_image)

def quit_app():
    root.quit()

# GUI Setup
root = tk.Tk()
root.title("Virtual Coin Toss")

heads_count = tk.IntVar(value=0)
tails_count = tk.IntVar(value=0)
history = []

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Enter the number of flips:")
label.pack()

entry = tk.Entry(frame)
entry.pack()

flip_button = tk.Button(frame, text="Flip Coin", command=flip_coin)
flip_button.pack()

# Load images for coin representation
heads_image = ImageTk.PhotoImage(Image.open("C:\\Users\Admin\\Downloads\\heads.png"))
tails_image = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Downloads\\tails.png"))
default_image = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Downloads\\default.png"))

coin_image_label = tk.Label(frame, image=default_image)
coin_image_label.pack()

result_label = tk.Label(frame, text="Heads: 0 (0.00%)\nTails: 0 (0.00%)", font=("Arial", 12))
result_label.pack()

history_button = tk.Button(frame, text="Show History", command=show_history)
history_button.pack()

reset_button = tk.Button(frame, text="Reset", command=reset)
reset_button.pack()

quit_button = tk.Button(frame, text="Quit", command=quit_app)
quit_button.pack()

root.mainloop()