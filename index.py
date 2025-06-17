import tkinter as tk

window = tk.Tk()

window.title("Simple GUI")

window_width = 500
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f'{window_width}x{window_height}+{x}+{y}')

label = tk.Label(window,text="Some text.")
label.pack()

window.mainloop()
