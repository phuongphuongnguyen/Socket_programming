import tkinter as tk
from TCPclient import requestClient

# Create main screen
screen = tk.Tk()
screen.title("Client")
screen.geometry('600x300')
screen.configure(bg="#f8c8dc")

clientInput = tk.StringVar()

def enter():
    input_text = clientInput.get()
    result = requestClient(input_text)
    print(input_text)
    outputLabel.config(text="Output: " + result)

# Title Label
label = tk.Label(screen, text="Client", font=('Arial', 24, 'bold'), fg="#6a1b9a", bg="#f8c8dc")  # Hồng nhạt + tím đậm
label.pack(pady=10)

# Input Entry
entry = tk.Entry(screen, textvariable=clientInput, font=('Arial', 14), bd=3, relief=tk.GROOVE, width=40)
entry.pack(pady=5)

# Enter Button
enter_button = tk.Button(screen, text="Convert", command=enter, font=('Arial', 12, 'bold'), bg="#e57373", fg="white", bd=3, relief=tk.RAISED, padx=10, pady=5)  # Hồng cam
enter_button.pack(pady=10)

# Output Label
outputLabel = tk.Label(screen, text="Output: ", font=('Arial', 14), fg="#6a1b9a", bg="#f8c8dc")  # Hồng nhạt + tím đậm
outputLabel.pack(pady=10)

screen.mainloop()
