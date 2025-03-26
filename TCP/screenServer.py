import tkinter as tk
import threading
from TCPserver import runServer

# Custom Styles
BG_COLOR = "#f8c8dc"  
TEXT_FG = "#6a1b9a"  
FONT = ("Arial", 14)

# Function to update GUI
def update_gui(input_text, output_text):
    input_label.config(text=f"Input: {input_text}")
    output_label.config(text=f"Output: {output_text}")

# Create Server GUI
screen = tk.Tk()
screen.title("TCPServer")
screen.geometry('600x150')
screen.configure(bg=BG_COLOR)

# Frame to align labels
frame = tk.Frame(screen, bg=BG_COLOR)
frame.pack(pady=20)

# Input Label (Client Message)
input_label = tk.Label(frame, text="Input: Waiting...", font=FONT, fg=TEXT_FG, bg=BG_COLOR, anchor="w", width=40)
input_label.pack(pady=5)

# Output Label (Processed Message)
output_label = tk.Label(frame, text="Output: Waiting...", font=FONT, fg=TEXT_FG, bg=BG_COLOR, anchor="w", width=40)
output_label.pack(pady=5)

threading.Thread(target=runServer, args=(update_gui,), daemon=True).start()

screen.mainloop()
