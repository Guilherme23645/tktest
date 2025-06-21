import tkinter as tk

window = tk.Tk()

window.title('Simple GUI')

window_width = 500
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f'{window_width}x{window_height}+{x}+{y}')

def your_name():
	response.config(text=f"Name: {txt.get('1.0','end-1c')}")

label = tk.Label(window,text="What is your name?")
label.pack(pady=(0,10))

txt = tk.Text(window, height=1, width=15)
txt.pack(pady=(0,10))

btn = tk.Button(window, text='Submit', command=your_name)
btn.pack(pady=(0,10))

response = tk.Label(window, text='')
response.pack(pady=(0,0))

window.mainloop()
